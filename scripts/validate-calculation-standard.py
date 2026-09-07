"""Validate the AM-08 calculation contract and worked fixtures."""

from __future__ import annotations

import json
from decimal import Decimal, InvalidOperation, ROUND_CEILING, getcontext
from pathlib import Path
import sys
from typing import Any


getcontext().prec = 40

FORMULA_KEYS = {
    "takt_time",
    "gross_capacity",
    "oee",
    "first_pass_yield",
    "scrap_rate",
    "mtbf",
    "mttr",
    "cp",
    "cpk",
    "xbar_control_limits",
}
STATUSES = {"CALCULATED", "PARTIAL", "BLOCKED", "INVALID_INPUT", "NOT_APPLICABLE", "REVIEW_REQUIRED"}
FIXTURE_CATEGORIES = {"worked_example", "unit_conversion", "missing_input", "invalid_input", "zero_denominator", "rounding", "edge_case"}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def text(value: Any, label: str) -> None:
    need(isinstance(value, str) and bool(value.strip()), f"{label}: expected non-empty text")


def dec(value: Any, label: str) -> Decimal:
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"{label}: expected decimal value") from exc


def close(actual: Decimal, expected: Any, tolerance: Decimal, label: str) -> None:
    target = dec(expected, label)
    need(abs(actual - target) <= tolerance, f"{label}: expected {target}, got {actual}")


def split_unit(unit: str) -> tuple[str, str | None]:
    if "/" in unit:
        numerator, denominator = unit.split("/", 1)
        return numerator, denominator
    return unit, None


def validate_contract(contract: dict[str, Any]) -> dict[str, dict[str, Any]]:
    need(contract.get("schema_version") == "AM-08-calculation-contract-1", "calculation contract schema version")
    need(contract.get("status") == "STANDARD_READY_NOT_IMPLEMENTED", "calculation contract status")
    need(len(contract.get("required_record_fields", [])) >= 12, "calculation record fields")
    need(set(contract.get("status_values", [])) == STATUSES, "calculation statuses")
    units = contract.get("unit_contract", {})
    dimensions = units.get("dimensions", {})
    need(len(dimensions) >= 9, "unit dimensions")
    need(set(units.get("canonical_units", {})) == set(dimensions), "canonical units for every dimension")
    need("conversion_rules" in units and "rules" in units, "unit conversion contract")
    rounding = contract.get("rounding_contract", {})
    need(len(rounding.get("policies", [])) >= 8, "rounding policies")
    need(len(rounding.get("rules", [])) >= 5, "rounding rules")
    validation = contract.get("validation_contract", {})
    need(len(validation.get("required_checks", [])) >= 10, "validation checks")
    need("failure_behavior" in validation and "zero_denominator_behavior" in validation, "validation failure behavior")
    formulas = contract.get("reference_formulas")
    need(isinstance(formulas, list) and len(formulas) == 10, "reference formula count")
    by_key: dict[str, dict[str, Any]] = {}
    for formula in formulas:
        key = formula.get("key")
        need(key not in by_key, f"duplicate formula {key}")
        need(key in FORMULA_KEYS, f"unknown formula {key}")
        for field in ("key", "purpose", "formula", "variables", "output", "assumptions", "edge_cases", "fixture_ids"):
            need(field in formula, f"{key}: missing {field}")
        need(isinstance(formula["variables"], list) and formula["variables"], f"{key}: variables")
        for variable in formula["variables"]:
            text(variable.get("name"), f"{key}.variable.name")
            text(variable.get("dimension"), f"{key}.{variable['name']}.dimension")
            text(variable.get("meaning"), f"{key}.{variable['name']}.meaning")
        need(isinstance(formula["fixture_ids"], list) and formula["fixture_ids"], f"{key}: fixture ids")
        by_key[key] = formula
    need(set(by_key) == FORMULA_KEYS, "all required manufacturing reference formulas")
    fixture_contract = contract.get("fixture_contract", {})
    need(set(fixture_contract.get("categories", [])) == FIXTURE_CATEGORIES, "fixture categories")
    need(len(fixture_contract.get("required_fields", [])) >= 8, "fixture fields")
    text(contract.get("safety_boundary"), "safety boundary")
    return by_key


def input_value(inputs: dict[str, Any], name: str) -> Decimal:
    need(name in inputs, f"missing input {name}")
    entry = inputs[name]
    return dec(entry.get("value"), f"input {name}.value")


