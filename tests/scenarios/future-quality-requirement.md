# Future quality-requirement route

Category: `correct_invocation`
Expected routing: `implemented:review-quality-requirement`

Prompt:

> Review a product quality requirement against the applicable inspection and customer evidence, identify missing acceptance criteria, and route the unresolved requirement to the quality owner.

Acceptance checks:

- Route to the implemented requirement-review package.
- Do not invent a specification, inspection limit, or compliance conclusion.
- Preserve the quality-owner handoff.

Risk and review notes:

- This scenario covers requirement interpretation while measurement-method selection remains a later dependency.
