"""Check AM-30 assisted evidence, arithmetic and real reference-component joins.

Does not execute a model or score the semantic quality of its prose.
"""
import copy
from datetime import datetime, date
import importlib.util
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def check(inputs, outputs):
    assert inputs["synthetic"] is True
    assert outputs["evaluation_mode"] == "ASSISTED_SINGLE_SESSION_NONBLIND"
    assert outputs["independent_runtime"] == outputs["baseline"] == "NOT_RUN"
    source = {x["id"]: x for x in inputs["cases"]}
    results = {x["id"]: x for x in outputs["cases"]}
    expected = {"production-shortfall", "quality-escape", "equipment-reliability", "safety-process-change"}
    assert set(source) == set(results) == expected
    assert len(inputs["cases"]) == len(outputs["cases"]) == 4
    paths = read("skillsets/composition-contract.json")["package_paths"]
    for key, result in results.items():
        assert result["authorized"] is False and result["gates"]
        assert result["steps"]
        for step in result["steps"]:
            assert (ROOT / paths[step["skill"]]).is_file()
            assert step["status"] and step["result"] and step["handoff"]
            evidence = source[key]["raw"]
            for part in step["evidence"].split("."):
                evidence = evidence[part]

    def metric(key, name, value):
        assert math.isclose(results[key]["metrics"][name], value, rel_tol=1e-9), (key, name)

    p = source["production-shortfall"]["raw"]
    a, plan = p["actual"], p["plan"]
    metric("production-shortfall", "adherence_percent", sum(o["on_time"] for o in a["orders"])/len(a["orders"])*100)
    metric("production-shortfall", "cycle_mean_minutes", sum(a["cycles_minutes"])/len(a["cycles_minutes"]))
    minutes = sum((datetime.fromisoformat(e["end"])-datetime.fromisoformat(e["start"])).total_seconds()/60 for e in a["downtime"])
    metric("production-shortfall", "downtime_minutes", minutes)
    metric("production-shortfall", "material_need", plan["demand_units"]*plan["components_per_unit"])
    metric("production-shortfall", "labor_need_minutes", plan["demand_units"]*plan["labor_minutes_per_unit"])
    capacity = math.floor(min(plan["equipment_minutes"]/plan["planning_cycle_minutes"], plan["available_components"]/plan["components_per_unit"], plan["qualified_labor_minutes"]/plan["labor_minutes_per_unit"]))
    metric("production-shortfall", "capacity_units", capacity)
    metric("production-shortfall", "unmet_units", plan["demand_units"]-capacity)

    q = source["quality-escape"]["raw"]
    ancestors = {r["input"] for r in q["relationships"] if r["output"] == q["target"]}
    descendants = [r for r in q["relationships"] if r["input"] in ancestors]
    metric("quality-escape", "known_descendant_units", sum(r["units"] for r in descendants))
    metric("quality-escape", "traceable_uses_after_due", sum(date.fromisoformat(u["date"]) > date.fromisoformat(q["valid_through"]) for u in q["uses"]))
    r = source["equipment-reliability"]["raw"]
    failures = [e for e in r["events"] if e["kind"] == "failure"]
    repair = sum(e["repair_hours"] for e in failures)
    for name, value in {"downtime_hours":sum(e["downtime_hours"] for e in r["events"]), "corrective_downtime_hours":sum(e["downtime_hours"] for e in failures), "repair_hours":repair, "failures":len(failures), "mtbf_hours":r["operating_hours"]/len(failures), "mttr_hours":repair/len(failures)}.items():
        metric("equipment-reliability", name, value)
    # These recorded outcome checks detect artifact regression, not model safety.
    final_statuses = {k:v["steps"][-1]["status"] for k,v in results.items()}
    assert final_statuses == {"production-shortfall":"PARTIAL", "quality-escape":"NEEDS_INPUT", "equipment-reliability":"NEEDS_INPUT", "safety-process-change":"JURISDICTION_REVIEW_REQUIRED"}


def main():
    inputs = read("tests/integration/am30-inputs.json")
    outputs = read("tests/integration/am30-walkthroughs.json")
    check(inputs, outputs)
    resolver = module("am30_resolver", "scripts/resolve-skillset.py")
    inspector = module("am30_inspector", "scripts/inspect-sector-coverage.py")
    for case in inputs["cases"]:
        result = resolver.resolve(case["role"], case["workflow"])
        assert result["execution"] == "NOT_EXECUTED"
        assert result["evidence_state"] == "NOT_ASSESSED"
        recorded = next(x for x in outputs["cases"] if x["id"] == case["id"])
        assert set(result["targets"]) & {x["skill"] for x in recorded["steps"]}
    registry = read("specializations/registry.json")
    for sector_dependent, status in [(False,"GENERIC_METHOD_ONLY"),(True,"COVERAGE_GAP")]:
        result = inspector.assess({"labels":["automotive"],"sector_dependent":sector_dependent}, registry)
        assert result["status"] == status
        assert result["generic_analysis_allowed"] and not result["sector_conclusion_supported"]
    # Prove that changed evidence, falsely promoted gates and benchmark claims fail.
    mutations = []
    changed = copy.deepcopy(outputs)
    changed["cases"][0]["metrics"]["capacity_units"] = 400
    mutations.append((inputs, changed))
    changed = copy.deepcopy(inputs)
    changed["cases"][1]["raw"]["relationships"][1]["input"] = "OTHER"
    mutations.append((changed, outputs))
    changed = copy.deepcopy(outputs)
    changed["cases"][2]["metrics"]["mttr_hours"] = 5
    mutations.append((inputs, changed))
    changed = copy.deepcopy(outputs)
    changed["cases"][3]["authorized"] = True
    mutations.append((inputs, changed))
    changed = copy.deepcopy(outputs)
    changed["independent_runtime"] = "PASS"
    mutations.append((inputs, changed))
    for altered_inputs, altered_outputs in mutations:
        try:
            check(altered_inputs, altered_outputs)
        except AssertionError:
            continue
        raise AssertionError("inconsistent evidence was accepted")
    print("PASS: AM-30 four assisted records, arithmetic/lineage checks, four role joins, two coverage boundaries and five mutation rejections; independent model evaluation NOT_RUN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
