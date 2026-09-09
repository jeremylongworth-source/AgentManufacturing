---
name: review-machine-guarding-risk
description: Assess machine-guarding concern evidence and qualified review needs without validating a guard or directing operation.
license: MIT
---

# Review Machine Guarding Risk

**Taxonomy metadata:** family `11` Manufacturing Safety; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Screen guarding observations, access, motion, and evidence for qualified review.

## Triggers
- Machine identity, point of access, guard/interlock observations, and applicable context are supplied.

## Non-Triggers
- Certifying guarding, changing interlocks, bypassing protection, or authorizing operation.

## Required Inputs
- Machine, hazard point, access path, guard state, observed behavior, and jurisdiction.

## Optional Inputs
- Drawings, risk assessment, safeguarding standard, maintenance history, and photos.

## Assumptions
- A visual observation does not establish compliance or safe operation.

## Core Workflow
1. Describe hazard point and access condition.
2. Compare supplied evidence with review criteria.
3. Return gaps and qualified engineering/safety handoff.

## Calculations
No calculation unless a declared clearance or distance basis is supplied; preserve units.

## Validation
- Check machine identity, access, guard state, interlock evidence, and standard context.

## Exception Handling
- Missing machine or hazard point returns `NEEDS_INPUT`.
- Operation or bypass request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/machine-guarding-review-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, machine/hazard map, evidence, gaps, applicable context, and qualified handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Never suggest bypassing guards or defeating interlocks.

## References
- `references/machine-guarding-review-checklist.md`

## Examples
A missing interlock test record remains unresolved; operation is not authorized.

## Testing
Cover correct invocation, missing access evidence, standards gap, expected output structure, and bypass refusal. Expected routing is not observed behavior.
