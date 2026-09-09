"""Validate AM-25 environment, energy and waste packages."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import sys


SECTIONS = ["Overview", "Triggers", "Non-Triggers", "Required Inputs", "Optional Inputs", "Assumptions", "Core Workflow", "Calculations", "Validation", "Exception Handling", "Source Usage", "Output Contract", "Safety Requirements", "References", "Examples", "Testing"]
EXPECTED = {
    "identify-manufacturing-environmental-aspect": ("skills/family-19-environment-energy-waste/identify-manufacturing-environmental-aspect", "P1", "REGULATED", "PENDING_CONTEXT", ["PROVINCIAL_REQUIRED","STANDARDS_DEPENDENT","SECTOR_REGULATED"]),
    "build-environmental-risk-register": ("skills/family-19-environment-energy-waste/build-environmental-risk-register", "P1", "REGULATED", "PENDING_CONTEXT", ["PROVINCIAL_REQUIRED","SECTOR_REGULATED"]),
    "analyze-energy-consumption": ("skills/family-19-environment-energy-waste/analyze-energy-consumption", "P2", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "analyze-waste-stream": ("skills/family-19-environment-energy-waste/analyze-waste-stream", "P1", "REGULATED", "PENDING_CONTEXT", ["PROVINCIAL_REQUIRED","SECTOR_REGULATED"]),
    "build-waste-reduction-plan": ("skills/family-19-environment-energy-waste/build-waste-reduction-plan", "P2", "REGULATED", "PENDING_CONTEXT", ["PROVINCIAL_REQUIRED","SECTOR_REGULATED"]),
    "review-environmental-objective": ("skills/family-19-environment-energy-waste/review-environmental-objective", "P2", "REGULATED", "PENDING_CONTEXT", ["PROVINCIAL_REQUIRED","STANDARDS_DEPENDENT","SECTOR_REGULATED"]),
}
PRIVATE_PATTERNS = [r"password", r"secret", r"credential", r"api[_ -]?key", r"token", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"]


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def taxonomy(root: Path) -> dict[str, dict]:
    data = json.loads((root / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8"))
    return {item["name"]: item for item in data["skills"]}


def validate_package(root: Path, name: str, spec: tuple, records: dict[str, dict]) -> None:
    package_rel, priority, safety, jurisdiction, flags = spec
    package = root / package_rel
    skill = package / "SKILL.md"
    need(skill.exists(), f"{name}: SKILL.md missing")
    content = skill.read_text(encoding="utf-8")
    need(content.startswith("---\n"), f"{name}: frontmatter")
    end = content.find("\n---", 4)
    need(end > 0, f"{name}: frontmatter end")
    fields = {}
    for line in content[4:end].splitlines():
        if line.strip():
            key, sep, value = line.partition(":")
            need(sep and value.strip(), f"{name}: malformed frontmatter")
            fields[key.strip()] = value.strip()
    need(fields.get("name") == name, f"{name}: name")
    need(fields.get("description", "").endswith("."), f"{name}: description")
    need(fields.get("license") == "MIT", f"{name}: licence")
    need(re.findall(r"^## ([^\n]+)$", content, re.MULTILINE) == SECTIONS, f"{name}: section order")
    metadata = next((line for line in content.splitlines() if line.startswith("**Taxonomy metadata:**")), "")
    need(metadata, f"{name}: metadata")
    record = records.get(name)
    need(record is not None and record["family"] == package.parent.name.split("-")[1], f"{name}: taxonomy family")
    need(record["priority"] == priority, f"{name}: priority")
    need(record["safety_class"] == safety, f"{name}: safety")
    need(record["jurisdiction"]["assessment"] == jurisdiction, f"{name}: jurisdiction")
    need(record["jurisdiction"]["flags"] == flags, f"{name}: jurisdiction flags")
    for marker in (record["family"], "CORE", priority, safety, jurisdiction, "TAXONOMY_ACCEPTED_NOT_IMPLEMENTED") + tuple(flags):
        need(marker in metadata, f"{name}: metadata {marker}")
    adapter = package / "agents/openai.yaml"
    need(adapter.exists(), f"{name}: adapter")
    adapter_text = adapter.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        need(re.search(rf"^\s+{key}:\s+.+$", adapter_text, re.MULTILINE), f"{name}: adapter {key}")
    need(f"${name}" in adapter_text, f"{name}: adapter invocation")
    refs = list((package / "references").glob("*.md"))
    need(refs, f"{name}: references")
    for ref in refs:
        text = ref.read_text(encoding="utf-8")
        need(text.strip(), f"{name}: empty reference")
        need(f"references/{ref.name}" in content, f"{name}: reference not linked")
        for pattern in PRIVATE_PATTERNS:
            need(re.search(pattern, text, re.IGNORECASE) is None, f"{name}: private pattern")
    need("Expected routing is not observed behavior" in content, f"{name}: evaluation boundary")


def validate_evaluation(root: Path) -> None:
    content = (root / "tests/evaluations/AM-25-environment-energy-waste-acceptance.md").read_text(encoding="utf-8")
    for phrase in ("Status: `READY_FOR_REVIEW`", "Runtime model behavior", "NOT_RUN", "Residual risk"):
        need(phrase in content, f"AM-25 evaluation missing {phrase!r}")
    for name in EXPECTED:
        need(f"`{name}`" in content, f"AM-25 evaluation missing {name}")


def validate_coverage(root: Path, records: dict[str, dict]) -> None:
    accepted = {name for name, record in records.items() if record["family"] in {"19"}}
    need(set(EXPECTED) == accepted, "AM-25 family coverage differs from frozen taxonomy")
    paths = {path.parent.relative_to(root).as_posix() for family in ("family-19-environment-energy-waste",) for path in (root / "skills" / family).glob("*/SKILL.md")}
    need(paths == {spec[0] for spec in EXPECTED.values()}, "AM-25 package inventory mismatch")
    manifest = json.loads((root / "tests/expected-routing.yaml").read_text(encoding="utf-8"))
    scenarios = [item for item in manifest["scenarios"] if item["scenario_id"].startswith("AM25-")]
    routes = {route for item in scenarios for route in item["expected_routes"]}
    need(routes == accepted, "AM-25 scenarios must cover exactly Family 19")
    for item in scenarios:
        need(item["route_mode"] == "IMPLEMENTED" and not item["future_routes"], "AM-25 route mode")
    for name in accepted:
        for provider in records[name]["dependencies"]["evidence_reuse"]:
            need(any((root / "skills").glob(f"*/{provider}/SKILL.md")), f"{name}: missing evidence provider {provider}")



def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    need(spec is not None and spec.loader is not None, f"Cannot import {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_fixtures(root: Path) -> int:
    module = load_module(root / "skills/family-19-environment-energy-waste/analyze-energy-consumption/scripts/energy_intensity.py", "am25_energy")
    fixtures = json.loads((root / "tests/fixtures/am25-energy-intensity.json").read_text(encoding="utf-8"))
    cases = fixtures["cases"]
    expected_ids = ["matched","mwh","mj","gj","rounding","zero_energy","zero_activity","power_unit","period_mismatch","missing_boundary","negative","nonfinite","boolean","cumulative","missing_energy","range_limit","comparable","office_boundary","output_basis","duplicate_id"]
    need(len(cases) == len(expected_ids) and {case["id"] for case in cases} == set(expected_ids), "AM-25 fixture coverage")
    for case in cases:
        result = module.analyze(case["input"])
        need(result["status"] == case["status"], f'{case["id"]}: status')
        need(result["comparable"] == case["comparable"], f'{case["id"]}: comparison eligibility')
        need([row["intensity"] for row in result["results"]] == case["intensities"], f'{case["id"]}: intensity')
        if case["status"] == "NEEDS_INPUT":
            need(result["gaps"], f'{case["id"]}: missing gaps')
        for row in result["results"]:
            if row["status"] == "READY_FOR_REVIEW":
                need(all(key in row for key in ("energy_kwh", "activity", "formula", "unit")), f'{case["id"]}: intermediates')
    return len(cases)


def validate_sources(root: Path) -> None:
    module = load_module(root / "scripts/validate-source-standards-standard.py", "am25_source")
    data = json.loads((root / "docs/architecture/am25-environment-source-records.json").read_text(encoding="utf-8"))
    keys = {record["source_key"] for record in data["records"]}
    need(keys == {"AM25-ISO-14001", "AM25-ECCC-WASTE-CONTACT"}, "AM-25 source coverage")
    for record in data["records"]:
        module.validate_record(record, record["source_key"])
    need(len(data["claims"]) == 2, "AM-25 bounded source claims")
    for claim in data["claims"]:
        need(claim["source_key"] in keys, "AM-25 claim source")
        need(all(claim.get(key) for key in ("claim_type", "scope", "as_of", "location", "support_status", "claim")), "AM-25 claim metadata")
    standard = next(record for record in data["records"] if record["source_key"] == "AM25-ISO-14001")
    need(standard["rights"]["content_handling"] == "METADATA_ONLY", "AM-25 standard text boundary")
    need(standard["source_class"] == "voluntary_standard", "AM-25 no assumed incorporation")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        records = taxonomy(root)
        for name, spec in EXPECTED.items():
            validate_package(root, name, spec, records)
        validate_evaluation(root)
        validate_coverage(root, records)
        fixture_count = validate_fixtures(root)
        validate_sources(root)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: AM-25 environment/energy/waste; six Family 19 packages, {fixture_count} energy fixtures, source metadata and scenario coverage validated; runtime model behavior remains NOT_RUN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
