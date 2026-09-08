# Analyze metered energy intensity

- Input records must describe interval consumption, not cumulative register readings or demand peaks. Confirm import/export and meter-reset treatment with the data owner.
- Require energy and activity to cover the same period per record. Different periods may be compared only on a consistent product/output and meter-allocation basis.
- Keep separate records for dissimilar meters. Even matching labels do not verify physical coverage; supplied boundaries remain assumptions.
- Do not sum a parent meter and its submeters or calculate emissions/savings from energy alone.

## Calculator input and interpretation

Run `python scripts/energy_intensity.py input.json` from this package, or pass JSON on stdin:

```json
{"records":[{"id":"M1-Aug","facility":"Plant A","boundary":"Line 1 only","allocation_basis":"metered dedicated line","product_basis":"Product A good output","activity_unit":"parts","period":"2026-08","energy_period":"2026-08","activity_period":"2026-08","reading_type":"interval_consumption","energy_unit":"kWh","energy":1200,"activity":400}]}
```

This example returns 1200 kWh / 400 parts = 3.0000 kWh/part. Each record needs its own ID and explicit interval, allocation, and output basis. Supported units are kWh, MWh, MJ, and GJ. Values must be finite, nonnegative, and at most 1e18; activity must be positive. Unknown units and cumulative readings require input reconciliation.

The helper retains valid rows alongside invalid rows. `comparable` is true only for multiple valid records sharing facility, meter boundary, allocation, product basis, and activity unit. It does not aggregate overlapping meters, verify labels, or prove efficiency gains.

## Source boundary

Record source ID, date, applicable scope, revision, claim location, and verification status. No source is assumed applicable from its title alone. For AM-25's bounded catalogue and government-guidance checks, see the repository [source evidence](../../../../docs/development/AM-25-source-evidence.md). Package methods remain usable with supplied evidence if this repository-level context is absent; a dependent source claim must await verification.
