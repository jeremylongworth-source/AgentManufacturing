# Scrap record missing approval

Category: `expected_output_structure`
Expected routing: `implemented:review-scrap-material-record`

Prompt:

> Review a scrap event with material identity, quantity, and reason but no approval or disposition status.

Acceptance checks:

- Approval/status gap is exposed.
- Disposal and disposition are withheld.

Risk and review notes:

- Authorized owner review remains required.
