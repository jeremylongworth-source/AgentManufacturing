"""Validate AM-26 federal capability packages and bounded source evidence."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import sys


SECTIONS = ["Overview", "Triggers", "Non-Triggers", "Required Inputs", "Optional Inputs", "Assumptions", "Core Workflow", "Calculations", "Validation", "Exception Handling", "Source Usage", "Output Contract", "Safety Requirements", "References", "Examples", "Testing"]
EXPECTED = {
    "identify-manufacturing-jurisdiction": ("skills/family-20-canadian-compliance/identify-manufacturing-jurisdiction", "P1", "REGULATED", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "identify-applicable-regulatory-layer": ("skills/family-20-canadian-compliance/identify-applicable-regulatory-layer", "P1", "REGULATED", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "assess-whmis-applicability": ("skills/family-20-canadian-compliance/assess-whmis-applicability", "P1", "REGULATED", "PENDING_CONTEXT", ["CANADA_FEDERAL","PROVINCIAL_REQUIRED","SECTOR_REGULATED"]),
    "review-whmis-readiness": ("skills/family-20-canadian-compliance/review-whmis-readiness", "P1", "REGULATED", "PENDING_CONTEXT", ["CANADA_FEDERAL","PROVINCIAL_REQUIRED","SECTOR_REGULATED"]),
    "assess-made-in-canada-claim": ("skills/family-20-canadian-compliance/assess-made-in-canada-claim", "P0", "REGULATED", "PENDING_CONTEXT", ["CANADA_FEDERAL","SECTOR_REGULATED"]),
    "assess-product-of-canada-claim": ("skills/family-20-canadian-compliance/assess-product-of-canada-claim", "P1", "REGULATED", "PENDING_CONTEXT", ["CANADA_FEDERAL","SECTOR_REGULATED"]),
    "review-nonfood-labelling-readiness": ("skills/family-20-canadian-compliance/review-nonfood-labelling-readiness", "P1", "REGULATED", "PENDING_CONTEXT", ["CANADA_FEDERAL","SECTOR_REGULATED"]),
    "verify-regulatory-source-freshness": ("skills/family-20-canadian-compliance/verify-regulatory-source-freshness", "P1", "REGULATED", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
}
PRIVATE_PATTERNS = [r"password", r"secret", r"credential", r"api[_ -]?key", r"token", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"]


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def taxonomy(root: Path) -> dict[str, dict]:
    data = json.loads((root / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8"))
    return {item["name"]: item for item in data["skills"]}


def validate_package(root: Path, name: str, spec: tuple, records: dict[str, dict]) -> None:
    package_rel, priority, safety, jurisdiction, flags = spec
    package = root / package_rel
    skill = package / "SKILL.md"
    need(skill.exists(), f"{name}: SKILL.md missing")
    content = skill.read_text(encoding="utf-8")
    need(content.startswith("---\n"), f"{name}: frontmatter")
    end = content.find("\n---", 4)
    need(end > 0, f"{name}: frontmatter end")
    fields = {}
    for line in content[4:end].splitlines():
        if line.strip():
            key, sep, value = line.partition(":")
            need(sep and value.strip(), f"{name}: malformed frontmatter")
            fields[key.strip()] = value.strip()
    need(fields.get("name") == name, f"{name}: name")
    need(fields.get("description", "").endswith("."), f"{name}: description")
    need(fields.get("license") == "MIT", f"{name}: licence")
    need(re.findall(r"^## ([^\n]+)$", content, re.MULTILINE) == SECTIONS, f"{name}: section order")
    metadata = next((line for line in content.splitlines() if line.startswith("**Taxonomy metadata:**")), "")
    need(metadata, f"{name}: metadata")
    record = records.get(name)
    need(record is not None and record["family"] == package.parent.name.split("-")[1], f"{name}: taxonomy family")
    need(record["priority"] == priority, f"{name}: priority")
    need(record["safety_class"] == safety, f"{name}: safety")
    need(record["jurisdiction"]["assessment"] == jurisdiction, f"{name}: jurisdiction")
    need(record["jurisdiction"]["flags"] == flags, f"{name}: jurisdiction flags")
    for marker in (record["family"], record["tier"], priority, safety, jurisdiction, "TAXONOMY_ACCEPTED_NOT_IMPLEMENTED") + tuple(flags):
        need(marker in metadata, f"{name}: metadata {marker}")
    adapter = package / "agents/openai.yaml"
    need(adapter.exists(), f"{name}: adapter")
    adapter_text = adapter.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        need(re.search(rf"^\s+{key}:\s+.+$", adapter_text, re.MULTILINE), f"{name}: adapter {key}")
    need(f"${name}" in adapter_text, f"{name}: adapter invocation")
    refs = list((package / "references").glob("*.md"))
    need(refs, f"{name}: references")
    for ref in refs:
        text = ref.read_text(encoding="utf-8")
        need(text.strip(), f"{name}: empty reference")
        need(f"references/{ref.name}" in content, f"{name}: reference not linked")
        for pattern in PRIVATE_PATTERNS:
            need(re.search(pattern, text, re.IGNORECASE) is None, f"{name}: private pattern")
    need("Expected routing is not observed behavior" in content, f"{name}: evaluation boundary")


def validate_evaluation(root: Path) -> None:
    content = (root / "tests/evaluations/AM-26-federal-capabilities-acceptance.md").read_text(encoding="utf-8")
    for phrase in ("Status: `READY_FOR_REVIEW`", "Runtime model behavior", "NOT_RUN", "Residual risk"):
        need(phrase in content, f"AM-26 evaluation missing {phrase!r}")
    for name in EXPECTED:
        need(f"`{name}`" in content, f"AM-26 evaluation missing {name}")


def validate_coverage(root: Path, records: dict[str, dict]) -> None:
    accepted = {name for name, record in records.items() if record["family"] == "20" and name != "identify-provincial-safety-overlay"}
    need(set(EXPECTED) == accepted, "AM-26 family coverage differs from frozen taxonomy")
    paths = {path.parent.relative_to(root).as_posix() for family in ("family-20-canadian-compliance",) for path in (root / "skills" / family).glob("*/SKILL.md")}
    need({spec[0] for spec in EXPECTED.values()} <= paths, "AM-26 package inventory mismatch")
    need(all(path.rsplit("/", 1)[-1] in records for path in paths), "AM-26 unknown package")
    manifest = json.loads((root / "tests/expected-routing.yaml").read_text(encoding="utf-8"))
    scenarios = [item for item in manifest["scenarios"] if item["scenario_id"].startswith("AM26-")]
    routes = {route for item in scenarios for route in item["expected_routes"]}
    need(routes == accepted, "AM-26 scenarios must cover exactly federal capabilities")
    for item in scenarios:
        need(item["route_mode"] in {"IMPLEMENTED", "NO_TRIGGER"} and not item["future_routes"], "AM-26 route mode")
    for name in accepted:
        for provider in records[name]["dependencies"]["evidence_reuse"]:
            need(any((root / "skills").glob(f"*/{provider}/SKILL.md")), f"{name}: missing evidence provider {provider}")



def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    need(spec is not None and spec.loader is not None, f"Cannot import {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_sources(root: Path) -> None:
    module = load_module(root / "scripts/validate-source-standards-standard.py", "am26_source")
    data = json.loads((root / "docs/architecture/am26-federal-source-records.json").read_text(encoding="utf-8"))
    expected_keys = ["AM26-WORKPLACE","AM26-WHMIS","AM26-WHMIS-TRANSITION","AM26-ORIGIN","AM26-LABELLING","AM26-HPA","AM26-HPR","AM26-CPLA","AM26-CPLR"]
    keys = {record["source_key"] for record in data["records"]}
    need(keys == set(expected_keys) and len(data["records"]) == len(keys), "AM-26 source coverage")
    for record in data["records"]:
        module.validate_record(record, record["source_key"])
        if record["source_class"] == "official_law_or_regulation":
            need(record["status"] == "PENDING_REVIEW", "AM-26 displayed currency gap must remain pending")
            need("2026-06-21" in record["version"]["currency_note"], "AM-26 displayed currency")
            need(record["freshness_policy"] == "VERIFY_AT_USE", "AM-26 legal recheck")
        else:
            need(record["status"] == "CURRENT_ON_ACCESS", "AM-26 guidance scope")
    need(len(data["claims"]) == len(keys), "AM-26 bounded claim count")
    need({claim["source_key"] for claim in data["claims"]} == keys, "AM-26 claim coverage")
    for claim in data["claims"]:
        need(all(claim.get(key) for key in ("claim_type", "scope", "as_of", "location", "support_status", "claim")), "AM-26 claim metadata")
    for name, spec in EXPECTED.items():
        for ref in (root / spec[0] / "references").glob("*.md"):
            for key in re.findall(r"\x60(AM26-[A-Z-]+)\x60", ref.read_text(encoding="utf-8")):
                need(key in keys, f"{name}: unknown source {key}")


def validate_scenario_cases(root: Path) -> None:
    data = json.loads((root / "tests/expected-routing.yaml").read_text(encoding="utf-8"))
    cases = [item for item in data["scenarios"] if item["scenario_id"].startswith("AM26-")]
    need({item["scenario_id"] for item in cases} == {f"AM26-S{i:02}" for i in range(1, 16)}, "AM-26 case inventory")
    categories = {item["category"] for item in cases}
    need({"jurisdiction_conflicts", "missing_inputs", "bad_inputs", "ambiguous_scenario", "unsupported_assumptions", "incorrect_invocation", "calculation_correctness", "expected_output_structure"} <= categories, "AM-26 scenario dimensions")
    by_id = {item["scenario_id"]: item for item in cases}
    for case_id in ("AM26-S09", "AM26-S10", "AM26-S11", "AM26-S13"):
        need(by_id[case_id]["expected_outcome"] == "SOURCE_REVIEW_REQUIRED", f"{case_id}: source boundary")
    need(by_id["AM26-S12"]["route_mode"] == "NO_TRIGGER" and not by_id["AM26-S12"]["expected_routes"], "AM-26 negative route")



def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        records = taxonomy(root)
        for name, spec in EXPECTED.items():
            validate_package(root, name, spec, records)
        validate_evaluation(root)
        validate_coverage(root, records)
        validate_scenario_cases(root)
        validate_sources(root)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("PASS: AM-26 federal capabilities; eight packages, nine source records and 15 review scenarios validated; runtime model behavior remains NOT_RUN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
