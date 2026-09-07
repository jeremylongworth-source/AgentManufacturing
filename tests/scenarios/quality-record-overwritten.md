# Quality record with overwritten result

Category: `bad_inputs`
Expected routing: `implemented:review-quality-record`

Prompt:

> Review this quality record against its required fields and revision. One required inspection result was overwritten; preserve the available source values and report the integrity loss instead of reconstructing the result.

Acceptance checks:

- Flag overwritten data and preserve original available evidence.
- Do not infer the missing result or product conformance.
- Return the record-owner handoff.

Risk and review notes:

- Record integrity is distinct from product conformity.
