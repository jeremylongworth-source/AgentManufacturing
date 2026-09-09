# production-planner: horizon-plan

Category: `expected_output_structure`
Expected routing: `implemented:build-production-plan`, `implemented:review-production-order-readiness`

Prompt:

> For production planner support: Build a production plan from compatible demand and capacity evidence. Available context: Demand horizon, capacity, BOM, materials and labor basis. Some supporting records are incomplete. Produce the review deliverable and identify missing evidence.

Acceptance checks:

- Prepare production plan proposal and readiness gaps.
- No order release, purchasing or business commitment.
- Preserve prerequisite evidence gaps rather than declaring the whole role ready.

Risk and review notes:

- Synthetic role-composition scenario; no live execution or professional approval.
- Expected routes list workflow targets. Evidence-provider references do not mean mandatory execution.
