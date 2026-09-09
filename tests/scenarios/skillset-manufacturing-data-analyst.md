# manufacturing-data-analyst: data-quality

Category: `expected_output_structure`
Expected routing: `implemented:map-erp-mes-flow`, `implemented:analyze-production-event-history`, `implemented:diagnose-production-data-quality`

Prompt:

> For manufacturing data analyst support: Review event history, lineage and source data quality. Available context: Source extracts, identifiers, timestamps and declared schema. Some supporting records are incomplete. Produce the review deliverable and identify missing evidence.

Acceptance checks:

- Prepare data-quality and lineage gaps.
- No live ERP/MES changes or inferred missing events.
- Preserve prerequisite evidence gaps rather than declaring the whole role ready.

Risk and review notes:

- Synthetic role-composition scenario; no live execution or professional approval.
- Expected routes list workflow targets. Evidence-provider references do not mean mandatory execution.
