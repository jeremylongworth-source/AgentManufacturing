---
name: triage-nonconformance
description: Prioritize a reported manufacturing nonconformance from supplied defect evidence while preserving unknown scope and routing the next review owner.
license: PENDING_PROJECT_GOVERNANCE
---

# Triage Nonconformance

## Overview

This reference skill creates an initial, evidence-bounded triage record for a reported defect or process nonconformance. It identifies known impact, urgency rationale, unknowns, and the next owner without inventing affected quantity, cause, disposition, or release status.

**Taxonomy metadata:** family `09` Quality & Nonconformance; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P0`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED` before AM-10 reference proof. Dependencies: `REVIEW`. Audit distinction: prioritize the initial issue and next owner; documentation, containment, and causal investigation are downstream.

## Triggers

- The user supplies an observed defect, affected product or process, some scope evidence, or immediate hold/escalation evidence.
- The user asks for an initial nonconformance triage, severity rationale, or next-owner handoff.

## Non-Triggers

- Root-cause analysis, final disposition, corrective or preventive action, customer notification, or quality-system certification.
- A command to place product on hold, release product, change a process, or alter a live quality record.

## Required Inputs

- Observed defect description and evidence source.
- Affected product, process, lot, asset, or time window if known.
- Known scope and explicit unknowns.
- Any existing hold, containment, escalation, or safety evidence.

## Optional Inputs

- Photos or inspection records, specification reference, detection method, recurrence history, traceability, customer impact, and proposed owner.

## Assumptions

- Unknown scope remains unknown; a missing quantity is not zero and a single sample is not the full lot.
- Priority is based only on supplied evidence and stated criteria. Cause and disposition require separate evidence.
- A triage record is a recommendation for review, not a quality release or containment command.

## Core Workflow

1. Separate observed facts, reported claims, and unknowns; capture product/process boundary and evidence time.
2. Assign a provisional priority with a short evidence-based rationale and identify immediate review or escalation needs.
3. Return the triage record, evidence gaps, and next owner without asserting cause, quantity, or disposition.

## Calculations

No calculation required. Do not derive affected quantity, defect rate, risk score, or severity from incomplete evidence. If a supplied quality metric is included, preserve its source and units and route metric validation separately.

## Validation

- Confirm the defect is observable and distinguish fact from hypothesis.
- Confirm product/process scope, lot or time boundaries, and whether hold/escalation evidence is direct or reported.
- Check that proposed priority is supported and that unknown scope is explicitly visible.
- Ensure output does not claim root cause, final disposition, release, or completed containment.

## Exception Handling

- Missing defect evidence or affected boundary returns `NEEDS_INPUT`.
- Unknown scope returns `PARTIAL` or `SAFETY_ESCALATION` when supplied evidence indicates immediate safety or regulatory exposure; it must name the escalation owner.
- Contradictory records preserve both versions and return `NEEDS_INPUT`.
- Release, hold-command, or customer-commitment requests return `OUT_OF_SCOPE` with the responsible quality process.

## Source Usage

- Use supplied inspection, traceability, and quality-system records as evidence; record source, timestamp, and owner.
- Use external standards or regulations only when the user identifies a requirement needing interpretation; preserve publisher, title, URL/local path, access date, and freshness rule.
- Do not copy protected standard text or turn a standard label into a compliance conclusion.

## Output Contract

Return `status`, issue scope, observed facts, evidence sources, provisional priority and rationale, known impact, unknowns, immediate review/escalation, next owner, assumptions, validation notes, and prohibited conclusions. Allowed statuses are `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SAFETY_ESCALATION`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. Do not issue a hold/release command, change a process, or certify product. Escalate supplied evidence of injury, hazardous exposure, regulatory reporting, or product safety risk to the qualified owner while retaining the safe evidence summary.

## References

- `references/nonconformance-triage-checklist.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/safety-boundary-model.md`

## Examples

Read `references/nonconformance-triage-checklist.md` for an unknown-scope example. It demonstrates an escalation and evidence gap, not observed model behavior.

## Testing

Cover correct invocation, incorrect invocation, missing inputs, bad inputs, ambiguous scenario, expected output structure, safety boundary, unsupported assumptions, and unknown defect scope. The acceptance case must retain unknown quantity and identify the next owner. Expected routing is not observed behavior.
