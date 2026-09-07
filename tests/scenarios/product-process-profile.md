# Profile product and process fit

Category: `expected_output_structure`
Expected routing: `implemented:analyze-product-process-profile`

Prompt:

> Profile three product variants with different mix and volumes against the supplied process descriptions. Show fit signals, missing changeover evidence, assumptions, and the next owner. Do not claim the process has capacity.

Acceptance checks:

- Keep variants and mix separate rather than averaging away differences.
- Identify missing changeover or capability evidence.
- Do not issue a capacity, release, or engineering approval.

Risk and review notes:

- This is a scoping profile, not a capacity or product approval.
