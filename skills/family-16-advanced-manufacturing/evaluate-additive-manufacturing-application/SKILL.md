---
name: evaluate-additive-manufacturing-application
description: Prepare an additive-manufacturing process suitability brief from supplied material, machine, and post-processing evidence for engineering and sector review.
license: MIT
---

# Evaluate Additive Manufacturing Application

**Taxonomy metadata:** family `16` Automation & Advanced Manufacturing; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Assess process and material suitability for a defined additive-manufacturing application.

## Triggers
- Part or process requirements, material and machine evidence, post-processing needs, and conformity basis are supplied.

## Non-Triggers
- Designing the part, setting live parameters, certifying material, or releasing production.

## Required Inputs
- Application requirements, material identity, machine/process evidence, build constraints, post-processing, and sector basis.

## Optional Inputs
- Test data, qualification plan, inspection method, orientation, support, and cost assumptions.

## Assumptions
- Material properties from a different process or machine are not interchangeable without evidence.

## Core Workflow
1. Bound application, material, machine, and post-processing basis.
2. Compare supplied evidence to requirements and sector review needs.
3. Return mismatches, qualification gaps, and qualified handoff.

## Calculations
Preserve supplied material, build, and cost units; do not infer qualification or part performance.

## Validation
- Check material identity, machine/process, orientation, post-processing, test basis, standards, and sector.

## Exception Handling
- Material or process mismatch returns `SOURCE_REVIEW_REQUIRED`.
- A request to release or certify a part returns `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/additive-application-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, application scope, evidence comparison, qualification gaps, standards questions, and handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not certify, release, or prescribe live process parameters.

## References
- `references/additive-application-checklist.md`

## Examples
Properties from a different process remain an evidence mismatch rather than proof of additive suitability.

## Testing
Cover correct invocation, material mismatch, standards gap, expected output structure, and release refusal. Expected routing is not observed behavior.
