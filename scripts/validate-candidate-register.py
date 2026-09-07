"""Validate AM-02 draft data and provenance; this does not evaluate agent behavior."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
from typing import Any


FIELDS = {
    "name", "family", "tier", "jurisdiction", "safety_class", "sector_dependency",
    "inputs", "outputs", "dependencies", "priority", "boundary", "source_names",
    "addition_rationale", "status",
}
SAFETY = {
    "ROUTINE", "REGULATED", "HAZARDOUS_OPERATION",
    "ENGINEERING_OR_CERTIFICATION_BOUNDARY",
}
FLAGS = {"CANADA_FEDERAL", "PROVINCIAL_REQUIRED", "SECTOR_REGULATED", "STANDARDS_DEPENDENT"}
REFERENCE_SKILLS = {
    "calculate-oee", "build-production-plan", "triage-nonconformance",
    "review-lockout-program", "assess-made-in-canada-claim",
}
NAME = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)+")


def original_candidates(text: str) -> list[tuple[str, str]]:
    """Read only candidate-like names in numbered source-family text fences."""
    result = []
    for family, block in re.findall(r"^## (\d+)\. ([\s\S]*?)(?=^## \d+\.|\Z)", text, re.M):
        for fence in re.findall(r"```text\n(.*?)```", block, re.S):
            for name in fence.splitlines():
                if re.fullmatch(r"[a-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+", name):
                    result.append((f"{int(family):02}", name))
    return result


def validate(data: Any, source_text: str) -> list[str]:
    errors: list[str] = []

    def check(ok: bool, message: str) -> None:
        if not ok:
            errors.append(message)

    def strings(value: Any, label: str, nonempty: bool = False) -> bool:
        ok = isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value)
        check(ok, f"{label}: expected list of nonblank strings")
        if ok:
            check(len(value) == len(set(value)), f"{label}: duplicate values")
            if nonempty:
                check(bool(value), f"{label}: empty list")
        return ok

    if not isinstance(data, dict):
        return ["register: expected object"]
    check(data.get("schema_version") == "AM-02-draft-1", "register: unsupported schema version")
    check(data.get("status") == "DRAFT_NOT_FROZEN", "register: must remain DRAFT_NOT_FROZEN")
    for key in ("source_taxonomy", "domain_contract", "scope_boundaries", "date"):
        check(isinstance(data.get(key), str) and bool(data[key].strip()), f"register: missing {key}")
    for key, filename in (("source_taxonomy", "master-taxonomy-v0.1.md"),
                          ("domain_contract", "domain-contract.md"),
                          ("scope_boundaries", "scope-boundaries.md")):
        check(data.get(key) == f"docs/architecture/{filename}", f"register: unexpected {key} reference")
    for key in ("families", "requirements", "source_dispositions", "candidates"):
        if not isinstance(data.get(key), list) or not all(isinstance(x, dict) for x in data[key]):
            errors.append(f"register: {key} must be a list of objects")
    if errors:
        return errors

    family_ids = [f.get("id") for f in data["families"]]
    check(family_ids == [f"{n:02}" for n in range(1, 21)], "families: require ordered 01 through 20")
    if errors:
        return errors
    requirements = data["requirements"]
    req_ids = [r.get("id") for r in requirements]
    if not all(isinstance(x, str) and x for x in req_ids):
        return errors + ["requirements: invalid IDs"]
    check(len(req_ids) == len(set(req_ids)), "requirements: duplicate IDs")
    for r in requirements:
        for key in ("kind", "owner_wave", "condition"):
            check(isinstance(r.get(key), str) and bool(r[key].strip()), f"requirement {r['id']}: missing {key}")
        check(r.get("status") == "PLANNED_REQUIREMENT", f"requirement {r['id']}: false implementation status")

    records = data["candidates"]
    names = [c.get("name") for c in records]
    if not all(isinstance(n, str) and NAME.fullmatch(n) for n in names):
        return errors + ["candidates: invalid lowercase kebab-case name"]
    check(len(names) == len(set(names)), "candidates: duplicate names")
    by_name = {c["name"]: c for c in records}
    counts = Counter(c.get("family") for c in records if isinstance(c.get("family"), str))
    for f in data["families"]:
        fid = f.get("id")
        check(isinstance(f.get("name"), str) and bool(f["name"].strip()), f"family {fid}: missing name")
        check(counts[fid] > 0, f"family {fid}: no candidates")
        check(type(f.get("candidate_count")) is int and f["candidate_count"] == counts[fid], f"family {fid}: count mismatch")
    adjacency: dict[str, list[str]] = {}
    for c in records:
        name = c["name"]
        check(set(c) == FIELDS, f"{name}: missing or unexpected candidate fields")
        check(c.get("family") in family_ids, f"{name}: unknown family")
        check(isinstance(c.get("tier"), str) and c["tier"] in {"CORE", "CANADA_OVERLAY"}, f"{name}: invalid draft tier")
        check(isinstance(c.get("safety_class"), str) and c["safety_class"] in SAFETY, f"{name}: invalid safety class")
        check(isinstance(c.get("priority"), str) and c["priority"] in {"P0", "P1", "P2"}, f"{name}: invalid priority")
        check(c.get("status") == "CANDIDATE_DRAFT", f"{name}: false implementation status")
        check(isinstance(c.get("boundary"), str) and bool(c["boundary"].strip()), f"{name}: missing boundary")
        strings(c.get("inputs"), f"{name}.inputs", True)
        if strings(c.get("outputs"), f"{name}.outputs", True):
            check(len(c["outputs"]) == 1, f"{name}: specify one primary output")
        strings(c.get("source_names"), f"{name}.source_names")
        check(isinstance(c.get("addition_rationale"), str), f"{name}: invalid addition rationale")
        if c.get("source_names") == []:
            check(bool(c.get("addition_rationale")), f"{name}: addition needs rationale")
        j = c.get("jurisdiction")
        if not isinstance(j, dict):
            errors.append(f"{name}: jurisdiction must be an object")
        else:
            if strings(j.get("flags"), f"{name}.jurisdiction.flags"):
                check(set(j["flags"]) <= FLAGS, f"{name}: unknown jurisdiction flag")
                expected_assessment = "PENDING_CONTEXT" if j["flags"] else "GENERIC_METHOD_ONLY"
                check(j.get("assessment") == expected_assessment, f"{name}: invalid/premature applicability assessment")
                if c.get("tier") == "CANADA_OVERLAY":
                    check(bool(set(j["flags"]) & {"CANADA_FEDERAL", "PROVINCIAL_REQUIRED"}), f"{name}: Canadian overlay lacks jurisdiction context")
            check(isinstance(j.get("note"), str) and bool(j["note"].strip()), f"{name}: missing jurisdiction note")
        s = c.get("sector_dependency")
        if not isinstance(s, dict):
            errors.append(f"{name}: sector_dependency must be an object")
        else:
            check(isinstance(s.get("mode"), str) and s["mode"] in {"NONE_FOR_GENERIC_METHOD", "CONDITIONAL_CONTEXT"}, f"{name}: invalid sector mode")
            check(s.get("sectors") == [], f"{name}: sector package requirements deferred to specialization audit")
            check(isinstance(s.get("note"), str) and bool(s["note"].strip()), f"{name}: missing sector note")
        deps = c.get("dependencies")
        if not isinstance(deps, dict):
            errors.append(f"{name}: dependencies must be an object")
            continue
        if strings(deps.get("candidates"), f"{name}.dependencies.candidates"):
            adjacency[name] = deps["candidates"]
            for dep in deps["candidates"]:
                check(dep in by_name, f"{name}: unknown candidate dependency {dep}")
                check(dep != name, f"{name}: self dependency")
                if dep in by_name and c.get("tier") == "CORE":
                    check(by_name[dep].get("tier") == "CORE", f"{name}: core cannot require overlay {dep}")
        if strings(deps.get("requirements"), f"{name}.dependencies.requirements"):
            check(set(deps["requirements"]) <= set(req_ids), f"{name}: unknown requirement dependency")

    # Reject structural cycles; final architectural dependency ordering remains AM-03.
    visited: set[str] = set()
    active: set[str] = set()

    def visit(name: str) -> None:
        if name in active:
            errors.append(f"dependencies: cycle at {name}")
            return
        if name in visited:
            return
        active.add(name)
        for dep in adjacency.get(name, []):
            visit(dep)
        active.remove(name)
        visited.add(name)

    for name in adjacency:
        visit(name)

    original = original_candidates(source_text)
    check(bool(original), "source taxonomy: no candidates parsed")
    observed = []
    reverse: dict[str, list[str]] = {n: [] for n in names}
    for source in data["source_dispositions"]:
        name, family = source.get("name"), source.get("family")
        if not isinstance(name, str) or not isinstance(family, str):
            errors.append("source disposition: invalid name or family")
            continue
        observed.append((family, name))
        action = source.get("disposition")
        if not isinstance(action, str):
            errors.append(f"source {name}: invalid disposition type")
            continue
        check(action in {"KEEP", "MERGE", "RENAME", "MOVE", "SPLIT", "DEFER"}, f"source {name}: invalid disposition")
        check(isinstance(source.get("reason"), str) and bool(source["reason"].strip()), f"source {name}: missing rationale")
        if not strings(source.get("targets"), f"source {name}.targets"):
            continue
        targets = source["targets"]
        if action == "DEFER":
            check(not targets, f"source {name}: deferred source has targets")
        elif action == "SPLIT":
            check(len(targets) >= 2, f"source {name}: split needs multiple targets")
        else:
            check(len(targets) == 1, f"source {name}: requires one target")
        for target in targets:
            check(target in by_name, f"source {name}: unresolved target {target}")
            if target not in by_name:
                continue
            reverse[target].append(name)
            if action in {"KEEP", "MOVE"}:
                check(name == target, f"source {name}: {action} changed the name")
                same_family = family == by_name[target].get("family")
                check(same_family if action == "KEEP" else not same_family, f"source {name}: {action} family mismatch")
            if action == "RENAME":
                check(name != target, f"source {name}: rename did not change name")
    check(Counter(observed) == Counter(original), "source dispositions: missing duplicate or invented original candidates")
    for c in records:
        if isinstance(c.get("source_names"), list) and all(isinstance(s, str) for s in c["source_names"]):
            check(Counter(c["source_names"]) == Counter(reverse[c["name"]]), f"{c['name']}: source_names do not match provenance")
    check({c["name"] for c in records if c.get("priority") == "P0"} == REFERENCE_SKILLS, "priority: P0 must identify exactly the five AM-10 reference skills")
    return errors


def validate_index(data: dict[str, Any], catalogue: str) -> list[str]:
    start, end = "<!-- candidate-index:start -->", "<!-- candidate-index:end -->"
    if catalogue.count(start) != 1 or catalogue.count(end) != 1:
        return ["review index: missing or duplicate delimiters"]
    actual = catalogue.split(start, 1)[1].split(end, 1)[0].strip().splitlines()
    expected = ["| Candidate | Family | Tier | Safety class | Priority | Primary output |",
                "|---|---|---|---|---|---|"]
    for c in data["candidates"]:
        expected.append("| " + " | ".join([
            c["name"], c["family"], c["tier"], c["safety_class"], c["priority"], c["outputs"][0]
        ]) + " |")
    return [] if actual == expected else ["review index: rows differ from canonical register"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--register", type=Path, help="Alternate register path for review; relative to repo root.")
    args = parser.parse_args()
    root = args.repo_root.resolve()
    register = args.register or Path("docs/architecture/candidate-register-v0.1.json")
    if not register.is_absolute():
        register = root / register
    try:
        data = json.loads(register.read_text(encoding="utf-8-sig"))
        source_text = (root / "docs/architecture/master-taxonomy-v0.1.md").read_text(encoding="utf-8-sig")
        errors = validate(data, source_text)
        if not errors:
            catalogue = (root / "docs/architecture/candidate-taxonomy-v0.1.md").read_text(encoding="utf-8-sig")
            errors.extend(validate_index(data, catalogue))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(data['candidates'])} draft candidates; {len(data['families'])} families; "
          f"{len(data['source_dispositions'])} original names traced; fields, metadata, provenance, "
          "dependency references/cycles, core isolation, AM-10 priorities, and review index checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
