---
name: calculate-pp-ppk
description: Calculate Pp and Ppk from overall variation for one coherent population without implying process stability.
license: MIT
---

# Calculate Pp and Ppk

**Taxonomy metadata:** family `08` SPC & Capability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compute long-term performance indices with an explicit sampling window and population.

## Triggers
- USL, LSL, mean, overall standard deviation, and coherent sampling window are supplied.

## Non-Triggers
- Mixing product specifications, claiming stability, or accepting product.

## Required Inputs
- USL, LSL, mean, overall standard deviation, units, and sampling window.

## Optional Inputs
- Stratification, exclusions, distribution notes, and reporting precision.

## Assumptions
- Overall performance indices do not establish a stable process.

## Core Workflow
1. Verify one characteristic, population, and spec set.
2. Calculate Pp and Ppk with visible intermediates.
3. State sampling and stability limits.

## Calculations
`Pp=(USL-LSL)/(6*sigma_overall)`; `Ppk=min((USL-mean)/(3*sigma_overall),(mean-LSL)/(3*sigma_overall))`.

## Validation
- Check mixed specs, units, positive sigma, and population coherence.

## Exception Handling
- Mixed product specs return `NEEDS_INPUT`.
- Acceptance request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/pp-ppk-calculation-checklist.md` and AM-08 calculation rules.

## Output Contract
Return `status`, inputs, formula, intermediates, Pp, Ppk, window, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not infer process control or authorize release.

## References
- `references/pp-ppk-calculation-checklist.md`

## Examples
Mixed specification limits require population separation before calculation.

## Testing
Cover correct invocation, mixed specs, zero sigma, expected output structure, and stability refusal. Expected routing is not observed behavior.
