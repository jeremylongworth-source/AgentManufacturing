---
name: review-housekeeping-risk
description: Review workplace obstruction, access, spill, and housekeeping hazard evidence without treating organization scores as safety assurance.
license: MIT
---

# Review Housekeeping Risk

**Taxonomy metadata:** family `11` Manufacturing Safety; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Screen housekeeping observations, exposure, and escalation needs.

## Triggers
- Area, obstruction/spill/storage observation, exposure, and evidence are supplied.

## Non-Triggers
- Directing cleanup in an active hazard, certifying an area, or replacing safety controls with 5S scores.

## Required Inputs
- Area, condition, access/exposure, time, and observation source.

## Optional Inputs
- Photos, traffic, materials, spill type, prior recurrence, and owner.

## Assumptions
- Organization scores are not a substitute for hazard assessment.

## Core Workflow
1. Capture condition and exposed route/persons.
2. Separate immediate escalation from routine evidence gaps.
3. Return owner and review questions.

## Calculations
No calculation; supplied scores retain their declared scale and scope.

## Validation
- Check area, condition, exposure, source, recurrence, and jurisdiction.

## Exception Handling
- Missing area or exposure returns `NEEDS_INPUT`.
- Immediate cleanup instruction returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/housekeeping-risk-checklist.md`.

## Output Contract
Return `status`, area/condition, exposure, evidence, urgency, gaps, and owner handoff.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Do not direct work in an active hazard or claim area safety.

## References
- `references/housekeeping-risk-checklist.md`

## Examples
A blocked egress is escalated; a 5S score cannot clear it.

## Testing
Cover correct invocation, missing exposure, recurrence gap, expected output structure, and unsafe-cleanup refusal. Expected routing is not observed behavior.
