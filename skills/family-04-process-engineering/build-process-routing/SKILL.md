---
name: build-process-routing
description: Draft product routing from approved operations, work centers, precedence constraints, and revision evidence without activating a system record.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Process Routing

## Overview

Draft a product-specific routing for engineering review from authorized operations and work-center evidence. Keep unresolved assignments and revision gaps visible; do not activate an ERP/MES routing.

**Taxonomy metadata:** family `04` Process and Industrial Engineering; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `map-manufacturing-process`, `REVIEW`. Audit distinction: assign approved operations to work centers; a descriptive process map is not a routing.

## Triggers

- Approved operations, work centers, sequence, precedence constraints, and a revision basis are supplied.

## Non-Triggers

- Inventing an operation or work center, activating a system record, certifying a routing, or issuing machine instructions.

## Required Inputs

- Approved operation list and revision basis.
- Work centers, sequence, and precedence constraints.

## Optional Inputs

- Standard times, tooling, quality gates, sector overlay, and engineering owner.

## Assumptions

- An operation without an approved work center remains unresolved.
- A draft routing is not an effective revision or production authorization.

## Core Workflow

1. Verify operation approval, revision, work-center identity, and precedence.
2. Assemble the draft routing and flag gaps, conflicts, and sector-dependent evidence.
3. Return an engineering-review package without system activation.

## Calculations

No calculation required; preserve supplied times and units.

## Validation

- Check every operation maps to an approved work center or an explicit gap.
- Verify revision, precedence, tooling, and quality evidence.
- Ensure no live system or certification claim appears.

## Exception Handling

- Missing approval or work center returns `NEEDS_INPUT`.
- Sector or engineering applicability returns `ENGINEERING_REVIEW_REQUIRED`.
- Activation or release requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/process-routing-review.md` and the process map where supplied.
- Record revision, source, owner, and sector/standards dependencies.

## Output Contract

Return `status`, product scope, revision, routing draft, unresolved assignments, constraints, assumptions, validation notes, and engineering handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not activate routing, certify design, issue machine steps, or approve production release; qualified engineering review is required.

## References

- `references/process-routing-review.md`

## Examples

Read the checklist for an operation with no approved work center.

## Testing

Cover correct invocation, missing work center, revision conflict, sector-dependent review, expected output structure, and system-activation refusal. Expected routing is not observed behavior.
