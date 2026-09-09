---
name: identify-out-of-calibration-risk
description: Screen measurement history for possible exposure to out-of-calibration equipment without deciding product disposition.
license: MIT
---

# Identify Out-of-Calibration Risk

**Taxonomy metadata:** family `07` Metrology & Measurement Systems; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Bound a retrospective risk screen when calibration status may have lapsed.

## Triggers
- Instrument identity, status evidence, and a use window are supplied.

## Non-Triggers
- Declaring product nonconforming, accepting risk, or changing calibration intervals.

## Required Inputs
- Instrument identity, calibration evidence, use history, and affected measurements.

## Optional Inputs
- Previous results, uncertainty, lot genealogy, and containment actions.

## Assumptions
- Incomplete use history leaves exposure unknown.

## Core Workflow
1. Establish the status boundary and last known valid evidence.
2. Map use events to the uncertain interval.
3. Return exposure scope, evidence gaps, and qualified owner handoffs.

## Calculations
Count only traceable use events; do not infer an exposure rate from missing records.

## Validation
- Check identity, dates, interval basis, and affected records.

## Exception Handling
- Missing history returns `NEEDS_INPUT` or `UNKNOWN_EXPOSURE`.
- Disposition requests return `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/out-of-calibration-risk-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, instrument, known-valid boundary, use-window map, exposure scope, gaps, assumptions, and owner handoff.

## Safety Requirements
AM-05 class: `REGULATED`. Do not certify, release, recall, or disposition product.

## References
- `references/out-of-calibration-risk-checklist.md`

## Examples
An incomplete use history must remain an unknown exposure rather than a cleared interval.

## Testing
Cover correct invocation, missing history, stale status, expected output structure, and disposition refusal. Expected routing is not observed behavior.
