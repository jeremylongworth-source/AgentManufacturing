---
name: review-operator-checklist
description: Review an operator checklist against approved task requirements and completion records for coverage and exception-handling gaps.
license: MIT
---

# Review Operator Checklist

## Overview

Assess one checklist revision against approved task requirements, completion records, and exception evidence. Identify coverage, ambiguity, and exception-handling gaps without approving the checklist or inferring operator qualification.

**Taxonomy metadata:** family `03` Standard Work & Work Instructions; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `REVIEW`. Audit distinction: review checklist coverage; drafting, training, and release are separate.

## Triggers

- The user supplies a checklist revision, approved task requirements, and completion or exception records and asks for a review.

## Non-Triggers

- Operator qualification, training signoff, live inspection direction, document release, or product disposition.

## Required Inputs

- Checklist revision and owner/effective context.
- Approved task requirements.
- Completion and exception records.

## Optional Inputs

- Operator feedback, audit observations, form template, and traceability fields.

## Assumptions

- A checked box is evidence of recording, not proof that a task was performed correctly.
- Missing exception records remain unknown.

## Core Workflow

1. Compare checklist coverage and fields with approved requirements.
2. Review completion and exception handling for gaps, ambiguity, and traceability.
3. Return findings, evidence gaps, and the document owner handoff.

## Calculations

No calculation required.

## Validation

- Check revision, requirement mapping, completion population, exception path, and traceability.
- Do not turn coverage into a compliance or qualification percentage.

## Exception Handling

- Missing approved requirements returns `NEEDS_INPUT`.
- Conflicting records return `PARTIAL` or `SOURCE_REVIEW_REQUIRED`.
- Safety or regulated checklist context escalates to the responsible owner.

## Source Usage

- Use `references/operator-checklist-review.md` and supplied controlled records.
- Record revision, source, date, and owner; do not reproduce protected procedures.

## Output Contract

Return `status`, checklist scope/version, requirement mapping, coverage findings, exception gaps, assumptions, validation notes, and owner/review handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `SOURCE_REVIEW_REQUIRED`, and `SAFETY_ESCALATION`.

## Safety Requirements

AM-05 class: `ROUTINE`; escalate safety-critical checklist gaps. Do not sign training, qualification, release, or compliance.

## References

- `references/operator-checklist-review.md`

## Examples

Read the checklist reference for a form missing an exception path.

## Testing

Cover correct invocation, missing requirements, incomplete exceptions, ambiguous coverage, safety escalation, expected output structure, and qualification refusal. Expected routing is not observed behavior.
