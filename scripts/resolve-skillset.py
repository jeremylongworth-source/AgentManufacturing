"""Resolve role workflow references only. No skill or model execution."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("Reference escapes repository")
    return json.loads(path.read_text(encoding="utf-8"))

def dependency_order(targets, records):
    ordered, active, done = [], set(), set()
    def visit(name):
        if name in active:
            raise ValueError(f"Evidence dependency cycle: {name}")
        if name in done:
            return
        if name not in records:
            raise ValueError(f"Unknown atomic skill: {name}")
        active.add(name)
        for provider in records[name]["dependencies"]["evidence_reuse"]:
            visit(provider)
        active.remove(name)
        done.add(name)
        ordered.append(name)
    for name in targets:
        visit(name)
    return ordered

def resolve(role, workflow, overlays=(), root=ROOT):
    index = read(root, "skillsets/index.json")
    entry = next((r for r in index["skillsets"] if r["name"] == role), None)
    if entry is None:
        raise ValueError(f"Unknown role: {role}")
    manifest = read(root, entry["manifest"])
    selected = next((w for w in manifest["workflows"] if w["id"] == workflow), None)
    if selected is None:
        raise ValueError(f"Unknown workflow for {role}: {workflow}")
    contract = read(root, "skillsets/composition-contract.json")
    available = {o["name"]: o for o in contract["overlays"]}
    overlays = list(dict.fromkeys(overlays))
    if any(name not in available for name in overlays):
        raise ValueError("Unknown overlay")
    targets = list(dict.fromkeys(selected["skills"] + [s for name in overlays for s in available[name]["skills"]]))
    records = {s["name"]: s for s in read(root, "docs/architecture/taxonomy-index.yaml")["skills"]}
    ordered = dependency_order(targets, records)
    references = []
    for name in ordered:
        relative = contract["package_paths"].get(name)
        if not relative:
            raise ValueError(f"Missing package mapping: {name}")
        path = (root / relative).resolve()
        if not path.is_relative_to(root.resolve()) or path.name != "SKILL.md" or path.parent.name != name or not path.is_file():
            raise ValueError(f"Invalid package reference: {name}")
        references.append({"name": name, "path": relative, "selection": "target" if name in targets else "evidence_provider", "safety_class": records[name]["safety_class"], "evidence_reuse": records[name]["dependencies"]["evidence_reuse"]})
    return {"status": "REFERENCES_RESOLVED", "role": role, "workflow": workflow, "explicit_overlays": overlays, "targets": targets, "ordered_references": references, "output": selected["output"], "review_boundary": selected["review_boundary"], "execution": "NOT_EXECUTED", "evidence_state": "NOT_ASSESSED", "note": contract["evidence_reuse_rule"]}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("role")
    parser.add_argument("workflow")
    parser.add_argument("--overlay", action="append", default=[])
    args = parser.parse_args()
    try:
        result = resolve(args.role, args.workflow, args.overlay)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "ERROR", "message": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
