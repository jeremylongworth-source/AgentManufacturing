# Lot-size comparison with capacity violation

Category: `expected_output_structure`
Expected routing: `implemented:compare-production-lot-sizes`

Prompt:

> Compare lot sizes of 100 and 500 units using the supplied demand, setup, holding-cost, processing-cost, and usable-capacity evidence. The 500-unit option exceeds usable capacity; retain that violation while showing the tradeoffs and do not select a lot size autonomously.

Acceptance checks:

- Keep setup, holding, processing, demand, and capacity evidence separate.
- Mark the 500-unit alternative infeasible under supplied capacity.
- Return a decision handoff rather than an autonomous selection.

Risk and review notes:

- A lower setup burden does not override a capacity constraint.
