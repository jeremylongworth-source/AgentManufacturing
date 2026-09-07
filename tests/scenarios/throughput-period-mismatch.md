# Throughput with mismatched periods

Category: `unit_mismatch`
Expected routing: `implemented:calculate-throughput`

Prompt:

> Calculate throughput from 480 completed units for yesterday and an elapsed-time denominator covering last week. Request matching periods rather than returning a misleading rate.

Acceptance checks:

- Identify the quantity/time period mismatch.
- Preserve both source periods and do not silently substitute one.
- Return a missing-input or review status.

Risk and review notes:

- A rate with mismatched periods is not decision-ready.
