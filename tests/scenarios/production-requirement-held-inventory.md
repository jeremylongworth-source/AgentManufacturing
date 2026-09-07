# Production requirement with held finished quantity

Category: `calculation_correctness`
Expected routing: `implemented:calculate-production-requirement`

Prompt:

> Calculate net production need for 1,000 units of demand with 300 finished units on hold, 100 usable finished units, and 200 committed receipts. Exclude held quantity unless the supplied inventory policy authorizes it, show the formula, and do not release an order.

Acceptance checks:

- Exclude held quantity from usable inventory unless policy evidence says otherwise.
- Preserve demand, usable quantity, receipts, policy, and net-need intermediates.
- Do not write inventory or release production.

Risk and review notes:

- Hold disposition is an authority-dependent input, not an arithmetic default.
