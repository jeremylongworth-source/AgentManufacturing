---
name: document-nonconformance
description: Structure a nonconformance record that separates observed evidence, requirement, scope, and review status.
license: MIT
---

# Document Nonconformance

**Taxonomy metadata:** family `09` Nonconformance, RCA & CAPA; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Capture a reviewable record without turning an allegation into a conclusion.

## Triggers
- Observation, requirement, evidence references, and record context are supplied.

## Non-Triggers
- Approving containment, disposition, root cause, or CAPA closure.

## Required Inputs
- Record identity, observation, requirement, date, source, and affected scope.

## Optional Inputs
- Attachments, reporter, initial risk, containment proposal, and owner.

## Assumptions
- Unknown facts remain unknown and are marked for review.

## Core Workflow
1. Capture verbatim observation and requirement separately.
2. Link evidence and identify scope gaps.
3. Return record fields and review status.

## Calculations
No calculation; counts or severity ratings retain their declared scale.

## Validation
- Check identity, revision, evidence links, dates, and scope.

## Exception Handling
- Missing observation or source returns `NEEDS_INPUT`.
- Closure request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/nonconformance-record-checklist.md`.

## Output Contract
Return `status`, record fields, observation, requirement, evidence, scope, gaps, assumptions, and owner handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not approve record closure or product disposition.

## References
- `references/nonconformance-record-checklist.md`

## Examples
Record what was observed before interpreting why it happened.

## Testing
Cover correct invocation, missing evidence, conflicting revisions, expected output structure, and closure refusal. Expected routing is not observed behavior.
