---
name: calculate-cp-cpk
description: Calculate Cp and Cpk from declared within-process variation while preserving specification, population, and stability assumptions.
license: PENDING_PROJECT_GOVERNANCE
---

# Calculate Cp and Cpk

**Taxonomy metadata:** family `08` SPC & Capability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compute short-term capability indices when the within-process variation basis is explicit.

## Triggers
- USL, LSL, mean, and within-process standard deviation are supplied for one coherent stable population.

## Non-Triggers
- Using overall standard deviation as a substitute, accepting product, or changing limits.

## Required Inputs
- USL, LSL, mean, within-process standard deviation, units, and population.

## Optional Inputs
- Subgroup design, stability evidence, rounding rule, and acceptance criterion.

## Assumptions
- Overall standard deviation is not within-process variation.

## Core Workflow
1. Validate limits, units, population, and sigma basis.
2. Calculate Cp and Cpk with visible intermediates.
3. Return result, assumptions, and review boundary.

## Calculations
`Cp=(USL-LSL)/(6*sigma_within)`; `Cpk=min((USL-mean)/(3*sigma_within),(mean-LSL)/(3*sigma_within))`.

## Validation
- Check positive sigma, coherent units, spec limits, and declared within basis.

## Exception Handling
- Only overall sigma returns `NEEDS_INPUT`.
- Acceptance request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/cp-cpk-calculation-checklist.md` and AM-08 calculation rules.

## Output Contract
Return `status`, inputs, formula, intermediates, Cp, Cpk, rounding, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not make release or acceptance decisions.

## References
- `references/cp-cpk-calculation-checklist.md`

## Examples
An overall standard deviation cannot be silently relabeled as within-process sigma.

## Testing
Cover correct invocation, overall-sigma misuse, zero sigma, expected output structure, and acceptance refusal. Expected routing is not observed behavior.
