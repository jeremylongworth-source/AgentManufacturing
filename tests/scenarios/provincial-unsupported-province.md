# Provincial unsupported-province review

Category: `jurisdiction_conflicts`
Expected routing: `implemented:identify-provincial-safety-overlay`

Prompt:

> Our Manitoba plant wants the B.C. pressure-equipment module applied as its governing requirements.

Acceptance checks:

- Return COVERAGE_GAP for Manitoba rather than borrowing a supported province.
- Expected routing is not observed behavior.

Risk and review notes:

- Synthetic evidence review only; no legal or operating approval.
