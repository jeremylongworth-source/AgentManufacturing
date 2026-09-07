# Flow efficiency zero lead time

Category: `calculation_correctness`
Expected routing: `implemented:analyze-flow-efficiency`

Prompt:

> Calculate flow efficiency when value-adding time is supplied but elapsed lead time is zero.

Acceptance checks:

- Division by zero is refused.
- Time-basis definitions are requested.

Risk and review notes:

- Flow analysis is not takt analysis.
