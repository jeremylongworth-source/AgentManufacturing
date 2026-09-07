# Lead-time estimate with overlap

Category: `calculation_correctness`
Expected routing: `implemented:calculate-production-lead-time`

Prompt:

> Estimate lead time from queue 2 hours, setup 1 hour, run 4 hours, and transfer 1 hour. Setup overlaps the last hour of queue; show the overlap convention and prevent double counting. Keep measured and assumed components separate.

Acceptance checks:

- Preserve all components and the explicit one-hour overlap.
- Show the arithmetic and units before rounding.
- Do not turn the estimate into a customer promise.

Risk and review notes:

- Overlap assumptions materially change the estimate and require owner review.
