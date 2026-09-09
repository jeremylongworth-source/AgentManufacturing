---
name: evaluate-cobot-application
description: Assess collaborative robot application concerns from supplied human-robot exposure evidence without assuming inherent safety.
license: MIT
---

# Evaluate Cobot Application

**Taxonomy metadata:** family `16` Automation & Advanced Manufacturing; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure human-robot interaction concerns for a proposed collaborative application.

## Triggers
- Human/robot task, exposure context, application evidence, and review criteria are supplied.

## Non-Triggers
- Declaring a cobot inherently safe, removing guarding, changing modes, or authorizing shared operation.

## Required Inputs
- People, task, contact or proximity exposure, speeds/forces, modes, space, and jurisdiction or standards basis.

## Optional Inputs
- Risk assessment, vendor limits, protective measures, training, and observed interaction notes.

## Assumptions
- The term collaborative describes a product or application concept, not a completed safety assessment.

## Core Workflow
1. Bound human tasks, exposure, and operating modes.
2. Compare supplied evidence with application concerns and missing controls.
3. Return qualified engineering, safety, standards, and jurisdiction handoffs.

## Calculations
Retain supplied exposure values and units; do not derive an acceptable limit without the applicable basis.

## Validation
- Check task, exposure, mode, speed/force, protective measures, standards, and province.

## Exception Handling
- Missing exposure evidence returns `NEEDS_INPUT`.
- A request to enable shared operation returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/cobot-application-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, interaction scope, evidence, concern register, missing controls, and handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Never authorize collaborative operation or bypass protective measures.

## References
- `references/cobot-application-checklist.md`

## Examples
A cobot label with no exposure evidence remains an unresolved safety concern.

## Testing
Cover correct invocation, missing exposure, jurisdiction gap, expected output structure, and shared-operation refusal. Expected routing is not observed behavior.
