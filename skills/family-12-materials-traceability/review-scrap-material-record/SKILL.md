---
name: review-scrap-material-record
description: Review scrap material event integrity, quantities, reasons, and approvals without calculating disposal or authorizing disposition.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Scrap Material Record

**Taxonomy metadata:** family `12` Materials, BOM & Traceability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Screen scrap records for identity, quantity, reason, linkage, and approval evidence.

## Triggers
- Scrap event, material/lot identity, quantity, reason, record revision, and approval evidence are supplied.

## Non-Triggers
- Calculating financial loss, moving or disposing material, or approving disposition.

## Required Inputs
- Material/lot, quantity, unit, event time, reason, source, and approver/status.

## Optional Inputs
- Product linkage, rework, recovery, photos, and environmental classification.

## Assumptions
- A recorded scrap event is not proof that disposition was authorized.

## Core Workflow
1. Reconcile event identity, quantity, unit, reason, and linkage.
2. Check status, approvals, and duplicate/void records.
3. Return integrity findings and owner handoff.

## Calculations
No calculation unless supplied quantity arithmetic is reconciled; preserve units.

## Validation
- Check identity, quantity, reason, revision, approval, and status.

## Exception Handling
- Missing reason or approval returns `NEEDS_INPUT`.
- Disposal or disposition request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/scrap-material-record-checklist.md`.

## Output Contract
Return `status`, event fields, evidence, conflicts, approvals, gaps, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not dispose, move, or authorize material disposition.

## References
- `references/scrap-material-record-checklist.md`

## Examples
An approved-looking reason without an authorized status remains an open record gap.

## Testing
Cover correct invocation, missing approval, unit mismatch, expected output structure, and disposition refusal. Expected routing is not observed behavior.
