"""Validate the AM-09 executable validation framework and evidence manifests."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import sys
from typing import Any


SCENARIO_CATEGORIES = {
    "correct_invocation",
    "incorrect_invocation",
    "missing_inputs",
    "bad_inputs",
    "calculation_correctness",
    "unit_mismatch",
    "ambiguous_scenario",
    "expected_output_structure",
    "safety_boundary",
    "jurisdiction_conflicts",
    "unsupported_assumptions",
}
ROUTE_MODES = {"IMPLEMENTED", "FUTURE_COVERAGE", "NO_TRIGGER"}
OUTCOMES = {"TRIGGER", "NO_TRIGGER", "NEEDS_INPUT", "SAFETY_ESCALATION", "SOURCE_REVIEW_REQUIRED", "JURISDICTION_REVIEW_REQUIRED", "ENGINEERING_REVIEW_REQUIRED", "FUTURE_COVERAGE"}
PRIVATE_PATTERNS = [r"password", r"secret", r"credential", r"api[_ -]?key", r"token", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"]
VALID_ROUTING_STATUSES = {"FRAMEWORK_READY_NOT_IMPLEMENTED", "REFERENCE_SKILLS_STRUCTURALLY_READY"}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def text(value: Any, label: str) -> None:
    need(isinstance(value, str) and bool(value.strip()), f"{label}: expected non-empty text")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_contract(contract: dict[str, Any]) -> dict[str, Any]:
    need(contract.get("schema_version") == "AM-09-validation-framework-1", "validation framework schema version")
    need(contract.get("status") == "FRAMEWORK_READY_NOT_IMPLEMENTED", "validation framework status")
    layers = contract.get("layers")
    need(isinstance(layers, list) and {layer.get("id") for layer in layers} == {"structural", "scenario_routing", "deterministic_fixture", "evaluation_report"}, "validation layers")
    categories = contract.get("scenario_categories")
    need(isinstance(categories, list) and {item.get("id") for item in categories} == SCENARIO_CATEGORIES, "scenario categories")
    need(all(item.get("required") is True for item in categories), "all scenario categories required")
    routing = contract.get("routing_manifest", {})
    need(set(routing.get("route_modes", [])) == ROUTE_MODES, "route modes")
    need(set(routing.get("outcomes", [])) == OUTCOMES, "routing outcomes")
    file_contract = contract.get("scenario_file_contract", {})
    need(len(file_contract.get("required_fields", [])) == 6, "scenario file fields")
    fixture_manifest = contract.get("fixture_manifest", {})
    need(len(fixture_manifest.get("required_fields", [])) == 5, "fixture manifest fields")
    need(set(fixture_manifest.get("required_categories", [])) == {"calculation_correctness", "unit_mismatch", "missing_inputs", "bad_inputs", "zero_denominator", "rounding"}, "fixture manifest categories")
    report = contract.get("evaluation_report_contract", {})
    need(set(report.get("statuses", [])) == {"NOT_RUN", "IN_PROGRESS", "READY_FOR_REVIEW", "REVIEWED"}, "evaluation statuses")
    need(len(report.get("required_fields", [])) == 7, "evaluation report fields")
    need(len(contract.get("release_gates", [])) >= 8, "release gates")
    text(contract.get("execution_boundary"), "execution boundary")
    return contract


def parse_scenario(path: Path) -> dict[str, Any]:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    title = next((line[2:].strip() for line in lines if line.startswith("# ")), "")
    category_match = re.search(r"^Category:\s*`?([a-z_]+)`?\s*$", content, re.MULTILINE)
    route_match = re.search(r"^Expected routing:\s*(.+?)\s*$", content, re.MULTILINE)
    prompt_match = re.search(r"^Prompt:\s*\n(.*?)(?=^Acceptance checks:)", content, re.MULTILINE | re.DOTALL)
    acceptance_match = re.search(r"^Acceptance checks:\s*\n(.*?)(?=^Risk and review notes:)", content, re.MULTILINE | re.DOTALL)
    risk_match = re.search(r"^Risk and review notes:\s*\n(.*)$", content, re.MULTILINE | re.DOTALL)
    need(title, f"{path.name}: title")
    need(category_match is not None, f"{path.name}: Category field")
    need(route_match is not None, f"{path.name}: Expected routing field")
    need(prompt_match is not None and prompt_match.group(1).strip(), f"{path.name}: prompt")
    need(acceptance_match is not None and acceptance_match.group(1).strip(), f"{path.name}: acceptance checks")
    need(risk_match is not None and risk_match.group(1).strip(), f"{path.name}: risk and review notes")
    for pattern in PRIVATE_PATTERNS:
        need(re.search(pattern, content, re.IGNORECASE) is None, f"{path.name}: private-data or credential pattern")
    return {"title": title, "category": category_match.group(1), "expected_routing": route_match.group(1).strip(), "prompt": prompt_match.group(1).strip(), "content": content}


def validate_routes(root: Path, manifest: dict[str, Any], contract: dict[str, Any]) -> tuple[int, set[str]]:
    need(manifest.get("schema_version") == "AM-09-routing-manifest-1", "routing manifest schema version")
    need(manifest.get("status") in VALID_ROUTING_STATUSES, "routing manifest status")
    future_names = manifest.get("future_skill_names")
    need(isinstance(future_names, list), "future skill names")
    need(len(set(future_names)) == len(future_names), "duplicate future skill name")
    scenarios = manifest.get("scenarios")
    need(isinstance(scenarios, list) and len(scenarios) >= 12, "scenario count")
    seen_ids: set[str] = set()
    seen_files: set[str] = set()
    categories: set[str] = set()
    scenario_root = root / "tests" / "scenarios"
    for item in scenarios:
        for field in ("scenario_id", "file", "category", "expected_routes", "future_routes", "expected_outcome", "route_mode", "acceptance_checks"):
            need(field in item, f"routing item missing {field}")
        sid = item["scenario_id"]
        text(sid, "scenario id")
        need(sid not in seen_ids, f"duplicate scenario id {sid}")
        seen_ids.add(sid)
        rel_file = item["file"]
        text(rel_file, f"{sid}.file")
        need(rel_file.startswith("tests/scenarios/") and rel_file.endswith(".md"), f"{sid}: invalid scenario path")
        need(rel_file not in seen_files, f"duplicate scenario file {rel_file}")
        seen_files.add(rel_file)
        scenario_path = root / rel_file
        need(scenario_path.exists(), f"{sid}: scenario file missing")
        parsed = parse_scenario(scenario_path)
        need(parsed["category"] == item["category"], f"{sid}: category mismatch")
        need(item["category"] in SCENARIO_CATEGORIES, f"{sid}: unknown category")
        categories.add(item["category"])
        expected_routes = item["expected_routes"]
        future_routes = item["future_routes"]
        need(isinstance(expected_routes, list) and isinstance(future_routes, list), f"{sid}: route lists")
        need(item["route_mode"] in ROUTE_MODES, f"{sid}: route mode")
        need(item["expected_outcome"] in OUTCOMES, f"{sid}: expected outcome")
        need(isinstance(item["acceptance_checks"], list) and item["acceptance_checks"], f"{sid}: acceptance checks")
        if item["route_mode"] == "NO_TRIGGER":
            need(not expected_routes and not future_routes, f"{sid}: no-trigger route must be empty")
            need(parsed["expected_routing"] == "[]", f"{sid}: no-trigger scenario file route")
        if item["route_mode"] == "FUTURE_COVERAGE":
            need(not expected_routes and future_routes, f"{sid}: future route mode requires future routes only")
            for route in future_routes:
                need(route in future_names, f"{sid}: undeclared future route {route}")
                need(f"future:{route}" in parsed["expected_routing"], f"{sid}: scenario file missing future route")
                need(route.lower() not in parsed["prompt"].lower(), f"{sid}: prompt names expected skill")
        if item["route_mode"] == "IMPLEMENTED":
            need(expected_routes and not future_routes, f"{sid}: implemented route mode requires implemented routes only")
            for route in expected_routes:
                package_dirs = [path.parent for path in (root / "skills").glob(f"*/{route}") if path.is_dir()]
                need(package_dirs, f"{sid}: implemented route folder missing {route}")
                need(f"implemented:{route}" in parsed["expected_routing"], f"{sid}: scenario file missing implemented route")
        if expected_routes:
            for route in expected_routes:
                need(route in parsed["expected_routing"], f"{sid}: scenario file missing implemented route")
    need(categories == SCENARIO_CATEGORIES, f"scenario category coverage missing {sorted(SCENARIO_CATEGORIES - categories)}")
    all_files = {f"tests/scenarios/{path.name}" for path in scenario_root.glob("*.md")}
    need(all_files == seen_files, "scenario files and manifest are not one-to-one")
    implemented = {path.parent.name for path in (root / "skills").glob("*/*/SKILL.md")}
    need(not (set(future_names) & implemented), "implemented skill incorrectly marked future")
    return len(scenarios), len(categories)


def validate_fixture_manifest(root: Path, manifest: dict[str, Any], contract: dict[str, Any]) -> int:
    need(manifest.get("schema_version") == "AM-09-fixture-manifest-1", "fixture manifest schema version")
    need(manifest.get("status") == "FRAMEWORK_READY_NOT_IMPLEMENTED", "fixture manifest status")
    source = root / manifest.get("source", "")
    need(source.exists(), "AM-08 fixture source missing")
    source_data = load_json(source)
    fixture_ids = {fixture.get("fixture_id") for fixture in source_data.get("fixtures", [])}
    need(len(fixture_ids) == manifest.get("expected_fixture_count"), "AM-08 fixture count mismatch")
    mapping = manifest.get("category_mapping")
    need(isinstance(mapping, dict), "fixture category mapping")
    required = set(contract["fixture_manifest"]["required_categories"])
    need(required <= set(mapping), "fixture manifest category coverage")
    mapped_ids: set[str] = set()
    for category, ids in mapping.items():
        need(isinstance(ids, list) and ids, f"fixture mapping {category}")
        for fixture_id in ids:
            need(fixture_id in fixture_ids, f"fixture mapping references unknown {fixture_id}")
            need(fixture_id not in mapped_ids, f"fixture mapped more than once: {fixture_id}")
            mapped_ids.add(fixture_id)
    need(mapped_ids == fixture_ids, "fixture manifest does not cover every AM-08 fixture")
    text(manifest.get("execution_rule"), "fixture execution rule")
    return len(fixture_ids)


def validate_evaluation_template(path: Path, contract: dict[str, Any]) -> None:
    content = path.read_text(encoding="utf-8")
    for phrase in ("# AM-09 evaluation report template", "Status: `NOT_RUN`", "Expected routing is not observed behavior.", "Do not invent a baseline.", "## Baseline behavior", "## Skill-enabled behavior", "## Failure modes", "## Reviewer disposition", "## Residual risk"):
        need(phrase in content, f"evaluation template missing {phrase!r}")
    for field in contract["evaluation_report_contract"]["required_fields"]:
        need(field.replace("_", " ") in content.lower() or field.replace("_", ":") in content.lower(), f"evaluation template missing {field}")


def validate_am08(root: Path) -> None:
    module_path = root / "scripts" / "validate-calculation-standard.py"
    spec = importlib.util.spec_from_file_location("am08_validator", module_path)
    need(spec is not None and spec.loader is not None, "AM-08 validator import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    calculation_contract = load_json(root / "docs/architecture/calculation-contract.json")
    calculation_fixtures = load_json(root / "docs/architecture/calculation-fixtures.json")
    formulas = module.validate_contract(calculation_contract)
    module.validate_fixture_set(calculation_contract, calculation_fixtures, formulas)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        framework = load_json(root / "docs/architecture/validation-framework-contract.json")
        routing = load_json(root / "tests/expected-routing.yaml")
        fixture_manifest = load_json(root / "tests/fixtures/am09-fixture-manifest.json")
        validate_contract(framework)
        scenario_count, category_count = validate_routes(root, routing, framework)
        fixture_count = validate_fixture_manifest(root, fixture_manifest, framework)
        validate_evaluation_template(root / "tests/evaluations/AM-09-evaluation-template.md", framework)
        validate_am08(root)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError, AttributeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(
        "PASS: AM-09 validation framework; "
        f"{scenario_count} scenarios across {category_count} categories; "
        f"{fixture_count} AM-08 fixtures mapped; four validation layers; "
        "future routes labeled, evaluation evidence separated, and no model behavior evaluated."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
