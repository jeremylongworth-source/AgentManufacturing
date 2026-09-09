---
name: compare-production-scenarios
description: Compare supplied production-plan alternatives under common demand, feasibility, cost, and resource assumptions.
license: MIT
---

# Compare Production Scenarios

## Overview

Produce a comparable tradeoff table for supplied production alternatives. Normalize shared assumptions, reject or flag infeasible options, and preserve unknown costs or capacity; do not generate or authorize a scenario.

**Taxonomy metadata:** family `02` Production Planning & Scheduling; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: compare supplied alternatives under a common basis; scenario generation and approval are separate.

## Triggers

- Two or more production alternatives and common demand, feasibility, and cost criteria are supplied.

## Non-Triggers

- Building all alternatives, approving a plan, committing overtime/capital, or hiding incomparable assumptions.

## Required Inputs

- Alternative plans and common demand assumptions.
- Feasibility constraints and cost criteria.

## Optional Inputs

- Risk, lead time, changeover, inventory, labor, quality, and sensitivity assumptions.

## Assumptions

- Alternatives are comparable only when scope, horizon, units, demand, and cost basis align.
- Missing cost or feasibility evidence remains unknown, not zero.

## Core Workflow

1. Normalize the common basis and identify scenario-specific assumptions.
2. Check feasibility, calculate transparent supplied comparisons, and mark rejected options.
3. Return tradeoffs, sensitivity, gaps, and decision-owner handoff.

## Calculations

Use only supplied arithmetic and declared cost/time bases. Preserve intermediate values, units, rounding, and noncomparable assumptions.

## Validation

- Check common demand, horizon, capacity, labor, material, and cost definitions.
- Reject or clearly flag an infeasible alternative; do not rank it as achievable.

## Exception Handling

- Missing common assumptions returns `NEEDS_INPUT`.
- Incomparable overtime or cost treatment returns `PARTIAL`/`NEEDS_INPUT`.
- Approval or commitment requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/scenario-comparison-checklist.md` and supplied plan records.
- Record source, period, assumptions, and owner; do not infer costs or capacity.

## Output Contract

Return `status`, common basis, scenario table, feasibility flags, calculations, tradeoffs, assumptions, validation notes, and decision handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, and `OUT_OF_SCOPE`.

## Safety Requirements

AM-05 class: `ROUTINE`. No scenario is approved, released, or represented as a customer commitment.

## References

- `references/scenario-comparison-checklist.md`

## Examples

Read the checklist for scenarios with inconsistent overtime assumptions.

## Testing

Cover correct invocation, incomparable assumptions, infeasible alternative, missing cost, expected output structure, and approval refusal. Expected routing is not observed behavior.
