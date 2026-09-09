# production-supervisor: shift-plan

Category: `expected_output_structure`
Expected routing: `implemented:review-production-order-readiness`, `implemented:build-shift-production-plan`, `implemented:balance-workforce`

Prompt:

> For production supervisor support: Allocate a supplied approved horizon to a shift. Available context: Approved plan, readiness, staffing qualifications and shift window. Some supporting records are incomplete. Produce the review deliverable and identify missing evidence.

Acceptance checks:

- Prepare shift allocation proposal with unmet constraints.
- Do not approve overtime or unqualified assignments.
- Preserve prerequisite evidence gaps rather than declaring the whole role ready.

Risk and review notes:

- Synthetic role-composition scenario; no live execution or professional approval.
- Expected routes list workflow targets. Evidence-provider references do not mean mandatory execution.
