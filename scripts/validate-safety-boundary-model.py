"""Validate the AM-05 safety and engineering boundary model."""

from __future__ import annotations

import collections
import json
from pathlib import Path
import sys
from typing import Any


CLASSES = {"ROUTINE", "REGULATED", "HAZARDOUS_OPERATION", "ENGINEERING_OR_CERTIFICATION_BOUNDARY"}
TOPICS = {"machine_guarding", "hazardous_energy", "electrical_work", "pressure_equipment", "robotics", "confined_spaces", "hot_work", "hazardous_chemicals", "structural_changes"}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def text(value: Any, label: str) -> None:
    need(isinstance(value, str) and bool(value.strip()), f"{label}: expected non-empty text")


def string_list(value: Any, label: str, minimum: int = 1) -> None:
    need(isinstance(value, list) and len(value) >= minimum and all(isinstance(x, str) and x.strip() for x in value), f"{label}: expected non-empty string list")
    need(len(value) == len(set(value)), f"{label}: duplicates")


def validate(model: dict[str, Any], registry: dict[str, Any], taxonomy: dict[str, Any]) -> None:
    need(model.get("schema_version") == "AM-05-safety-boundary-1", "model schema version")
    need(model.get("status") == "MODEL_READY_NOT_IMPLEMENTED", "model status")
    need(set(model.get("classes", {})) == CLASSES, "four safety classes")
    for name, item in model["classes"].items():
        for field in ("meaning", "required_review"):
            text(item.get(field), f"{name}.{field}")
        string_list(item.get("allowed_support"), f"{name}.allowed_support")
        string_list(item.get("stop_conditions"), f"{name}.stop_conditions")
    composition = model.get("composition")
    need(isinstance(composition, dict), "composition object")
    need(composition.get("static_field") == "safety_class", "static field")
    need(composition.get("precedence") == ["ENGINEERING_OR_CERTIFICATION_BOUNDARY", "HAZARDOUS_OPERATION", "REGULATED", "ROUTINE"], "precedence")
    text(composition.get("rule"), "composition.rule")
    text(composition.get("authorization"), "composition.authorization")
    common = model.get("common_gate")
    need(isinstance(common, dict), "common gate")
    for key in ("input_context", "output_contract", "stop_and_escalate"):
        string_list(common.get(key), f"common_gate.{key}")
    text(common.get("safe_continuation"), "common_gate.safe_continuation")
    gates = model.get("topic_gates")
    need(isinstance(gates, dict) and set(gates) == TOPICS, "nine topic gates")
    registry_keys = set()
    for source in registry.get("sources", []):
        key = source.get("key")
        text(key, "source.key")
        need(key not in registry_keys, f"duplicate source {key}")
        registry_keys.add(key)
        for field in ("publisher", "title", "url", "source_class", "scope", "freshness", "notes"):
            text(source.get(field), f"{key}.{field}")
        need(source["url"].startswith("https://"), f"{key}: HTTPS URL required")
    for topic, gate in gates.items():
        need(gate.get("minimum_class") in CLASSES, f"{topic}: invalid minimum class")
        need(gate.get("escalate_to") in CLASSES, f"{topic}: invalid escalation class")
        for field in ("when", "allowed_support", "prohibited_output"):
            text(gate.get(field), f"{topic}.{field}")
        string_list(gate.get("required_evidence"), f"{topic}.required_evidence", 3)
        string_list(gate.get("source_keys"), f"{topic}.source_keys")
        need(set(gate["source_keys"]) <= registry_keys, f"{topic}: unknown source key")
    scenarios = model.get("acceptance_scenarios")
    need(isinstance(scenarios, list) and len(scenarios) >= 12, "acceptance scenarios")
    scenario_ids = set()
    for scenario in scenarios:
        sid = scenario.get("id")
        text(sid, "scenario.id")
        need(sid not in scenario_ids, f"duplicate scenario {sid}")
        scenario_ids.add(sid)
        for field in ("input", "expected_result"):
            text(scenario.get(field), f"{sid}.{field}")
        need(scenario.get("expected_class") in CLASSES, f"{sid}: invalid expected class")
    string_list(model.get("negative_guards"), "negative_guards", 6)
    records = taxonomy.get("skills")
    need(isinstance(records, list) and len(records) == 159, "AM-03 record count")
    counts = collections.Counter(record.get("safety_class") for record in records)
    need(set(counts) == CLASSES, "AM-03 classes")
    need(counts == collections.Counter({"ROUTINE": 95, "REGULATED": 28, "HAZARDOUS_OPERATION": 11, "ENGINEERING_OR_CERTIFICATION_BOUNDARY": 25}), f"AM-03 class counts changed: {counts}")
    need(taxonomy.get("status") == "TAXONOMY_FROZEN_NOT_IMPLEMENTED", "AM-03 frozen status")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        model = json.loads((root / "docs/architecture/safety-boundary-model.json").read_text(encoding="utf-8"))
        registry = json.loads((root / "docs/architecture/safety-source-registry.json").read_text(encoding="utf-8"))
        taxonomy = json.loads((root / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8-sig"))
        validate(model, registry, taxonomy)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("PASS: AM-05 model; 4 classes; 9 topic gates; "
          f"{len(registry['sources'])} source records; {len(model['acceptance_scenarios'])} acceptance scenarios; "
          "AM-03 safety counts preserved (95/28/11/25); no safety approval, engineering signoff, or skill behavior evaluated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
