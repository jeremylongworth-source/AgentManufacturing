---
name: build-manufacturing-skills-matrix
description: Organize task, revision, skill, and evidence relationships without deciding qualification or assignment.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Manufacturing Skills Matrix

**Taxonomy metadata:** family `13` Workforce & Shift Operations; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Map tasks and evidence to stated skills, revisions, and gaps.

## Triggers
- Task requirements, role/worker identifiers, skill evidence, and revision context are supplied.

## Non-Triggers
- Certifying qualification, assigning work, or changing training records.

## Required Inputs
- Task, required skill, revision, person/role, evidence, and review date.

## Optional Inputs
- Expiry, supervisor review, language, accommodation, and cross-training context.

## Assumptions
- A matrix gap is not proof that a person is unqualified.

## Core Workflow
1. Normalize task and skill definitions.
2. Map supplied evidence and identify gaps or conflicts.
3. Return owner review questions.

## Calculations
No calculation; counts retain population and evidence scope.

## Validation
- Check task revision, skill evidence, dates, identity, and source.

## Exception Handling
- Missing requirement or evidence returns `NEEDS_INPUT`.
- Assignment or qualification request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/skills-matrix-checklist.md`.

## Output Contract
Return `status`, task/skill map, evidence, gaps, assumptions, and owner handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not certify qualification or assign personnel.

## References
- `references/skills-matrix-checklist.md`

## Examples
An expired training record is an evidence gap, not an automatic qualification conclusion.

## Testing
Cover correct invocation, missing revision, conflicting evidence, expected output structure, and assignment refusal. Expected routing is not observed behavior.
