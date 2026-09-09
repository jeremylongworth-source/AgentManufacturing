---
name: build-predictive-maintenance-plan
description: Define condition-monitoring signals, thresholds, and review ownership from failure modes without autonomous intervention.
license: MIT
---

# Build Predictive Maintenance Plan

**Taxonomy metadata:** family `10` Maintenance & Reliability; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure monitoring objectives and review triggers from supplied failure modes and evidence.

## Triggers
- Failure modes, measurable indicators, thresholds, sampling basis, and review owner are supplied.

## Non-Triggers
- Autonomous alarm action, process adjustment, or maintenance authorization.

## Required Inputs
- Asset, failure mode, indicator, threshold basis, sampling, and owner.

## Optional Inputs
- Sensor limitations, baseline, environment, model validation, and escalation path.

## Assumptions
- A threshold proposal requires qualified validation before use.

## Core Workflow
1. Map failure modes to measurable indicators.
2. Declare threshold, sampling, data-quality, and owner basis.
3. Return validation gaps and escalation handoff.

## Calculations
Preserve supplied threshold or trend calculations and units; do not infer alarm limits.

## Validation
- Check indicator relevance, baseline, sampling, sensor limits, and sector rules.

## Exception Handling
- Missing threshold basis returns `NEEDS_INPUT`.
- Autonomous intervention request returns `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/predictive-maintenance-plan-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, asset/mode map, indicators, thresholds, sampling, owner, gaps, and validation handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not authorize autonomous intervention or maintenance.

## References
- `references/predictive-maintenance-plan-checklist.md`

## Examples
A vibration threshold is a review proposal until baseline and sensor suitability are validated.

## Testing
Cover correct invocation, missing threshold basis, sector gap, expected output structure, and autonomous-action refusal. Expected routing is not observed behavior.
