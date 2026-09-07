"""Validate the AM-07 source, standards, rights, and freshness contracts."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
import re
import sys
from typing import Any


SOURCE_CLASSES = {
    "official_law_or_regulation",
    "official_registry_or_gazette",
    "official_government_guidance",
    "delegated_regulator",
    "incorporated_standard",
    "voluntary_standard",
    "manufacturer_specification",
    "contract_or_site_document",
    "secondary",
}
RIGHTS = {"OPEN_OFFICIAL", "LICENSE_REQUIRED", "USER_SUPPLIED", "PUBLIC_DOMAIN", "UNKNOWN"}
HANDLING = {"METADATA_ONLY", "METADATA_AND_PARAPHRASE", "LICENSED_EXCERPT", "FULL_TEXT_PERMITTED", "NO_REPRODUCTION"}
STATUSES = {"CURRENT", "CURRENT_ON_ACCESS", "HISTORICAL", "SUPERSEDED", "STALE", "UNKNOWN", "CONFLICTING", "PENDING_REVIEW"}
POLICIES = {"VERIFY_AT_USE", "VERIFY_BEFORE_RELEASE", "SCHEDULED_REVIEW", "HISTORICAL_ONLY"}
LEGACY_CLASSES = {"official_government_guidance", "official_law_or_regulation", "official_guidance", "delegated_regulator"}
EXPECTED_SCENARIOS = {f"AM07-S{i:02d}" for i in range(1, 13)}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def text(value: Any, label: str) -> None:
    need(isinstance(value, str) and bool(value.strip()), f"{label}: expected non-empty text")


def iso_date(value: Any, label: str, nullable: bool = False) -> None:
    if value is None and nullable:
        return
    text(value, label)
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{label}: expected ISO date") from exc


def validate_schema(schema: dict[str, Any]) -> None:
    need(schema.get("schema_version") == "AM-07-source-record-1", "source record schema version")
    need(schema.get("status") == "STANDARD_READY_NOT_IMPLEMENTED", "source record schema status")
    need(len(schema.get("required_fields", [])) >= 12, "source record required fields")
    need(set(schema.get("source_classes", {})) == SOURCE_CLASSES, "source class coverage")
    precedence = schema.get("source_precedence")
    need(isinstance(precedence, list) and [item.get("rank") for item in precedence] == [1, 2, 3, 4, 5], "source precedence ranks")
    need(all(item.get("classes") for item in precedence), "source precedence classes")
    provincial = schema.get("provincial_systems")
    need(isinstance(provincial, list) and {item.get("jurisdiction") for item in provincial} == {"federal", "Ontario", "British Columbia", "Alberta", "Quebec"}, "provincial source systems")
    need(set(schema.get("status_values", [])) == STATUSES, "source status values")
    need(set(schema.get("rights_values", [])) == RIGHTS, "rights values")
    need(set(schema.get("content_handling_values", [])) == HANDLING, "content handling values")
    need(set(schema.get("freshness_policy_values", [])) == POLICIES, "freshness policy values")
    claim = schema.get("claim_record", {})
    need(set(claim.get("required_fields", [])) == {"claim_id", "source_key", "claim_type", "scope", "as_of", "location", "support_status"}, "claim fields")
    need(set(claim.get("support_status_values", [])) == {"SUPPORTED", "PARTIAL", "CONFLICTING", "UNSUPPORTED", "PENDING_REVIEW"}, "claim statuses")
    need(len(schema.get("standard_record_requirements", [])) >= 7, "standard metadata requirements")


def validate_policy(policy: dict[str, Any]) -> None:
    need(policy.get("schema_version") == "AM-07-source-freshness-1", "freshness policy schema version")
    need(policy.get("status") == "STANDARD_READY_NOT_IMPLEMENTED", "freshness policy status")
    need(len(policy.get("states", {})) == len(STATUSES) and set(policy["states"]) == STATUSES, "freshness states")
    need(set(policy.get("policies", {})) == POLICIES, "freshness policy names")
    need(len(policy.get("recheck_triggers", [])) >= 7, "freshness recheck triggers")
    transitions = policy.get("transition_rules", [])
    need(len(transitions) >= 6, "freshness transition rules")
    need(set(policy.get("blocking_states_for_current_claims", [])) >= {"HISTORICAL", "SUPERSEDED", "STALE", "UNKNOWN", "CONFLICTING", "PENDING_REVIEW"}, "blocking states")
    need(set(policy.get("required_output_fields", [])) >= {"source_key", "source_status", "as_of", "verification_date", "version_or_currency_note", "review_owner_or_handoff"}, "freshness output fields")


def validate_record(record: dict[str, Any], label: str) -> None:
    key = record.get("source_key")
    text(key, f"{label}.source_key")
    need(re.fullmatch(r"[A-Z0-9][A-Z0-9._-]+", key) is not None, f"{label}.source_key: invalid format")
    for field in ("title", "publisher", "scope", "applicability_basis"):
        text(record.get(field), f"{key}.{field}")
    text(record.get("url"), f"{key}.url")
    need(record["url"].startswith("https://"), f"{key}: https URL required")
    need(record.get("source_class") in SOURCE_CLASSES, f"{key}: unknown source class")
    jurisdiction = record.get("jurisdiction")
    need(isinstance(jurisdiction, dict), f"{key}.jurisdiction: object required")
    for field in ("country", "level", "sector"):
        text(jurisdiction.get(field), f"{key}.jurisdiction.{field}")
    need("province_or_territory" in jurisdiction, f"{key}.jurisdiction.province_or_territory required")
    need(isinstance(jurisdiction.get("obligation_domains"), list) and jurisdiction["obligation_domains"], f"{key}.jurisdiction.obligation_domains")
    need(record.get("status") in STATUSES, f"{key}: unknown status")
    version = record.get("version")
    need(isinstance(version, dict), f"{key}.version: object required")
    authority = record.get("authority")
    need(isinstance(authority, dict), f"{key}.authority: object required")
    text(authority.get("official_status"), f"{key}.authority.official_status")
    text(authority.get("incorporation_basis"), f"{key}.authority.incorporation_basis")
    rights = record.get("rights")
    need(isinstance(rights, dict), f"{key}.rights: object required")
    need(rights.get("rights_status") in RIGHTS, f"{key}.rights.rights_status")
    need(rights.get("content_handling") in HANDLING, f"{key}.rights.content_handling")
    text(rights.get("permission_note"), f"{key}.rights.permission_note")
    need(record.get("freshness_policy") in POLICIES, f"{key}: unknown freshness policy")
    iso_date(record.get("retrieved_at"), f"{key}.retrieved_at")
    iso_date(record.get("last_verified_at"), f"{key}.last_verified_at")
    iso_date(record.get("published_at"), f"{key}.published_at", nullable=True)
    if record["rights"]["rights_status"] in {"LICENSE_REQUIRED", "UNKNOWN"}:
        need(record["rights"]["content_handling"] in {"METADATA_ONLY", "NO_REPRODUCTION"}, f"{key}: protected or unknown rights require metadata-only handling")
    if record["source_class"] == "incorporated_standard":
        need(record["authority"]["incorporation_basis"].strip() not in {"", "none", "unknown"}, f"{key}: incorporated standard needs basis")


def validate_examples(examples: dict[str, Any]) -> None:
    need(examples.get("schema_version") == "AM-07-source-examples-1", "source examples schema version")
    records = examples.get("records")
    need(isinstance(records, list) and len(records) >= 6, "source examples coverage")
    seen: set[str] = set()
    for record in records:
        validate_record(record, "example")
        need(record["source_key"] not in seen, f"duplicate example source key {record['source_key']}")
        seen.add(record["source_key"])
    provinces = {record["jurisdiction"]["province_or_territory"] for record in records}
    need({"Ontario", "British Columbia", "Alberta", "Quebec"} <= provinces, "provincial examples")
    need(any(record["source_class"] in {"voluntary_standard", "incorporated_standard"} for record in records), "standards example")
    need(any(record["rights"]["rights_status"] == "LICENSE_REQUIRED" for record in records), "licensed standards example")
    claims = examples.get("claims")
    need(isinstance(claims, list) and len(claims) >= 2, "claim examples")
    claim_ids: set[str] = set()
    for claim in claims:
        for field in ("claim_id", "source_key", "claim_type", "scope", "location"):
            text(claim.get(field), f"claim.{field}")
        iso_date(claim.get("as_of"), f"{claim['claim_id']}.as_of")
        need(claim.get("source_key") in seen, f"{claim['claim_id']}: source key missing")
        need(claim.get("support_status") in {"SUPPORTED", "PARTIAL", "CONFLICTING", "UNSUPPORTED", "PENDING_REVIEW"}, f"{claim['claim_id']}: support status")
        need(claim["claim_id"] not in claim_ids, f"duplicate claim id {claim['claim_id']}")
        claim_ids.add(claim["claim_id"])


def validate_legacy_registry(path: Path) -> int:
    registry = json.loads(path.read_text(encoding="utf-8"))
    sources = registry.get("sources")
    need(isinstance(sources, list) and sources, f"{path.name}: sources required")
    keys: set[str] = set()
    for source in sources:
        key = source.get("key")
        text(key, f"{path.name}.key")
        need(key not in keys, f"{path.name}: duplicate key {key}")
        keys.add(key)
        for field in ("publisher", "title", "url", "source_class", "scope", "freshness", "notes"):
            text(source.get(field), f"{path.name}.{key}.{field}")
        need(source["url"].startswith("https://"), f"{path.name}.{key}: https URL required")
        need(source["source_class"] in LEGACY_CLASSES, f"{path.name}.{key}: unexpected legacy source class")
    return len(sources)


def validate_standard_document(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    for phrase in (
        "# AM-07 source and standards standard",
        "Source precedence",
        "Copyright and protected-standard handling",
        "Freshness and version control",
        "Government and provincial regulatory sourcing",
        "Sector-standard sourcing",
        "STANDARD_READY_NOT_IMPLEMENTED",
        "Do not paste, reconstruct, or distribute the standard text",
    ):
        need(phrase in content, f"standard document missing {phrase!r}")
    need(EXPECTED_SCENARIOS <= set(re.findall(r"AM07-S\d{2}", content)), "acceptance scenarios")
    for url in (
        "https://laws-lois.justice.gc.ca/eng/acts/",
        "https://www.ontario.ca/laws",
        "https://www.bclaws.gov.bc.ca/",
        "https://www.alberta.ca/alberta-kings-printer",
        "https://www.legisquebec.gouv.qc.ca/?siteLocale=fr_CA",
        "https://www.canada.ca/en/canadian-heritage/services/crown-copyright-request.html",
    ):
        need(url in content, f"standard document missing source URL {url}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        schema = json.loads((root / "docs/architecture/source-record-schema.json").read_text(encoding="utf-8"))
        policy = json.loads((root / "docs/architecture/source-freshness-policy.json").read_text(encoding="utf-8"))
        examples = json.loads((root / "docs/architecture/source-record-examples.json").read_text(encoding="utf-8"))
        validate_schema(schema)
        validate_policy(policy)
        validate_examples(examples)
        legacy_counts = [
            validate_legacy_registry(root / "docs/architecture/canadian-source-registry.json"),
            validate_legacy_registry(root / "docs/architecture/safety-source-registry.json"),
        ]
        validate_standard_document(root / "docs/architecture/source-standards-standard.md")
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(
        "PASS: AM-07 source and standards standard; "
        f"{len(schema['source_classes'])} source classes; "
        f"{len(schema['source_precedence'])} precedence ranks; "
        f"{len(schema['provincial_systems'])} jurisdiction systems; "
        f"{len(examples['records'])} example records; "
        f"{len(policy['states'])} freshness states; "
        f"{sum(legacy_counts)} legacy AM-04/05 source records compatible; "
        f"{len(EXPECTED_SCENARIOS)} acceptance scenarios; no source fetched or legal applicability evaluated."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
