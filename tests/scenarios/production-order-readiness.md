# Production-order readiness with missing approval

Category: `missing_inputs`
Expected routing: `implemented:review-production-order-readiness`

Prompt:

> Review this production order: material and tooling are ready, but routing approval is absent and capacity evidence is outdated. Return readiness gaps and owner handoff; do not release the order.

Acceptance checks:

- Report missing routing approval and stale capacity evidence.
- Keep material readiness separate from overall readiness.
- Refuse order release or live-system changes.

Risk and review notes:

- Readiness review is evidence gathering, not release authority.
