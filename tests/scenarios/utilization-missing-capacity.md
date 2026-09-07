# Utilization with missing rated capacity

Category: `missing_inputs`
Expected routing: `implemented:calculate-capacity-utilization`

Prompt:

> Calculate capacity utilization from actual occupied time for one shift. The rated available time denominator is absent; identify the missing denominator instead of inventing a utilization percentage.

Acceptance checks:

- Return the missing rated-capacity evidence.
- Do not use zero or a generic benchmark as the denominator.
- Keep utilization distinct from a capacity estimate and OEE.

Risk and review notes:

- Utilization cannot be calculated without a defined capacity basis.
