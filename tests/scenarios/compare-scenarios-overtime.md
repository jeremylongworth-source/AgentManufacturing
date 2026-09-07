# Compare production scenarios with inconsistent overtime

Category: `ambiguous_scenario`
Expected routing: `implemented:compare-production-scenarios`

Prompt:

> Compare two production plans under the same demand. Scenario A includes overtime cost and capacity; Scenario B omits overtime but uses the same output target. Show the noncomparable assumption before ranking either option.

Acceptance checks:

- Identify the inconsistent overtime and capacity basis.
- Do not rank incomparable alternatives as if they shared assumptions.
- Return the evidence needed from the decision owner.

Risk and review notes:

- Cost and feasibility conclusions depend on a common basis.
