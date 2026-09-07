# Gauge control missing identity

Category: `bad_inputs`
Expected routing: `implemented:review-gauge-control`

Prompt:

> Review a calibrated gauge record whose physical label and unique identity are missing.

Acceptance checks:

- Identity and status control gaps are reported.
- Use approval is withheld.

Risk and review notes:

- Calibration evidence cannot substitute for gauge control.
