"""Validate the AM-12 Family 02 production-planning packages."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


SECTIONS = ["Overview", "Triggers", "Non-Triggers", "Required Inputs", "Optional Inputs", "Assumptions", "Core Workflow", "Calculations", "Validation", "Exception Handling", "Source Usage", "Output Contract", "Safety Requirements", "References", "Examples", "Testing"]
EXPECTED = {
    "build-production-plan": ("skills/family-02-production-planning/build-production-plan", "P0"),
    "calculate-production-requirement": ("skills/family-02-production-planning/calculate-production-requirement", "P1"),
    "sequence-production-orders": ("skills/family-02-production-planning/sequence-production-orders", "P1"),
    "analyze-schedule-adherence": ("skills/family-02-production-planning/analyze-schedule-adherence", "P2"),
    "identify-capacity-shortfall": ("skills/family-02-production-planning/identify-capacity-shortfall", "P1"),
    "plan-production-changeover": ("skills/family-02-production-planning/plan-production-changeover", "P1"),
    "compare-production-scenarios": ("skills/family-02-production-planning/compare-production-scenarios", "P2"),
    "calculate-production-lead-time": ("skills/family-02-production-planning/calculate-production-lead-time", "P1"),
    "review-production-order-readiness": ("skills/family-02-production-planning/review-production-order-readiness", "P1"),
    "compare-production-lot-sizes": ("skills/family-02-production-planning/compare-production-lot-sizes", "P2"),
}
PRIVATE_PATTERNS = [r"password", r"secret", r"credential", r"api[_ -]?key", r"token", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"]


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def load_taxonomy(root: Path) -> dict[str, dict]:
    data = json.loads((root / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8"))
    return {item["name"]: item for item in data["skills"]}


def validate_package(root: Path, name: str, package_rel: str, priority: str, records: dict[str, dict]) -> None:
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
    need(fields.get("name") == name, f"{name}: frontmatter name")
    need(fields.get("description", "").endswith("."), f"{name}: description")
    need(fields.get("license") == "PENDING_PROJECT_GOVERNANCE", f"{name}: licence")
    need(re.findall(r"^## ([^\n]+)$", content, re.MULTILINE) == SECTIONS, f"{name}: section order")
    metadata = next((line for line in content.splitlines() if line.startswith("**Taxonomy metadata:**")), "")
    need(metadata, f"{name}: metadata block")
    record = records.get(name)
    need(record is not None and record["family"] == "02", f"{name}: family 02 taxonomy trace")
    need(record["priority"] == priority, f"{name}: priority trace")
    for marker in ("02", "CORE", priority, "ROUTINE", "GENERIC_METHOD_ONLY", "TAXONOMY_ACCEPTED_NOT_IMPLEMENTED"):
        need(marker in metadata, f"{name}: metadata {marker}")
    adapter = package / "agents/openai.yaml"
    need(adapter.exists(), f"{name}: adapter")
    adapter_text = adapter.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        need(re.search(rf"^\s+{key}:\s+.+$", adapter_text, re.MULTILINE), f"{name}: adapter {key}")
    need(f"${name}" in adapter_text, f"{name}: adapter invocation")
    refs = list((package / "references").glob("*.md"))
    need(refs, f"{name}: reference")
    for ref in refs:
        text = ref.read_text(encoding="utf-8")
        need(text.strip(), f"{name}: empty reference")
        for pattern in PRIVATE_PATTERNS:
            need(re.search(pattern, text, re.IGNORECASE) is None, f"{name}: private pattern")
    need("Expected routing is not observed behavior" in content, f"{name}: boundary reminder")


def validate_evaluation(root: Path) -> None:
    content = (root / "tests/evaluations/AM-12-production-planning-acceptance.md").read_text(encoding="utf-8")
    for phrase in ("Status: `READY_FOR_REVIEW`", "Runtime model behavior", "NOT_RUN", "Residual risk"):
        need(phrase in content, f"AM-12 evaluation missing {phrase!r}")
    for name in EXPECTED:
        need(f"`{name}`" in content, f"AM-12 evaluation missing {name}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        records = load_taxonomy(root)
        for name, (package, priority) in EXPECTED.items():
            validate_package(root, name, package, priority, records)
        validate_evaluation(root)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("PASS: AM-12 production planning; ten Family 02 packages, taxonomy traces, adapters, references, and acceptance evidence validated; runtime model behavior remains NOT_RUN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
