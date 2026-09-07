---
name: analyze-production-event-history
description: Reconstruct a production-event chronology from supplied exports while preserving timestamp, identity, and missing-event uncertainty.
license: PENDING_PROJECT_GOVERNANCE
---

# Analyze Production Event History

**Taxonomy metadata:** family `15` Manufacturing Systems & Data; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Analyze the order and timing of exported production events for gaps, duplicates, and conflicts.

## Triggers
- Event rows, asset or order identities, event definitions, and timestamp conventions are supplied.

## Non-Triggers
- Rewriting history, inferring unrecorded work, dispatching production, or changing machine controls.

## Required Inputs
- Event identifiers, event types, timestamps, timezone basis, asset/order identity, and requested period.

## Optional Inputs
- Source revision, sequence rules, downtime codes, operator notes, and known clock offsets.

## Assumptions
- Chronology is limited to supplied records and cannot prove physical occurrence.

## Core Workflow
1. Normalize timestamps only where the source basis is explicit.
2. Order events by identity and time, retaining duplicates and conflicts.
3. Report gaps, overlaps, and evidence needed for interpretation.

## Calculations
Elapsed intervals use supplied timestamps and timezone rules; uncertain conversions remain unresolved.

## Validation
- Check event identity, time zone, ordering, duplicate IDs, missing starts or ends, and period scope.

## Exception Handling
- Conflicting timezone rules return `NEEDS_INPUT`.
- A request to repair or delete event history returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/production-event-history-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, chronology, normalization basis, anomalies, evidence gaps, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not direct production or alter event records.

## References
- `references/production-event-history-checklist.md`

## Examples
Events from two timezones stay marked as uncertain when no authoritative conversion basis is supplied.

## Testing
Cover correct invocation, timezone conflict, duplicate event, expected output structure, and history-repair refusal. Expected routing is not observed behavior.
