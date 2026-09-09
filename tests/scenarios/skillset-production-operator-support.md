# production-operator-support: work-review

Category: `expected_output_structure`
Expected routing: `implemented:review-document-revision`, `implemented:review-work-instruction`, `implemented:review-operator-checklist`

Prompt:

> For production operator support support: Review the supplied operator instruction and checklist. Available context: Current document revision, task and checklist. Some supporting records are incomplete. Produce the review deliverable and identify missing evidence.

Acceptance checks:

- Prepare document/checklist evidence gaps.
- Do not modify an approved instruction or authorize machine operation.
- Preserve prerequisite evidence gaps rather than declaring the whole role ready.

Risk and review notes:

- Synthetic role-composition scenario; no live execution or professional approval.
- Expected routes list workflow targets. Evidence-provider references do not mean mandatory execution.
