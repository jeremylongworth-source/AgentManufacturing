---
name: evaluate-machine-vision-application
description: Prepare a machine-vision feasibility brief from supplied inspection and imaging evidence without deploying a production model or releasing product.
license: PENDING_PROJECT_GOVERNANCE
---

# Evaluate Machine Vision Application

**Taxonomy metadata:** family `16` Automation & Advanced Manufacturing; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Assess whether supplied imaging and defect evidence supports a defined inspection application.

## Triggers
- Inspection task, defect examples, imaging conditions, acceptance criteria, and dataset scope are supplied.

## Non-Triggers
- Training or deploying a production model, releasing product, or overriding an inspection decision.

## Required Inputs
- Inspection characteristic, defect classes, representative samples, imaging conditions, decision threshold, and validation basis.

## Optional Inputs
- Lighting, camera, fixtures, annotation rules, false-accept/reject costs, and line integration.

## Assumptions
- A small or clean sample cannot prove production performance or sector conformity.

## Core Workflow
1. Bound the inspection decision and defect population.
2. Check imaging feasibility, sample coverage, labels, and validation design.
3. Return gaps and qualified quality or engineering review needs.

## Calculations
Retain supplied sample counts and error measures; do not invent performance from absent defect examples.

## Validation
- Check representative coverage, labels, conditions, acceptance basis, validation split, and sector context.

## Exception Handling
- Missing defect examples returns `NEEDS_INPUT`.
- A product-release or live-model request returns `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/machine-vision-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, inspection scope, evidence, feasibility gaps, validation needs, and handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not deploy a model, release product, or bypass inspection controls.

## References
- `references/machine-vision-checklist.md`

## Examples
No defect examples means validation coverage is missing, not that the vision concept is ready.

## Testing
Cover correct invocation, missing defect set, sector gap, expected output structure, and production-deployment refusal. Expected routing is not observed behavior.
