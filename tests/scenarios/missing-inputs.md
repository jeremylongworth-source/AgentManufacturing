# OEE request with missing quality input

Category: `missing_inputs`
Expected routing: `implemented:calculate-oee`

Prompt:

> Calculate OEE for a line using 480 minutes planned, 420 minutes run, a 0.5 minute ideal cycle, and 780 total units. I do not have the good-unit count yet.

Acceptance checks:

- Return valid availability and performance partial values if calculated.
- Request good count before returning OEE.
- Do not assume all total units were good.

Risk and review notes:

- Missing quality evidence blocks the final OEE result.
- Preserve the missing-input handoff for the responsible production or quality owner.
