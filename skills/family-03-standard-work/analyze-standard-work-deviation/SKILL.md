---
name: analyze-standard-work-deviation
description: Analyze observed execution records against an applicable standard version to separate instruction gaps from execution variance.
license: PENDING_PROJECT_GOVERNANCE
---

# Analyze Standard Work Deviation

## Overview

Create a deviation analysis for one standard version, observed execution record, and timing/context boundary. Separate a document gap from an execution variance without blaming an operator or authorizing a corrective action.

**Taxonomy metadata:** family `03` Standard Work & Work Instructions; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `review-document-revision`, `REVIEW`. Audit distinction: analyze one deviation; document review and corrective action are separate.

## Triggers

- The user supplies an applicable standard version, observed execution records, and deviation timing/context.

## Non-Triggers

- Operator discipline judgments, live coaching commands, document release, or corrective-action approval.

## Required Inputs

- Applicable standard version and source.
- Observed execution records with timing/context and boundary.
- Description of the deviation.

## Optional Inputs

- Operator feedback, equipment state, training record, prior deviations, and revision history.

## Assumptions

- Observation is evidence for a bounded event, not proof of general behavior.
- A deviation may arise from instruction, training, equipment, material, or context; cause remains open.

## Core Workflow

1. Verify standard version, observation boundary, and deviation definition.
2. Compare expected versus observed elements and classify document, execution, or evidence gaps.
3. Return findings, uncertainty, and review owner without assigning blame or approving action.

## Calculations

No calculation required; preserve supplied times and units.

## Validation

- Check version/effective date, observation source, units, and context.
- Require evidence before calling a deviation systemic or causal.

## Exception Handling

- Missing standard or observation returns `NEEDS_INPUT`.
- Stale/conflicting standard returns `SOURCE_REVIEW_REQUIRED`.
- Safety or engineering deviations return `SAFETY_ESCALATION` or `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage

- Use `references/standard-work-deviation-checklist.md` and controlled records.
- Record revision, source, date, and observer; do not reproduce protected procedures.

## Output Contract

Return `status`, standard and observation scope, expected/observed comparison, classification, evidence gaps, assumptions, validation notes, and owner handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `SOURCE_REVIEW_REQUIRED`, `SAFETY_ESCALATION`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE` with escalation for supplied hazardous or engineering content. Do not issue discipline, operating, or corrective-action authority.

## References

- `references/standard-work-deviation-checklist.md`

## Examples

Read the checklist for a timing deviation with a stale document revision.

## Testing

Cover correct invocation, missing standard, stale version, ambiguous observation, safety escalation, expected output structure, and instruction-gap versus execution-variance separation. Expected routing is not observed behavior.
