"""Read-only energy intensity for declared interval consumption summaries."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
import json
from pathlib import Path
import sys

ENERGY_UNITS = {"kWh", "MWh", "MJ", "GJ"}
SCOPE_KEYS = ("facility", "boundary", "allocation_basis", "product_basis", "activity_unit")


def analyze(data):
    if not isinstance(data, dict) or not isinstance(data.get("records"), list) or not data["records"]:
        return {"status": "NEEDS_INPUT", "results": [], "comparable": False, "gaps": ["Nonempty records list required"]}
    results, signatures, seen, gaps = [], [], set(), []
    for row in data["records"]:
        if not isinstance(row, dict):
            gaps.append("Each record must be an object")
            continue
        errors = []
        for field in ("id", "period", "energy_period", "activity_period") + SCOPE_KEYS:
            if not isinstance(row.get(field), str) or not row[field].strip():
                errors.append(f"Missing {field}")
        identity = row.get("id")
        if isinstance(identity, str):
            if identity in seen:
                errors.append("Duplicate record ID")
            seen.add(identity)
        if row.get("period") != row.get("energy_period") or row.get("period") != row.get("activity_period"):
            errors.append("Energy and activity periods must match")
        if row.get("reading_type") != "interval_consumption":
            errors.append("Interval consumption required; cumulative readings are not supported")
        unit = row.get("energy_unit")
        if not isinstance(unit, str) or unit not in ENERGY_UNITS:
            errors.append("Unsupported energy unit; power and volume are not energy")
        values = {}
        for field in ("energy", "activity"):
            try:
                raw = row.get(field)
                value = Decimal(str(raw))
                if isinstance(raw, bool) or not value.is_finite() or value < 0 or value > Decimal("1e18"):
                    raise ValueError()
                if field == "activity" and value == 0:
                    raise ValueError()
                values[field] = value
            except (InvalidOperation, ValueError):
                errors.append(f"Invalid {field}; activity must be positive, values finite and nonnegative within 1e18")
        if errors:
            results.append({"id": identity, "status": "NEEDS_INPUT", "intensity": None, "gaps": errors})
            gaps.extend(errors)
            continue
        with localcontext() as ctx:
            ctx.prec = 60
            # Division is explicit so conversion precision is retained until display.
            energy = values["energy"]
            kwh = energy if unit == "kWh" else energy * 1000 if unit == "MWh" else energy / Decimal("3.6") if unit == "MJ" else energy * 1000 / Decimal("3.6")
            try:
                intensity = (kwh / values["activity"]).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
            except InvalidOperation:
                results.append({"id": identity, "status": "NEEDS_INPUT", "intensity": None, "gaps": ["Numeric range exceeds supported precision"]})
                gaps.append("Numeric range exceeds supported precision")
                continue
        signatures.append(tuple(row[key] for key in SCOPE_KEYS))
        results.append({"id": identity, "status": "READY_FOR_REVIEW", "period": row["period"],
                        "energy_kwh": str(kwh), "activity": str(values["activity"]),
                        "unit": "kWh/" + row["activity_unit"], "intensity": str(intensity),
                        "formula": "interval energy in kWh / matched production activity"})
    comparable = len(results) > 1 and not gaps and len(set(signatures)) == 1
    if len(set(signatures)) > 1:
        gaps.append("Meter boundary, facility, allocation, product basis, or activity units differ")
    return {"status": "NEEDS_INPUT" if gaps else "READY_FOR_REVIEW", "results": results,
            "comparable": comparable, "gaps": gaps,
            "limitation": "Supplied boundaries are not independently verified; no causal savings or efficiency gain is established."}


def main():
    try:
        content = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) == 2 else sys.stdin.read()
        print(json.dumps(analyze(json.loads(content)), indent=2))
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
