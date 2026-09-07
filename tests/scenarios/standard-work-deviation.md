# Analyze standard-work deviation

Category: `ambiguous_scenario`
Expected routing: `implemented:analyze-standard-work-deviation`

Prompt:

> Compare the supplied execution record with the applicable standard revision. One task took longer, but the record does not say whether the instruction, material, equipment, or context caused it. Separate possible instruction and execution gaps without assigning blame.

Acceptance checks:

- Preserve the causal uncertainty and observation boundary.
- Compare expected and observed elements using the stated revision.
- Return a review owner without discipline or corrective-action approval.

Risk and review notes:

- One observation does not establish systemic operator behavior or root cause.
