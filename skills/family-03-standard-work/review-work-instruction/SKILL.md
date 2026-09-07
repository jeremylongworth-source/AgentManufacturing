---
name: review-work-instruction
description: Review an existing work instruction for ambiguous, missing, conflicting, or uncontrolled steps against authorized process and acceptance evidence.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Work Instruction

## Overview

Produce a defect list tied to the supplied instruction version, authorized process, acceptance criteria, and operator feedback. Focus on clarity and control gaps; do not rewrite or release the instruction without an owner decision.

**Taxonomy metadata:** family `03` Standard Work & Work Instructions; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `REVIEW`. Audit distinction: review one instruction; drafting, deviation analysis, and release remain separate.

## Triggers

- The user supplies an instruction revision, authorized process and criteria, and operator feedback and asks for a review.

## Non-Triggers

- Effective document release, training qualification, machine operation, or inventing missing process steps.

## Required Inputs

- Instruction version and revision/effective context.
- Authorized process and acceptance criteria.
- Operator feedback or observed execution evidence.

## Optional Inputs

- Photos, defect records, change history, reviewer comments, and controlled-document metadata.

## Assumptions

- An ambiguous step is a defect or evidence gap, not an invitation to guess.
- Operator feedback is preserved as evidence and not treated as authorization.

## Core Workflow

1. Compare each instruction section with authorized process and criteria.
2. Classify gaps as missing, ambiguous, conflicting, stale, or unsupported; tie each to evidence.
3. Return prioritized review findings and an owner handoff.

## Calculations

No calculation required.

## Validation

- Confirm version, scope, source, and acceptance criteria alignment.
- Check that findings are reproducible and that safety or engineering concerns are escalated.

## Exception Handling

- Missing controlled version returns `NEEDS_INPUT`.
- Conflicting process evidence returns `SOURCE_REVIEW_REQUIRED` or `ENGINEERING_REVIEW_REQUIRED`.
- Requests to silently repair or release the instruction return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/work-instruction-review-checklist.md` and supplied controlled records.
- Record source, revision, effective date, and reviewer; do not reproduce protected manuals.

## Output Contract

Return `status`, reviewed version, evidence set, defect list, severity/rationale, unknowns, recommended owner, assumptions, validation notes, and release boundary. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE` with escalation for hazardous or engineering content. Do not approve operation, training, permit, or release.

## References

- `references/work-instruction-review-checklist.md`

## Examples

Read the checklist for a revision with an ambiguous inspection step.

## Testing

Cover correct invocation, missing revision, ambiguous step, conflicting source, safety escalation, expected output structure, and release refusal. Expected routing is not observed behavior.
