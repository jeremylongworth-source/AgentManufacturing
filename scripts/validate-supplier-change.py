"""Validate AM-24 supplier quality and engineering change packages."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import sys


SECTIONS = ["Overview", "Triggers", "Non-Triggers", "Required Inputs", "Optional Inputs", "Assumptions", "Core Workflow", "Calculations", "Validation", "Exception Handling", "Source Usage", "Output Contract", "Safety Requirements", "References", "Examples", "Testing"]
EXPECTED = {
    "review-supplier-qualification": ("skills/family-17-supplier-quality/review-supplier-qualification", "P1", "REGULATED", "PENDING_CONTEXT", ["STANDARDS_DEPENDENT","SECTOR_REGULATED"]),
    "analyze-supplier-defect": ("skills/family-17-supplier-quality/analyze-supplier-defect", "P2", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "draft-supplier-corrective-action": ("skills/family-17-supplier-quality/draft-supplier-corrective-action", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "review-certificate-of-conformance": ("skills/family-17-supplier-quality/review-certificate-of-conformance", "P1", "REGULATED", "PENDING_CONTEXT", ["STANDARDS_DEPENDENT","SECTOR_REGULATED"]),
    "review-supplier-change-impact": ("skills/family-17-supplier-quality/review-supplier-change-impact", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["STANDARDS_DEPENDENT","SECTOR_REGULATED"]),
    "review-change-package": ("skills/family-18-engineering-change/review-change-package", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "build-engineering-change-impact-assessment": ("skills/family-18-engineering-change/build-engineering-change-impact-assessment", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "review-bom-change": ("skills/family-18-engineering-change/review-bom-change", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "review-routing-change": ("skills/family-18-engineering-change/review-routing-change", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "review-process-change": ("skills/family-18-engineering-change/review-process-change", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["PROVINCIAL_REQUIRED","SECTOR_REGULATED"]),
    "draft-document-revision-plan": ("skills/family-18-engineering-change/draft-document-revision-plan", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "identify-obsolete-document": ("skills/family-18-engineering-change/identify-obsolete-document", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "verify-change-implementation": ("skills/family-18-engineering-change/verify-change-implementation", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "review-document-revision": ("skills/family-18-engineering-change/review-document-revision", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
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
    content = (root / "tests/evaluations/AM-24-supplier-change-acceptance.md").read_text(encoding="utf-8")
    for phrase in ("Status: `READY_FOR_REVIEW`", "Runtime model behavior", "NOT_RUN", "Residual risk"):
        need(phrase in content, f"AM-24 evaluation missing {phrase!r}")
    for name in EXPECTED:
        need(f"`{name}`" in content, f"AM-24 evaluation missing {name}")


def validate_coverage(root: Path, records: dict[str, dict]) -> None:
    accepted = {name for name, record in records.items() if record["family"] in {"17", "18"}}
    need(set(EXPECTED) == accepted, "AM-24 family coverage differs from frozen taxonomy")
    paths = {path.parent.relative_to(root).as_posix() for family in ("family-17-supplier-quality", "family-18-engineering-change") for path in (root / "skills" / family).glob("*/SKILL.md")}
    need(paths == {spec[0] for spec in EXPECTED.values()}, "AM-24 package inventory mismatch")
    manifest = json.loads((root / "tests/expected-routing.yaml").read_text(encoding="utf-8"))
    scenarios = [item for item in manifest["scenarios"] if item["scenario_id"].startswith("AM24-")]
    routes = {route for item in scenarios for route in item["expected_routes"]}
    need(routes == accepted, "AM-24 scenarios must cover exactly Families 17 and 18")
    for item in scenarios:
        need(item["route_mode"] == "IMPLEMENTED" and not item["future_routes"], "AM-24 route mode")
    for name in accepted:
        for provider in records[name]["dependencies"]["evidence_reuse"]:
            need(any((root / "skills").glob(f"*/{provider}/SKILL.md")), f"{name}: missing evidence provider {provider}")


def validate_fixtures(root: Path) -> int:
    path = root / "skills/family-17-supplier-quality/analyze-supplier-defect/scripts/defect_rate.py"
    spec = importlib.util.spec_from_file_location("am24_defect_rate", path)
    need(spec is not None and spec.loader is not None, "AM-24 calculator import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    fixtures = json.loads((root / "tests/fixtures/am24-supplier-defect.json").read_text(encoding="utf-8"))
    cases = fixtures["cases"]
    need({case["id"] for case in cases} == {"matched_counts", "rounding", "zero_defects", "zero_exposure", "missing_lot", "mixed_units", "excess_count", "occurrences_separate", "missing_count", "negative_count", "fractional_count", "nonfinite_count", "boolean_count"}, "AM-24 fixture coverage")
    for case in cases:
        result = module.calculate(case["input"])
        need(result["status"] == case["status"], f'{case["id"]}: status')
        need(result["rate_percent"] == case["rate"], f'{case["id"]}: rate')
        if case["status"] == "NEEDS_INPUT":
            need(result["gaps"], f'{case["id"]}: gaps missing')
        else:
            need(result["numerator"] == str(case["input"]["defective_units"]), f'{case["id"]}: numerator')
            need(result["denominator"] == str(case["input"]["exposed_units"]), f'{case["id"]}: denominator')
            need("causation is not established" in result["attribution"], f'{case["id"]}: attribution boundary')
    return len(cases)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        records = taxonomy(root)
        for name, spec in EXPECTED.items():
            validate_package(root, name, spec, records)
        validate_evaluation(root)
        validate_coverage(root, records)
        fixture_count = validate_fixtures(root)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: AM-24 supplier/change; 14 Family 17/18 packages and {fixture_count} deterministic fixtures; taxonomy, adapters, references, scenario coverage and acceptance evidence validated; runtime model behavior remains NOT_RUN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
