---
name: build-kaizen-plan
description: Define one bounded improvement intervention with measures, owner, and review gates without implementing the change.
license: MIT
---

# Build Kaizen Plan

**Taxonomy metadata:** family `14` Lean & Continuous Improvement; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure a scoped improvement experiment and measurement plan.

## Triggers
- Problem, baseline, intervention idea, metric, owner, and review window are supplied.

## Non-Triggers
- Implementing, approving, or declaring the intervention effective.

## Required Inputs
- Problem boundary, baseline, proposed intervention, metric, owner, and window.

## Optional Inputs
- Hypothesis, guardrails, stakeholders, dependencies, and rollback criteria.

## Assumptions
- A plan is not evidence that the intervention works.

## Core Workflow
1. Define problem, baseline, and hypothesis.
2. Specify measure, guardrail, owner, and review gate.
3. Return dependencies and approval questions.

## Calculations
Preserve supplied baseline arithmetic and units; do not forecast savings without evidence.

## Validation
- Check scope, baseline, measure, guardrail, window, and owner.

## Exception Handling
- Missing baseline or metric returns `NEEDS_INPUT`.
- Implementation request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/kaizen-plan-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, problem, hypothesis, intervention, measures, guardrails, owner, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not implement or approve an improvement.

## References
- `references/kaizen-plan-checklist.md`

## Examples
A target reduction is a hypothesis until before/after evidence is collected.

## Testing
Cover correct invocation, missing baseline, unit mismatch, expected output structure, and implementation refusal. Expected routing is not observed behavior.
