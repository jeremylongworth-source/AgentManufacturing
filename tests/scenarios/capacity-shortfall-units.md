# Capacity shortfall with incompatible time basis

Category: `unit_mismatch`
Expected routing: `implemented:identify-capacity-shortfall`

Prompt:

> Compare required load of 480 units per day with available capacity of 30 units per hour for the same operation. Identify the time-basis conversion needed before reporting a shortfall; do not assume a 24-hour production day.

Acceptance checks:

- Identify the units/day versus units/hour mismatch.
- Request or use a supplied operating-hours basis before comparison.
- Do not invent a calendar, overtime, or recovery capacity.

Risk and review notes:

- Capacity is calendar-dependent; a silent 24-hour assumption would mislead planning.
