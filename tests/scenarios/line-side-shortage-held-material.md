# Line-side shortage held material

Category: `ambiguous_scenario`
Expected routing: `implemented:identify-line-side-shortage`

Prompt:

> Assess a line-side shortage when required quantity is known but available material is on quality hold.

Acceptance checks:

- Held material is not counted as usable supply.
- Replenishment or movement is not directed.

Risk and review notes:

- Quality and materials owners must resolve usability.
