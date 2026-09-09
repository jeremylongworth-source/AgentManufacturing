# quality-engineer-support: corrective-action

Category: `expected_output_structure`
Expected routing: `implemented:triage-nonconformance`, `implemented:perform-root-cause-analysis`, `implemented:build-corrective-action`, `implemented:verify-corrective-action-effectiveness`

Prompt:

> For quality engineer support support: Build a corrective-action draft from investigation evidence. Available context: Nonconformance, containment, causal evidence and verification plan. Some supporting records are incomplete. Produce the review deliverable and identify missing evidence.

Acceptance checks:

- Prepare causal evidence and action/effectiveness review.
- Do not convert a proposed cause into a verified one.
- Preserve prerequisite evidence gaps rather than declaring the whole role ready.

Risk and review notes:

- Synthetic role-composition scenario; no live execution or professional approval.
- Expected routes list workflow targets. Evidence-provider references do not mean mandatory execution.
