---
name: build-job-safety-analysis
description: Organize task hazards, existing controls, and review questions without generating equipment-specific operating procedures.
license: MIT
---

# Build Job Safety Analysis

**Taxonomy metadata:** family `11` Manufacturing Safety; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure task steps, hazards, existing controls, and unresolved review items.

## Triggers
- A task, work area, hazards, and existing control evidence are supplied.

## Non-Triggers
- Writing executable operating, isolation, rescue, or emergency procedures.

## Required Inputs
- Task boundary, steps, hazards, exposed roles, existing controls, and reviewer.

## Optional Inputs
- Tools, materials, permits, environmental conditions, and incident history.

## Assumptions
- Listed controls are evidence claims pending qualified validation.

## Core Workflow
1. Bound the task and sequence as supplied.
2. Map hazards and existing controls per step.
3. Return gaps, escalation questions, and review owner.

## Calculations
Use only declared risk-ranking scales; do not invent severity or likelihood values.

## Validation
- Check task steps, exposure, control evidence, jurisdiction, and revision.

## Exception Handling
- Missing task or controls returns `NEEDS_INPUT`.
- Work instruction or shortcut request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/job-safety-analysis-checklist.md`.

## Output Contract
Return `status`, task map, hazards, controls, gaps, assumptions, and qualified handoff.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Do not create guard bypass, interlock defeat, or unsafe energy-control steps.

## References
- `references/job-safety-analysis-checklist.md`

## Examples
An absent control is a review gap, not an invitation to improvise a workaround.

## Testing
Cover correct invocation, missing control evidence, jurisdiction gap, expected output structure, and unsafe-procedure refusal. Expected routing is not observed behavior.
