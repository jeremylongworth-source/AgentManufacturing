# Nonconformance triage missing requirement

Category: `missing_inputs`
Expected routing: `implemented:triage-nonconformance`

Prompt:

> Triage a reported deviation when the observed condition is supplied but the governing requirement is missing.

Acceptance checks:

- Observation is separated from confirmed nonconformance.
- Requirement gap and next owner are returned.

Risk and review notes:

- Disposition is not decided.
