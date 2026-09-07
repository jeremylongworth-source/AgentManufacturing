# Review operator checklist coverage

Category: `expected_output_structure`
Expected routing: `implemented:review-operator-checklist`

Prompt:

> Review this checklist revision against the approved task requirements and completion records. The checklist has no exception field for an out-of-spec result. Report the coverage and traceability gap without signing operator qualification.

Acceptance checks:

- Map the missing exception path to the approved requirement.
- Distinguish a recorded checkbox from proof of task quality.
- Hand the finding to the document owner without qualification or release approval.

Risk and review notes:

- A checklist review is not a training or product-release decision.