def input_unit(inputs: dict[str, Any], name: str) -> str:
    text(inputs[name].get("unit"), f"input {name}.unit")
    return inputs[name]["unit"]


def time_to_seconds(value: Decimal, unit: str, label: str) -> Decimal:
    factors = {"s": Decimal("1"), "min": Decimal("60"), "h": Decimal("3600"), "day": Decimal("86400")}
    need(unit in factors, f"{label}: unsupported time unit {unit}")
    return value * factors[unit]


def rate_time_to_seconds(value: Decimal, unit: str, label: str) -> Decimal:
    numerator, denominator = split_unit(unit)
    need(denominator in {"each", "unit", "piece"}, f"{label}: expected time/count unit")
    return time_to_seconds(value, numerator, label)


def count_unit(unit: str, label: str) -> None:
    need(unit in {"each", "unit", "piece", "batch", "failure"}, f"{label}: expected count unit")


def same_measurement_unit(inputs: dict[str, Any], names: list[str], label: str) -> str:
    units = [input_unit(inputs, name) for name in names]
    need(len(set(units)) == 1, f"{label}: incompatible measurement units {units}")
    return units[0]


def evaluate(formula_key: str, inputs: dict[str, Any]) -> tuple[dict[str, Decimal], dict[str, Decimal]]:
    """Return intermediate and final values for a valid fixture."""
    if formula_key == "takt_time":
        t = time_to_seconds(input_value(inputs, "available_production_time"), input_unit(inputs, "available_production_time"), "available production time")
        demand = input_value(inputs, "required_demand")
        count_unit(input_unit(inputs, "required_demand"), "required demand")
        need(t > 0 and demand > 0, "takt time requires positive time and demand")
        return {"available_production_time_normalized_s": t}, {"takt_time_seconds_per_each": t / demand}
    if formula_key == "gross_capacity":
        t = time_to_seconds(input_value(inputs, "available_production_time"), input_unit(inputs, "available_production_time"), "available production time")
        cycle = rate_time_to_seconds(input_value(inputs, "cycle_time"), input_unit(inputs, "cycle_time"), "cycle time")
        need(t > 0 and cycle > 0, "gross capacity requires positive time and cycle time")
        return {"available_production_time_normalized_s": t, "cycle_time_normalized_s_per_each": cycle}, {"gross_capacity_raw_each": t / cycle}
    if formula_key == "oee":
        planned = time_to_seconds(input_value(inputs, "planned_production_time"), input_unit(inputs, "planned_production_time"), "planned production time")
        run = time_to_seconds(input_value(inputs, "run_time"), input_unit(inputs, "run_time"), "run time")
        cycle = rate_time_to_seconds(input_value(inputs, "ideal_cycle_time"), input_unit(inputs, "ideal_cycle_time"), "ideal cycle time")
        total = input_value(inputs, "total_count")
        good = input_value(inputs, "good_count")
        for name in ("total_count", "good_count"):
            count_unit(input_unit(inputs, name), name)
        need(planned > 0 and run > 0 and cycle > 0 and total > 0, "OEE requires positive time, cycle, and total count")
        need(0 <= good <= total, "OEE good count must be between zero and total count")
        availability = run / planned
        performance = cycle * total / run
        quality = good / total
        need(run <= planned, "OEE run time cannot exceed planned time without an explicit exception")
        return {"availability": availability, "performance": performance, "quality": quality}, {"oee": availability * performance * quality}
    if formula_key == "first_pass_yield":
        good = input_value(inputs, "first_pass_good_count")
        entered = input_value(inputs, "units_entering_operation")
        count_unit(input_unit(inputs, "first_pass_good_count"), "first-pass good count")
        count_unit(input_unit(inputs, "units_entering_operation"), "units entering operation")
        need(entered > 0, "FPY denominator must be positive")
        need(0 <= good <= entered, "FPY good count must be between zero and units entering")
        return {}, {"fpy": good / entered}
    if formula_key == "scrap_rate":
        scrap = input_value(inputs, "scrap_count")
        started = input_value(inputs, "units_started")
        count_unit(input_unit(inputs, "scrap_count"), "scrap count")
        count_unit(input_unit(inputs, "units_started"), "units started")
        need(started > 0, "scrap rate denominator must be positive")
        need(0 <= scrap <= started, "scrap count must be between zero and units started")
        return {}, {"scrap_rate": scrap / started}
    if formula_key in {"mtbf", "mttr"}:
        time_name = "operating_time" if formula_key == "mtbf" else "corrective_repair_time"
        time_value = input_value(inputs, time_name)
        time_unit = input_unit(inputs, time_name)
        failures = input_value(inputs, "failure_count")
        count_unit(input_unit(inputs, "failure_count"), "failure count")
        need(time_value >= 0 and failures > 0, f"{formula_key} requires non-negative time and positive failure count")
        need(time_unit in {"s", "min", "h", "day"}, f"{formula_key}: unsupported time unit")
        return {}, {formula_key: time_value / failures}
    if formula_key in {"cp", "cpk"}:
        names = ["upper_spec_limit", "lower_spec_limit", "within_sigma"] + (["mean"] if formula_key == "cpk" else [])
        unit = same_measurement_unit(inputs, names, formula_key)
        need(unit in {"mm", "cm", "m", "in", "ft"}, f"{formula_key}: unsupported measurement unit")
        usl = input_value(inputs, "upper_spec_limit")
        lsl = input_value(inputs, "lower_spec_limit")
        sigma = input_value(inputs, "within_sigma")
        need(usl > lsl and sigma > 0, f"{formula_key}: specification limits and sigma must be valid")
        if formula_key == "cp":
            return {"specification_width": usl - lsl, "six_sigma": 6 * sigma}, {"cp": (usl - lsl) / (6 * sigma)}
        mean = input_value(inputs, "mean")
        upper = (usl - mean) / (3 * sigma)
        lower = (mean - lsl) / (3 * sigma)
        return {"upper_capability": upper, "lower_capability": lower}, {"cpk": min(upper, lower)}
    if formula_key == "xbar_control_limits":
        unit = same_measurement_unit(inputs, ["center_line", "within_sigma"], formula_key)
        need(unit in {"mm", "cm", "m", "in", "ft"}, "xbar control limits: unsupported measurement unit")
        center = input_value(inputs, "center_line")
        sigma = input_value(inputs, "within_sigma")
        n = input_value(inputs, "subgroup_size")
        count_unit(input_unit(inputs, "subgroup_size"), "subgroup size")
        need(sigma > 0 and n > 0, "xbar control limits require positive sigma and subgroup size")
        spread = 3 * sigma / n.sqrt()
        return {"three_sigma_over_sqrt_n": spread}, {"ucl": center + spread, "lcl": center - spread}
    raise ValueError(f"unsupported formula {formula_key}")


