# Alberta provincial research module

Status: `RESEARCH_BASELINE`. Observations: 2026-09-08. Read only for this province; no substitution for other jurisdictions.

Alberta separates OHS research, local safety-code services, ABSA pressure-equipment oversight and environmental approval research. A Code update date does not prove current text for every subject.

## Research map

| Topic | Source key | Research question | Evidence needed | Review owner |
|---|---|---|---|---|
| ohs | `AM27-AB-OHS` | Start with the OHS Act, Regulation and Code; check effective amendments for the requested date, not only a 2025 summary. | Workplace regime, undertaking, facility activity, applicable sector and assessment date | Workplace regulatory/safety reviewer |
| machinery | `AM27-AB-OHS` | Find the current Code equipment/safeguard requirements for the actual machine and task; preserve manufacturer and engineering evidence separately. | Machine identity, task, guarding evidence, modification history and engineering documents | Qualified machinery safety/engineering reviewer |
| hazardous_energy | `AM27-AB-OHS` | Research the current Code hazardous-energy provisions and task conditions; do not substitute a 2009 download or cross-province procedure. | Task and equipment scope, all energy types, existing site procedure and authorized review owner | Qualified site hazardous-energy reviewer |
| electrical | `AM27-AB-ELECTRICAL` | Identify the local accredited municipality or agency and applicable discipline/code; keep workplace safety and installation permission separate. | Work versus installation scope, location, equipment, proposed change and existing permit evidence | Qualified electrical reviewer and authority having jurisdiction |
| pressure_equipment | `AM27-AB-PRESSURE` | Use ABSA to research pressure-equipment scope and the applicable Safety Codes Act instruments; a registration record alone is not operating permission. | Equipment type, service, nameplate/design records, location and proposed lifecycle activity | Qualified pressure-equipment reviewer and competent authority |
| environment | `AM27-AB-ENV` | Research EPEA approval, registration and associated conditions for each activity; do not assign a route without classification evidence. | Activity, emissions/discharges/waste, location, receiving environment and existing permissions | Environmental permissions reviewer |
| worker_training | `AM27-AB-OHS` | Research training, competency and supervision requirements by task and role; a course date does not prove continuing competence. | Worker role, task and equipment, training content, demonstrated competency and supervision evidence | Workplace training/safety reviewer |

## Source entry points

- `AM27-AB-OHS`: [Government of Alberta: OHS Act, regulation and code](https://www.alberta.ca/ohs-act-regulation-code). This observation is not verification of all subsequent amendments or any task-specific duty.
- `AM27-AB-ELECTRICAL`: [Government of Alberta: Permits and Alberta's Safety Code System](https://www.alberta.ca/permits-and-albertas-safety-code-system). Check location, discipline and accreditation; no permit issuance or electrical authorization.
- `AM27-AB-PRESSURE`: [ABSA: ABSA the pressure equipment safety authority](https://www.absa.ca/home/). Retrieved directly after web fetch failed; instrument and equipment-specific scope remain for review.
- `AM27-AB-ENV`: [Government of Alberta: Environmental Protection and Enhancement Act approvals](https://www.alberta.ca/apply-for-environmental-protection-and-enhancement-act-approvals). No registration eligibility, exemption or site authorization verified.

The [source register](../../../../docs/architecture/am27-provincial-source-records.json) preserves class, authority, rights and freshness. Guidance and topic indexes are research entry points. Retrieve current applicable instruments, amendments and commencement evidence before stating any requirement. Protect standard text and document incorporation; do not assume a national code edition applies unchanged.

## Output and limits

Return separate rows for supported research, missing facts, currency gaps and reviewer handoffs. Province selection does not establish the employer's workplace regime or a local authority's scope. Record unknown jurisdiction as `PENDING_CONTEXT`, unsupported coverage as `COVERAGE_GAP`, conflicting evidence as `CONFLICT_REVIEW_REQUIRED`, and dependent source questions as `SOURCE_REVIEW_REQUIRED`.

No machine intervention, isolation procedure, energized-work instruction, pressure-equipment approval, environmental permission, exemption or training certification is provided. An environmental topic here is an authority handoff, not a replacement for Family 19 analysis.
