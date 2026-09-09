---
name: identify-hazardous-energy-source
description: Inventory potential hazardous energy sources and unknowns without issuing lockout steps or isolation instructions.
license: MIT
---

# Identify Hazardous Energy Source

**Taxonomy metadata:** family `11` Manufacturing Safety; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Map possible energy sources, interfaces, stored energy, and evidence gaps for qualified review.

## Triggers
- Equipment, task, energy observations, and affected boundary are supplied.

## Non-Triggers
- Writing lockout/tagout steps, selecting devices, or authorizing isolation.

## Required Inputs
- Equipment/task identity, energy types, interfaces, stored-energy observations, and boundary.

## Optional Inputs
- Drawings, permits, prior procedures, inspection evidence, and jurisdiction.

## Assumptions
- An inventory is not a verified zero-energy state.

## Core Workflow
1. Enumerate known, suspected, and unknown energy sources.
2. Map source-to-boundary relationships.
3. Escalate verification and qualified isolation review needs.

## Calculations
Preserve supplied pressure, voltage, temperature, mass, or motion values and units; do not calculate safe release steps.

## Validation
- Check source type, boundary, stored energy, drawings, and owner.

## Exception Handling
- Missing equipment or boundary returns `NEEDS_INPUT`.
- Isolation instruction request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/hazardous-energy-inventory-checklist.md`.

## Output Contract
Return `status`, equipment/task boundary, energy inventory, unknowns, evidence, escalation owner, and no-isolation note.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Never provide unsafe energy-control shortcuts or claim zero energy.

## References
- `references/hazardous-energy-inventory-checklist.md`

## Examples
Residual pneumatic pressure is recorded as a suspected source requiring qualified verification.

## Testing
Cover correct invocation, missing boundary, stored-energy uncertainty, expected output structure, and lockout-step refusal. Expected routing is not observed behavior.
