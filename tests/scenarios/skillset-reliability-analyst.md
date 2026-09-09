# reliability-analyst: reliability-metrics

Category: `expected_output_structure`
Expected routing: `implemented:analyze-failure-history`, `implemented:calculate-mtbf`, `implemented:calculate-mttr`, `implemented:analyze-equipment-downtime`

Prompt:

> For reliability analyst support: Review failures and calculate supported reliability metrics. Available context: Failure counts, exposure intervals, repair durations and consistent boundaries. Some supporting records are incomplete. Produce the review deliverable and identify missing evidence.

Acceptance checks:

- Prepare reliability metrics with population and time basis.
- Do not infer future reliability or causal improvement.
- Preserve prerequisite evidence gaps rather than declaring the whole role ready.

Risk and review notes:

- Synthetic role-composition scenario; no live execution or professional approval.
- Expected routes list workflow targets. Evidence-provider references do not mean mandatory execution.
