"""Validate the bounded AM-11 manufacturing core and standard-work packages."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from typing import Any


SECTIONS = [
    "Overview", "Triggers", "Non-Triggers", "Required Inputs", "Optional Inputs", "Assumptions",
    "Core Workflow", "Calculations", "Validation", "Exception Handling", "Source Usage", "Output Contract",
    "Safety Requirements", "References", "Examples", "Testing",
]
EXPECTED = {
    "classify-manufacturing-operation": {"family": "01", "package": "skills/family-01-fundamentals/classify-manufacturing-operation", "priority": "P1"},
    "analyze-product-process-profile": {"family": "01", "package": "skills/family-01-fundamentals/analyze-product-process-profile", "priority": "P2"},
    "analyze-production-constraints": {"family": "01", "package": "skills/family-01-fundamentals/analyze-production-constraints", "priority": "P1"},
    "identify-manufacturing-bottleneck": {"family": "01", "package": "skills/family-01-fundamentals/identify-manufacturing-bottleneck", "priority": "P1"},
    "draft-work-instruction": {"family": "03", "package": "skills/family-03-standard-work/draft-work-instruction", "priority": "P1"},
    "review-work-instruction": {"family": "03", "package": "skills/family-03-standard-work/review-work-instruction", "priority": "P1"},
    "build-standard-work": {"family": "03", "package": "skills/family-03-standard-work/build-standard-work", "priority": "P1"},
    "analyze-standard-work-deviation": {"family": "03", "package": "skills/family-03-standard-work/analyze-standard-work-deviation", "priority": "P2"},
    "review-operator-checklist": {"family": "03", "package": "skills/family-03-standard-work/review-operator-checklist", "priority": "P2"},
}
PRIVATE_PATTERNS = [r"password", r"secret", r"credential", r"api[_ -]?key", r"token", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"]


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def frontmatter(content: str, name: str) -> dict[str, str]:
    need(content.startswith("---\n"), f"{name}: frontmatter start")
    end = content.find("\n---", 4)
    need(end > 0, f"{name}: frontmatter end")
    values: dict[str, str] = {}
    for line in content[4:end].splitlines():
        key, sep, value = line.partition(":")
        if line.strip():
            need(sep and key.strip() and value.strip(), f"{name}: malformed frontmatter")
            values[key.strip()] = value.strip()
    return values


def taxonomy(root: Path) -> dict[str, dict[str, Any]]:
    data = json.loads((root / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8"))
    return {record["name"]: record for record in data["skills"]}


def validate_package(root: Path, name: str, expected: dict[str, str], records: dict[str, dict[str, Any]]) -> None:
    package = root / expected["package"]
    skill = package / "SKILL.md"
    need(skill.exists(), f"{name}: SKILL.md missing")
    content = skill.read_text(encoding="utf-8")
    fields = frontmatter(content, name)
    need(fields.get("name") == name, f"{name}: name")
    need(fields.get("description", "").endswith("."), f"{name}: description")
    need(fields.get("license") == "MIT", f"{name}: approved licence")
    need(re.findall(r"^## ([^\n]+)$", content, re.MULTILINE) == SECTIONS, f"{name}: sections")
    metadata = next((line for line in content.splitlines() if line.startswith("**Taxonomy metadata:**")), "")
    need(metadata, f"{name}: taxonomy metadata")
    record = records.get(name)
    need(record is not None, f"{name}: canonical taxonomy record")
    need(record["family"] == expected["family"], f"{name}: family mismatch")
    need(record["priority"] == expected["priority"], f"{name}: priority mismatch")
    for marker in (expected["family"], "CORE", expected["priority"], "ROUTINE", "GENERIC_METHOD_ONLY", "TAXONOMY_ACCEPTED_NOT_IMPLEMENTED"):
        need(marker in metadata, f"{name}: metadata {marker}")
    adapter = package / "agents" / "openai.yaml"
    need(adapter.exists(), f"{name}: adapter missing")
    adapter_text = adapter.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        need(re.search(rf"^\s+{key}:\s+.+$", adapter_text, re.MULTILINE), f"{name}: adapter {key}")
    need(f"${name}" in adapter_text, f"{name}: adapter invocation")
    refs = list((package / "references").glob("*.md"))
    need(refs, f"{name}: references")
    for ref in refs:
        text = ref.read_text(encoding="utf-8")
        need(text.strip(), f"{name}: empty reference {ref.name}")
        for pattern in PRIVATE_PATTERNS:
            need(re.search(pattern, text, re.IGNORECASE) is None, f"{name}: private pattern in {ref.name}")
    need("Expected routing is not observed behavior" in content, f"{name}: evaluation boundary")


def validate_evaluation(root: Path) -> None:
    content = (root / "tests/evaluations/AM-11-core-acceptance.md").read_text(encoding="utf-8")
    for phrase in ("Status: `READY_FOR_REVIEW`", "Runtime model behavior", "NOT_RUN", "Residual risk"):
        need(phrase in content, f"AM-11 evaluation missing {phrase!r}")
    for name in EXPECTED:
        need(f"`{name}`" in content, f"AM-11 evaluation missing {name}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        records = taxonomy(root)
        for name, expected in EXPECTED.items():
            validate_package(root, name, expected, records)
        validate_evaluation(root)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("PASS: AM-11 manufacturing core; nine family-01/family-03 packages, taxonomy traces, adapters, references, and acceptance evidence validated; runtime model behavior remains NOT_RUN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