def validate_fixture(fixture: dict[str, Any], formula_keys: set[str]) -> None:
    for field in ("fixture_id", "formula_key", "category", "inputs", "expected_status", "expected_units", "notes"):
        need(field in fixture, f"fixture missing {field}")
    fid = fixture["fixture_id"]
    text(fid, "fixture_id")
    need(fixture["formula_key"] in formula_keys, f"{fid}: formula not in contract")
    need(fixture["category"] in FIXTURE_CATEGORIES, f"{fid}: unknown category")
    need(isinstance(fixture["inputs"], dict) and fixture["inputs"], f"{fid}: inputs")
    for name, entry in fixture["inputs"].items():
        for field in ("name", "value", "unit", "source_or_origin", "quality_note"):
            text(entry.get(field), f"{fid}.{name}.{field}")
        dec(entry["value"], f"{fid}.{name}.value")
    status = fixture["expected_status"]
    need(status in STATUSES, f"{fid}: invalid expected status")
    need(isinstance(fixture["expected_units"], dict), f"{fid}: expected units")
    text(fixture.get("notes"), f"{fid}.notes")
    tolerance = dec(fixture.get("tolerance", "0.0000001"), f"{fid}.tolerance")
    need(tolerance >= 0, f"{fid}: negative tolerance")
    expected_intermediate = fixture.get("expected_intermediate_values", {})
    expected_final = fixture.get("expected_final_values", {})
    need(isinstance(expected_intermediate, dict) and isinstance(expected_final, dict), f"{fid}: expected values objects")
    if status == "CALCULATED":
        actual_intermediate, actual_final = evaluate(fixture["formula_key"], fixture["inputs"])
        if fixture["category"] == "rounding" and fixture["rounding"]["policy"] == "CEILING":
            raw_key = "gross_capacity_raw_each"
            actual_final["gross_capacity_rounded_each"] = actual_final[raw_key].to_integral_value(rounding=ROUND_CEILING)
        for key, value in expected_intermediate.items():
            need(key in actual_intermediate, f"{fid}: unexpected intermediate key {key}")
            close(actual_intermediate[key], value, tolerance, f"{fid}.{key}")
        for key, value in expected_final.items():
            need(key in actual_final, f"{fid}: unexpected final key {key}")
            close(actual_final[key], value, tolerance, f"{fid}.{key}")
        need(set(expected_final) == set(actual_final) or fixture["formula_key"] == "gross_capacity" and set(expected_final) == {"gross_capacity_raw_each", "gross_capacity_rounded_each"}, f"{fid}: expected final values do not cover evaluator outputs")
    else:
        need("expected_missing_inputs" in fixture or "expected_error_fields" in fixture or "expected_review_flags" in fixture, f"{fid}: failure fixture needs failure fields")
    if fixture["category"] == "rounding":
        rounding = fixture.get("rounding")
        need(isinstance(rounding, dict) and rounding.get("policy") in {"CEILING", "FLOOR", "NEAREST", "INCREMENT", "ORDER_MULTIPLE"}, f"{fid}: rounding policy required")
        need("gross_capacity_raw_each" in expected_final and "gross_capacity_rounded_each" in expected_final, f"{fid}: raw and rounded values required")


