---
name: build-shift-production-plan
description: Allocate an existing production horizon to one shift using readiness evidence without authorizing overtime or unsafe work.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Shift Production Plan

**Taxonomy metadata:** family `13` Workforce & Shift Operations; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Translate an approved horizon plan into a shift-level allocation with constraints visible.

## Triggers
- Existing horizon plan, shift window, work readiness, staffing, and constraints are supplied.

## Non-Triggers
- Creating the horizon plan, approving overtime, changing priorities, or directing unsafe work.

## Required Inputs
- Shift window, approved work, staffing/skills, material readiness, capacity, and constraints.

## Optional Inputs
- Breaks, changeovers, absences, maintenance windows, and escalation path.

## Assumptions
- Shift allocation is subordinate to approved plan and local authorization.

## Core Workflow
1. Validate horizon scope and shift readiness.
2. Allocate feasible work with gaps and unmet demand visible.
3. Return supervisor handoff and unresolved approvals.

## Calculations
Preserve supplied time, capacity, and demand units; do not invent staffing or overtime.

## Validation
- Check horizon, shift time, skills, material, capacity, and safety constraints.

## Exception Handling
- Missing readiness returns `NEEDS_INPUT`.
- Overtime or unsafe assignment request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/shift-production-plan-checklist.md`.

## Output Contract
Return `status`, shift allocation, constraints, unmet work, assumptions, and supervisor handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not approve overtime or assign unsafe work.

## References
- `references/shift-production-plan-checklist.md`

## Examples
Missing material readiness remains an unmet constraint rather than an instruction to substitute.

## Testing
Cover correct invocation, missing staffing, unit mismatch, expected output structure, and overtime refusal. Expected routing is not observed behavior.
