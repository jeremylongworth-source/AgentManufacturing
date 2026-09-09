---
name: analyze-failure-history
description: Analyze failure modes and exposure trends while keeping supplied metrics, event definitions, and causal investigation distinct.
license: MIT
---

# Analyze Failure History

**Taxonomy metadata:** family `10` Maintenance & Reliability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Summarize failure events, modes, exposure, and trend boundaries for a defined population.

## Triggers
- Failure history, mode taxonomy, exposure basis, and observation period are supplied.

## Non-Triggers
- Declaring physical cause, changing maintenance policy, or predicting lifetime.

## Required Inputs
- Asset population, event definition, failure modes, exposure, and period.

## Optional Inputs
- MTBF/MTTR, censored assets, changes, environment, and confidence method.

## Assumptions
- Failure counts without exposure do not establish worsening reliability.

## Core Workflow
1. Normalize event and mode definitions.
2. Compare modes against exposure and period.
3. Return trends, uncertainty, and investigation handoff.

## Calculations
Use declared rates or shares with visible denominators; do not infer causation.

## Validation
- Check population, exposure, mode consistency, censoring, and period.

## Exception Handling
- Missing exposure returns `NEEDS_INPUT`.
- Repair or lifetime claim returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/failure-history-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, population, modes, exposure, trends, uncertainties, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not direct repair or infer a certified reliability claim.

## References
- `references/failure-history-checklist.md`

## Examples
Failure counts rising while exposure doubles must retain the exposure denominator.

## Testing
Cover correct invocation, missing exposure, mixed mode definitions, expected output structure, and lifetime-claim refusal. Expected routing is not observed behavior.
