# bom change mixed revision

Category: `ambiguous_scenario`
Expected routing: `implemented:review-bom-change`

Prompt:

> Compare BOM revisions with a proposed effective date overlapping old stock and open orders. No disposition rule is supplied.

Acceptance checks:

- Mixed-revision stock and order exposure are identified.
- Stock consumption and substitution are not authorized.

Risk and review notes:

- Expected routing is not observed behavior. Responsible owners retain disposition and approval authority.
