# change package missing signatures

Category: `missing_inputs`
Expected routing: `implemented:review-change-package`

Prompt:

> Review a change package with a scheduled implementation date and required signatures left blank.

Acceptance checks:

- Approval gaps are tied to required signatories.
- An implementation date does not imply approval.

Risk and review notes:

- Expected routing is not observed behavior. Responsible owners retain disposition and approval authority.
