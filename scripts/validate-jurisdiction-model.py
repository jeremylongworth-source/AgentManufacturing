"""Validate the AM-04 Canadian jurisdiction model and source registry."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any


FLAGS = {"CANADA_FEDERAL", "PROVINCIAL_REQUIRED", "SECTOR_REGULATED", "STANDARDS_DEPENDENT"}
STATES = {"GENERIC_METHOD_ONLY", "PENDING_CONTEXT", "SOURCE_REVIEW_REQUIRED", "COVERAGE_GAP", "CONFLICT_REVIEW_REQUIRED"}
DOMAINS = {"product", "supplier", "workplace", "environmental", "transport", "labelling", "contract_standard", "other"}
EXTENSIONS = {"federal", "ontario", "british_columbia", "alberta", "quebec"}
INDEX_ASSESSMENTS = {"GENERIC_METHOD_ONLY", "PENDING_CONTEXT"}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def nonempty_text(value: Any, label: str) -> None:
    need(isinstance(value, str) and bool(value.strip()), f"{label}: expected non-empty text")


def validate(model: dict[str, Any], registry: dict[str, Any], taxonomy: dict[str, Any]) -> None:
    need(model.get("schema_version") == "AM-04-jurisdiction-1", "model schema version")
    need(model.get("status") == "MODEL_READY_NOT_IMPLEMENTED", "model status")
    need(set(model.get("flags", {})) == FLAGS, "all four flags are required")
    for flag, item in model["flags"].items():
        need(isinstance(item, dict), f"{flag}: object required")
        nonempty_text(item.get("meaning"), f"{flag}.meaning")
        need(isinstance(item.get("requires"), list) and item["requires"], f"{flag}.requires")
        nonempty_text(item.get("does_not_mean"), f"{flag}.does_not_mean")
    need(set(model.get("applicability_states", {})) == STATES, "applicability states")
    for state, meaning in model["applicability_states"].items():
        nonempty_text(meaning, f"{state}.meaning")
    fields = model.get("context_fields")
    need(isinstance(fields, dict) and len(fields) >= 10, "context fields")
    need(DOMAINS <= set(fields["obligation_domain"].get("allowed", [])), "obligation domains")
    for name, field in fields.items():
        need(isinstance(field, dict), f"{name}: field object")
        need("unknown_behavior" in field, f"{name}: unknown behavior")
    hierarchy = model.get("source_hierarchy")
    need(isinstance(hierarchy, list) and [x.get("rank") for x in hierarchy] == [1, 2, 3, 4, 5], "source hierarchy ranks")
    for item in hierarchy:
        nonempty_text(item.get("class"), "source hierarchy class")
        nonempty_text(item.get("use"), "source hierarchy use")
    extensions = model.get("extension_pattern")
    need(isinstance(extensions, dict) and set(extensions) == EXTENSIONS, "initial extension pattern")
    source_items = registry.get("sources")
    need(isinstance(source_items, list) and len(source_items) >= 8, "source registry coverage")
    by_key = {}
    for item in source_items:
        key = item.get("key")
        nonempty_text(key, "source key")
        need(key not in by_key, f"duplicate source key {key}")
        by_key[key] = item
        for field in ("publisher", "title", "url", "source_class", "scope", "freshness", "notes"):
            nonempty_text(item.get(field), f"{key}.{field}")
        need(item["url"].startswith("https://"), f"{key}: https source required")
    for extension, item in extensions.items():
        key = item.get("source_key")
        need(key in by_key, f"{extension}: source key missing from registry")
        nonempty_text(item.get("coverage"), f"{extension}.coverage")
    scenarios = model.get("acceptance_scenarios")
    need(isinstance(scenarios, list) and len(scenarios) >= 7, "acceptance scenarios")
    ids = set()
    for scenario in scenarios:
        sid = scenario.get("id")
        need(sid not in ids, f"duplicate scenario {sid}")
        ids.add(sid)
        for field in ("id", "input", "expected_state", "expected_behavior"):
            nonempty_text(scenario.get(field), f"scenario.{field}")
        need(scenario["expected_state"] in STATES, f"{sid}: unknown state")
    guards = model.get("negative_guards")
    need(isinstance(guards, list) and len(guards) >= 5 and all(isinstance(g, str) and g.strip() for g in guards), "negative guards")
    procedure = model.get("decision_procedure")
    need(isinstance(procedure, list) and len(procedure) == 7, "decision procedure")
    records = taxonomy.get("skills")
    need(isinstance(records, list) and len(records) == 159, "AM-03 accepted index count")
    assessments = [record.get("jurisdiction", {}).get("assessment") for record in records]
    need(set(assessments) <= INDEX_ASSESSMENTS, "AM-03 index contains an unmapped applicability state")
    need(set(assessments) == INDEX_ASSESSMENTS, "AM-03 index must retain both baseline applicability states")
    need(taxonomy.get("classification_status") == "BASELINE_PENDING_AM04_AM05_FORMALIZATION", "AM-03 freeze status")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        model = json.loads((root / "docs/architecture/canadian-jurisdiction-model.json").read_text(encoding="utf-8"))
        registry = json.loads((root / "docs/architecture/canadian-source-registry.json").read_text(encoding="utf-8"))
        taxonomy = json.loads((root / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8-sig"))
        validate(model, registry, taxonomy)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: AM-04 model; {len(model['flags'])} flags; {len(model['applicability_states'])} applicability states; "
          f"{len(registry['sources'])} source records; {len(model['extension_pattern'])} initial extensions; "
          f"{len(model['acceptance_scenarios'])} acceptance scenarios; no legal applicability or skill behavior evaluated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
