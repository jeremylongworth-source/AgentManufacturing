---
name: map-mes-machine-data-flow
description: Map supplied machine-event signals into MES information flows while keeping PLC and SCADA control channels out of scope.
license: PENDING_PROJECT_GOVERNANCE
---

# Map MES Machine Data Flow

**Taxonomy metadata:** family `15` Manufacturing Systems & Data; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Describe how read-only machine events, timestamps, and identities are collected and consumed by MES.

## Triggers
- Read-only architecture records, signal definitions, asset identities, and MES consumers are supplied.

## Non-Triggers
- Programming PLCs, changing SCADA tags, commanding machines, or approving controls.

## Required Inputs
- Asset and signal identities, source system, event meaning, timestamp basis, and destination consumer.

## Optional Inputs
- Gateway details, buffering, quality flags, sample payloads, and network zones.

## Assumptions
- A signal list is not proof that a signal is live, unique, or safe to use.

## Core Workflow
1. Bound the read-only signal and consumer path.
2. Reconcile signal names, asset identities, units, and timestamps.
3. Return ambiguity, missing lineage, and qualified owner questions.

## Calculations
No control value is calculated; event counts preserve the supplied time and asset scope.

## Validation
- Check signal uniqueness, source identity, units, timestamp basis, quality status, and consumer.

## Exception Handling
- Ambiguous signal ownership returns `NEEDS_INPUT`.
- A control-channel request returns `SAFETY_ESCALATION` and `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/mes-machine-data-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, read-only flow map, signal lineage, identity and time basis, gaps, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Never program, bypass, or command PLC/SCADA or machinery.

## References
- `references/mes-machine-data-checklist.md`

## Examples
If one signal name is reused by two assets, report the ambiguity instead of selecting an asset.

## Testing
Cover correct invocation, duplicate signal, timestamp mismatch, expected output structure, and PLC/SCADA control refusal. Expected routing is not observed behavior.
