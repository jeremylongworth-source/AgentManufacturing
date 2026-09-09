"""Run the repository's dependency-free validation gate in order."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


VALIDATORS = [
    "validate-candidate-register.py",
    "validate-taxonomy.py",
    "validate-jurisdiction-model.py",
    "validate-safety-boundary-model.py",
    "validate-skill-authoring-standard.py",
    "validate-source-standards-standard.py",
    "validate-calculation-standard.py",
    "validate-validation-framework.py",
    "validate-reference-skills.py",
    "validate-implemented-skills.py",
    "validate-production-planning.py",
    "validate-process-engineering.py",
    "validate-quality-management.py",
    "validate-metrology-spc.py",
    "validate-nonconformance-capa.py",
    "validate-maintenance-reliability.py",
    "validate-manufacturing-safety.py",
    "validate-materials-traceability.py",
    "validate-workforce-shift.py",
    "validate-lean-improvement.py",
    "validate-systems-data.py",
    "validate-advanced-manufacturing.py",
    "validate-supplier-change.py",
    "validate-environment-energy-waste.py",
    "validate-canadian-federal.py",
    "validate-provincial-overlays.py",
    "validate-professional-skillsets.py",
    "validate-sector-framework.py",
    "validate-integration-evaluation.py",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    for validator in VALIDATORS:
        path = root / "scripts" / validator
        completed = subprocess.run([sys.executable, str(path)], cwd=root, check=False)
        if completed.returncode != 0:
            print(f"FAIL: validation gate stopped at {validator}", file=sys.stderr)
            return completed.returncode
    print(f"PASS: all {len(VALIDATORS)} repository validators completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
