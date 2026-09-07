# Process stream without measurement basis

Category: `bad_inputs`
Expected routing: `implemented:identify-process-inputs-outputs`

Prompt:

> Inventory material, energy, and information streams for the supplied process boundary. An energy stream is named but has no meter, unit, or measurement period; list it as unquantified rather than assigning a balance.

Acceptance checks:

- Keep the energy stream visible and unquantified.
- Separate observed, supplied, inferred, and unverified streams.
- Do not claim mass/energy conservation or environmental compliance.

Risk and review notes:

- A missing measurement basis is an evidence gap, not zero consumption.
