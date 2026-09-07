# Takt with zero demand

Category: `calculation_correctness`
Expected routing: `implemented:calculate-takt-time`

Prompt:

> Calculate takt time from 480 minutes of net available time and zero customer demand for the stated period. Show the denominator and return undefined or not applicable instead of dividing by zero.

Acceptance checks:

- Preserve zero demand as the denominator evidence.
- Return an undefined/not-applicable status rather than infinity or a fabricated rate.
- Do not turn takt into a machine setting.

Risk and review notes:

- Zero demand is a valid edge case with no finite takt result.
