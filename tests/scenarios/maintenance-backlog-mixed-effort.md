# Maintenance backlog mixed effort

Category: `unit_mismatch`
Expected routing: `implemented:analyze-maintenance-backlog`

Prompt:

> Analyze backlog effort where some estimates are labor hours and others are calendar days without a conversion basis.

Acceptance checks:

- Mixed effort units are not combined.
- Dispatch and priority decisions remain out of scope.

Risk and review notes:

- Capacity period must be declared.
