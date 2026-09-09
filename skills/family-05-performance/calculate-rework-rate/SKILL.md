---
name: calculate-rework-rate
description: Calculate rework rate from supplied units requiring rework using an explicit population, period, and repeated-event counting rule.
license: MIT
---

# Calculate Rework Rate

## Overview

Calculate rework rate for one operation or population while distinguishing units requiring rework from repeated rework events. Preserve the counting rule, period, and denominator; do not treat the result as first-pass yield or a disposition decision.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: count units needing rework with an explicit repeat-event rule; this is not first-pass yield.

## Triggers

- Units requiring rework, population definition, period, and repeated-rework counting rule are supplied.

## Non-Triggers

- Root cause, corrective action, first-pass yield, product release, or rework authorization.

## Required Inputs

- Rework units/events and denominator population.
- Period and rule for repeated rework.

## Optional Inputs

- Operation, product/lot, rework reason, repeat count, and source owner.

## Assumptions

- One unit reworked twice may count as one unit or two events only according to the supplied rule.
- Missing population or period remains unresolved.

## Core Workflow

1. Confirm unit/event basis, denominator, period, and repeat rule.
2. Calculate and show units needing rework versus event count.
3. Return result, gaps, assumptions, and quality handoff.

## Calculations

Use `rework rate = units requiring rework / defined population` when the unit basis is requested; provide event rate separately only with a supplied event denominator. Preserve intermediates and rounding.

## Validation

- Check numerator/denominator populations and repeat-event treatment.
- Reject mixed periods or numerator greater than denominator for a unit rate.
- Keep rework distinct from first-pass yield, scrap, and rolled yield.

## Exception Handling

- Missing repeat rule returns `NEEDS_INPUT`.
- Conflicting unit/event records return `SOURCE_REVIEW_REQUIRED`.
- Release or corrective-action requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/rework-rate-formula.md` and AM-08 rules.
- Record source, population, period, counting rule, and owner.

## Output Contract

Return `status`, scope, unit/event basis, numerator/denominator, formula, rate, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. No product disposition, process change, or corrective-action approval is issued.

## References

- `references/rework-rate-formula.md`

## Examples

Read the formula reference for one unit reworked twice.

## Testing

Cover calculation correctness, repeated-event rule, zero denominator, mixed population, expected output structure, and disposition refusal. Expected routing is not observed behavior.
