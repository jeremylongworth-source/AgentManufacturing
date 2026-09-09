---
name: prepare-shift-handoff
description: Transfer current shift status, exceptions, and unresolved issues without implicitly generating a new production schedule.
license: MIT
---

# Prepare Shift Handoff

**Taxonomy metadata:** family `13` Workforce & Shift Operations; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure a factual handoff between shifts.

## Triggers
- Current shift status, completed work, open issues, holds, and next-owner context are supplied.

## Non-Triggers
- Generating a new schedule, changing priorities, or authorizing work.

## Required Inputs
- Shift identity/time, work status, exceptions, holds, equipment/material state, and owner.

## Optional Inputs
- Metrics, photos, open permits, staffing notes, and escalation history.

## Assumptions
- Handoff records current state; it does not make unresolved work approved.

## Core Workflow
1. Capture completed, active, blocked, and unstarted work.
2. Link exceptions, owners, and evidence.
3. Return next-shift questions without inventing a plan.

## Calculations
No calculation; supplied counts and durations retain shift scope.

## Validation
- Check time, status, issue owner, holds, and evidence references.

## Exception Handling
- Missing shift or status returns `NEEDS_INPUT`.
- Schedule or authorization request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/shift-handoff-checklist.md`.

## Output Contract
Return `status`, shift context, work states, exceptions, owners, gaps, and handoff questions.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not authorize work, restart, or create a schedule implicitly.

## References
- `references/shift-handoff-checklist.md`

## Examples
A blocked operation is handed off with its owner and evidence gap, not silently rescheduled.

## Testing
Cover correct invocation, missing status, conflicting owners, expected output structure, and authorization refusal. Expected routing is not observed behavior.
