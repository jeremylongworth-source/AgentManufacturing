"""Validate the AM-03 frozen catalogue, audit, provenance, graph and projections."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


CRITERIA = {"atomicity", "duplicate_responsibility", "naming", "dependency_order",
            "regulatory_scope", "engineering_boundary", "testability", "specialization_need"}
P0 = {"calculate-oee", "build-production-plan", "triage-nonconformance",
      "review-lockout-program", "assess-made-in-canada-claim"}
CLASS_STATUS = "BASELINE_PENDING_AM04_AM05_FORMALIZATION"
SAFETY = {"ROUTINE", "REGULATED", "HAZARDOUS_OPERATION", "ENGINEERING_OR_CERTIFICATION_BOUNDARY"}
FLAGS = {"CANADA_FEDERAL", "PROVINCIAL_REQUIRED", "SECTOR_REGULATED", "STANDARDS_DEPENDENT"}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def string_list(value: Any, label: str, nonempty: bool = False) -> None:
    need(isinstance(value, list) and all(text(x) for x in value), f"{label}: expected string list")
    need(len(value) == len(set(value)), f"{label}: duplicates")
    need(not nonempty or bool(value), f"{label}: empty list")


def objects(value: Any, label: str) -> None:
    need(isinstance(value, list) and all(isinstance(x, dict) for x in value), f"{label}: expected object list")


def validate(data: Any, draft: dict[str, Any], draft_hash: str) -> None:
    need(isinstance(data, dict), "index: expected object")
    need(data.get("schema_version") == "AM-03-taxonomy-1", "index: schema version")
    need(data.get("status") == "TAXONOMY_FROZEN_NOT_IMPLEMENTED", "index: false implementation status")
    need(data.get("classification_status") == CLASS_STATUS, "index: classification must remain baseline pending formalization")
    need(data.get("draft_sha256") == draft_hash, "index: draft hash mismatch")
    need(data.get("draft_register") == "docs/architecture/candidate-register-v0.1.json", "index: draft reference mismatch")
    for key in ("skills", "audit_records", "families", "requirements", "original_routes", "dependency_edges"):
        objects(data.get(key), key)
    need(data["requirements"] == draft["requirements"], "requirements: unexplained change from draft")
    req_ids = {r["id"] for r in data["requirements"]}
    families = [f.get("id") for f in data["families"]]
    need(families == [f"{i:02}" for i in range(1, 21)], "families: require ordered 01 through 20")
    records = data["skills"]
    names = [c.get("name") for c in records]
    string_list(names, "accepted names", True)
    need(all(re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)+", n) for n in names), "accepted names: invalid naming")
    by_name = {c["name"]: c for c in records}
    draft_by_name = {c["name"]: c for c in draft["candidates"]}
    order = data.get("dependency_order")
    string_list(order, "dependency order")
    need(set(order) == set(names), "dependency order: missing or invented record")
    pos = {n: i + 1 for i, n in enumerate(order)}
    expected_edges = []
    expected_fields = set(draft["candidates"][0]) | {
        "draft_names", "audit_distinction", "acceptance_scenario", "classification_status",
        "acceptance_status", "dependency_order",
    }
    for c in records:
        name = c["name"]
        need(set(c) == expected_fields, f"{name}: missing/unexpected record fields")
        need(c.get("family") in families, f"{name}: unknown family")
        need(isinstance(c.get("tier"), str) and c["tier"] in {"CORE", "CANADA_OVERLAY"}, f"{name}: invalid tier")
        need(isinstance(c.get("safety_class"), str) and c["safety_class"] in SAFETY, f"{name}: invalid safety class")
        need(isinstance(c.get("priority"), str) and c["priority"] in {"P0", "P1", "P2"}, f"{name}: invalid priority")
        need(c.get("status") == "TAXONOMY_ACCEPTED_NOT_IMPLEMENTED", f"{name}: false skill status")
        need(c.get("classification_status") == CLASS_STATUS, f"{name}: false classification status")
        need(c.get("acceptance_status") == "SPECIFIED_NOT_EXECUTED", f"{name}: false test execution status")
        for key in ("boundary", "audit_distinction", "acceptance_scenario"):
            need(text(c.get(key)), f"{name}: missing {key}")
        string_list(c.get("inputs"), f"{name}.inputs", True)
        string_list(c.get("outputs"), f"{name}.outputs", True)
        need(len(c["outputs"]) == 1, f"{name}: one primary output required")
        string_list(c.get("draft_names"), f"{name}.draft_names", True)
        need(set(c["draft_names"]) <= set(draft_by_name), f"{name}: unknown draft provenance")
        string_list(c.get("source_names"), f"{name}.source_names")
        sources = {s for n in c["draft_names"] for s in draft_by_name[n]["source_names"]}
        need(set(c["source_names"]) == sources, f"{name}: original source provenance mismatch")
        need(isinstance(c.get("addition_rationale"), str), f"{name}: invalid addition rationale")
        need(bool(sources) or text(c["addition_rationale"]), f"{name}: unexplained addition")
        j = c.get("jurisdiction")
        need(isinstance(j, dict), f"{name}: invalid jurisdiction")
        string_list(j.get("flags"), f"{name}.flags")
        need(set(j["flags"]) <= FLAGS, f"{name}: unknown applicability flag")
        need(j.get("assessment") == ("PENDING_CONTEXT" if j["flags"] else "GENERIC_METHOD_ONLY"), f"{name}: false applicability assessment")
        need(text(j.get("note")), f"{name}: missing jurisdiction note")
        if c["tier"] == "CANADA_OVERLAY":
            need(bool(set(j["flags"]) & {"CANADA_FEDERAL", "PROVINCIAL_REQUIRED"}), f"{name}: overlay lacks jurisdiction context")
        sector = c.get("sector_dependency")
        need(isinstance(sector, dict) and isinstance(sector.get("mode"), str) and
             sector["mode"] in {"NONE_FOR_GENERIC_METHOD", "CONDITIONAL_CONTEXT"}, f"{name}: invalid sector mode")
        need(sector.get("sectors") == [] and text(sector.get("note")), f"{name}: undeclared sector package or missing note")
        deps = c.get("dependencies")
        need(isinstance(deps, dict) and set(deps) == {"evidence_reuse", "requirements"}, f"{name}: dependency kinds")
        string_list(deps["evidence_reuse"], f"{name}.evidence_reuse")
        string_list(deps["requirements"], f"{name}.requirements")
        need(set(deps["requirements"]) <= req_ids, f"{name}: unknown shared requirement")
        need(type(c.get("dependency_order")) is int and c["dependency_order"] == pos[name], f"{name}: order mismatch")
        for dep in deps["evidence_reuse"]:
            need(dep in by_name, f"{name}: unknown provider {dep}")
            need(dep != name and pos[dep] < pos[name], f"{name}: invalid order, self edge or cycle")
            need(c["tier"] != "CORE" or by_name[dep]["tier"] == "CORE", f"{name}: core-to-overlay dependency")
            expected_edges.append((dep, name))
    for f in data["families"]:
        count = sum(c["family"] == f["id"] for c in records)
        need(count > 0 and type(f.get("accepted_count")) is int and count == f["accepted_count"], f"family {f['id']}: count/coverage mismatch")
    need({c["name"] for c in records if c["priority"] == "P0"} == P0, "reference skills: P0 drift")
    actual_edges = []
    for e in data["dependency_edges"]:
        need(text(e.get("provider")) and text(e.get("consumer")), "edges: missing endpoint")
        need(e.get("type") == "EVIDENCE_REUSE" and text(e.get("equivalent_input")), "edges: must allow supplied evidence, not mandatory runtime execution")
        actual_edges.append((e["provider"], e["consumer"]))
    need(Counter(actual_edges) == Counter(expected_edges), "edges: graph differs from accepted record dependencies")

    audit_names = [a.get("draft_name") for a in data["audit_records"]]
    string_list(audit_names, "audit draft names")
    need(set(audit_names) == set(draft_by_name), "audit: missing or invented draft record")
    routes = {}
    for a in data["audit_records"]:
        name, target = a["draft_name"], a.get("target")
        need(isinstance(target, str) and target in by_name, f"audit {name}: unknown target")
        need(a.get("verdict") in ("RETAIN", "EXPAND_SCOPE", "RENAME_AND_EXPAND", "MERGE"), f"audit {name}: unresolved disposition")
        if a["verdict"] in ("RETAIN", "EXPAND_SCOPE"):
            need(name == target, f"audit {name}: retained name changed")
        else:
            need(name != target, f"audit {name}: renamed/merged target unchanged")
        need(name in by_name[target]["draft_names"], f"audit {name}: target lacks reverse provenance")
        criteria = a.get("criteria")
        need(isinstance(criteria, dict) and set(criteria) == CRITERIA, f"audit {name}: eight criteria required")
        for key, item in criteria.items():
            need(isinstance(item, dict), f"audit {name}.{key}: invalid criterion")
            expected = "SPECIFIED_NOT_EXECUTED" if key == "testability" else "RESOLVED"
            need(item.get("verdict") == expected, f"audit {name}.{key}: unresolved or false execution verdict")
            need(isinstance(item.get("evidence"), (str, dict)) and bool(item["evidence"]), f"audit {name}.{key}: missing evidence")
        c = by_name[target]
        need(criteria["dependency_order"]["evidence"].get("position") == pos[target] and
             criteria["dependency_order"]["evidence"].get("evidence_reuse") == c["dependencies"]["evidence_reuse"], f"audit {name}: stale dependency evidence")
        need(criteria["engineering_boundary"]["evidence"] == {"safety_class": c["safety_class"], "boundary": c["boundary"]}, f"audit {name}: stale safety evidence")
        reg = criteria["regulatory_scope"]["evidence"]
        need(reg.get("tier") == c["tier"] and reg.get("flags") == c["jurisdiction"]["flags"] and
             reg.get("assessment") == c["jurisdiction"]["assessment"], f"audit {name}: stale regulatory evidence")
        routes[name] = target
    need(Counter(n for c in records for n in c["draft_names"]) == Counter(audit_names), "accepted records: missing/duplicate draft provenance")
    expected_routes = [{"source_name": s["name"], "source_family": s["family"],
                        "accepted_targets": sorted({routes[n] for n in s["targets"]})}
                       for s in draft["source_dispositions"]]
    need(data["original_routes"] == expected_routes, "original routes: missing, stale or invented source mapping")


def projections(data: dict[str, Any]) -> list[tuple[str, str, list[str]]]:
    result = []
    rows = ["| Accepted skill | Family | Tier | Safety class | Priority | Primary output |", "|---|---|---|---|---|---|"]
    rows += ["| " + " | ".join([c["name"], c["family"], c["tier"], c["safety_class"], c["priority"], c["outputs"][0]]) + " |" for c in data["skills"]]
    result.append(("master-taxonomy-v1.md", "accepted-index", rows))
    rows = ["| Order | Accepted skill |", "|---|---|"] + [f"| {i} | {n} |" for i, n in enumerate(data["dependency_order"], 1)]
    result.append(("dependency-map.md", "dependency-order", rows))
    rows = ["| Provider | Consumer | Type |", "|---|---|---|"] + [f"| {e['provider']} | {e['consumer']} | {e['type']} |" for e in data["dependency_edges"]]
    result.append(("dependency-map.md", "dependency-edges", rows))
    rows = ["| Draft candidate | Disposition | Accepted target | Responsibility distinction | Future scenario / expected outcome |", "|---|---|---|---|---|"]
    rows += ["| " + " | ".join([a["draft_name"], a["verdict"], a["target"], a["criteria"]["atomicity"]["evidence"], a["criteria"]["testability"]["evidence"]]) + " |" for a in data["audit_records"]]
    result.append(("taxonomy-audit-v1.md", "audit-index", rows))
    return result


def validate_projection(content: str, marker: str, expected: list[str]) -> None:
    start, end = f"<!-- {marker}:start -->", f"<!-- {marker}:end -->"
    need(content.count(start) == 1 and content.count(end) == 1, f"{marker}: missing/duplicate projection markers")
    need(content.index(start) < content.index(end), f"{marker}: reversed markers")
    actual = content.split(start, 1)[1].split(end, 1)[0].strip().splitlines()
    need(actual == expected, f"{marker}: document rows differ from index")


def no_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        need(key not in result, f"JSON/YAML: duplicate key {key}")
        result[key] = value
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.repo_root.resolve()
    try:
        draft_bytes = (root / "docs/architecture/candidate-register-v0.1.json").read_bytes()
        draft = json.loads(draft_bytes, object_pairs_hook=no_duplicate_keys)
        data = json.loads((root / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8-sig"), object_pairs_hook=no_duplicate_keys)
        validate(data, draft, hashlib.sha256(draft_bytes).hexdigest())
        for filename, marker, rows in projections(data):
            validate_projection((root / "docs/architecture" / filename).read_text(encoding="utf-8"), marker, rows)
    except (OSError, UnicodeError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: {len(data['skills'])} accepted records; {len(data['audit_records'])} drafts audited across eight criteria; "
          f"{len(data['original_routes'])} original names traced; {len(data['dependency_edges'])} ordered evidence-reuse edges; "
          "core isolation, reference priorities, pending classifications and all document projections verified. No skill behavior evaluated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
