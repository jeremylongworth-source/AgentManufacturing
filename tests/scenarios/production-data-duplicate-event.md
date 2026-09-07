# Production data duplicate event

Category: `missing_inputs`
Expected routing: `implemented:diagnose-production-data-quality`

Prompt:

> Diagnose a production dataset with repeated event IDs and no reliable source-system rule for which row is authoritative.

Acceptance checks:

- Duplicate scope and affected records are listed.
- No record is deleted or silently selected.

Risk and review notes:

- Source-owner review is required before remediation.
