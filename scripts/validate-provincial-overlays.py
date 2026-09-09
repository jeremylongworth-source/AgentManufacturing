"""Validate the AM-27 provincial research baseline without asserting legal currency."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = "identify-provincial-safety-overlay"
PACKAGE = "skills/family-20-canadian-compliance/" + NAME
PROVINCES = {"ontario": "Ontario", "british-columbia": "British Columbia", "alberta": "Alberta", "quebec": "Quebec"}
TOPICS = {"ohs", "machinery", "hazardous_energy", "electrical", "pressure_equipment", "environment", "worker_training"}

def need(condition, message):
    if not condition:
        raise ValueError(message)

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def module(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

def main():
    try:
        base = module("scripts/validate-canadian-federal.py", "am27_packages")
        records = base.taxonomy(ROOT)
        base.validate_package(ROOT, NAME, (PACKAGE, "P1", "REGULATED", "PENDING_CONTEXT", ["PROVINCIAL_REQUIRED", "SECTOR_REGULATED"]), records)
        for provider in records[NAME]["dependencies"]["evidence_reuse"]:
            need(any((ROOT / "skills").glob(f"*/{provider}/SKILL.md")), f"Missing provider {provider}")
        sources = read("docs/architecture/am27-provincial-source-records.json")
        by_key = {item["source_key"]: item for item in sources["records"]}
        need(len(by_key) == len(sources["records"]) == 16, "Source count or duplicates")
        source_check = module("scripts/validate-source-standards-standard.py", "am27_sources")
        for key, record in by_key.items():
            source_check.validate_record(record, key)
            need(record["jurisdiction"]["province_or_territory"] in PROVINCES.values(), "Source jurisdiction")
        need(len(sources["claims"]) == 16 and {c["source_key"] for c in sources["claims"]} == set(by_key), "Claim coverage")
        for claim in sources["claims"]:
            need(all(claim.get(k) for k in ("scope", "as_of", "location", "support_status", "claim")), "Claim evidence")
        for key in ("AM27-ON-REG", "AM27-QC-OHS"):
            need(by_key[key]["status"] == "PENDING_REVIEW", "Unresolved legal currency promoted")
        index = read(PACKAGE + "/references/overlay-index.json")
        need({m["id"] for m in index["modules"]} == set(PROVINCES) and len(index["modules"]) == 4, "Four module coverage")
        used = set()
        for item in index["modules"]:
            need(item["province"] == PROVINCES[item["id"]], "Module province mismatch")
            need(item["status"] == "RESEARCH_BASELINE", "Module authority boundary")
            note = (ROOT / PACKAGE / "references" / (item["id"] + ".md")).read_text(encoding="utf-8")
            need(len(item["topics"]) == 7 and {t["topic"] for t in item["topics"]} == TOPICS, "Seven topic coverage")
            for row in item["topics"]:
                need(all(row.get(k) for k in ("source_keys", "research_question", "required_evidence", "review_owner")), "Research row evidence")
                need(row["applicability_state"] == "SOURCE_REVIEW_REQUIRED", "Research not applicability approval")
                for key in row["source_keys"]:
                    need(key in by_key and by_key[key]["jurisdiction"]["province_or_territory"] == item["province"], "Cross-province source substitution")
                    need(key in note, "Source not discoverable in module")
                    used.add(key)
        need(used == set(by_key), "Unreferenced source")
        routing = read("tests/expected-routing.yaml")
        cases = [s for s in routing["scenarios"] if s["scenario_id"].startswith("AM27-")]
        need({s["scenario_id"] for s in cases} == {f"AM27-S{i:02}" for i in range(1, 15)}, "AM-27 scenario coverage")
        for case in cases:
            need(not case["future_routes"], "AM-27 still future")
            need(case["expected_routes"] == ([] if case["route_mode"] == "NO_TRIGGER" else [NAME]), "AM-27 unexpected route")
        evaluation = (ROOT / "tests/evaluations/AM-27-provincial-acceptance.md").read_text(encoding="utf-8")
        for phrase in ("READY_FOR_REVIEW", "NOT_RUN", "Residual risk", NAME):
            need(phrase in evaluation, "Evaluation boundary missing")
        implemented = {p.parent.name for p in (ROOT / "skills").glob("*/*/SKILL.md")}
        need(set(records) <= implemented, "Frozen catalogue package coverage incomplete")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("PASS: AM-27 provincial selector, four modules, 28 topic paths, 16 source records and 14 scenarios; runtime model behavior NOT_RUN.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
