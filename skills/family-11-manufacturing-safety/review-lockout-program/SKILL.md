---
name: review-lockout-program
description: Review lockout-program evidence, roles, training, and verification records without generating equipment-specific isolation procedures.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Lockout Program

**Taxonomy metadata:** family `11` Manufacturing Safety; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P0`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Screen program-level lockout evidence and escalation gaps.

## Triggers
- Program, roles, training, energy-control records, audits, and jurisdiction are supplied.

## Non-Triggers
- Writing an equipment procedure, authorizing isolation, or directing restart.

## Required Inputs
- Program scope, roles, training, verification, records, and applicable jurisdiction.

## Optional Inputs
- Periodic inspection, contractor controls, device control, and incident history.

## Assumptions
- Program evidence does not prove a specific machine is safe to service.

## Core Workflow
1. Map requirements to supplied program evidence.
2. Identify missing roles, training, verification, and records.
3. Return qualified review and escalation needs.

## Calculations
No calculation; counts of records retain scope and period.

## Validation
- Check program scope, jurisdiction, role evidence, training, verification, and revision.

## Exception Handling
- Missing scope or jurisdiction returns `NEEDS_INPUT`.
- Isolation/restart request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/lockout-program-review-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, scope, evidence matrix, gaps, jurisdiction, escalation owner, and boundary note.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Do not create shortcuts, authorize lockout, or direct restart.

## References
- `references/lockout-program-review-checklist.md`

## Examples
A current training roster does not prove machine-specific energy verification.

## Testing
Cover correct invocation, missing jurisdiction, absent verification, expected output structure, and isolation refusal. Expected routing is not observed behavior.
