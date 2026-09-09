---
name: identify-manufacturing-hazard
description: Recognize potential manufacturing hazards and evidence gaps for qualified safety review without directing controls or work.
license: MIT
---

# Identify Manufacturing Hazard

**Taxonomy metadata:** family `11` Manufacturing Safety; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Create a broad hazard inventory and escalation package.

## Triggers
- Manufacturing activity, equipment, material, environment, or observed unsafe condition is supplied.

## Non-Triggers
- Giving operating, rescue, isolation, guard-bypass, or emergency-response instructions.

## Required Inputs
- Activity/location, hazard observation, exposed persons, time, and evidence source.

## Optional Inputs
- Energy, chemical, ergonomic, fire, environmental, and prior-incident context.

## Assumptions
- Recognition is not a risk assessment or proof of control adequacy.

## Core Workflow
1. Capture hazard observation and exposure context.
2. Classify known, suspected, and unknown conditions.
3. Return escalation owner and evidence needs.

## Calculations
No calculation; supplied severity or likelihood scales retain their definitions.

## Validation
- Check location, activity, exposed persons, source, and jurisdiction context.

## Exception Handling
- Missing exposure context returns `NEEDS_INPUT`.
- Immediate danger request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/hazard-recognition-checklist.md` and AM-07 jurisdiction rules.

## Output Contract
Return `status`, hazard observation, exposure, evidence, unknowns, escalation owner, and boundary note.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Never advise bypassing guards, defeating interlocks, or using unsafe energy-control shortcuts.

## References
- `references/hazard-recognition-checklist.md`

## Examples
An unguarded point of operation is escalated for qualified review; no bypass or workaround is proposed.

## Testing
Cover correct invocation, missing exposure, immediate-danger escalation, expected output structure, and unsafe-shortcut refusal. Expected routing is not observed behavior.
