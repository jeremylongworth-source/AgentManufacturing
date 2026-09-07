---
name: review-lockout-program
description: Review lockout program evidence for documented gaps and qualified handoff without providing equipment-specific isolation or restart instructions.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Lockout Program

## Overview

This reference skill performs a document and evidence-gap review of a lockout or hazardous-energy program. It identifies missing program elements, jurisdiction/source questions, training and audit gaps, and qualified review needs. It never supplies an equipment-specific isolation sequence or restart authorization.

**Taxonomy metadata:** family `11` Manufacturing Safety & Risk; tier `CORE`; safety class `HAZARDOUS_OPERATION`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `STANDARDS_DEPENDENT`, and `SECTOR_REGULATED`; priority `P0`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED` before AM-10 reference proof. Dependencies: `identify-hazardous-energy-source`, `JURIS`, `STANDARDS`, `REVIEW`. Audit distinction: review program evidence only; an energy inventory is not authority for an equipment procedure.

## Triggers

- The user supplies a lockout program, policy, training/audit records, equipment scope, and workplace jurisdiction for a review.
- The user asks for program readiness, evidence gaps, or a qualified handoff.

## Non-Triggers

- A request for the steps to isolate, verify zero energy, bypass a guard/interlock, issue a permit, or restart a named machine.
- A compliance certification, legal conclusion, incident investigation, or authorization to perform hazardous work.

## Required Inputs

- Program or procedure documents and version/effective date.
- Equipment or process scope at a document level, not an instruction request.
- Training, authorization, inspection, and audit evidence if available.
- Workplace province/territory, sector, and applicable source context.

## Optional Inputs

- Hazardous-energy inventory, role definitions, contractor controls, change-management records, incident history, and corrective-action status.

## Assumptions

- Jurisdiction and sector are not inferred from location shorthand or a company name.
- Program documents are evidence for review, not proof of field implementation.
- No missing procedure, authorization, training, or inspection record is treated as complete.

## Core Workflow

1. Confirm jurisdiction, sector, scope, document versions, and supplied evidence.
2. Map evidence to program-level controls and mark each item present, missing, stale, contradictory, or requiring qualified review.
3. Refuse unsafe operating instructions, return the evidence-gap review, and identify the responsible safety/engineering owner.

## Calculations

No calculation required. Do not compute a safety score or compliance percentage that could hide a critical missing control.

## Validation

- Check source freshness, version/effective dates, jurisdiction, sector applicability, and document-to-equipment scope.
- Confirm training/audit evidence has an owner, date, population, and status; do not equate a policy with implementation.
- Verify that the output contains no equipment-specific isolation, verification, bypass, permit, or restart steps.

## Exception Handling

- Missing jurisdiction, sector, or current source returns `SOURCE_REVIEW_REQUIRED` or `NEEDS_INPUT`.
- A request to avoid isolation, bypass a safeguard, or restart without qualified control returns `SAFETY_ESCALATION`; record the program concern and stop the unsafe path.
- Contradictory procedures remain visible and require qualified safety/engineering review.
- Certification, permit issuance, or work authorization returns `OUT_OF_SCOPE` with the responsible owner.

## Source Usage

- Start with `docs/architecture/safety-boundary-model.md`, `docs/architecture/safety-source-registry.json`, and `references/lockout-program-review-checklist.md`.
- Use official provincial, federal, standards, or sector sources only when their applicability and freshness are recorded. Do not reproduce protected standard text.
- Current source review is mandatory when a conclusion depends on a legal or standards requirement.

## Output Contract

Return `status`, review scope, jurisdiction/sector context, evidence inventory, gap matrix, source/freshness notes, unsafe-request disposition, assumptions, validation notes, qualified review owner, and next actions. Allowed statuses are `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SAFETY_ESCALATION`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`; `COMPLETE` is reserved for a bounded evidence review with no unresolved critical gate.

## Safety Requirements

AM-05 class: `HAZARDOUS_OPERATION`. Do not provide operating steps, isolation points, verification sequence, bypass instructions, permit language, restart authorization, or certification. Escalate immediately when the request would enable hazardous work or bypass a control; qualified safety/engineering review is required.

## References

- `references/lockout-program-review-checklist.md`
- `docs/architecture/safety-boundary-model.md`
- `docs/architecture/safety-source-registry.json`

## Examples

Read `references/lockout-program-review-checklist.md` for a program-gap example and an unsafe quick-repair request. The example is a review boundary, not an operating procedure.

## Testing

Cover correct invocation, incorrect invocation, missing inputs, ambiguous scenario, expected output structure, safety boundary, jurisdiction conflicts, stale standards, unsupported assumptions, and engineering handoff. The unsafe acceptance case must refuse the requested action while retaining a safe program concern. Expected routing is not observed behavior.
