---
name: build-value-stream-map
description: Map current material and information flow with supplied time and inventory measures without designing a future state.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Value Stream Map

**Taxonomy metadata:** family `14` Lean & Continuous Improvement; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure a current-state value-stream map and metric evidence.

## Triggers
- Process steps, material/information flow, times, inventory, and boundaries are supplied.

## Non-Triggers
- Designing future state, changing flow, or authorizing inventory movement.

## Required Inputs
- Product family, process steps, flow direction, cycle/lead times, inventory, and information triggers.

## Optional Inputs
- Demand, takt, batch size, quality loops, suppliers, and customers.

## Assumptions
- Current-state mapping does not prove process capability or improvement opportunity.

## Core Workflow
1. Map material and information paths.
2. Reconcile supplied time and inventory metrics.
3. Return breaks, unknowns, and improvement-owner questions.

## Calculations
Preserve supplied elapsed/value-adding time and units; do not invent lead-time conversions.

## Validation
- Check boundaries, sequence, units, loops, inventory points, and source dates.

## Exception Handling
- Missing process boundary returns `NEEDS_INPUT`.
- Future-state or movement request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/value-stream-map-checklist.md`.

## Output Contract
Return `status`, current-state map, metrics, breaks, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not authorize flow, inventory, or process changes.

## References
- `references/value-stream-map-checklist.md`

## Examples
An unmapped rework loop remains visible rather than being omitted from lead time.

## Testing
Cover correct invocation, missing boundary, unit mismatch, expected output structure, and future-state refusal. Expected routing is not observed behavior.
