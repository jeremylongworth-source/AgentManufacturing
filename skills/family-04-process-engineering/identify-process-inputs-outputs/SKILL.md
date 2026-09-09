---
name: identify-process-inputs-outputs
description: Inventory process-boundary material, energy, and information streams with units and unverified streams made explicit.
license: MIT
---

# Identify Process Inputs and Outputs

## Overview

Create an input/output inventory for one stated process boundary from supplied material, energy, information, and transformation evidence. Mark streams without a measurement basis instead of inventing a balance.

**Taxonomy metadata:** family `04` Process and Industrial Engineering; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Audit distinction: define boundary-crossing streams; it does not reconstruct the entire process flow.

## Triggers

- A process boundary and material, energy, information, and transformation evidence are supplied.

## Non-Triggers

- Mass/energy balance certification, environmental compliance, process mapping, or operating instructions.

## Required Inputs

- Process boundary and transformation description.
- Known material, energy, and information streams with units where available.

## Optional Inputs

- Measurement method, source date, loss/rework streams, ownership, and environmental overlay.

## Assumptions

- An unmeasured stream remains unquantified.
- A listed input/output is evidence to review, not proof of conservation or compliance.

## Core Workflow

1. Confirm boundary, stream identity, direction, unit, and source.
2. Build the inventory and mark unverified or unquantified streams.
3. Return gaps, assumptions, and owner handoff.

## Calculations

No calculation required. Do not invent a mass, energy, or information balance.

## Validation

- Check stream direction, units, period, measurement basis, and boundary membership.
- Distinguish observed, supplied, inferred, and unverified streams.

## Exception Handling

- Missing boundary returns `NEEDS_INPUT`.
- Contradictory stream definitions return `SOURCE_REVIEW_REQUIRED`.
- Compliance or certification requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/process-stream-inventory.md` and supplied records.
- Record measurement source, period, units, and owner; cite external requirements only when requested.

## Output Contract

Return `status`, boundary, stream inventory, units, evidence quality, unverified streams, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`; escalate hazardous materials or energy context to the qualified owner.

## References

- `references/process-stream-inventory.md`

## Examples

Read the reference for an unquantified energy stream.

## Testing

Cover correct invocation, missing boundary, unmeasured stream, unit conflict, expected output structure, and compliance-claim refusal. Expected routing is not observed behavior.
