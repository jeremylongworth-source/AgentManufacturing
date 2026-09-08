# energy office boundary mismatch

Category: `ambiguous_scenario`
Expected routing: `implemented:analyze-energy-consumption`

Prompt:

> Compare two production periods: the first meter includes office load and the second covers only the line. Output units match but no allocation reconciliation is supplied.

Acceptance checks:

- Preserve the independent readings and explain allocation noncomparability.
- Do not report an efficiency gain from the boundary change.

Risk and review notes:

- Expected routing is not observed behavior. Evidence gaps and responsible review remain visible.
