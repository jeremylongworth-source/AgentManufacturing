---
name: calculate-scrap-rate
description: Calculate scrap rate from supplied scrap quantity and a defined comparable input or output denominator.
license: MIT
---

# Calculate Scrap Rate

## Overview

Calculate scrap rate for one product/process population and period. Define the denominator, units, exclusions, and scrap boundary explicitly; do not mix mass and unit counts without a supported conversion.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: measure scrap against a stated denominator; material variance is broader.

## Triggers

- Scrap quantity, relevant denominator, period, and unit basis are supplied.

## Non-Triggers

- Scrap disposition, environmental compliance, root cause, or product release.

## Required Inputs

- Scrap quantity and denominator definition.
- Common period and compatible unit basis.

## Optional Inputs

- Product/lot, scrap reason, rework distinction, source, and exclusion policy.

## Assumptions

- The denominator is the supplied input/output population; it is not selected silently.
- Scrap mass and count remain separate unless an authorized conversion exists.

## Core Workflow

1. Confirm scrap boundary, denominator, units, period, and exclusions.
2. Calculate the rate with numerator/denominator visible.
3. Return gaps and quality/environmental owner handoff.

## Calculations

Use `scrap rate = scrap quantity / defined denominator`. Preserve numerator, denominator, units, period, and rounding. Mixed dimensions require a supported conversion or separate results.

## Validation

- Reject numerator greater than denominator when populations should match.
- Check positive denominator and unit compatibility.
- Keep scrap rate distinct from rework and rolled yield.

## Exception Handling

- Missing denominator returns `NEEDS_INPUT`.
- Mass/count mismatch returns `NEEDS_INPUT`.
- Disposition or compliance requests return `OUT_OF_SCOPE`/`SOURCE_REVIEW_REQUIRED`.

## Source Usage

- Use `references/scrap-rate-formula.md` and AM-08 rules.
- Record source, period, denominator policy, units, and owner.

## Output Contract

Return `status`, scope, numerator/denominator, formula, scrap rate, units, exclusions, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. Do not approve disposal, environmental compliance, product release, or process change.

## References

- `references/scrap-rate-formula.md`

## Examples

Read the formula reference for mass scrap with unit-count denominator.

## Testing

Cover calculation correctness, unit mismatch, zero denominator, boundary definition, expected output structure, and disposition refusal. Expected routing is not observed behavior.
