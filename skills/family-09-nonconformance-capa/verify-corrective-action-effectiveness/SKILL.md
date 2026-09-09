---
name: verify-corrective-action-effectiveness
description: Assess predefined evidence that a corrective action addressed a cause without closing the record or approving release.
license: MIT
---

# Verify Corrective-Action Effectiveness

**Taxonomy metadata:** family `09` Nonconformance, RCA & CAPA; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compare effectiveness evidence with a predefined criterion and observation window.

## Triggers
- Corrective action, cause, verification criterion, baseline, and post-action evidence are supplied.

## Non-Triggers
- Declaring CAPA closure, accepting product, or changing the criterion after seeing results.

## Required Inputs
- Action identity, criterion, baseline, post-action data, window, and population.

## Optional Inputs
- Recurrence history, confidence basis, exclusions, and independent reviewer.

## Assumptions
- Implementation completion alone is not effectiveness evidence.

## Core Workflow
1. Reconcile criterion, baseline, population, and window.
2. Compare evidence with declared method and exclusions.
3. Return effective, inconclusive, or ineffective status for owner review.

## Calculations
Use the declared metric and comparison method; preserve units, denominators, and intervals.

## Validation
- Check baseline, post-action evidence, recurrence, criterion, and exclusions.

## Exception Handling
- Missing post-action evidence returns `NEEDS_INPUT`.
- Closure or release request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/effectiveness-verification-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, action, criterion, baseline, evidence, comparison, uncertainty, and owner handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not close CAPA or authorize release.

## References
- `references/effectiveness-verification-checklist.md`

## Examples
An implemented action with no post-action observation window is inconclusive.

## Testing
Cover correct invocation, missing window, denominator mismatch, expected output structure, and closure refusal. Expected routing is not observed behavior.
