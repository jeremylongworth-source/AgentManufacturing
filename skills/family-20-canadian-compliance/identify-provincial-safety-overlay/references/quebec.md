# Quebec provincial research module

Status: `RESEARCH_BASELINE`. Observations: 2026-09-08. Read only for this province; no substitution for other jurisdictions.

Quebec sources retain their French identity and instrument version. The observed OHS consolidation ends on 2026-04-01; currency through a later activity remains unresolved.

## Research map

| Topic | Source key | Research question | Evidence needed | Review owner |
|---|---|---|---|---|
| ohs | `AM27-QC-OHS` | Preserve the official French title, instrument identifier and consolidation date; research Act/regulation scope with the workplace owner. | Workplace regime, undertaking, facility activity, applicable sector and assessment date | Workplace regulatory/safety reviewer |
| machinery | `AM27-QC-OHS` | Research the current machinery provisions and change history in the official regulation; translated extracts must retain the original source. | Machine identity, task, guarding evidence, modification history and engineering documents | Qualified machinery safety/engineering reviewer |
| hazardous_energy | `AM27-QC-OHS` | Use cadenassage/control-of-energy research for the actual task; do not treat a translated Ontario procedure as Quebec conformity. | Task and equipment scope, all energy types, existing site procedure and authorized review owner | Qualified site hazardous-energy reviewer |
| electrical | `AM27-QC-ELECTRICAL` | Use RBQ electrical research for applicable chapters and installation context; maintain workplace safety and professional qualification questions separately. | Work versus installation scope, location, equipment, proposed change and existing permit evidence | Qualified electrical reviewer and authority having jurisdiction |
| pressure_equipment | `AM27-QC-PRESSURE` | Use RBQ pressure-installation research with type, service and activity evidence; do not infer applicability from a provincial registration elsewhere. | Equipment type, service, nameplate/design records, location and proposed lifecycle activity | Qualified pressure-equipment reviewer and competent authority |
| environment | `AM27-QC-ENV` | Research LQE/REAFIE activity conditions and applicable authorization route without assigning a risk level from the plant's industry label. | Activity, emissions/discharges/waste, location, receiving environment and existing permissions | Environmental permissions reviewer |
| worker_training | `AM27-QC-OHS` | Research role/task training requirements and comprehension evidence; translated attendance records do not establish practical competency. | Worker role, task and equipment, training content, demonstrated competency and supervision evidence | Workplace training/safety reviewer |

## Source entry points

- `AM27-QC-OHS`: [Éditeur officiel du Québec: Règlement sur la santé et la sécurité du travail, S-2.1, r. 13](https://www.legisquebec.gouv.qc.ca/fr/document/rc/S-2.1,%20%20r.%2013?langcont=fr). PENDING_REVIEW: displayed currency does not cover retrieval date 2026-09-08; retain French source identity.
- `AM27-QC-ELECTRICAL`: [Régie du bâtiment du Québec: Électricité](https://www.rbq.gouv.qc.ca/domaines-dintervention/electricite/). Domain identity only; applicable code chapter, edition, exclusions and permissions require review.
- `AM27-QC-PRESSURE`: [Régie du bâtiment du Québec: Installations sous pression](https://www.rbq.gouv.qc.ca/domaines-dintervention/installations-sous-pression/). Domain identity only; equipment classifications and authorizations remain unassessed.
- `AM27-QC-ENV`: [Government of Quebec: Règlement sur l’encadrement d’activités en fonction de leur impact sur l’environnement (REAFIE)](https://www.environnement.gouv.qc.ca/lqe/autorisations/reafie/index.htm). Guidance only; no risk category or exemption is assigned to a site.

The [source register](../../../../docs/architecture/am27-provincial-source-records.json) preserves class, authority, rights and freshness. Guidance and topic indexes are research entry points. Retrieve current applicable instruments, amendments and commencement evidence before stating any requirement. Protect standard text and document incorporation; do not assume a national code edition applies unchanged.

## Output and limits

Return separate rows for supported research, missing facts, currency gaps and reviewer handoffs. Province selection does not establish the employer's workplace regime or a local authority's scope. Record unknown jurisdiction as `PENDING_CONTEXT`, unsupported coverage as `COVERAGE_GAP`, conflicting evidence as `CONFLICT_REVIEW_REQUIRED`, and dependent source questions as `SOURCE_REVIEW_REQUIRED`.

No machine intervention, isolation procedure, energized-work instruction, pressure-equipment approval, environmental permission, exemption or training certification is provided. An environmental topic here is an authority handoff, not a replacement for Family 19 analysis.
