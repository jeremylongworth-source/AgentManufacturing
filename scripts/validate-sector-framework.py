"""Validate AM-29 planning architecture and conservative coverage inspection."""
import copy
import importlib.util
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def need(value, message):
    if not value:
        raise ValueError(message)

def main():
    try:
        registry = read("specializations/registry.json")
        need(registry["schema_version"] == "AM-29-specialization-contract-1" and registry["status"] == "FRAMEWORK_READY", "Registry contract")
        roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8").split("## AM-29: Sector specialization framework", 1)[1].split("## AM-30:", 1)[0]
        groups = set(re.search(r"```text\n(.*?)\n```", roadmap, re.S).group(1).splitlines())
        priorities = registry["priorities"]
        need(len(priorities) == 12 and {p["id"] for p in priorities} == groups, "Twelve roadmap priorities")
        need({p["rank"] for p in priorities} == set(range(1, 13)), "Unique ranks")
        need(all(p["phase"] and p["rationale"] for p in priorities), "Priority rationale")
        domain = (ROOT / "docs/architecture/domain-contract.md").read_text(encoding="utf-8").split("## D-05:", 1)[1].split("## D-06:", 1)[0]
        labels = set(re.findall(r"^\| `([a-z-]+)` \|", domain, re.M))
        records = {c["id"]: c for c in registry["candidates"]}
        need(len(records) == len(registry["candidates"]) == 18 and set(records) == labels, "D-05 label coverage")
        need(records["wood-paper"]["kind"] == "umbrella_alias" and records["wood-paper"]["related_candidates"] == ["wood-products", "pulp-paper"], "Wood umbrella")
        need(records["process-manufacturing"]["kind"] == "operating_mode", "Operating mode")
        for label in ("welding", "additive-manufacturing"):
            need(records[label]["kind"] == "process_overlay", "Cross-sector process")
        skills = {s["name"] for s in read("docs/architecture/taxonomy-index.yaml")["skills"]}
        roles = {r["name"] for r in read("skillsets/index.json")["skillsets"]}
        for record in records.values():
            need(record["implementation_path"] is None and record["requirement_sources"] == [], "Unimplemented coverage overstated")
            expected_status = {"umbrella_alias": "CONTEXT_REQUIRED", "operating_mode": "GENERIC_MODE_ONLY"}.get(record["kind"], "PLANNED_NOT_IMPLEMENTED")
            need(record["status"] == expected_status, "Candidate state")
            need(record["core_skill_refs"] and set(record["core_skill_refs"]) <= skills, "Core references")
            need(record["role_refs"] and set(record["role_refs"]) <= roles, "Role references")
            need(set(record["related_candidates"]) <= set(records), "Candidate relationship")
            need(all(record.get(k) for k in ("scope", "exclusions", "scope_questions", "readiness_gaps", "acceptance_case")), "Candidate scope contract")
        need(not list((ROOT / "specializations").rglob("SKILL.md")), "Unexpected sector package implementation")
        for field in ("requirement_deltas", "source_records", "rights_and_access", "applicability_basis", "observed_evaluation", "version_history"):
            need(field in registry["required_future_package_fields"], "Future package contract")
        for field in ("source_key", "source_locator", "effective_version", "applicability_basis", "review_owner"):
            need(field in registry["requirement_delta_fields"], "Requirement provenance")
        need(len(registry["promotion_gates"]) >= 8, "Promotion gates")
        for path in ("source_contract", "freshness_contract", "taxonomy", "composition"):
            need((ROOT / registry[path]).is_file(), "Referenced contract missing")
        spec = importlib.util.spec_from_file_location("coverage", ROOT / "scripts/inspect-sector-coverage.py")
        inspector = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(inspector)
        fixtures = read("tests/fixtures/am29-sector-coverage.json")["cases"]
        need(len(fixtures) == len({f["id"] for f in fixtures}) == 14, "Fixture coverage")
        for f in fixtures:
            result = inspector.assess(f["input"], registry)
            for key, value in f["expected"].items():
                need(result[key] == value, f"{f['id']}: {key}")
            need(result["generic_analysis_allowed"] and not result["sector_conclusion_supported"], "Coverage overclaim")
            need(result["execution"] == "NOT_EXECUTED" and result["applicability"] == "NOT_ASSESSED", "Inspector execution boundary")
        invalid = [None, {}, {"labels": "automotive", "sector_dependent": True}, {"labels": [None], "sector_dependent": True}, {"labels": [], "sector_dependent": "yes"}]
        for request in invalid:
            try:
                inspector.assess(request, registry)
            except ValueError:
                pass
            else:
                raise ValueError("Malformed request accepted")
        promoted = copy.deepcopy(registry)
        promoted["candidates"][0]["implementation_path"] = "unverified/SKILL.md"
        try:
            inspector.assess({"labels": [promoted["candidates"][0]["id"]], "sector_dependent": True}, promoted)
        except ValueError:
            pass
        else:
            raise ValueError("Unsupported promotion accepted")
        scenarios = [s for s in read("tests/expected-routing.yaml")["scenarios"] if s["scenario_id"].startswith("AM29-")]
        need(len(scenarios) == 8 and all(set(s["sector_labels"]) <= labels for s in scenarios), "AM-29 scenarios")
        evaluation = (ROOT / "tests/evaluations/AM-29-specialization-acceptance.md").read_text(encoding="utf-8")
        need(all(t in evaluation for t in ("READY_FOR_REVIEW", "NOT_RUN", "Residual risk")), "Evaluation evidence")
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("PASS: AM-29; 12 priorities, 18 labels, 14 coverage fixtures, six rejection checks and eight scenarios. No sector requirements implemented; model behavior NOT_RUN.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
