# Register production constraints

Category: `missing_inputs`
Expected routing: `implemented:analyze-production-constraints`

Prompt:

> Build a constraint register for a weekly output objective using supplied labor, equipment, material, policy, and demand notes. The observation period is missing; identify what must be supplied before ranking a bottleneck.

Acceptance checks:

- Request the observation period and preserve the supplied notes.
- Separate hard constraints from hypotheses.
- Do not declare a bottleneck or invent a rate.

Risk and review notes:

- Without a common period, constraint evidence cannot be compared.
