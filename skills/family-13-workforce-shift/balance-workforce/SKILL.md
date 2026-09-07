---
name: balance-workforce
description: Allocate available skills and hours to declared tasks under restrictions without authorizing overtime or personnel assignment.
license: PENDING_PROJECT_GOVERNANCE
---

# Balance Workforce

**Taxonomy metadata:** family `13` Workforce & Shift Operations; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compare task workload with available skill/hours and expose infeasible assignments.

## Triggers
- Tasks, workload, skills, available hours, restrictions, and horizon are supplied.

## Non-Triggers
- Assigning people, approving overtime, hiring, or directing unsafe work.

## Required Inputs
- Task workload, skill requirements, available hours, horizon, and restrictions.

## Optional Inputs
- Absences, breaks, cross-training, learning curve, and overtime policy.

## Assumptions
- A feasible arithmetic allocation is not a personnel authorization.

## Core Workflow
1. Normalize workload, skills, hours, and horizon.
2. Allocate within stated restrictions and show gaps.
3. Return supervisor/HR review questions.

## Calculations
Use supplied workload-to-hour conversions and units; do not invent availability.

## Validation
- Check skill compatibility, hours, horizon, breaks, and restrictions.

## Exception Handling
- Missing skills or hours returns `NEEDS_INPUT`.
- Overtime or assignment request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/workforce-balance-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, task allocation, available hours, gaps, assumptions, and owner handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not assign personnel or approve overtime.

## References
- `references/workforce-balance-checklist.md`

## Examples
An unsatisfied skill requirement remains a gap rather than an automatic reassignment.

## Testing
Cover correct invocation, missing skill, unit mismatch, expected output structure, and assignment refusal. Expected routing is not observed behavior.
