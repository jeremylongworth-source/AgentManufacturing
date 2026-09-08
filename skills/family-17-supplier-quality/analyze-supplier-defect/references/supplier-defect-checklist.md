# Supplier defect checklist

- Supplier, lot, part, and period identity
- Defect mode and reason coding
- Receipt or inspection exposure
- Denominator and rate basis
- Attribution and disposition boundary

## Count-summary calculation

Use the local helper only for a supplied summary of unique defective units and a matched exposure population. It does not deduplicate raw rows or verify lot provenance.

```json
{
  "scope": {"supplier": "A", "lot": "L1", "part": "P1", "period": "2026-08", "population_basis": "inspected"},
  "units": {"defective": "parts", "exposure": "parts"},
  "defective_units": 5,
  "exposed_units": 200
}
```

Run `python scripts/defect_rate.py input.json` from this package directory, or supply JSON on stdin. The result is 2.50 percent. Seven defect occurrences on five units must still use five unique defective units in this formula.

Missing linkage, missing/mixed units, invalid counts, zero exposure, or a numerator exceeding exposure returns `NEEDS_INPUT` with a null rate. Negative, fractional, nonfinite, and boolean counts are invalid. Keep raw observations intact; grouping and a rate do not prove supplier causation.
