---
name: calculate-first-pass-yield
description: Calculate first-pass yield from initial units and units accepted without rework using an explicit period and exclusion basis.
license: PENDING_PROJECT_GOVERNANCE
---

# Calculate First-Pass Yield

## Overview

Calculate first-pass yield for one operation and population. Keep the initial denominator, first-pass numerator, rework, exclusions, units, and period explicit; do not count later reworked passes as first-pass acceptance.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: count first-pass acceptance; rework rate and rolled yield use different populations.

## Triggers

- Initial units entering operation, units passing without rework, period, and exclusion basis are supplied.

## Non-Triggers

- Rolled yield, rework investigation, product release, or a quality-system conclusion.

## Required Inputs

- Initial units entering the operation.
- Units accepted without rework, period, and exclusions.

## Optional Inputs

- Product/lot, rework events, scrap, inspection definition, and source owner.

## Assumptions

- Reworked units later passing are excluded from the first-pass numerator.
- Population and period remain aligned; missing exclusions are not assumed.

## Core Workflow

1. Confirm population, first-pass definition, units, period, and exclusions.
2. Calculate and preserve numerator/denominator and rework distinction.
3. Return result, gaps, assumptions, and quality handoff.

## Calculations

Use `first-pass yield = units accepted without rework / initial units entering operation`. Preserve numerator, denominator, exclusions, units, and rounding. Zero denominator returns `NEEDS_INPUT`.

## Validation

- Reject numerator greater than denominator or mixed populations.
- Check reworked units are not counted as first-pass.
- Keep quality result separate from final disposition.

## Exception Handling

- Missing first-pass definition returns `NEEDS_INPUT`.
- Rework population conflict returns `SOURCE_REVIEW_REQUIRED`.
- Release or certification requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/first-pass-yield-formula.md` and AM-08 calculation rules.
- Record source, lot/period, exclusion basis, and owner.

## Output Contract

Return `status`, scope, numerator/denominator, formula, intermediates, yield, rework distinction, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. No product release, quality certification, or process authorization is issued.

## References

- `references/first-pass-yield-formula.md`

## Examples

Read the formula reference for reworked units that later pass.

## Testing

Cover calculation correctness, zero denominator, numerator/denominator validation, rework exclusion, expected output structure, and release refusal. Expected routing is not observed behavior.
