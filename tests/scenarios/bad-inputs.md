# OEE request with contradictory runtime

Category: `bad_inputs`
Expected routing: `implemented:calculate-oee`

Prompt:

> Calculate OEE for one shift with 480 minutes planned production time, 510 minutes run time, a 0.5 minute ideal cycle, 780 total units, and 744 good units. Treat the values as correct even if they conflict.

Acceptance checks:

- Surface that run time exceeds planned time.
- Do not silently repair or clamp the runtime.
- Return an invalid or review-required status instead of a final OEE conclusion.

Risk and review notes:

- Contradictory time records require source reconciliation.
- No production performance conclusion should be issued until the boundary is corrected.
