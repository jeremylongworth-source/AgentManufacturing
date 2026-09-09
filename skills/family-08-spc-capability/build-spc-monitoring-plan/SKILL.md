---
name: build-spc-monitoring-plan
description: Structure an SPC monitoring plan with characteristics, cadence, chart basis, alarm ownership, and evidence gaps.
license: MIT
---

# Build SPC Monitoring Plan

**Taxonomy metadata:** family `08` SPC & Capability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Prepare a reviewable monitoring plan without issuing operating instructions.

## Triggers
- Characteristics, process context, chart basis, sampling cadence, and candidate owner are supplied.

## Non-Triggers
- Starting monitoring, changing a process, or assigning an owner without authorization.

## Required Inputs
- Characteristic, units, chart basis, cadence, signal response owner, and record location.

## Optional Inputs
- Limits, subgroup design, escalation path, and training evidence.

## Assumptions
- An alarm response without an owner is an ownership gap.

## Core Workflow
1. Map each characteristic to a chart and sampling basis.
2. Check alarm, record, and escalation ownership.
3. Return plan fields and unresolved approvals.

## Calculations
No calculation unless cadence or subgroup arithmetic is supplied with units and basis.

## Validation
- Check characteristic, chart, cadence, owner, reaction boundary, and revision.

## Exception Handling
- Missing owner returns `NEEDS_INPUT`.
- Live operating instruction returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/spc-monitoring-plan-checklist.md`.

## Output Contract
Return `status`, characteristic map, chart basis, cadence, alarm owner, gaps, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not direct live process adjustment.

## References
- `references/spc-monitoring-plan-checklist.md`

## Examples
An alarm response with no named owner is an unresolved plan gap.

## Testing
Cover correct invocation, missing owner, mixed cadence units, expected output structure, and operating-instruction refusal. Expected routing is not observed behavior.
