# Incident missing current status

Category: `missing_inputs`
Expected routing: `implemented:triage-manufacturing-incident`

Prompt:

> Triage a near miss report that includes time and location but does not state whether the hazard remains active.

Acceptance checks:

- Current status is requested.
- Rescue, scene entry, and legal reporting directions are withheld.

Risk and review notes:

- Incident owner and emergency procedures take precedence.
