---
name: assess-automation-process-readiness
description: Assess process stability and automation prerequisites from supplied evidence before concept selection or engineering execution.
license: MIT
---

# Assess Automation Process Readiness

**Taxonomy metadata:** family `16` Automation & Advanced Manufacturing; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Identify prerequisite gaps in process stability, standard work, variability, and interfaces before automation screening.

## Triggers
- Process stability evidence, input variation, standard work, interface or control documentation, and sector context are supplied.

## Non-Triggers
- Choosing a technology, approving automation, changing controls, or issuing operating instructions.

## Required Inputs
- Process scope, stability period, variation, standard work, interfaces, controls, and affected quality or safety constraints.

## Optional Inputs
- Cycle-time data, downtime, changeover, training, maintenance, and candidate concept.

## Assumptions
- A readiness finding describes prerequisites; it does not approve a chosen solution.

## Core Workflow
1. Bound the process and evidence period.
2. Check stability, variation, standard work, interfaces, and unresolved constraints.
3. Return prerequisite gaps and review ownership.

## Calculations
Retain supplied variation and stability measures with their population and period; do not infer capability.

## Validation
- Check evidence period, process boundary, variation, standard work, interface documentation, and sector context.

## Exception Handling
- Missing stability evidence returns `NEEDS_INPUT`.
- A request to approve concept selection returns `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/automation-readiness-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, prerequisite matrix, evidence, gaps, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not approve, configure, or operate automation.

## References
- `references/automation-readiness-checklist.md`

## Examples
Input variation outside the documented process scope is a readiness gap, not a reason to approve automation.

## Testing
Cover correct invocation, variable inputs, missing interface basis, expected output structure, and concept-approval refusal. Expected routing is not observed behavior.
