"""Validate AM-23 automation and advanced-manufacturing packages."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


SECTIONS = ["Overview", "Triggers", "Non-Triggers", "Required Inputs", "Optional Inputs", "Assumptions", "Core Workflow", "Calculations", "Validation", "Exception Handling", "Source Usage", "Output Contract", "Safety Requirements", "References", "Examples", "Testing"]
EXPECTED = {
    "assess-automation-opportunity": ("skills/family-16-advanced-manufacturing/assess-automation-opportunity", "P2", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "evaluate-robotics-application": ("skills/family-16-advanced-manufacturing/evaluate-robotics-application", "P2", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["PROVINCIAL_REQUIRED", "STANDARDS_DEPENDENT", "SECTOR_REGULATED"]),
    "evaluate-cobot-application": ("skills/family-16-advanced-manufacturing/evaluate-cobot-application", "P2", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["PROVINCIAL_REQUIRED", "STANDARDS_DEPENDENT", "SECTOR_REGULATED"]),
    "evaluate-machine-vision-application": ("skills/family-16-advanced-manufacturing/evaluate-machine-vision-application", "P2", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "evaluate-additive-manufacturing-application": ("skills/family-16-advanced-manufacturing/evaluate-additive-manufacturing-application", "P2", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["STANDARDS_DEPENDENT", "SECTOR_REGULATED"]),
    "build-automation-business-case": ("skills/family-16-advanced-manufacturing/build-automation-business-case", "P2", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "assess-automation-process-readiness": ("skills/family-16-advanced-manufacturing/assess-automation-process-readiness", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "review-human-machine-interface-risk": ("skills/family-16-advanced-manufacturing/review-human-machine-interface-risk", "P2", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["STANDARDS_DEPENDENT", "SECTOR_REGULATED"]),
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
    need(record is not None and record["family"] == "16", f"{name}: taxonomy family")
    need(record["priority"] == priority, f"{name}: priority")
    need(record["safety_class"] == safety, f"{name}: safety")
    need(record["jurisdiction"]["assessment"] == jurisdiction, f"{name}: jurisdiction")
    for marker in ("16", "CORE", priority, safety, jurisdiction, "TAXONOMY_ACCEPTED_NOT_IMPLEMENTED") + tuple(flags):
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
        for pattern in PRIVATE_PATTERNS:
            need(re.search(pattern, text, re.IGNORECASE) is None, f"{name}: private pattern")
    need("Expected routing is not observed behavior" in content, f"{name}: evaluation boundary")


def validate_evaluation(root: Path) -> None:
    content = (root / "tests/evaluations/AM-23-advanced-manufacturing-acceptance.md").read_text(encoding="utf-8")
    for phrase in ("Status: `READY_FOR_REVIEW`", "Runtime model behavior", "NOT_RUN", "Residual risk"):
        need(phrase in content, f"AM-23 evaluation missing {phrase!r}")
    for name in EXPECTED:
        need(f"`{name}`" in content, f"AM-23 evaluation missing {name}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        records = taxonomy(root)
        for name, spec in EXPECTED.items():
            validate_package(root, name, spec, records)
        validate_evaluation(root)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("PASS: AM-23 advanced manufacturing; eight Family 16 packages, taxonomy traces, adapters, references, and acceptance evidence validated; runtime model behavior remains NOT_RUN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
