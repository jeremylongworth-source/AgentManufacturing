---
name: review-ppe-requirement
description: Review the evidence and context behind PPE requirements without selecting equipment or declaring protection adequacy.
license: PENDING_PROJECT_GOVERNANCE
---

# Review PPE Requirement

**Taxonomy metadata:** family `11` Manufacturing Safety; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Map task hazards, exposure, and supplied PPE criteria to review gaps.

## Triggers
- Task hazard, exposure pathway, PPE basis, and applicable context are supplied.

## Non-Triggers
- Selecting, fitting, certifying, or authorizing PPE use.

## Required Inputs
- Task, hazard, exposure, PPE requirement, criteria, and jurisdiction.

## Optional Inputs
- Fit testing, compatibility, inspection, training, and environmental conditions.

## Assumptions
- A PPE list does not prove suitability, fit, or adequacy.

## Core Workflow
1. Link hazard and exposure to the supplied requirement.
2. Check criteria, compatibility, fit, training, and evidence gaps.
3. Return qualified safety review questions.

## Calculations
Preserve supplied exposure values and units; do not derive safe thresholds.

## Validation
- Check hazard, pathway, criteria, compatibility, fit evidence, and jurisdiction.

## Exception Handling
- Missing hazard or requirement returns `NEEDS_INPUT`.
- Immediate-use request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/ppe-review-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, hazard/exposure, PPE basis, evidence, gaps, assumptions, and safety-owner handoff.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Do not select PPE for immediate use or claim protection adequacy.

## References
- `references/ppe-review-checklist.md`

## Examples
A glove material list without compatibility evidence remains unresolved.

## Testing
Cover correct invocation, missing exposure, compatibility gap, expected output structure, and immediate-use refusal. Expected routing is not observed behavior.
