---
name: map-manufacturing-traceability-data
description: Map manufacturing traceability schemas and lineage from supplied identifiers without claiming an executed product genealogy.
license: MIT
---

# Map Manufacturing Traceability Data

**Taxonomy metadata:** family `15` Manufacturing Systems & Data; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Describe how lot, serial, order, material, process, and disposition identifiers could link across supplied systems.

## Triggers
- System schemas, identifier examples, event ownership, and integration mappings are supplied.

## Non-Triggers
- Querying a live genealogy, directing custody, releasing product, or asserting a successful lot trace.

## Required Inputs
- Identifier definitions, source systems, event types, ownership, and relationship rules.

## Optional Inputs
- Sample records, revision history, retention rules, exception paths, and downstream consumers.

## Assumptions
- A lineage map is architecture evidence and is not an executed trace for any lot.

## Core Workflow
1. Set product, lot, order, and event boundaries.
2. Map identifiers and relationship edges across systems.
3. Flag missing links, conflicting keys, ownership gaps, and evidence needed for trace execution.

## Calculations
No genealogy result is calculated; edge counts preserve the supplied sample and scope.

## Validation
- Check identifier uniqueness, relationship direction, revision, event ownership, and source completeness.

## Exception Handling
- Conflicting lot identifiers return `NEEDS_INPUT`.
- A request to direct material custody or release returns `SAFETY_ESCALATION` and `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/traceability-data-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, lineage map, identifier mapping, missing edges, assumptions, and qualified handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not claim custody, release, or a completed genealogy without executed evidence.

## References
- `references/traceability-data-checklist.md`

## Examples
Two systems with different lot identifiers produce a mapping requirement, not a claimed successful trace.

## Testing
Cover correct invocation, identifier mismatch, missing event owner, expected output structure, and release/custody refusal. Expected routing is not observed behavior.
