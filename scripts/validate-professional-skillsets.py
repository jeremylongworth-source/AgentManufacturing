"""Validate AM-28 role composition and run the read-only resolver tests."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def need(value, message):
    if not value:
        raise ValueError(message)

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    try:
        spec = importlib.util.spec_from_file_location("am28_resolver", ROOT / "scripts/resolve-skillset.py")
        resolver = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(resolver)
        framework = (ROOT / "docs/architecture/domain-framework.md").read_text(encoding="utf-8")
        section = framework.split("## Professional skillsets", 1)[1].split("## ", 1)[0]
        expected = set(re.search(r"```text\n(.*?)\n```", section, re.S).group(1).splitlines())
        index = read("skillsets/index.json")
        entries = index["skillsets"]
        need(len(entries) == 18 and {r["name"] for r in entries} == expected, "Preserved role coverage")
        need({p.name for p in (ROOT / "skillsets").iterdir() if p.is_dir()} == expected, "Role directory inventory")
        contract = read("skillsets/composition-contract.json")
        need(contract["schema_version"] == "AM-28-composition-1" and contract["license"] == "MIT", "Composition schema/licence")
        need(all(contract.get(k) for k in ("selection_rule", "evidence_reuse_rule", "gate_rule", "sector_rule", "output_fields")), "Shared boundaries")
        taxonomy = {s["name"]: s for s in read("docs/architecture/taxonomy-index.yaml")["skills"]}
        need(set(contract["package_paths"]) == set(taxonomy), "Canonical package coverage")
        for name, relative in contract["package_paths"].items():
            p = (ROOT / relative).resolve()
            need(p.is_relative_to(ROOT) and p.is_file() and p.parent.name == name and p.name == "SKILL.md", "Invalid canonical path")
        need({o["name"] for o in contract["overlays"]} == {"jurisdiction", "source", "provincial", "whmis"}, "Overlay routes")
        for overlay in contract["overlays"]:
            need(overlay["when"] and set(overlay["skills"]) <= set(taxonomy), "Overlay target")
        workflows = 0
        for entry in entries:
            name = entry["name"]
            need(entry["manifest"] == f"skillsets/{name}/skillset.yaml" and entry["guide"] == f"skillsets/{name}/SKILLSET.md", "Role paths")
            m = read(entry["manifest"])
            need(m["schema_version"] == "AM-28-skillset-1" and m["name"] == name, "Role identity")
            need(m["status"] == "STRUCTURALLY_READY" and m["license"] == "MIT", "Role boundary")
            need(m["composition_contract"] == "../composition-contract.json", "Shared contract path")
            need(len(m["skills"]) == len(set(m["skills"])) and set(m["skills"]) <= set(taxonomy), "Atomic membership")
            need(len({w["id"] for w in m["workflows"]}) == len(m["workflows"]), "Duplicate workflow")
            need(set(m["skills"]) == {s for w in m["workflows"] for s in w["skills"]}, "Workflow inventory")
            guide = (ROOT / entry["guide"]).read_text(encoding="utf-8")
            need("NOT_RUN" in guide, "Guide runtime boundary")
            for w in m["workflows"]:
                need(all(w.get(k) for k in ("id", "trigger", "required_inputs", "skills", "output", "review_boundary")), "Workflow contract")
                need(len(w["skills"]) == len(set(w["skills"])), "Duplicate workflow target")
                for overlays in ([], [o["name"] for o in contract["overlays"]]):
                    plan = resolver.resolve(name, w["id"], overlays)
                    refs = plan["ordered_references"]
                    positions = {r["name"]: i for i, r in enumerate(refs)}
                    need(len(positions) == len(refs), "Repeated resolved skill")
                    for ref in refs:
                        for provider in ref["evidence_reuse"]:
                            need(positions[provider] < positions[ref["name"]], "Dependency order")
                    need(plan["execution"] == "NOT_EXECUTED" and plan["evidence_state"] == "NOT_ASSESSED", "Resolver overclaim")
                workflows += 1
        need(workflows == 38, "Workflow coverage")
        scenarios = [s for s in read("tests/expected-routing.yaml")["scenarios"] if s["scenario_id"].startswith("AM28-")]
        need(len(scenarios) == 22 and {s["skillset"] for s in scenarios} == expected, "Role scenario coverage")
        for s in scenarios:
            m = read(f"skillsets/{s['skillset']}/skillset.yaml")
            w = next(w for w in m["workflows"] if w["id"] == s["workflow"])
            need(s["expected_routes"] == w["skills"] and not s["future_routes"], "Scenario target mismatch")
        evaluation = (ROOT / "tests/evaluations/AM-28-professional-skillsets-acceptance.md").read_text(encoding="utf-8")
        need(all(t in evaluation for t in ("READY_FOR_REVIEW", "NOT_RUN", "Residual risk")), "Acceptance evidence")
    except (OSError, ValueError, KeyError, TypeError, StopIteration, AttributeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    result = subprocess.run([sys.executable, str(ROOT / "tests/skillsets/test_resolver.py")], cwd=ROOT)
    if result.returncode:
        return result.returncode
    print("PASS: AM-28; 18 role skillsets, 38 workflows, 22 scenarios and 12 resolver tests. Runtime model behavior NOT_RUN.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
