# Control chart missing order

Category: `missing_inputs`
Expected routing: `implemented:build-control-chart`

Prompt:

> Build a control chart from readings with values and limits but no timestamp or observation order.

Acceptance checks:

- Missing chronology is reported.
- No signal interpretation is fabricated.

Risk and review notes:

- Chart construction requires ordered evidence.
