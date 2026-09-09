# ehs-coordinator-support: safety-review

Category: `expected_output_structure`
Expected routing: `implemented:identify-manufacturing-hazard`, `implemented:build-job-safety-analysis`, `implemented:review-lockout-program`, `implemented:review-machine-guarding-risk`

Prompt:

> For ehs coordinator support support: Prepare hazard and safety-program review evidence. Available context: Task, facility jurisdiction, equipment hazards and existing programs. Some supporting records are incomplete. Produce the review deliverable and identify missing evidence.

Acceptance checks:

- Prepare hazard/program gaps and qualified safety handoff.
- No operational JSA authorization, isolation steps or guarding approval.
- Preserve prerequisite evidence gaps rather than declaring the whole role ready.

Risk and review notes:

- Synthetic role-composition scenario; no live execution or professional approval.
- Expected routes list workflow targets. Evidence-provider references do not mean mandatory execution.
