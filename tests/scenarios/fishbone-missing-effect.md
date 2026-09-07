# Fishbone missing effect

Category: `missing_inputs`
Expected routing: `implemented:build-fishbone-analysis`

Prompt:

> Build a fishbone analysis from category labels but without a bounded problem or effect statement.

Acceptance checks:

- Missing effect is reported.
- Candidate categories are not treated as causes.

Risk and review notes:

- Investigation scope remains unresolved.
