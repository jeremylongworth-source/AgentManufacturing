---
name: plan-production-changeover
description: Allocate a reviewable changeover window and readiness checklist from approved steps, durations, product sequence, and resource calendar evidence.
license: MIT
---

# Plan Production Changeover

## Overview

Plan a time window for an approved changeover and identify readiness gaps. Preserve approved duration and safety steps; do not provide operating instructions or shorten work to fit a schedule.

**Taxonomy metadata:** family `02` Production Planning & Scheduling; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `REVIEW`. Audit distinction: allocate a window for approved changeover work; loss measurement and SMED improvement are separate.

## Triggers

- From/to products, approved changeover steps and durations, and a resource calendar are supplied.

## Non-Triggers

- Inventing setup steps, modifying safety controls, reducing approved duration, or issuing a changeover instruction.

## Required Inputs

- From/to product sequence.
- Approved changeover steps and durations.
- Resource calendar and next-order timing.

## Optional Inputs

- Materials/tools readiness, qualified personnel, cleaning/inspection evidence, and changeover owner.

## Assumptions

- Approved steps and durations are authoritative evidence for planning only.
- A window that does not fit creates a conflict; it does not justify shorter safety or quality work.

## Core Workflow

1. Confirm sequence, approved steps, duration units, resource calendar, and readiness evidence.
2. Allocate a window and check overlap with orders, maintenance, and calendar constraints.
3. Return the window, readiness checklist, conflicts, and planner/operations handoff.

## Calculations

Use supplied durations and transparent start/finish arithmetic. Preserve setup components and any stated overlap; never infer parallel work.

## Validation

- Check step approval, duration source, resource calendar, next-order boundary, and readiness owner.
- Flag missing tools, material, training, or inspection evidence.
- Ensure safety or quality steps remain intact.

## Exception Handling

- Missing approved duration or calendar returns `NEEDS_INPUT`.
- Window conflict returns `PARTIAL` with the conflict visible.
- Requests to shorten or bypass a safety step return `SAFETY_ESCALATION`.

## Source Usage

- Use `references/changeover-window-checklist.md` and supplied approved records.
- Record revision, owner, duration units, and effective date.

## Output Contract

Return `status`, sequence, window, duration basis, readiness checklist, conflicts, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `SAFETY_ESCALATION`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE` with escalation for bypass or unsafe compression. No operating instruction, permit, or release is issued.

## References

- `references/changeover-window-checklist.md`

## Examples

Read the checklist for an approved changeover that does not fit before the next order.

## Testing

Cover correct invocation, window conflict, missing readiness, approved-duration preservation, safety-boundary request, and expected output structure. Expected routing is not observed behavior.
