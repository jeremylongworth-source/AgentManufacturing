# Process alternative missing validation evidence

Category: `jurisdiction_conflicts`
Expected routing: `implemented:compare-process-alternatives`

Prompt:

> Compare two process concepts against the supplied product requirements, capacity, and resource evidence. Concept B has no quality-validation evidence and the sector context is not yet confirmed; report those gaps instead of concluding equivalence.

Acceptance checks:

- Preserve the missing validation evidence and pending sector context.
- Do not select, certify, or implement either concept.
- Return an engineering-review handoff.

Risk and review notes:

- Sector requirements may change the comparison criteria.
