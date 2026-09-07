---
name: analyze-flow-efficiency
description: Compare declared value-adding and elapsed times while keeping flow analysis distinct from cycle-time and takt calculations.
license: PENDING_PROJECT_GOVERNANCE
---

# Analyze Flow Efficiency

**Taxonomy metadata:** family `14` Lean & Continuous Improvement; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Assess flow efficiency from one coherent process and time basis.

## Triggers
- Value-adding time, elapsed lead time, process boundary, and units are supplied.

## Non-Triggers
- Claiming takt, changing flow, or authorizing improvement.

## Required Inputs
- Process boundary, value-adding time, elapsed time, population, and period.

## Optional Inputs
- Queue, transport, rework, batch, and product mix evidence.

## Assumptions
- Value-adding classification is supplied and reviewable.

## Core Workflow
1. Validate time definitions and population.
2. Calculate flow-efficiency measure with intermediates.
3. Return comparability gaps and owner questions.

## Calculations
`flow efficiency = value-adding time / elapsed lead time`; preserve units and denominator.

## Validation
- Check time basis, boundary, overlap, population, and zero denominator.

## Exception Handling
- Missing elapsed time returns `NEEDS_INPUT`.
- Takt or intervention request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/flow-efficiency-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, times, formula, result, assumptions, gaps, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not authorize flow changes or substitute for takt analysis.

## References
- `references/flow-efficiency-checklist.md`

## Examples
Queue time belongs in elapsed lead time when the declared boundary includes it.

## Testing
Cover correct invocation, zero denominator, time mismatch, expected output structure, and intervention refusal. Expected routing is not observed behavior.
