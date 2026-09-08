# supplier defect count basis

Category: `calculation_correctness`
Expected routing: `implemented:analyze-supplier-defect`

Prompt:

> Analyze 5 unique defective units among 200 inspected units for one linked supplier, lot, part, and period. Seven defect occurrences were logged on those five units. Use the inspected-unit basis.

Acceptance checks:

- The defective-unit rate is 2.5 percent with 5 and 200 shown; seven occurrences are separate.
- Lot linkage supports grouping but does not prove supplier causation.

Risk and review notes:

- Expected routing is not observed behavior. Responsible owners retain disposition and approval authority.
