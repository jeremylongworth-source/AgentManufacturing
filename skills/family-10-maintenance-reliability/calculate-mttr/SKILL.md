---
name: calculate-mttr
description: Calculate mean time to repair from a defined repair clock and qualifying repair events without treating it as all downtime.
license: PENDING_PROJECT_GOVERNANCE
---

# Calculate MTTR

**Taxonomy metadata:** family `10` Maintenance & Reliability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compute repair-event duration on a declared start/stop clock.

## Triggers
- Qualifying repair events, clock definition, durations, and population are supplied.

## Non-Triggers
- Treating MTTR as all downtime, directing repair, or approving staffing changes.

## Required Inputs
- Repair start/stop rule, event durations, asset/population, and inclusion criteria.

## Optional Inputs
- Waiting time, parts delay, labor time, exclusions, and segmentation.

## Assumptions
- MTTR excludes time outside the declared repair clock.

## Core Workflow
1. Validate event boundaries and clock definition.
2. Calculate average qualifying repair duration.
3. Report excluded waiting or downtime components.

## Calculations
`MTTR = total qualifying repair time / number of qualifying repairs`.

## Validation
- Check timestamps, units, zero events, overlaps, and clock consistency.

## Exception Handling
- Zero repairs returns `NEEDS_INPUT`.
- Repair instruction request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/mttr-calculation-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, clock, events, formula, intermediates, MTTR, exclusions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not direct repair or staffing decisions.

## References
- `references/mttr-calculation-checklist.md`

## Examples
Waiting for parts is not repair time unless the declared clock includes it.

## Testing
Cover correct invocation, zero repairs, clock mismatch, expected output structure, and repair-direction refusal. Expected routing is not observed behavior.
