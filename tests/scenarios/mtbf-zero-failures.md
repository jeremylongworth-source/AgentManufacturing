# MTBF zero failures

Category: `calculation_correctness`
Expected routing: `implemented:calculate-mtbf`

Prompt:

> Calculate MTBF for a repairable asset with operating exposure but zero qualifying failures.

Acceptance checks:

- No finite MTBF is invented.
- Estimation or interval treatment is requested.

Risk and review notes:

- MTBF does not guarantee lifetime.
