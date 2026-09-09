"""Validate the AM-13 Families 04 and 05 process-engineering packages."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


SECTIONS = ["Overview", "Triggers", "Non-Triggers", "Required Inputs", "Optional Inputs", "Assumptions", "Core Workflow", "Calculations", "Validation", "Exception Handling", "Source Usage", "Output Contract", "Safety Requirements", "References", "Examples", "Testing"]
EXPECTED = {
    "map-manufacturing-process": ("04", "skills/family-04-process-engineering/map-manufacturing-process", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "build-process-routing": ("04", "skills/family-04-process-engineering/build-process-routing", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "identify-process-inputs-outputs": ("04", "skills/family-04-process-engineering/identify-process-inputs-outputs", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "review-process-parameter-control": ("04", "skills/family-04-process-engineering/review-process-parameter-control", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["STANDARDS_DEPENDENT", "SECTOR_REGULATED"]),
    "compare-process-alternatives": ("04", "skills/family-04-process-engineering/compare-process-alternatives", "P2", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["SECTOR_REGULATED"]),
    "build-process-control-plan": ("04", "skills/family-04-process-engineering/build-process-control-plan", "P1", "ENGINEERING_OR_CERTIFICATION_BOUNDARY", "PENDING_CONTEXT", ["STANDARDS_DEPENDENT", "SECTOR_REGULATED"]),
    "calculate-takt-time": ("05", "skills/family-05-performance/calculate-takt-time", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "calculate-production-capacity": ("05", "skills/family-05-performance/calculate-production-capacity", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "analyze-cycle-time": ("05", "skills/family-05-performance/analyze-cycle-time", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "balance-production-line": ("05", "skills/family-05-performance/balance-production-line", "P2", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "calculate-first-pass-yield": ("05", "skills/family-05-performance/calculate-first-pass-yield", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "calculate-oee": ("05", "skills/family-05-performance/calculate-oee", "P0", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "analyze-changeover-loss": ("05", "skills/family-05-performance/analyze-changeover-loss", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "calculate-throughput": ("05", "skills/family-05-performance/calculate-throughput", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "calculate-capacity-utilization": ("05", "skills/family-05-performance/calculate-capacity-utilization", "P2", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "calculate-rolled-throughput-yield": ("05", "skills/family-05-performance/calculate-rolled-throughput-yield", "P2", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "calculate-scrap-rate": ("05", "skills/family-05-performance/calculate-scrap-rate", "P1", "ROUTINE", "GENERIC_METHOD_ONLY", []),
    "calculate-rework-rate": ("05", "skills/family-05-performance/calculate-rework-rate", "P2", "ROUTINE", "GENERIC_METHOD_ONLY", []),
}
PRIVATE_PATTERNS = [r"password", r"secret", r"credential", r"api[_ -]?key", r"token", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"]


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def taxonomy(root: Path) -> dict[str, dict]:
    data = json.loads((root / "docs/architecture/taxonomy-index.yaml").read_text(encoding="utf-8"))
    return {item["name"]: item for item in data["skills"]}


def validate_package(root: Path, name: str, spec: tuple, records: dict[str, dict]) -> None:
    family, package_rel, priority, safety, jurisdiction, flags = spec
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
    need(fields.get("license") == "MIT", f"{name}: licence")
    need(re.findall(r"^## ([^\n]+)$", content, re.MULTILINE) == SECTIONS, f"{name}: sections")
    metadata = next((line for line in content.splitlines() if line.startswith("**Taxonomy metadata:**")), "")
    need(metadata, f"{name}: metadata block")
    record = records.get(name)
    need(record is not None and record["family"] == family, f"{name}: taxonomy family")
    need(record["priority"] == priority, f"{name}: taxonomy priority")
    need(record["safety_class"] == safety, f"{name}: taxonomy safety")
    need(record["jurisdiction"]["assessment"] == jurisdiction, f"{name}: taxonomy jurisdiction")
    for marker in (family, priority, safety, jurisdiction, "TAXONOMY_ACCEPTED_NOT_IMPLEMENTED") + tuple(flags):
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
    content = (root / "tests/evaluations/AM-13-process-engineering-acceptance.md").read_text(encoding="utf-8")
    for phrase in ("Status: `READY_FOR_REVIEW`", "Runtime model behavior", "NOT_RUN", "Residual risk"):
        need(phrase in content, f"AM-13 evaluation missing {phrase!r}")
    for name in EXPECTED:
        need(f"`{name}`" in content, f"AM-13 evaluation missing {name}")


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
    print("PASS: AM-13 process engineering; eighteen Family 04/05 packages, taxonomy traces, adapters, references, and acceptance evidence validated; runtime model behavior remains NOT_RUN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
