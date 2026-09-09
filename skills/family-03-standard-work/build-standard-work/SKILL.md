---
name: build-standard-work
description: Draft standard work from observed task elements, approved sequence, time evidence, takt context, and allowed work-in-process limits.
license: MIT
---

# Build Standard Work

## Overview

Create a standard-work draft relating sequence, observed task elements and times, takt context, and allowed WIP. Preserve missing observations and approvals; do not publish the draft as an effective operating standard.

**Taxonomy metadata:** family `03` Standard Work & Work Instructions; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `calculate-takt-time`, `analyze-cycle-time`, `REVIEW`. Audit distinction: build one standard-work draft; takt and cycle-time calculations remain separate owners.

## Triggers

- The user supplies observed task elements/times, an approved sequence, takt context, and WIP constraints and asks for standard work.

## Non-Triggers

- Inventing a takt time, changing staffing or machine settings, releasing a work instruction, or authorizing hazardous operation.

## Required Inputs

- Observed task elements and times with units and observation boundary.
- Approved sequence, takt context, and allowed WIP constraints.

## Optional Inputs

- Operator feedback, balance observations, quality checks, ergonomic review, and document template.

## Assumptions

- Observed time is not a target or guarantee; takt and cycle definitions must be supplied by their owner.
- Missing approval, WIP, or time evidence remains visible.

## Core Workflow

1. Align sequence, observations, takt context, and WIP definitions.
2. Structure a draft sequence with time evidence, checks, WIP limits, and unresolved balance questions.
3. Return a review package for operations, quality, and safety owners.

## Calculations

No new formula is required. Preserve supplied takt or cycle values and units; route their calculation to the owning skill.

## Validation

- Check time units, observation period, sequence approval, and WIP definition.
- Flag any task that cannot be supported by observation or authorized process evidence.
- Ensure the result is a draft and does not imply staffing or equipment authority.

## Exception Handling

- Missing or incompatible time evidence returns `NEEDS_INPUT`.
- Conflicting sequence or WIP rules return `SOURCE_REVIEW_REQUIRED`.
- Unsafe step requests return `SAFETY_ESCALATION` and are withheld.

## Source Usage

- Use `references/standard-work-draft-checklist.md` and supplied observation records.
- Record source, units, observer, date, and owner; do not copy protected standards text.

## Output Contract

Return `status`, scope, sequence, observed time evidence, takt/WIP context, draft standard work, unknowns, assumptions, validation notes, and review owner. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `SAFETY_ESCALATION`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE` unless supplied work crosses a hazardous or engineering boundary. No operating authorization, staffing command, or release is issued.

## References

- `references/standard-work-draft-checklist.md`

## Examples

Read the checklist for a draft with observed times but missing takt definition.

## Testing

Cover correct invocation, missing time evidence, unit mismatch, conflicting sequence, safety boundary, expected output structure, and draft-versus-release distinction. Expected routing is not observed behavior.
