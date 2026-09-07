# Root cause correlation only

Category: `ambiguous_scenario`
Expected routing: `implemented:perform-root-cause-analysis`

Prompt:

> Evaluate a candidate cause that changed near the failure but has no confirming or disconfirming evidence.

Acceptance checks:

- Correlation is not declared root cause.
- Alternative hypotheses and evidence requests remain visible.

Risk and review notes:

- Corrective action is not selected.
