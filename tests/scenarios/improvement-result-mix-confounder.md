# Improvement result mix confounder

Category: `ambiguous_scenario`
Expected routing: `implemented:measure-improvement-result`

Prompt:

> Measure a before/after cycle-time improvement when the post-period has a different product mix and a concurrent staffing change.

Acceptance checks:

- Confounders remain visible.
- Causation and rollout are not claimed.

Risk and review notes:

- Measurement owner must define a comparable population.
