# change impact missing owners

Category: `missing_inputs`
Expected routing: `implemented:build-engineering-change-impact-assessment`

Prompt:

> Assess a change that affects production, quality, and maintenance. Only production has supplied an impact review.

Acceptance checks:

- The matrix names missing quality and maintenance reviewers and evidence.
- No impact is assumed absent and implementation is not approved.

Risk and review notes:

- Expected routing is not observed behavior. Responsible owners retain disposition and approval authority.
