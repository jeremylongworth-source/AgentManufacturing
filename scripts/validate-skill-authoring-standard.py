"""Validate the AM-06 authoring and validation contracts and templates."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from typing import Any


SKILL_SECTIONS = [
    "Overview", "Triggers", "Non-Triggers", "Required Inputs", "Optional Inputs", "Assumptions",
    "Core Workflow", "Calculations", "Validation", "Exception Handling", "Source Usage",
    "Output Contract", "Safety Requirements", "References", "Examples", "Testing",
]
CLASSES = {"ROUTINE", "REGULATED", "HAZARDOUS_OPERATION", "ENGINEERING_OR_CERTIFICATION_BOUNDARY"}
STATUSES = {"COMPLETE", "PARTIAL", "NEEDS_INPUT", "OUT_OF_SCOPE", "SAFETY_ESCALATION", "SOURCE_REVIEW_REQUIRED", "ENGINEERING_REVIEW_REQUIRED"}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def text(value: Any, label: str) -> None:
    need(isinstance(value, str) and bool(value.strip()), f"{label}: expected non-empty text")


def string_list(value: Any, label: str, minimum: int = 1) -> None:
    need(isinstance(value, list) and len(value) >= minimum and all(isinstance(x, str) and x.strip() for x in value), f"{label}: expected string list")
    need(len(value) == len(set(value)), f"{label}: duplicates")


def validate_schema(schema: dict[str, Any], contract: dict[str, Any]) -> None:
    need(schema.get("schema_version") == "AM-06-skill-package-1", "package schema version")
    need(schema.get("status") == "STANDARD_READY_NOT_IMPLEMENTED", "package schema status")
    need(schema.get("package_root") == "skills/<domain-family>/<skill-name>/", "package root")
    need(schema.get("required_files") == ["SKILL.md", "agents/openai.yaml", "references/"], "required package files")
    need(schema.get("frontmatter", {}).get("required_keys") == ["name", "description", "license"], "frontmatter keys")
    need(schema.get("required_sections") == SKILL_SECTIONS, "required section order")
    need(schema.get("host_metadata", {}).get("required_interface_keys") == ["display_name", "short_description", "default_prompt"], "host interface keys")
    need(schema.get("license_policy", {}).get("current_project_status") == "MIT", "license governance status")
    need(schema.get("license_policy", {}).get("frontmatter_key") == "license", "license key")
    need(schema.get("output_contract", {}).get("status_values") and set(schema["output_contract"]["status_values"]) == STATUSES, "output status values")
    string_list(schema.get("output_contract", {}).get("required_fields"), "output fields", 8)
    need(schema.get("taxonomy_traceability", {}).get("required_fields") == ["accepted_name", "family", "tier", "jurisdiction_flags", "safety_class", "dependencies", "priority"], "taxonomy traceability")
    need(len(contract.get("layers", [])) == 4, "four validation layers")
    need([layer.get("id") for layer in contract["layers"]] == ["structural", "scenario_routing", "deterministic_fixture", "evaluation_report"], "validation layer order")
    categories = contract.get("scenario_categories")
    need(isinstance(categories, list) and len(categories) == 11, "scenario categories")
    need({item.get("id") for item in categories} == {"correct_invocation", "incorrect_invocation", "missing_inputs", "bad_inputs", "calculation_correctness", "unit_mismatch", "ambiguous_scenario", "expected_output_structure", "safety_boundary", "jurisdiction_conflicts", "unsupported_assumptions"}, "scenario category set")
    for item in categories:
        text(item.get("rule"), f"category {item.get('id')}.rule")
    need(contract.get("scenario_file_contract", {}).get("required_fields") == ["title", "category", "expected_routing", "prompt", "acceptance_checks", "risk_and_review_notes"], "scenario file fields")
    need(contract.get("fixture_contract", {}).get("required_fields") == ["case_id", "category", "target_skill", "inputs", "expected_status"], "fixture fields")
    need(set(contract.get("output_invariants", [])) >= {"status is declared", "scope is declared", "inputs/evidence are preserved", "assumptions are explicit", "validation notes are present", "missing/conflicting evidence is visible", "review or handoff owner is visible", "no approval claim exceeds authority boundary"}, "output invariants")
    need(len(contract.get("evaluation_rules", [])) >= 5, "evaluation rules")


def validate_templates(root: Path) -> None:
    skill = (root / "docs/templates/manufacturing-skill/SKILL.md.template").read_text(encoding="utf-8")
    metadata = (root / "docs/templates/manufacturing-skill/agents/openai.yaml.template").read_text(encoding="utf-8")
    reference = (root / "docs/templates/manufacturing-skill/references/checklist.md").read_text(encoding="utf-8")
    scenario = (root / "docs/templates/manufacturing-skill/tests/scenario.md.template").read_text(encoding="utf-8")
    fixture = json.loads((root / "docs/templates/manufacturing-skill/tests/fixture.json.template").read_text(encoding="utf-8").replace("<case-id>", "template-case").replace("<accepted-skill-name>", "template-skill").replace("<scenario-category>", "correct_invocation").replace("<COMPLETE|PARTIAL|NEEDS_INPUT|OUT_OF_SCOPE|SAFETY_ESCALATION|SOURCE_REVIEW_REQUIRED|ENGINEERING_REVIEW_REQUIRED>", "NEEDS_INPUT"))
    for section in SKILL_SECTIONS:
        need(re.search(rf"^## {re.escape(section)}\s*$", skill, re.MULTILINE), f"template missing section {section}")
    for marker in ("display_name", "short_description", "default_prompt"):
        need(marker in metadata, f"metadata template missing {marker}")
    for marker in ("Publisher or owner:", "Freshness rule:", "Permitted-use note:"):
        need(marker in reference, f"reference template missing {marker}")
    for marker in ("Category:", "Expected routing:", "Acceptance checks:", "Risk and review notes:"):
        need(marker in scenario, f"scenario template missing {marker}")
    need(set(fixture) >= {"case_id", "category", "target_skill", "inputs", "expected_status"}, "fixture template fields")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        schema = json.loads((root / "docs/architecture/skill-package-schema.json").read_text(encoding="utf-8"))
        contract = json.loads((root / "docs/architecture/skill-validation-contract.json").read_text(encoding="utf-8"))
        validate_schema(schema, contract)
        validate_templates(root)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("PASS: AM-06 authoring standard; package layout, frontmatter, 16 ordered sections, host metadata, references, output contract, 4 validation layers, 11 scenario categories, and templates verified; no skill implementation or host installation evaluated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
