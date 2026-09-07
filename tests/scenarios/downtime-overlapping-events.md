# Downtime overlapping events

Category: `calculation_correctness`
Expected routing: `implemented:analyze-equipment-downtime`

Prompt:

> Total equipment downtime where planned and unplanned event records overlap in time.

Acceptance checks:

- Overlap rule is required before summing.
- Failure cause is not inferred from downtime totals.

Risk and review notes:

- Event definitions remain explicit.
