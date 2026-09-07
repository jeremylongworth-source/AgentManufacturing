# Job safety analysis missing controls

Category: `missing_inputs`
Expected routing: `implemented:build-job-safety-analysis`

Prompt:

> Build a job safety analysis from task steps and hazards when existing control evidence is missing.

Acceptance checks:

- Missing controls are reported.
- No executable procedure or shortcut is created.

Risk and review notes:

- Qualified safety review is required.
