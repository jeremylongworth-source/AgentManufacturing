# First-pass yield excludes later rework

Category: `calculation_correctness`
Expected routing: `implemented:calculate-first-pass-yield`

Prompt:

> Calculate first-pass yield for 100 initial units, 92 accepted without rework, and 6 units that passed only after rework. Keep the later passes out of the first-pass numerator and show the population basis.

Acceptance checks:

- Use 92 as the no-rework numerator.
- Keep the six reworked units visible but excluded from first-pass yield.
- Do not make a release or quality certification decision.

Risk and review notes:

- First-pass yield and final accepted quantity are different measures.
