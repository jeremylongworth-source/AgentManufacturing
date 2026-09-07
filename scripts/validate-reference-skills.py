"""Validate the five AM-10 reference skill packages and their proof record."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from typing import Any


REQUIRED_SECTIONS = [
    "Overview", "Triggers", "Non-Triggers", "Required Inputs", "Optional Inputs", "Assumptions",
    "Core Workflow", "Calculations", "Validation", "Exception Handling", "Source Usage", "Output Contract",
    "Safety Requirements", "References", "Examples", "Testing",
]
EXPECTED = {
    "calculate-oee": {"family": "05", "package": "skills/family-05-performance/calculate-oee", "safety": "ROUTINE", "tier": "CORE", "jurisdiction": "GENERIC_METHOD_ONLY", "evidence": ["AM08-F05"]},
    "build-production-plan": {"family": "02", "package": "skills/family-02-production-planning/build-production-plan", "safety": "ROUTINE", "tier": "CORE", "jurisdiction": "GENERIC_METHOD_ONLY", "evidence": []},
    "triage-nonconformance": {"family": "09", "package": "skills/family-09-quality/triage-nonconformance", "safety": "ROUTINE", "tier": "CORE", "jurisdiction": "GENERIC_METHOD_ONLY", "evidence": []},
    "review-lockout-program": {"family": "11", "package": "skills/family-11-safety/review-lockout-program", "safety": "HAZARDOUS_OPERATION", "tier": "CORE", "jurisdiction": "PENDING_CONTEXT", "evidence": []},
    "assess-made-in-canada-claim": {"family": "20", "package": "skills/family-20-canadian-compliance/assess-made-in-canada-claim", "safety": "REGULATED", "tier": "CANADA_OVERLAY", "jurisdiction": "PENDING_CONTEXT", "evidence": []},
}
PRIVATE_PATTERNS = [r"password", r"secret", r"credential", r"api[_ -]?key", r"token", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"]


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def parse_frontmatter(content: str, label: str) -> dict[str, str]:
    need(content.startswith("---\n"), f"{label}: frontmatter start")
    end = content.find("\n---", 4)
    need(end > 0, f"{label}: frontmatter end")
    fields: dict[str, str] = {}
    for line in content[4:end].splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        need(separator and key.strip() and value.strip(), f"{label}: malformed frontmatter")
        fields[key.strip()] = value.strip()
    return fields


def load_taxonomy(root: Path) -> dict[str, dict[str, Any]]:
    data = json.loads((root / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8"))
    return {item["name"]: item for item in data.get("skills", [])}


def parse_openai_metadata(path: Path, name: str) -> str:
    content = path.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        need(re.search(rf"^\s+{key}:\s+.+$", content, re.MULTILINE), f"{name}: openai metadata {key}")
    prompt = re.search(r"^\s+default_prompt:\s+(.+)$", content, re.MULTILINE)
    need(prompt is not None and f"${name}" in prompt.group(1), f"{name}: default prompt invocation")
    return content


def validate_package(root: Path, name: str, expected: dict[str, Any], taxonomy: dict[str, dict[str, Any]]) -> None:
    package = root / expected["package"]
    skill_path = package / "SKILL.md"
    need(skill_path.exists(), f"{name}: SKILL.md missing")
    content = skill_path.read_text(encoding="utf-8")
    fields = parse_frontmatter(content, name)
    need(fields.get("name") == name, f"{name}: frontmatter name")
    need(fields.get("description", "").endswith("."), f"{name}: one-sentence description")
    need(fields.get("license") == "PENDING_PROJECT_GOVERNANCE", f"{name}: licence placeholder")
    headings = re.findall(r"^## ([^\n]+)$", content, re.MULTILINE)
    need(headings == REQUIRED_SECTIONS, f"{name}: section order")
    metadata = next((line for line in content.splitlines() if line.startswith("**Taxonomy metadata:**")), "")
    need(metadata, f"{name}: taxonomy metadata block")
    for value in (expected["family"], expected["tier"], expected["safety"], expected["jurisdiction"], "P0", "TAXONOMY_ACCEPTED_NOT_IMPLEMENTED"):
        need(value in metadata, f"{name}: taxonomy metadata {value}")
    record = taxonomy.get(name)
    need(record is not None, f"{name}: accepted taxonomy record missing")
    need(record.get("family") == expected["family"], f"{name}: taxonomy family mismatch")
    need(record.get("tier") == expected["tier"], f"{name}: taxonomy tier mismatch")
    need(record.get("safety_class") == expected["safety"], f"{name}: taxonomy safety mismatch")
    need(record.get("jurisdiction", {}).get("assessment") == expected["jurisdiction"], f"{name}: taxonomy jurisdiction mismatch")
    need((package / "agents" / "openai.yaml").exists(), f"{name}: agents/openai.yaml missing")
    parse_openai_metadata(package / "agents" / "openai.yaml", name)
    references = list((package / "references").glob("*.md"))
    need(references, f"{name}: reference file missing")
    for ref in references:
        ref_text = ref.read_text(encoding="utf-8")
        need(ref_text.strip(), f"{name}: empty reference {ref.name}")
        for pattern in PRIVATE_PATTERNS:
            need(re.search(pattern, ref_text, re.IGNORECASE) is None, f"{name}: private-data pattern in {ref.name}")
    need("Expected routing is not observed behavior" in content, f"{name}: evaluation boundary reminder")
    for evidence in expected["evidence"]:
        need(evidence in "\n".join(ref.read_text(encoding="utf-8") for ref in references), f"{name}: deterministic evidence {evidence}")


def validate_proof_record(root: Path) -> None:
    path = root / "tests/evaluations/AM-10-reference-skill-acceptance.md"
    content = path.read_text(encoding="utf-8")
    for phrase in ("Status: `READY_FOR_REVIEW`", "Runtime model behavior", "NOT_RUN", "Residual risk", "No package is installed"):
        need(phrase in content, f"AM-10 proof record missing {phrase!r}")
    for name in EXPECTED:
        need(f"`{name}`" in content, f"AM-10 proof record missing {name}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        contract = json.loads((root / "docs/architecture/reference-skill-proof-contract.json").read_text(encoding="utf-8"))
        need(contract.get("schema_version") == "AM-10-reference-skill-proof-1", "AM-10 contract schema version")
        need(contract.get("status") == "REFERENCE_PACKAGES_READY_NOT_BEHAVIORALLY_EVALUATED", "AM-10 contract status")
        need(contract.get("required_sections") == REQUIRED_SECTIONS, "AM-10 required sections")
        taxonomy = load_taxonomy(root)
        for name, expected in EXPECTED.items():
            validate_package(root, name, expected, taxonomy)
        validate_proof_record(root)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("PASS: AM-10 reference packages; five taxonomy records, package contracts, references, and review evidence validated; runtime model behavior remains NOT_RUN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
