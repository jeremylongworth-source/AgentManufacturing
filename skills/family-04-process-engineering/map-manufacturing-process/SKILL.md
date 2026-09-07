---
name: map-manufacturing-process
description: Map supplied manufacturing operations, branches, inputs, outputs, and rework loops into a bounded process flow.
license: PENDING_PROJECT_GOVERNANCE
---

# Map Manufacturing Process

## Overview

Create a process map with a defined start, end, decision points, branches, and rework loops from supplied operation descriptions. Keep the map descriptive and evidence-based; do not infer a process capability or value-stream metric.

**Taxonomy metadata:** family `04` Process and Industrial Engineering; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Audit distinction: map sequence, branches, and rework loops; value-stream metrics belong elsewhere.

## Triggers

- The user supplies operation descriptions, flow sequence, inputs, outputs, and rework loops and asks for a process map.

## Non-Triggers

- Routing activation, process validation, control-limit design, value-stream time study, or machine operating instructions.

## Required Inputs

- Operation descriptions and start/end boundary.
- Flow sequence, branches, inputs, outputs, and rework loops.

## Optional Inputs

- Inspection points, WIP locations, ownership, revision, and source diagrams.

## Assumptions

- An absent branch or loop remains unknown; a linear map must not erase supplied rework.
- The map reflects supplied evidence, not a verified shop-floor observation.

## Core Workflow

1. Confirm boundary, operation identity, sequence, branch criteria, and loop return points.
2. Draw the map with evidence labels and unresolved transitions.
3. Return the map, gaps, assumptions, and review owner.

## Calculations

No calculation required.

## Validation

- Check every operation has a predecessor/successor within the stated boundary.
- Verify rework loops return to the supplied operation and decisions retain criteria.
- Do not infer time, capacity, or compliance.

## Exception Handling

- Missing boundary or sequence returns `NEEDS_INPUT`.
- Conflicting flow descriptions return `SOURCE_REVIEW_REQUIRED`.
- Requests for system activation or operating instructions return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/process-map-checklist.md` and supplied process records.
- Record source, revision, date, and owner; do not reproduce protected diagrams beyond permitted use.

## Output Contract

Return `status`, boundary, map, evidence, branch/loop notes, gaps, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`; escalate any supplied hazardous or engineering operation instead of adding instructions.

## References

- `references/process-map-checklist.md`

## Examples

Read the checklist for a process containing a rework loop.

## Testing

Cover correct invocation, missing boundary, rework-loop preservation, conflicting flow, expected output structure, and activation refusal. Expected routing is not observed behavior.
