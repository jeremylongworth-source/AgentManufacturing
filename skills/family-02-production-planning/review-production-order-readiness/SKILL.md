---
name: review-production-order-readiness
description: Review whether an existing production order has routing, material, tooling, approval, and capacity evidence without releasing it.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Production Order Readiness

## Overview

Create a readiness gap list for an existing production order. Check routing revision, material/tooling readiness, required approvals, and capacity evidence; do not release or alter the order.

**Taxonomy metadata:** family `02` Production Planning & Scheduling; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `REVIEW`. Audit distinction: check evidence for an existing order; plan feasibility is not release authority.

## Triggers

- An order, routing/revision, material and tooling evidence, approvals, and capacity evidence are supplied for readiness review.

## Non-Triggers

- Order release, procurement, schedule change, production execution, or certification.

## Required Inputs

- Order routing and revision.
- Material/tooling readiness.
- Required approvals and capacity evidence.

## Optional Inputs

- Quality plan, work instruction, operator qualification, due date, supplier status, and exception log.

## Assumptions

- Ready material does not compensate for missing routing approval or capacity evidence.
- A readiness gap is not a release prohibition unless the responsible process says so; the skill reports evidence.

## Core Workflow

1. Confirm order identity, revision, horizon, and required readiness gates.
2. Map evidence to routing, material, tooling, approval, capacity, quality, and qualification checks.
3. Return ready/not-ready evidence gaps and the responsible owner without releasing the order.

## Calculations

No calculation required; preserve supplied capacity and quantity evidence.

## Validation

- Check revision alignment, evidence date, owner, approval status, and capacity basis.
- Keep missing evidence distinct from a negative finding.

## Exception Handling

- Missing routing or approval returns `NEEDS_INPUT`.
- Conflicting revisions return `SOURCE_REVIEW_REQUIRED`.
- Release or system-write requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/order-readiness-checklist.md` and supplied controlled records.
- Record revision, effective date, source, and owner.

## Output Contract

Return `status`, order scope, evidence matrix, readiness gaps, unknowns, assumptions, validation notes, owner, and release boundary. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`; escalate safety or engineering evidence gaps. Do not release, certify, or authorize production.

## References

- `references/order-readiness-checklist.md`

## Examples

Read the checklist for ready material with missing routing approval.

## Testing

Cover correct invocation, missing approval, conflicting revision, incomplete capacity, expected output structure, and order-release refusal. Expected routing is not observed behavior.
