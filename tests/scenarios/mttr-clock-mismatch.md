# MTTR clock mismatch

Category: `unit_mismatch`
Expected routing: `implemented:calculate-mttr`

Prompt:

> Calculate MTTR when one record measures repair labor time and another measures elapsed outage time.

Acceptance checks:

- Clock definitions are not mixed.
- A coherent repair-time basis is requested.

Risk and review notes:

- MTTR is not all downtime.
