---
name: triage-manufacturing-incident
description: Organize immediate manufacturing-incident facts and escalation while avoiding rescue, legal-reporting, or investigation determinations.
license: PENDING_PROJECT_GOVERNANCE
---

# Triage Manufacturing Incident

**Taxonomy metadata:** family `11` Manufacturing Safety; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Capture incident facts, current status, witnesses, evidence, and escalation needs.

## Triggers
- Injury, near miss, property damage, release, fire, or suspected safety incident is supplied.

## Non-Triggers
- Rescue direction, emergency command, legal-reporting determination, or full causal investigation.

## Required Inputs
- What happened, when/where, persons affected, current status, reporter, and evidence.

## Optional Inputs
- Witnesses, equipment state, scene preservation, notifications, and jurisdiction.

## Assumptions
- Immediate emergency services and site procedures take precedence.

## Core Workflow
1. Record facts without speculation.
2. Identify current hazards, evidence needs, and escalation owner.
3. Return a bounded handoff for qualified incident management.

## Calculations
No calculation; supplied counts or durations retain their source and scope.

## Validation
- Check time, location, affected persons, scene state, evidence, and jurisdiction.

## Exception Handling
- Missing current-status information returns `NEEDS_INPUT`.
- Emergency or rescue request returns `SAFETY_ESCALATION`.

## Source Usage
- Apply `references/incident-triage-checklist.md` and AM-07 jurisdiction rules.

## Output Contract
Return `status`, factual timeline, affected persons, current hazards, evidence, notifications, and escalation handoff.

## Safety Requirements
AM-05 class: `HAZARDOUS_OPERATION`. Do not direct rescue, emergency action, unsafe scene entry, or legal reporting conclusions.

## References
- `references/incident-triage-checklist.md`

## Examples
A near miss is documented and escalated without inventing a cause or directing scene entry.

## Testing
Cover correct invocation, missing current status, jurisdiction gap, expected output structure, and rescue-direction refusal. Expected routing is not observed behavior.
