# Quality KPI with unequal supplier exposure

Category: `unit_mismatch`
Expected routing: `implemented:analyze-quality-kpis`

Prompt:

> Compare supplier defect totals for the same quarter. Supplier A received 10,000 units and Supplier B received 500; use comparable denominators and flag any missing exposure data before ranking suppliers.

Acceptance checks:

- Preserve receipt exposure and calculate only supported denominators.
- Do not rank supplier performance from raw totals alone.
- Return a metric-owner handoff for missing exposure or definitions.

Risk and review notes:

- Unequal exposure can reverse a raw-count comparison.
