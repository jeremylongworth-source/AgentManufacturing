# Ontario provincial research module

Status: `RESEARCH_BASELINE`. Observations: 2026-09-08. Read only for this province; no substitution for other jurisdictions.

Ontario machinery research starts with the industrial workplace context. ESA and TSSA questions remain distinct from workplace safety and environmental permission research.

## Research map

| Topic | Source key | Research question | Evidence needed | Review owner |
|---|---|---|---|---|
| ohs | `AM27-ON-OHS` | Confirm OHSA and industrial-sector scope; use current e-Laws instruments before stating duties. | Workplace regime, undertaking, facility activity, applicable sector and assessment date | Workplace regulatory/safety reviewer |
| machinery | `AM27-ON-REG` | Research Regulation 851 machinery provisions and whether a pre-start review question arises for the proposed change; do not assume every modification qualifies. | Machine identity, task, guarding evidence, modification history and engineering documents | Qualified machinery safety/engineering reviewer |
| hazardous_energy | `AM27-ON-REG` | Research task-specific energy-isolation provisions in the current industrial regulation; do not copy another province's procedure. | Task and equipment scope, all energy types, existing site procedure and authorized review owner | Qualified site hazardous-energy reviewer |
| electrical | `AM27-ON-ELECTRICAL` | Separate workplace electrical safety research from ESA installation/code and notification questions. | Work versus installation scope, location, equipment, proposed change and existing permit evidence | Qualified electrical reviewer and authority having jurisdiction |
| pressure_equipment | `AM27-ON-PRESSURE` | Research Regulation 220/01 and the applicable adoption document with equipment facts; do not infer exemption from size alone. | Equipment type, service, nameplate/design records, location and proposed lifecycle activity | Qualified pressure-equipment reviewer and competent authority |
| environment | `AM27-ON-ENV` | Research ECA versus EASR and other permission routes for the actual activity; existing registration is not proof for a changed process. | Activity, emissions/discharges/waste, location, receiving environment and existing permissions | Environmental permissions reviewer |
| worker_training | `AM27-ON-OHS` | Research applicable awareness and task-specific training requirements separately; attendance is not demonstrated competence. | Worker role, task and equipment, training content, demonstrated competency and supervision evidence | Workplace training/safety reviewer |

## Source entry points

- `AM27-ON-OHS`: [Government of Ontario: Industrial Health and Safety Program](https://www.ontario.ca/page/industrial-health-and-safety-program). Program scope only; current applicable provisions require e-Laws review.
- `AM27-ON-REG`: [Government of Ontario: Industrial Establishments, R.R.O. 1990, Reg. 851](https://www.ontario.ca/laws/regulation/900851). PENDING_REVIEW: HTTP success and search identity only; effective text not verified.
- `AM27-ON-ELECTRICAL`: [Electrical Safety Authority: Ontario Electrical Safety Code](https://esasafe.com/role/oesc/). Overview accessed; no protected code clauses reproduced or installation applicability determined.
- `AM27-ON-PRESSURE`: [Technical Standards and Safety Authority: Am I Regulated? Boilers and Pressure Vessels](https://www.tssa.org/am-i-regulated-1). Scope guidance only; equipment-specific exclusions and permissions remain unassessed.
- `AM27-ON-ENV`: [Government of Ontario: Environmental Compliance Approval](https://www.ontario.ca/page/environmental-compliance-approval). Routing guidance retrieved directly; no activity permission eligibility established.

The [source register](../../../../docs/architecture/am27-provincial-source-records.json) preserves class, authority, rights and freshness. Guidance and topic indexes are research entry points. Retrieve current applicable instruments, amendments and commencement evidence before stating any requirement. Protect standard text and document incorporation; do not assume a national code edition applies unchanged.

## Output and limits

Return separate rows for supported research, missing facts, currency gaps and reviewer handoffs. Province selection does not establish the employer's workplace regime or a local authority's scope. Record unknown jurisdiction as `PENDING_CONTEXT`, unsupported coverage as `COVERAGE_GAP`, conflicting evidence as `CONFLICT_REVIEW_REQUIRED`, and dependent source questions as `SOURCE_REVIEW_REQUIRED`.

No machine intervention, isolation procedure, energized-work instruction, pressure-equipment approval, environmental permission, exemption or training certification is provided. An environmental topic here is an authority handoff, not a replacement for Family 19 analysis.
