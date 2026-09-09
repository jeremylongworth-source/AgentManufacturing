# maintenance-planner: maintenance-priority

Category: `expected_output_structure`
Expected routing: `implemented:analyze-maintenance-backlog`, `implemented:prioritize-maintenance-work`, `implemented:review-spare-parts-criticality`

Prompt:

> For maintenance planner support: Review backlog and propose maintenance priorities. Available context: Backlog, risk criteria, resource constraints and equipment context. Some supporting records are incomplete. Produce the review deliverable and identify missing evidence.

Acceptance checks:

- Prepare prioritized review list and parts evidence gaps.
- No equipment shutdown/startup or procurement authority.
- Preserve prerequisite evidence gaps rather than declaring the whole role ready.

Risk and review notes:

- Synthetic role-composition scenario; no live execution or professional approval.
- Expected routes list workflow targets. Evidence-provider references do not mean mandatory execution.
