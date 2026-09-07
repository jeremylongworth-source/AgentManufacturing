---
name: review-ergonomic-risk
description: Assess task-level ergonomic exposure concerns and evidence gaps without diagnosing health conditions or prescribing work changes.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Ergonomic Risk

**Taxonomy metadata:** family `11` Manufacturing Safety; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure task exposure observations for qualified ergonomic and occupational review.

## Triggers
- Task, posture, force, repetition, duration, and observation evidence are supplied.

## Non-Triggers
- Diagnosing a worker, prescribing treatment, or authorizing redesign.

## Required Inputs
- Task identity, exposure dimensions, observation period, and affected role.

## Optional Inputs
- Load, reach, vibration, recovery, worker feedback, and prior assessments.

## Assumptions
- Screening observations are not a medical or ergonomic certification.

## Core Workflow
1. Capture task and exposure dimensions.
2. Identify missing measurements and context.
3. Return qualified review questions and owner handoff.

## Calculations
Use only supplied exposure arithmetic and units; do not create safe limits.

## Validation
- Check task, duration, force, posture, repetition, and population.

## Exception Handling
- Missing exposure basis returns `NEEDS_INPUT`.
- Health diagnosis or immediate work-direction request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/ergonomic-risk-checklist.md`.

## Output Contract
Return `status`, task exposure, evidence, gaps, assumptions, and qualified handoff.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Do not diagnose, prescribe treatment, or direct unsafe work changes.

## References
- `references/ergonomic-risk-checklist.md`

## Examples
Repetition concern can be escalated without declaring an occupational diagnosis.

## Testing
Cover correct invocation, missing exposure, unit mismatch, expected output structure, and diagnosis refusal. Expected routing is not observed behavior.
