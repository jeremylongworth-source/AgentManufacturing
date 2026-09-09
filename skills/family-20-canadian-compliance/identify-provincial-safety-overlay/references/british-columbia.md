# British Columbia provincial research module

Status: `RESEARCH_BASELINE`. Observations: 2026-09-08. Read only for this province; no substitution for other jurisdictions.

Technical Safety BC identifies local electrical/gas jurisdiction exceptions. Select the authority by location and technology; do not generalize an electrical exception to pressure equipment.

## Research map

| Topic | Source key | Research question | Evidence needed | Review owner |
|---|---|---|---|---|
| ohs | `AM27-BC-OHS` | Check WorkSafeBC inspectional jurisdiction and relevant Workers Compensation Act/OHS Regulation scope before selecting duties. | Workplace regime, undertaking, facility activity, applicable sector and assessment date | Workplace regulatory/safety reviewer |
| machinery | `AM27-BC-OHS` | Use the Part 12 research path and equipment-specific provisions; keep regulations distinct from interpretive guidelines. | Machine identity, task, guarding evidence, modification history and engineering documents | Qualified machinery safety/engineering reviewer |
| hazardous_energy | `AM27-BC-OHS` | Use the Part 10 research path with task and energy evidence; no equivalence with an Ontario program is assumed. | Task and equipment scope, all energy types, existing site procedure and authorized review owner | Qualified site hazardous-energy reviewer |
| electrical | `AM27-BC-TECH`, `AM27-BC-OHS` | Check local electrical jurisdiction with Technical Safety BC; separately research workplace electrical safety through WorkSafeBC Part 19. | Work versus installation scope, location, equipment, proposed change and existing permit evidence | Qualified electrical reviewer and authority having jurisdiction |
| pressure_equipment | `AM27-BC-TECH` | Research the pressure technology, applicable safety regulation and lifecycle permissions independently of electrical municipal exceptions. | Equipment type, service, nameplate/design records, location and proposed lifecycle activity | Qualified pressure-equipment reviewer and competent authority |
| environment | `AM27-BC-ENV` | Research each waste/discharge activity and receiving medium; one authorization need not cover all activities. | Activity, emissions/discharges/waste, location, receiving environment and existing permissions | Environmental permissions reviewer |
| worker_training | `AM27-BC-OHS` | Research orientation and task/equipment training provisions for the actual worker role; do not equate a general course with all required evidence. | Worker role, task and equipment, training content, demonstrated competency and supervision evidence | Workplace training/safety reviewer |

## Source entry points

- `AM27-BC-OHS`: [WorkSafeBC: Searchable OHS Regulation and related materials](https://www.worksafebc.com/en/law-policy/occupational-health-safety/searchable-ohs-regulation). Index and scope read; no full in-force amendment audit or inspectional jurisdiction determination.
- `AM27-BC-TECH`: [Technical Safety BC: Jurisdiction](https://www.technicalsafetybc.ca/learn-about/technical-safety-bc/jurisdiction). Location and technology must be researched together; no blanket permitting authority assignment.
- `AM27-BC-ENV`: [Government of British Columbia: Do you need a waste discharge authorization](https://www2.gov.bc.ca//gov/content/environment/waste-management/waste-discharge-authorization/need). Displayed update 2026-03-10; no site discharge authorization determined.

The [source register](../../../../docs/architecture/am27-provincial-source-records.json) preserves class, authority, rights and freshness. Guidance and topic indexes are research entry points. Retrieve current applicable instruments, amendments and commencement evidence before stating any requirement. Protect standard text and document incorporation; do not assume a national code edition applies unchanged.

## Output and limits

Return separate rows for supported research, missing facts, currency gaps and reviewer handoffs. Province selection does not establish the employer's workplace regime or a local authority's scope. Record unknown jurisdiction as `PENDING_CONTEXT`, unsupported coverage as `COVERAGE_GAP`, conflicting evidence as `CONFLICT_REVIEW_REQUIRED`, and dependent source questions as `SOURCE_REVIEW_REQUIRED`.

No machine intervention, isolation procedure, energized-work instruction, pressure-equipment approval, environmental permission, exemption or training certification is provided. An environmental topic here is an authority handoff, not a replacement for Family 19 analysis.
