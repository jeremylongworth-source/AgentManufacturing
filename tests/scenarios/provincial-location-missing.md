# Provincial location-missing review

Category: `missing_inputs`
Expected routing: `implemented:identify-provincial-safety-overlay`

Prompt:

> Identify provincial training authority for our Canadian plant; the facility location and workplace regime have not been supplied.

Acceptance checks:

- Return PENDING_CONTEXT and request location, regime and task evidence; no default province.
- Expected routing is not observed behavior.

Risk and review notes:

- Synthetic evidence review only; no legal or operating approval.
