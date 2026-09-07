# Effectiveness without post-action window

Category: `calculation_correctness`
Expected routing: `implemented:verify-corrective-action-effectiveness`

Prompt:

> Verify corrective-action effectiveness from an implementation date alone with no post-action observation window or population.

Acceptance checks:

- Completion is not treated as effectiveness evidence.
- A defined window and population are requested.

Risk and review notes:

- CAPA closure remains owner-controlled.
