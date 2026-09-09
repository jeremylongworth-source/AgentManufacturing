---
name: review-control-limits
description: Review the evidence and exclusions behind control limits while keeping specification limits separate.
license: MIT
---

# Review Control Limits

**Taxonomy metadata:** family `08` SPC & Capability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Screen control-limit calculations, baseline scope, and exclusion reasons.

## Triggers
- Control limits, baseline data, exclusions, and chart basis are supplied.

## Non-Triggers
- Recasting specifications as controls, changing limits, or directing intervention.

## Required Inputs
- Baseline data, chart family, limits, and exclusion reasons.

## Optional Inputs
- Signal history, subgroup rationale, and approved revision history.

## Assumptions
- Unsupported exclusions weaken the limit basis.

## Core Workflow
1. Reconcile limits to chart family and baseline.
2. Inspect every exclusion and reason.
3. Return supported, unsupported, and review-required findings.

## Calculations
Recalculate only from the declared baseline and method; never substitute specs for controls.

## Validation
- Check chronology, exclusions, units, and revision ownership.

## Exception Handling
- Missing exclusion reasons returns `SOURCE_REVIEW_REQUIRED`.
- Limit-change request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/control-limit-review-checklist.md`.

## Output Contract
Return `status`, chart basis, baseline, limits, exclusions, gaps, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not authorize limit changes.

## References
- `references/control-limit-review-checklist.md`

## Examples
A baseline exclusion without a reason is unsupported even if the resulting limits look plausible.

## Testing
Cover correct invocation, unjustified exclusion, spec/control confusion, expected output structure, and limit-change refusal. Expected routing is not observed behavior.
