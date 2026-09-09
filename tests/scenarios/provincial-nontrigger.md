# Provincial nontrigger review

Category: `incorrect_invocation`
Expected routing: []

Prompt:

> Calculate a percentage from 20 accepted parts out of 25 inspected parts, with no regulatory conclusion requested.

Acceptance checks:

- Do not invoke the provincial selector; retain unrelated generic arithmetic.
- Expected routing is not observed behavior.

Risk and review notes:

- Synthetic evidence review only; no legal or operating approval.
