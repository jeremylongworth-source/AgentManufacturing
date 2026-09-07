# Rework rate with repeated rework

Category: `expected_output_structure`
Expected routing: `implemented:calculate-rework-rate`

Prompt:

> Calculate rework rate for 100 units, where 8 units required rework and one of those units was reworked twice. Show the unit-based result, disclose the repeated-event count, and preserve the counting rule.

Acceptance checks:

- Keep eight units as the unit numerator under the stated basis.
- Disclose nine rework events separately if the event definition supports it.
- Do not call the result first-pass yield or authorize disposition.

Risk and review notes:

- Unit and event rates answer different questions.
