---
name: compare-production-lot-sizes
description: Compare candidate production lot sizes using supplied demand, setup constraints, holding and processing cost bases, and capacity evidence.
license: PENDING_PROJECT_GOVERNANCE
---

# Compare Production Lot Sizes

## Overview

Create a bounded lot-size comparison showing setup, inventory, processing, capacity, and demand consequences for supplied alternatives. Preserve unavailable costs and capacity violations; do not choose or release a lot size.

**Taxonomy metadata:** family `02` Production Planning & Scheduling; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: compare bounded lot alternatives using supplied economics; this is not procurement EOQ or autonomous scheduling.

## Triggers

- Candidate lot sizes, demand, setup constraints, holding/processing cost bases, and capacity evidence are supplied.

## Non-Triggers

- Procurement EOQ, inventory-policy approval, customer commitment, or autonomous schedule selection.

## Required Inputs

- Candidate lot sizes and demand horizon.
- Setup constraints and supplied holding/processing cost bases.
- Capacity evidence relevant to each lot.

## Optional Inputs

- Yield, scrap, WIP, lead time, changeover, service-level, and sensitivity assumptions.

## Assumptions

- Costs are comparable only when definitions, period, and currency basis align.
- A lot exceeding usable capacity remains infeasible even if its setup cost is lower.

## Core Workflow

1. Normalize lot, demand, capacity, setup, inventory, and cost definitions.
2. Compare each candidate with transparent arithmetic and feasibility flags.
3. Return tradeoffs, missing evidence, and owner decision handoff.

## Calculations

Use only supplied cost and quantity components; preserve setup, processing, holding, and capacity intermediates. Do not infer EOQ, demand variability, or a cost not supplied.

## Validation

- Check lot units, horizon, capacity, cost definitions, and currency/period.
- Flag capacity violations and noncomparable economics.
- Do not rank an infeasible option as achievable.

## Exception Handling

- Missing cost or capacity basis returns `NEEDS_INPUT`.
- Contradictory demand or setup evidence returns `PARTIAL`.
- Approval or autonomous selection returns `OUT_OF_SCOPE`.

## Source Usage

- Use `references/lot-size-comparison-checklist.md` and supplied planning records.
- Record source, effective period, cost owner, and assumptions.

## Output Contract

Return `status`, common basis, candidate table, calculations, feasibility/capacity consequences, assumptions, validation notes, and decision handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, and `OUT_OF_SCOPE`.

## Safety Requirements

AM-05 class: `ROUTINE`. No inventory policy, procurement, schedule, or customer commitment is approved.

## References

- `references/lot-size-comparison-checklist.md`

## Examples

Read the checklist for a larger lot that exceeds usable capacity.

## Testing

Cover correct invocation, capacity violation, missing cost basis, unit mismatch, expected output structure, and autonomous-selection refusal. Expected routing is not observed behavior.
