---
name: calculate-mtbf
description: Calculate mean time between failures for repairable assets using one declared exposure and failure definition.
license: MIT
---

# Calculate MTBF

**Taxonomy metadata:** family `10` Maintenance & Reliability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compute MTBF from operating exposure and qualifying failure events.

## Triggers
- Repairable asset, exposure duration, qualifying failure count, and definition are supplied.

## Non-Triggers
- Guaranteeing lifetime, predicting a specific failure, or authorizing maintenance.

## Required Inputs
- Asset/population, exposure window, operating-time basis, failure definition, and failure count.

## Optional Inputs
- Censoring, exclusions, confidence method, and segmentation.

## Assumptions
- MTBF is meaningful only for the declared repairable population and failure definition.

## Core Workflow
1. Validate exposure and qualifying failures.
2. Calculate and show numerator/denominator.
3. State censoring, exclusions, and interpretation limits.

## Calculations
`MTBF = total qualifying operating time / number of qualifying failures`.

## Validation
- Check zero failures, units, exposure, and failure inclusion rule.

## Exception Handling
- Zero failure count returns an interval/estimation boundary, not a finite MTBF.
- Lifetime guarantee request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/mtbf-calculation-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, inputs, formula, intermediates, MTBF, units, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not make reliability guarantees or maintenance decisions.

## References
- `references/mtbf-calculation-checklist.md`

## Examples
Failure counts rising while exposure doubles require exposure context before comparison.

## Testing
Cover correct invocation, zero failures, unit mismatch, expected output structure, and lifetime-guarantee refusal. Expected routing is not observed behavior.
