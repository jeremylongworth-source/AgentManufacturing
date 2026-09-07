---
name: build-preventive-maintenance-plan
description: Structure a preventive-maintenance plan from approved evidence without providing equipment-specific repair or isolation directions.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Preventive Maintenance Plan

**Taxonomy metadata:** family `10` Maintenance & Reliability; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Assemble assets, tasks, intervals, evidence, owners, and approval gaps for qualified review.

## Triggers
- Asset context, approved maintenance basis, task candidates, and interval evidence are supplied.

## Non-Triggers
- Giving repair steps, isolation instructions, or authorizing maintenance execution.

## Required Inputs
- Asset identity, task basis, interval basis, operating context, and qualified owner.

## Optional Inputs
- Failure history, manufacturer evidence, criticality, permits, and spare dependencies.

## Assumptions
- An interval proposal is not an approved work instruction.

## Core Workflow
1. Map tasks to assets and approved evidence.
2. Check intervals, criticality, access, and owner approvals.
3. Return a reviewable plan with hazards and unresolved authority.

## Calculations
Preserve supplied interval arithmetic and units; do not infer safe intervals.

## Validation
- Check asset identity, evidence revision, interval basis, hazards, and jurisdiction.

## Exception Handling
- Missing basis returns `NEEDS_INPUT`.
- Repair, isolation, or execution request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/preventive-maintenance-plan-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, asset/task map, interval basis, owner, evidence, hazards, gaps, and qualified handoff.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Do not instruct, authorize, or sequence live maintenance or energy isolation.

## References
- `references/preventive-maintenance-plan-checklist.md`

## Examples
An OEM interval can be recorded as evidence without becoming an executable instruction.

## Testing
Cover correct invocation, missing interval basis, jurisdiction gap, expected output structure, and isolation refusal. Expected routing is not observed behavior.
