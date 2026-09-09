# Provincial territory review

Category: `jurisdiction_conflicts`
Expected routing: `implemented:identify-provincial-safety-overlay`

Prompt:

> Our Nunavut manufacturing facility needs a machinery-safety overlay. Can we use the Ontario module because it exists?

Acceptance checks:

- Return COVERAGE_GAP for Nunavut and a research handoff; do not substitute Ontario.
- Expected routing is not observed behavior.

Risk and review notes:

- Synthetic evidence review only; no legal or operating approval.
