---
name: evaluate-robotics-application
description: Prepare a robotics concept suitability brief from supplied task, payload, environment, and integration evidence without approving deployment.
license: PENDING_PROJECT_GOVERNANCE
---

# Evaluate Robotics Application

**Taxonomy metadata:** family `16` Automation & Advanced Manufacturing; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compare supplied robot-task and integration evidence to an application brief for qualified engineering review.

## Triggers
- Task, payload or reach needs, environment, integration constraints, vendor evidence, and jurisdiction are supplied.

## Non-Triggers
- Robot selection, cell design, safety validation, commissioning, or programming.

## Required Inputs
- Task sequence, payload, reach, speed, environment, interfaces, vendor evidence, and applicable review context.

## Optional Inputs
- Cycle-time target, guarding concept, utilities, maintenance, and quality requirements.

## Assumptions
- Vendor ratings and a robot label do not establish application suitability or safety.

## Core Workflow
1. Bound task, environment, and integration evidence.
2. Compare requirements with supplied robot capability evidence.
3. Return feasibility gaps and qualified engineering or jurisdiction handoff.

## Calculations
Preserve supplied payload, reach, speed, and cycle assumptions; do not infer a safe envelope.

## Validation
- Check task coverage, payload/reach basis, environment, interfaces, standards, and province or sector.

## Exception Handling
- Missing vendor or application evidence returns `NEEDS_INPUT`.
- A commissioning, guard, or program request returns `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/robotics-application-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, application brief, evidence comparison, gaps, jurisdiction questions, and handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not certify, commission, program, or provide bypass steps.

## References
- `references/robotics-application-checklist.md`

## Examples
Incomplete reach and payload evidence produces a suitability gap rather than robot approval.

## Testing
Cover correct invocation, missing vendor evidence, jurisdiction gap, expected output structure, and commissioning refusal. Expected routing is not observed behavior.
