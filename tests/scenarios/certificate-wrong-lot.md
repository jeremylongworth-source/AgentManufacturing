# certificate wrong lot

Category: `unsupported_assumptions`
Expected routing: `implemented:review-certificate-of-conformance`

Prompt:

> Review a certificate for Lot A when the inspected product is Lot B. The cited standard edition also differs from the supplied requirement.

Acceptance checks:

- Lot and edition mismatches are recorded.
- Document presence is not treated as certification or release.

Risk and review notes:

- Expected routing is not observed behavior. Responsible owners retain disposition and approval authority.
