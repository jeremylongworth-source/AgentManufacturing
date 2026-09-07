---
name: draft-work-instruction
description: Draft a controlled work-instruction structure from an authorized process description, task sequence, acceptance criteria, audience, and template.
license: PENDING_PROJECT_GOVERNANCE
---

# Draft Work Instruction

## Overview

Create a reviewable work-instruction draft from supplied authorized process evidence. Expose unresolved steps, acceptance criteria, roles, and document controls without inventing a procedure or making the draft effective.

**Taxonomy metadata:** family `03` Standard Work & Work Instructions; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `REVIEW`. Audit distinction: draft one controlled instruction; review and standard-work analysis remain separate.

## Triggers

- The user supplies an authorized process description, task sequence, acceptance criteria, audience, and document template and asks for a draft.

## Non-Triggers

- Machine-specific hazardous-energy instructions, unapproved process creation, document release, certification, or training qualification.

## Required Inputs

- Authorized process description and task sequence.
- Acceptance criteria, audience, and document template or required fields.

## Optional Inputs

- Photos, tools/materials, quality records, revision history, ergonomic notes, and reviewer/owner.

## Assumptions

- Missing step detail is marked unresolved; the skill does not fill it from generic practice.
- The draft is uncontrolled until an authorized owner reviews and releases it.

## Core Workflow

1. Confirm scope, authorization, audience, sequence, criteria, and document controls.
2. Structure the draft with steps, prerequisites, evidence points, exceptions, and unresolved fields.
3. Return a review package with owner, version placeholder, and release boundary.

## Calculations

No calculation required. Preserve supplied times or quantities with units if included.

## Validation

- Check that each task has a source, sequence position, acceptance criterion, and exception path where supplied.
- Flag missing approvals, ambiguous terms, and conflicting revisions.
- Ensure the output does not claim effective status or qualification.

## Exception Handling

- Missing authorization or process evidence returns `NEEDS_INPUT`.
- Conflicting revisions return `REVIEW_REQUIRED` via `SOURCE_REVIEW_REQUIRED` or `ENGINEERING_REVIEW_REQUIRED` as applicable.
- Hazardous operating steps return `SAFETY_ESCALATION` and are withheld.

## Source Usage

- Use `references/work-instruction-draft-checklist.md` and supplied authorized records.
- Record document owner, revision, effective date, and source provenance; do not copy protected manuals beyond permitted use.

## Output Contract

Return `status`, draft scope, source evidence, structured instruction, unresolved details, assumptions, validation notes, owner/reviewer, and release boundary. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `SAFETY_ESCALATION`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE` unless supplied content enters a hazardous or engineering boundary. Do not issue effective work authorization, permit, qualification, or unsafe operating steps.

## References

- `references/work-instruction-draft-checklist.md`

## Examples

Read the checklist for a draft with an unresolved acceptance criterion.

## Testing

Cover correct invocation, missing authorization, conflicting revision, safety boundary, expected output structure, and draft-versus-release distinction. Expected routing is not observed behavior.
