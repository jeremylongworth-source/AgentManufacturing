---
name: analyze-labor-productivity
description: Relate output to declared labor exposure and units without ranking workers or predicting staffing needs.
license: PENDING_PROJECT_GOVERNANCE
---

# Analyze Labor Productivity

**Taxonomy metadata:** family `13` Workforce & Shift Operations; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compare output with labor exposure for a defined population, period, and metric.

## Triggers
- Output, labor hours/exposure, units, population, and period are supplied.

## Non-Triggers
- Ranking individuals, setting quotas, hiring, or approving overtime.

## Required Inputs
- Output quantity, labor exposure, unit basis, period, and population.

## Optional Inputs
- Product mix, rework, absences, learning curve, and exclusions.

## Assumptions
- Productivity is sensitive to mix, quality, and exposure definitions.

## Core Workflow
1. Reconcile output and labor exposure.
2. Calculate declared productivity metric with intermediates.
3. Return comparability gaps and owner review.

## Calculations
`labor productivity = output quantity / labor exposure`; preserve units and population.

## Validation
- Check output, labor denominator, mix, rework, period, and units.

## Exception Handling
- Missing labor denominator returns `NEEDS_INPUT`.
- Worker ranking or quota request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/labor-productivity-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, population, inputs, formula, result, comparability gaps, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not rank workers, set quotas, or approve staffing action.

## References
- `references/labor-productivity-checklist.md`

## Examples
Mixed product output cannot be compared without a declared mix basis.

## Testing
Cover correct invocation, missing denominator, mixed output units, expected output structure, and quota refusal. Expected routing is not observed behavior.
