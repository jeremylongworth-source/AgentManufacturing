# Conflicting customer quality revisions

Category: `unsupported_assumptions`
Expected routing: `implemented:review-quality-requirement`

Prompt:

> Review two customer requirement revisions that specify different acceptance criteria for the same characteristic. Identify the conflict, applicability evidence, and resolution owner without selecting the easier criterion.

Acceptance checks:

- Preserve both revisions and their effective dates.
- Do not choose a criterion or claim conformance.
- Return a qualified requirement-resolution handoff.

Risk and review notes:

- Requirement interpretation must precede inspection or release decisions.
