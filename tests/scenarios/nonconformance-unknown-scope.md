# Nonconformance with unknown scope

Category: `expected_output_structure`
Expected routing: `implemented:triage-nonconformance`

Prompt:

> A scratch was found on one inspected housing from an otherwise unidentified lot. Triage the nonconformance, retain the unknown affected quantity, assign a provisional priority from the evidence, and identify the next quality owner. Do not invent the lot scope or final disposition.

Acceptance checks:

- Keep affected quantity and lot scope unknown unless supplied evidence resolves them.
- Separate the observed scratch from any unproven cause or disposition.
- Identify a quality review owner and any containment or escalation evidence still needed.

Risk and review notes:

- An inspected sample is not the affected lot.
- The output is a triage handoff, not a hold/release command or corrective-action conclusion.
