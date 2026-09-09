---
name: calculate-capacity-utilization
description: Calculate utilization by comparing actual output or occupied time with a supplied rated-capacity basis.
license: MIT
---

# Calculate Capacity Utilization

## Overview

Compare actual output or occupied time with an identified rated-capacity denominator. Preserve the capacity definition and comparable basis; do not estimate a missing denominator.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: compare actual use against identified capacity; capacity estimation remains separate.

## Triggers

- Actual output or occupied time, rated available capacity, and comparable basis are supplied.

## Non-Triggers

- Capacity estimation, utilization target-setting, staffing, or machine-setting changes.

## Required Inputs

- Actual output/occupied time and rated capacity.
- Common period, units, resource, and capacity definition.

## Optional Inputs

- Losses, planned stops, product mix, calendar, and source owner.

## Assumptions

- Rated capacity is supplied evidence; absent capacity is not zero or an invitation to estimate.
- Actual and capacity bases must match resource, period, product, and unit.

## Core Workflow

1. Verify actual and denominator definitions, units, period, and source.
2. Calculate utilization and preserve capacity basis and intermediates.
3. Return gaps and handoff without creating a target.

## Calculations

Use `utilization = actual output or occupied time / rated available capacity or time`. Preserve numerator, denominator, units, period, and rounding. Missing denominator returns `NEEDS_INPUT`.

## Validation

- Reject non-comparable output/time bases and zero denominator.
- Flag results outside expected range for review rather than clamping.
- Distinguish utilization from capacity estimate and OEE.

## Exception Handling

- Missing rated capacity returns `NEEDS_INPUT`.
- Mixed product or calendar basis returns `SOURCE_REVIEW_REQUIRED`.
- Target or operating-change requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/capacity-utilization-formula.md` and AM-08 rules.
- Record source, capacity definition, period, units, and owner.

## Output Contract

Return `status`, scope, numerator/denominator, capacity basis, formula, utilization, assumptions, validation notes, gaps, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. No target, staffing, machine, or customer commitment is issued.

## References

- `references/capacity-utilization-formula.md`

## Examples

Read the formula reference for a missing rated-capacity denominator.

## Testing

Cover calculation correctness, missing denominator, mixed basis, zero denominator, expected output structure, and target-setting refusal. Expected routing is not observed behavior.
