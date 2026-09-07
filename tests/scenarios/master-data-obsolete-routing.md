# Master data obsolete routing

Category: `unsupported_assumptions`
Expected routing: `implemented:review-production-master-data`

Prompt:

> Review an item export where an obsolete routing remains referenced. The proposed replacement has no approved revision or effective date.

Acceptance checks:

- The stale reference and missing revision basis are reported.
- No replacement routing is activated.

Risk and review notes:

- Master-data correction requires an approved change owner.
