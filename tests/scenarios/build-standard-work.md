# Build standard work from observations

Category: `unit_mismatch`
Expected routing: `implemented:build-standard-work`

Prompt:

> Draft standard work from observed task times in seconds, the approved sequence, and a WIP limit. The supplied takt value is in units per hour but its product definition is missing; preserve the gap and do not convert it silently.

Acceptance checks:

- Preserve the observed time units and identify the missing takt definition.
- Keep the WIP limit and approved sequence visible.
- Do not invent a conversion or publish the draft as standard work.

Risk and review notes:

- Time and demand definitions must be reconciled by the responsible owner.
