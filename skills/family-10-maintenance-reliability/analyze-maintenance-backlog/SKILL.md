---
name: analyze-maintenance-backlog
description: Measure maintenance backlog age, effort, capacity, and composition without deciding priority or dispatch.
license: MIT
---

# Analyze Maintenance Backlog

**Taxonomy metadata:** family `10` Maintenance & Reliability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Describe queued work using declared age, effort, capacity, and status definitions.

## Triggers
- Backlog records, dates, estimated effort, capacity basis, and status rules are supplied.

## Non-Triggers
- Prioritizing, dispatching, resourcing, or authorizing work.

## Required Inputs
- Item identity, created/due dates, effort units, status, and observation date.

## Optional Inputs
- Skill, permit, spare, outage, and capacity constraints.

## Assumptions
- Backlog age and backlog risk are different measures.

## Core Workflow
1. Normalize item status, dates, and effort units.
2. Summarize age, effort, composition, and capacity gaps.
3. Return data-quality findings and owner handoff.

## Calculations
Age = observation date - created date; retain calendar and timezone basis.

## Validation
- Check date basis, effort units, duplicates, status definitions, and capacity period.

## Exception Handling
- Missing observation date returns `NEEDS_INPUT`.
- Priority or dispatch request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/maintenance-backlog-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, backlog scope, age/effort summaries, capacity basis, gaps, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not schedule, dispatch, or authorize work.

## References
- `references/maintenance-backlog-checklist.md`

## Examples
Old work is not automatically high risk without a declared risk basis.

## Testing
Cover correct invocation, missing date, mixed effort units, expected output structure, and dispatch refusal. Expected routing is not observed behavior.
