# origin cost near threshold

Category: `calculation_correctness`

Expected routing: `implemented:assess-product-of-canada-claim`

Prompt:

> For a non-food Product of Canada evidence review, the supplied complete reconciled ledger uses the same product, period and CAD basis: Canadian qualifying direct costs 9799 and total direct costs 10000. Show the unrounded ratio alongside the supplied 98 percent guidance indicator; transformation evidence is still missing.

Acceptance checks:

- Show 97.99 percent, without rounding it up to 98 percent.
- Retain missing transformation substantiation and withhold approval regardless of the arithmetic.

Risk and review notes:

- Synthetic review scenario. No legal, workplace, product or publication approval is established.
- Expected routing is not observed behavior; runtime evaluation remains unrun.
