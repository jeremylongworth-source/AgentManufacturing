# Correct OEE calculation request

Category: `correct_invocation`
Expected routing: `implemented:calculate-oee`

Prompt:

> Calculate OEE for one production asset for yesterday's planned production period. I have planned production time, run time, ideal cycle time, total count, and good count. Show availability, performance, quality, the raw ratio, percentage display, assumptions, and validation notes.

Acceptance checks:

- Keep the asset and time window as one declared boundary.
- Show all three OEE components and the raw ratio before display rounding.
- State that the result is analysis support, not a release or compliance decision.

Risk and review notes:

- The reference package is implemented for structural and routing proof; runtime behavior remains a separate evaluation.
- A planner or quality reviewer should confirm the count and ideal-cycle definitions.
