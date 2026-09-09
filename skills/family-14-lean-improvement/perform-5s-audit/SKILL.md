---
name: perform-5s-audit
description: Evaluate supplied 5S organization criteria and observations without treating a score as safety clearance or process proof.
license: MIT
---

# Perform 5S Audit

**Taxonomy metadata:** family `14` Lean & Continuous Improvement; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Review area observations against a declared 5S checklist and retain exceptions.

## Triggers
- Area, checklist revision, observations, score fields, and audit date are supplied.

## Non-Triggers
- Declaring safety, disciplining workers, or authorizing housekeeping work.

## Required Inputs
- Area, criteria, observations, date, auditor, and evidence.

## Optional Inputs
- Photos, recurrence, owner, and action tracking.

## Assumptions
- A 5S score is not a substitute for hazard review.

## Core Workflow
1. Reconcile criteria and observations.
2. Record pass, gap, and unknown items with evidence.
3. Return owner questions and safety escalation where needed.

## Calculations
Preserve supplied score scale; do not invent weights or thresholds.

## Validation
- Check checklist revision, area, date, evidence, and score basis.

## Exception Handling
- Missing criteria returns `NEEDS_INPUT`.
- Hazard clearance or immediate-work request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/5s-audit-checklist.md`.

## Output Contract
Return `status`, criteria, observations, score basis, exceptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not use 5S scoring as safety clearance.

## References
- `references/5s-audit-checklist.md`

## Examples
A blocked egress remains a safety escalation even when the 5S score is high.

## Testing
Cover correct invocation, missing criteria, safety exception, expected output structure, and clearance refusal. Expected routing is not observed behavior.
