"""Calculate a bounded defective-unit rate from supplied, linked counts."""

from __future__ import annotations

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import json
from pathlib import Path
import sys


def calculate(data: dict) -> dict:
    """Return NEEDS_INPUT for incomplete scope, inconsistent counts, or units."""
    gaps = []
    scope = data.get("scope", {})
    if not isinstance(scope, dict):
        scope = {}
    for key in ("supplier", "lot", "part", "period", "population_basis"):
        if not isinstance(scope.get(key), str) or not scope[key].strip():
            gaps.append(f"Missing scope: {key}")
    units = data.get("units", {})
    if not isinstance(units, dict):
        units = {}
    if not isinstance(units.get("defective"), str) or not units["defective"].strip() or units.get("defective") != units.get("exposure"):
        gaps.append("Defective and exposure counts require the same explicit unit")
    counts = {}
    for key in ("defective_units", "exposed_units"):
        raw = data.get(key)
        try:
            value = Decimal(str(raw))
            if isinstance(raw, bool) or not value.is_finite() or value < 0 or value != value.to_integral_value():
                raise ValueError()
            counts[key] = value
        except (InvalidOperation, ValueError):
            gaps.append(f"Invalid or missing count: {key}")
    if "exposed_units" in counts and counts["exposed_units"] == 0:
        gaps.append("Exposure must be greater than zero")
    if len(counts) == 2 and counts["defective_units"] > counts["exposed_units"]:
        gaps.append("Unique defective units exceed exposure")
    if gaps:
        return {"status": "NEEDS_INPUT", "scope": scope, "gaps": gaps, "rate_percent": None}
    numerator = counts["defective_units"]
    denominator = counts["exposed_units"]
    rate = numerator / denominator * Decimal(100)
    return {
        "status": "READY_FOR_REVIEW",
        "scope": scope,
        "numerator": str(numerator),
        "denominator": str(denominator),
        "units": units["defective"],
        "formula": "unique defective units / exposed units * 100",
        "rate_percent": str(rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)),
        "rounding": "two decimal places, ROUND_HALF_UP",
        "attribution": "Grouping uses supplied lot linkage; causation is not established.",
    }


def main() -> int:
    try:
        content = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) == 2 else sys.stdin.read()
        data = json.loads(content)
        if not isinstance(data, dict):
            raise ValueError("Input must be a JSON object")
        print(json.dumps(calculate(data), indent=2))
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
