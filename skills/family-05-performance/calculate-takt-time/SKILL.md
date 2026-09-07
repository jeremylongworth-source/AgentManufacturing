---
name: calculate-takt-time
description: Calculate demand-driven takt time from net available production time and customer demand on a common period and unit basis.
license: PENDING_PROJECT_GOVERNANCE
---

# Calculate Takt Time

## Overview

Calculate a traceable takt result for one product or demand basis. Keep available-time exclusions, demand units, period, and zero-demand handling explicit; takt is not measured cycle time or capacity.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: demand-driven available-time rate differs from measured cycle time and machine capacity.

## Triggers

- Net available production time, customer demand, common period, and compatible units are supplied.

## Non-Triggers

- Cycle-time measurement, capacity estimation, staffing, schedule release, or machine operating targets.

## Required Inputs

- Net available production time and exclusions.
- Customer demand, common period, and compatible quantity/time units.

## Optional Inputs

- Product mix, shift calendar, planned losses, and source owner.

## Assumptions

- Available time is supplied evidence; planned stops are not silently included.
- Zero demand produces undefined/not-applicable takt, not division by zero or infinity.

## Core Workflow

1. Align time basis, demand unit, product scope, and availability exclusions.
2. Calculate takt and preserve numerator, denominator, units, and period.
3. Return gaps and distinguish takt from cycle time and capacity.

## Calculations

Use `takt time = net available production time / customer demand` with a common period and quantity basis. Preserve intermediate values and round only at the end. Zero demand returns `NEEDS_INPUT` or `PARTIAL` with `NOT_APPLICABLE`.

## Validation

- Reject incompatible dimensions such as hours and litres without a supplied conversion.
- Check positive available time and non-negative demand.
- Do not convert takt into a machine setting or guarantee.

## Exception Handling

- Missing demand or availability returns `NEEDS_INPUT`.
- Zero demand returns `PARTIAL`/`NEEDS_INPUT` with undefined/not-applicable status.
- Operating-target requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/takt-time-formula.md` and the AM-08 calculation standard.
- Record calendar, source, period, units, and exclusions.

## Output Contract

Return `status`, scope/period, available-time evidence, demand evidence, formula, intermediates, takt result, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, and `OUT_OF_SCOPE`.

## Safety Requirements

AM-05 class: `ROUTINE`. No machine setting, staffing change, or production authorization is issued.

## References

- `references/takt-time-formula.md`

## Examples

Read the formula reference for zero demand and incompatible units.

## Testing

Cover calculation correctness, zero demand, unit mismatch, missing available time, expected output structure, and operating-target refusal. Expected routing is not observed behavior.
