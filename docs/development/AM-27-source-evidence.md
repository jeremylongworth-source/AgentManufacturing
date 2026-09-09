# AM-27 provincial source evidence

Access date: 2026-09-08. Scope: four provincial research modules, seven topics each. [Source records](../architecture/am27-provincial-source-records.json) retain 16 bounded observations.

- `AM27-ON-OHS` — Program overview identifies industrial workplace scope and points to Regulation 851 and training regulations. [Industrial Health and Safety Program](https://www.ontario.ca/page/industrial-health-and-safety-program).
- `AM27-ON-REG` — Official source entry for industrial-establishment requirements; the retrieved page did not establish the current consolidation interval. [Industrial Establishments, R.R.O. 1990, Reg. 851](https://www.ontario.ca/laws/regulation/900851).
- `AM27-ON-ELECTRICAL` — ESA identifies the 2024 Ontario code and provincial amendments; code adoption and activity date require explicit review. [Ontario Electrical Safety Code](https://esasafe.com/role/oesc/).
- `AM27-ON-PRESSURE` — TSSA points to Ontario Regulation 220/01 and the Code Adoption Document for pressure equipment scope and exclusions. [Am I Regulated? Boilers and Pressure Vessels](https://www.tssa.org/am-i-regulated-1).
- `AM27-ON-ENV` — The page directs users to confirm the relevant permission type, including ECA or EASR research. [Environmental Compliance Approval](https://www.ontario.ca/page/environmental-compliance-approval).
- `AM27-BC-OHS` — The index separates regulation, policies and guidelines; Part 10 concerns hazardous energy, Part 12 machinery and Part 19 electrical safety. [Searchable OHS Regulation and related materials](https://www.worksafebc.com/en/law-policy/occupational-health-safety/searchable-ohs-regulation).
- `AM27-BC-TECH` — Technical Safety BC describes regulated technologies and local-government exceptions for electrical or gas oversight. [Jurisdiction](https://www.technicalsafetybc.ca/learn-about/technical-safety-bc/jurisdiction).
- `AM27-BC-ENV` — Guidance organizes waste-discharge authorization research by activity under the Environmental Management Act and Waste Discharge Regulation. [Do you need a waste discharge authorization](https://www2.gov.bc.ca//gov/content/environment/waste-management/waste-discharge-authorization/need).
- `AM27-AB-OHS` — The framework page links the OHS instruments and records Code changes effective 2025-03-31. [OHS Act, regulation and code](https://www.alberta.ca/ohs-act-regulation-code).
- `AM27-AB-ELECTRICAL` — The provincial safety-code system uses accredited municipalities and agencies for local permit services. [Permits and Alberta's Safety Code System](https://www.alberta.ca/permits-and-albertas-safety-code-system).
- `AM27-AB-PRESSURE` — ABSA describes its role administering Alberta pressure-equipment safety under the Safety Codes Act. [ABSA the pressure equipment safety authority](https://www.absa.ca/home/).
- `AM27-AB-ENV` — The guidance distinguishes EPEA approvals and registrations, including their associated conditions. [Environmental Protection and Enhancement Act approvals](https://www.alberta.ca/apply-for-environmental-protection-and-enhancement-act-approvals).
- `AM27-QC-OHS` — The French official regulation includes machinery, hazardous-energy control and training subjects; displayed consolidation is 2026-04-01. [Règlement sur la santé et la sécurité du travail, S-2.1, r. 13](https://www.legisquebec.gouv.qc.ca/fr/document/rc/S-2.1,%20%20r.%2013?langcont=fr).
- `AM27-QC-ELECTRICAL` — RBQ provides a dedicated electrical domain and regulatory research entry point. [Électricité](https://www.rbq.gouv.qc.ca/domaines-dintervention/electricite/).
- `AM27-QC-PRESSURE` — RBQ provides a dedicated pressure-installations domain and regulatory research entry point. [Installations sous pression](https://www.rbq.gouv.qc.ca/domaines-dintervention/installations-sous-pression/).
- `AM27-QC-ENV` — The REAFIE overview differentiates activity-risk routes and conditions for authorization, declarations and exemptions. [Règlement sur l’encadrement d’activités en fonction de leur impact sur l’environnement (REAFIE)](https://www.environnement.gouv.qc.ca/lqe/autorisations/reafie/index.htm).

## Access and currency limits

WorkSafeBC, Technical Safety BC, ESA, TSSA, Alberta government, Quebec government, RBQ and Légis Québec pages were accessed through the web tool. Ontario program/ECA pages and ABSA were retrieved with Invoke-WebRequest after browser-tool failures. Ontario Regulation 851 returned HTTP 200 but its retrieved body did not establish consolidation currency; only source identity from official search evidence is recorded. Its record is PENDING_REVIEW.

Quebec's French OHS regulation displayed currency to 2026-04-01. Its record remains PENDING_REVIEW for later activity dates. Other records are CURRENT_ON_ACCESS for the limited overview/authority-path observation, not CURRENT for a site-specific legal claim. No protected code clauses were copied. No complete amendment audit, incorporation determination or permission eligibility review was performed.

## Validation boundary

The baseline supports selecting research and evidence requests. Package and source validators check structure and coverage; Runtime model behavior remains NOT_RUN. Source accessibility and research coverage do not prove jurisdiction, compliance, competence or safe operation.
