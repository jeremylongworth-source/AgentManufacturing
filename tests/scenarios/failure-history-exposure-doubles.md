# Failure history exposure doubles

Category: `ambiguous_scenario`
Expected routing: `implemented:analyze-failure-history`

Prompt:

> Analyze failure counts that rise while operating exposure doubles over the same comparison period.

Acceptance checks:

- Exposure context is retained.
- Worsened reliability is not declared from counts alone.

Risk and review notes:

- Mode and denominator definitions need review.