def validate_fixture_set(contract: dict[str, Any], fixtures: dict[str, Any], formulas: dict[str, dict[str, Any]]) -> None:
    need(fixtures.get("schema_version") == "AM-08-calculation-fixtures-1", "calculation fixtures schema version")
    need(fixtures.get("status") == "STANDARD_READY_NOT_IMPLEMENTED", "calculation fixtures status")
    items = fixtures.get("fixtures")
    need(isinstance(items, list) and len(items) >= 16, "worked fixture count")
    seen: set[str] = set()
    categories: set[str] = set()
    for fixture in items:
        validate_fixture(fixture, set(formulas))
        fid = fixture["fixture_id"]
        need(fid not in seen, f"duplicate fixture {fid}")
        seen.add(fid)
        categories.add(fixture["category"])
    need(FIXTURE_CATEGORIES <= categories, "fixture category coverage")
    declared = {fid for formula in formulas.values() for fid in formula["fixture_ids"]}
    need(declared <= seen, f"formula fixture ids missing: {sorted(declared - seen)}")
    need(any(f["category"] == "unit_conversion" for f in items), "unit conversion fixture")
    need(any(f["category"] == "missing_input" for f in items), "missing input fixture")
    need(any(f["category"] == "invalid_input" for f in items), "invalid input fixture")
    need(any(f["category"] == "zero_denominator" for f in items), "zero denominator fixture")
    need(any(f["category"] == "rounding" for f in items), "rounding fixture")


def validate_document(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    required = [
        "# AM-08 calculation standard",
        "Variables and units",
        "Formula contract",
        "Assumptions",
        "Rounding and precision",
        "Missing inputs and edge cases",
        "Worked fixtures",
        "Takt time",
        "Gross capacity",
        "OEE",
        "First-pass yield",
        "scrap rate",
        "MTBF",
        "MTTR",
        "Cp",
        "Cpk",
        "control limits",
        "AGENTMANUFACTURING_AM_08_CALCULATION_STANDARD_READY",
    ]
    for phrase in required:
        need(phrase in content, f"calculation standard missing {phrase!r}")
    need("Do not force a final numeric result" in content, "missing safe failure behavior")
    need("Control limits are not specification limits" in content, "missing control/spec distinction")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        contract = json.loads((root / "docs/architecture/calculation-contract.json").read_text(encoding="utf-8"))
        fixtures = json.loads((root / "docs/architecture/calculation-fixtures.json").read_text(encoding="utf-8"))
        formulas = validate_contract(contract)
        validate_fixture_set(contract, fixtures, formulas)
        validate_document(root / "docs/architecture/calculation-standard.md")
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(
        "PASS: AM-08 calculation standard; "
        f"{len(formulas)} reference formulas; "
        f"{len(fixtures['fixtures'])} worked fixtures; "
        f"{len(contract['unit_contract']['dimensions'])} unit dimensions; "
        f"{len(contract['rounding_contract']['policies'])} rounding policies; "
        "numeric fixture values, failure states, and output invariants checked; no skill behavior evaluated."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
