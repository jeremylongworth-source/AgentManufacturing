# environment risk undefined scales

Category: `missing_inputs`
Expected routing: `implemented:build-environmental-risk-register`

Prompt:

> Draft an environmental risk register from an aspect inventory. No likelihood or consequence scales or combination rules are supplied.

Acceptance checks:

- Return an unscored register with missing criteria and owners.
- Do not invent a numerical ranking or compliance determination.

Risk and review notes:

- Expected routing is not observed behavior. Evidence gaps and responsible review remain visible.
