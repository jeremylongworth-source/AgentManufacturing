---
name: identify-eight-wastes
description: Classify observed lean waste opportunities from supplied evidence without quantifying savings or authorizing change.
license: PENDING_PROJECT_GOVERNANCE
---

# Identify Eight Wastes

**Taxonomy metadata:** family `14` Lean & Continuous Improvement; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Classify observations against a declared waste taxonomy and preserve evidence gaps.

## Triggers
- Process observations, examples, and scope are supplied.

## Non-Triggers
- Quantifying savings, changing work, or ranking workers.

## Required Inputs
- Observation, process boundary, taxonomy, date, and source.

## Optional Inputs
- Time, inventory, defects, motion, transport, waiting, overproduction, and unused talent evidence.

## Assumptions
- A waste classification is a hypothesis, not a validated loss estimate.

## Core Workflow
1. Separate observation from interpretation.
2. Classify candidate waste types with evidence.
3. Return questions for time-study or owner review.

## Calculations
No calculation; supplied quantities retain unit and source basis.

## Validation
- Check process scope, taxonomy, evidence, and observation date.

## Exception Handling
- Missing observation returns `NEEDS_INPUT`.
- Change or savings request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/eight-wastes-checklist.md`.

## Output Contract
Return `status`, observation, waste classification, evidence, gaps, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not authorize change or claim savings.

## References
- `references/eight-wastes-checklist.md`

## Examples
Waiting is classified from an observed queue; savings require a separate measured baseline.

## Testing
Cover correct invocation, missing observation, mixed taxonomy, expected output structure, and change refusal. Expected routing is not observed behavior.
