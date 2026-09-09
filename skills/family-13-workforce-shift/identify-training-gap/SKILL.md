---
name: identify-training-gap
description: Compare task and revision requirements with supplied learning evidence without certifying qualification.
license: MIT
---

# Identify Training Gap

**Taxonomy metadata:** family `13` Workforce & Shift Operations; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Map required task knowledge or skill to learning evidence and unresolved gaps.

## Triggers
- Task/revision requirement, worker/role, training evidence, and review date are supplied.

## Non-Triggers
- Certifying qualification, assigning work, or prescribing a training course.

## Required Inputs
- Task, revision, required skill, person/role, evidence, and date.

## Optional Inputs
- Assessment result, language, accommodation, refresher interval, and supervisor review.

## Assumptions
- A training gap is not itself a qualification verdict.

## Core Workflow
1. Compare requirement revision to learning evidence.
2. Identify missing, stale, or conflicting evidence.
3. Return owner review and documentation questions.

## Calculations
No calculation; evidence counts retain scope and date.

## Validation
- Check task revision, evidence identity, dates, and requirement source.

## Exception Handling
- Missing requirement or evidence returns `NEEDS_INPUT`.
- Qualification or assignment request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/training-gap-checklist.md`.

## Output Contract
Return `status`, requirement, evidence, gap types, assumptions, and owner handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not certify qualification or assign work.

## References
- `references/training-gap-checklist.md`

## Examples
A new work-instruction revision with old training evidence is a review gap.

## Testing
Cover correct invocation, stale revision, missing evidence, expected output structure, and qualification refusal. Expected routing is not observed behavior.
