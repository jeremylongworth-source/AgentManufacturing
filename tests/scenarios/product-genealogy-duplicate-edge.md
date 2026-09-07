# Product genealogy duplicate edge

Category: `bad_inputs`
Expected routing: `implemented:build-product-genealogy`

Prompt:

> Build product genealogy from records containing two conflicting output links for one process event.

Acceptance checks:

- Duplicate/conflicting edge is reported.
- Warehouse movement is not directed.

Risk and review notes:

- Source-system reconciliation is required.
