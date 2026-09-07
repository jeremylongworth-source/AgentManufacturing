---
name: prioritize-maintenance-work
description: Rank maintenance backlog items using supplied risk and operating restrictions without authorizing hazardous work.
license: PENDING_PROJECT_GOVERNANCE
---

# Prioritize Maintenance Work

**Taxonomy metadata:** family `10` Maintenance & Reliability; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Produce a transparent backlog ranking from declared criteria and constraints.

## Triggers
- Backlog items, risk basis, due constraints, and available capacity are supplied.

## Non-Triggers
- Dispatching work, changing priority policy, or authorizing a hazardous task.

## Required Inputs
- Work items, asset criticality, risk criteria, due dates, and restrictions.

## Optional Inputs
- Capacity, outage windows, permits, skills, spares, and consequence data.

## Assumptions
- A ranking is advisory and does not replace authorization or planning.

## Core Workflow
1. Normalize item identity, risk, and constraints.
2. Apply the declared ranking method with visible inputs.
3. Return ties, gaps, and owner review points.

## Calculations
Use only supplied scoring rules; preserve units and do not invent weights.

## Validation
- Check criteria, data freshness, restrictions, and capacity basis.

## Exception Handling
- Missing risk basis returns `NEEDS_INPUT`.
- Execution or dispatch request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/maintenance-priority-checklist.md`.

## Output Contract
Return `status`, ranked items, criteria, constraints, ties, gaps, and authorized owner handoff.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Do not dispatch, schedule, or authorize hazardous work.

## References
- `references/maintenance-priority-checklist.md`

## Examples
A high-risk item with no safe outage window remains a constrained priority, not an instruction to proceed.

## Testing
Cover correct invocation, missing risk basis, capacity mismatch, expected output structure, and dispatch refusal. Expected routing is not observed behavior.
