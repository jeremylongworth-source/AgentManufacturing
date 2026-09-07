# Material variance unbalanced events

Category: `missing_inputs`
Expected routing: `implemented:analyze-material-variance`

Prompt:

> Explain planned versus actual material usage when issue records exist but returns and scrap events are missing.

Acceptance checks:

- Reconciliation gap is reported.
- No variance driver or blame is invented.

Risk and review notes:

- Event owner must complete the balance.
