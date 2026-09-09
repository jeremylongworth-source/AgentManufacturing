# plant-manager-support: plant-review

Category: `expected_output_structure`
Expected routing: `implemented:build-manufacturing-kpi-model`, `implemented:review-production-order-readiness`, `implemented:review-operator-qualification-record`

Prompt:

> For plant manager support support: Review plant KPI, readiness and qualification evidence. Available context: KPI model, production readiness, qualification records and unresolved issues. Some supporting records are incomplete. Produce the review deliverable and identify missing evidence.

Acceptance checks:

- Prepare plant review brief with unresolved decisions and owners.
- Do not certify workers or release operations from a summary.
- Preserve prerequisite evidence gaps rather than declaring the whole role ready.

Risk and review notes:

- Synthetic role-composition scenario; no live execution or professional approval.
- Expected routes list workflow targets. Evidence-provider references do not mean mandatory execution.
