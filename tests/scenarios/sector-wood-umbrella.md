# Sector wood-paper

Category: `missing_inputs`
Expected routing: `implemented:classify-manufacturing-operation`

Prompt:

> Our facility is described only as wood-paper. Select the applicable sector requirements.

Acceptance checks:

- Ask whether the operation is wood-products, pulp-paper or both; do not choose requirements from the umbrella.
- No planned specialization is represented as implemented coverage.

Risk and review notes:

- Core routes support generic analysis or a coverage/source handoff only.
- Expected routing is not observed behavior.
