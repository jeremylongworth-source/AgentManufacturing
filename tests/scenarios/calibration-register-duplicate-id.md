# Calibration register duplicate ID

Category: `bad_inputs`
Expected routing: `implemented:build-calibration-register`

Prompt:

> Build a calibration register from records containing the same instrument identifier at two locations.

Acceptance checks:

- Duplicate identity is reported.
- No status or validity is inferred.

Risk and review notes:

- Identity reconciliation requires a metrology owner.
