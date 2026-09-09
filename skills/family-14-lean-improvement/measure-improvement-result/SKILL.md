---
name: measure-improvement-result
description: Assess before-and-after improvement evidence across a declared population and metric without claiming causation or closure.
license: MIT
---

# Measure Improvement Result

**Taxonomy metadata:** family `14` Lean & Continuous Improvement; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compare baseline and post-intervention evidence on one declared metric.

## Triggers
- Baseline, post-period, metric, population, window, and intervention context are supplied.

## Non-Triggers
- Claiming causation, closing CAPA, or approving rollout.

## Required Inputs
- Metric, baseline, post-period, units, population, dates, and comparison rule.

## Optional Inputs
- Guardrails, exclusions, confidence method, seasonality, and concurrent changes.

## Assumptions
- Before/after difference alone does not prove causation.

## Core Workflow
1. Reconcile metric, population, periods, and exclusions.
2. Calculate change with visible intermediates.
3. Return confounders, guardrails, and owner review.

## Calculations
`absolute change = post - baseline`; `relative change = (post - baseline) / baseline` when baseline is nonzero.

## Validation
- Check units, denominator, periods, exclusions, guardrails, and concurrent changes.

## Exception Handling
- Missing baseline or post data returns `NEEDS_INPUT`.
- Rollout or closure request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/improvement-measurement-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, metric, baseline/post evidence, formulas, change, confounders, guardrails, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not claim causation, approve rollout, or close an action.

## References
- `references/improvement-measurement-checklist.md`

## Examples
A lower cycle time with changed product mix is a result requiring confounder review.

## Testing
Cover correct invocation, zero baseline, unit mismatch, expected output structure, and rollout refusal. Expected routing is not observed behavior.
