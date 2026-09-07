# Review a work-instruction revision

Category: `unsupported_assumptions`
Expected routing: `implemented:review-work-instruction`

Prompt:

> Review revision 3 of the supplied work instruction against the authorized process, acceptance criteria, and operator feedback. The inspection step is ambiguous and the effective date is missing. List the defects and handoff; do not silently repair or release it.

Acceptance checks:

- Identify the ambiguous step and missing control metadata.
- Preserve evidence and route the issue to the document owner.
- Refuse to release or silently rewrite the controlled document.

Risk and review notes:

- The review must distinguish a document defect from an execution problem.
