---
name: calculate-throughput
description: Calculate completed output per elapsed time from a common product, unit, period, and counting-exclusion basis.
license: PENDING_PROJECT_GOVERNANCE
---

# Calculate Throughput

## Overview

Calculate throughput for one product/process boundary and elapsed period. Keep completed quantity, time denominator, exclusions, and units aligned; throughput is not labor productivity, capacity, or customer commitment.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: measure completed output per elapsed time; labor productivity uses labor exposure.

## Triggers

- Completed quantity, elapsed period, product/unit basis, and counting exclusions are supplied.

## Non-Triggers

- Capacity estimate, labor productivity, schedule release, or output guarantee.

## Required Inputs

- Completed quantity and elapsed time denominator.
- Product/unit basis, period, and exclusions.

## Optional Inputs

- Asset, shift, good/scrap/rework definitions, source, and target comparison.

## Assumptions

- Quantity and time periods match; missing exclusions remain unresolved.
- Completed output is not assumed to be good output unless stated.

## Core Workflow

1. Align quantity, period, unit, completion definition, and exclusions.
2. Calculate rate and preserve numerator/denominator.
3. Return gaps and a review handoff.

## Calculations

Use `throughput = completed quantity / elapsed time`. Preserve units, period, exclusions, intermediates, and rounding. Zero elapsed time returns `NEEDS_INPUT`.

## Validation

- Reject mismatched quantity/time intervals and incompatible units.
- Check non-negative quantity and positive time.
- Distinguish output throughput from quality and capacity.

## Exception Handling

- Missing denominator returns `NEEDS_INPUT`.
- Period mismatch returns `SOURCE_REVIEW_REQUIRED`.
- Guarantee or release requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/throughput-formula.md` and AM-08 calculation rules.
- Record source, period, unit, and exclusions.

## Output Contract

Return `status`, scope, numerator/denominator, formula, throughput, units, exclusions, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. No production target, staffing, or customer promise is issued.

## References

- `references/throughput-formula.md`

## Examples

Read the formula reference for mismatched output and time periods.

## Testing

Cover calculation correctness, zero time, period mismatch, unit mismatch, expected output structure, and guarantee refusal. Expected routing is not observed behavior.
