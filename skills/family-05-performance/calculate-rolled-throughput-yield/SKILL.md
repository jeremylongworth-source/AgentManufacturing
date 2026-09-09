---
name: calculate-rolled-throughput-yield
description: Calculate rolled throughput yield from sequential first-pass yields while preserving routing applicability and dependence assumptions.
license: MIT
---

# Calculate Rolled Throughput Yield

## Overview

Combine supplied sequential first-pass yields for one routing into a rolled yield estimate. Keep operation order, applicability, rework definition, and dependence assumptions visible; reject a parallel routing interpreted as sequential.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `calculate-first-pass-yield`, `CALC`. Audit distinction: combine sequential first-pass yields; this is distinct from a single-operation yield.

## Triggers

- First-pass yields by sequential operation, routing applicability, and rework/dependence assumptions are supplied.

## Non-Triggers

- Single-operation yield, quality release, root cause, or a new process routing.

## Required Inputs

- First-pass yields for each sequential operation.
- Routing order, applicability, and rework/dependence assumptions.

## Optional Inputs

- Lot/period, numerator/denominator, parallel branches, and source owner.

## Assumptions

- Multiplication is appropriate only for sequential operations with a stated basis.
- Parallel alternatives are not multiplied as sequential steps.

## Core Workflow

1. Verify operation order, yield definitions, population, period, and routing.
2. Multiply sequential yields with intermediates and disclose dependence assumptions.
3. Return estimate, gaps, and quality handoff.

## Calculations

Use `rolled yield = yield_1 × yield_2 × ... × yield_n` for applicable sequential first-pass yields. Preserve each input, intermediate product, units, and rounding. Reject incompatible or parallel routing.

## Validation

- Check each yield is in a valid proportion range and shares the population basis.
- Verify routing is sequential and applicable to the same product/period.
- Do not claim final quality acceptance.

## Exception Handling

- Missing yield or routing returns `NEEDS_INPUT`.
- Parallel/sequential conflict returns `SOURCE_REVIEW_REQUIRED`.
- Release or certification requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/rolled-yield-formula.md` and AM-08 rules.
- Record operation sources, period, routing revision, and owner.

## Output Contract

Return `status`, routing scope, input yields, formula, intermediates, rolled result, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. No product release, process change, or quality certification is issued.

## References

- `references/rolled-yield-formula.md`

## Examples

Read the formula reference for parallel alternatives incorrectly supplied as sequential steps.

## Testing

Cover calculation correctness, invalid proportions, parallel-routing rejection, missing yield, expected output structure, and release refusal. Expected routing is not observed behavior.
