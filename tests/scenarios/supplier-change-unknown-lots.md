# supplier change unknown lots

Category: `missing_inputs`
Expected routing: `implemented:review-supplier-change-impact`

Prompt:

> Review a supplier notice changing material processing. It contains no affected-lot list or evidence of validation coverage.

Acceptance checks:

- Lot exposure and validation gaps remain unresolved.
- No change acceptance or implementation decision is made.

Risk and review notes:

- Expected routing is not observed behavior. Responsible owners retain disposition and approval authority.
