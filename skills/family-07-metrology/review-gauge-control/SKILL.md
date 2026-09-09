---
name: review-gauge-control
description: Review whether gauge identification, status, storage, and use controls are evidenced without approving the gauge.
license: MIT
---

# Review Gauge Control

**Taxonomy metadata:** family `07` Metrology & Measurement Systems; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Screen gauge-control records for identity, status, protection, and ownership gaps.

## Triggers
- A gauge list, labels, status records, and use controls are supplied.

## Non-Triggers
- Calibrating, releasing, or approving a gauge for production.

## Required Inputs
- Gauge identity, location, status, calibration evidence, and control procedure.

## Optional Inputs
- Storage, damage checks, software lockout, and user training records.

## Assumptions
- A calibrated result without identity/status control is not controlled use evidence.

## Core Workflow
1. Reconcile physical identity with records.
2. Check status visibility, protection, and overdue handling.
3. Return gaps and qualified ownership.

## Calculations
No calculation; count reconciled and unreconciled records only.

## Validation
- Check unique identity, current status, location, and escalation path.

## Exception Handling
- Missing identity or status returns `NEEDS_INPUT`.
- Approval requests return `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/gauge-control-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, gauge population, identity/status findings, evidence gaps, assumptions, and handoff.

## Safety Requirements
AM-05 class: `REGULATED`. Do not authorize measurement or certify control effectiveness.

## References
- `references/gauge-control-checklist.md`

## Examples
A calibrated gauge with no identity or status control remains an uncontrolled-use gap.

## Testing
Cover correct invocation, missing identity, stale status, expected output structure, and approval refusal. Expected routing is not observed behavior.
