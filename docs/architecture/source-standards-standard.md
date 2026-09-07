# AM-07 source and standards standard

## Purpose and status

This standard defines how AgentManufacturing records, selects, cites, and refreshes external sources. It covers government sources, provincial regulatory systems, sector standards, source rights, and version control. It is an authoring and evidence contract; it does not make a legal applicability finding, certify a product, or grant permission to copy protected text.

Status: `STANDARD_READY_NOT_IMPLEMENTED`.

The machine-readable contracts are [source-record-schema.json](source-record-schema.json), [source-freshness-policy.json](source-freshness-policy.json), and [source-record-examples.json](source-record-examples.json). The validator checks those contracts and compatibility with the AM-04 and AM-05 registries; it does not fetch sources or evaluate a skill's behavior.

## Source precedence

Use the highest applicable source class that directly answers the question. Precedence is a selection rule, not permission to ignore a more specific scope or a conflicting instrument.

| Rank | Source class | Use | Required handling |
| --- | --- | --- | --- |
| 1 | Current enacted law, regulation, official consolidation, order, proclamation, or official Gazette instrument | Primary legal or in-force requirement | Record instrument, version, effective date, publisher, and jurisdiction. |
| 2 | Official registry, delegated regulator, or government guidance | Scope, administration, interpretation, filings, or operational context | Label guidance as guidance; do not turn it into law by paraphrase. |
| 3 | Incorporated standard or controlled technical requirement | Technical requirement only when incorporation is evidenced | Record the incorporating law, contract, licence, customer requirement, or certification basis. |
| 4 | Manufacturer, site, contract, permit, drawing, or controlled local document | Equipment or site-specific constraints | Treat as local evidence; check its owner, revision, and authority. |
| 5 | Secondary commentary or search result | Discovery and context | Never carry a primary conclusion by itself. |

When two sources conflict, preserve both records, identify the scope and as-of date for each, and route to `CONFLICTING` or `PENDING_REVIEW`. Resolve by authority, jurisdiction, temporal applicability, and directness only when the evidence supports that resolution. Do not select a source because it is easier to access or produces a more convenient result.

## Source records and claims

Every new source record follows the [AM-07 schema](source-record-schema.json). At minimum it identifies the publisher, URL, source class, jurisdiction, scope, status, rights, retrieval date, verification date, and freshness policy. Standards also require an identifier, edition or revision, publisher, sector/application, and applicability or incorporation basis.

A source record describes what the source is. A claim record describes what the project is relying on. Keep them separate. Each claim has a source key, claim type, scope, as-of date, stable location (section, page, clause, table, or URL fragment where available), and support status. A current-looking URL without a claim location and as-of date is insufficient for a source-dependent conclusion.

## Government and provincial regulatory sourcing

Government-source selection is jurisdiction-specific. The initial Canadian source map is:

| Scope | Preferred system | Record |
| --- | --- | --- |
| Federal Acts and regulations | Department of Justice Canada, Justice Laws Website, plus the Canada Gazette for published instruments | Current consolidation or instrument, previous version when an as-of date is requested, and retrieval/verification dates. |
| Ontario | Ontario e-Laws | Current consolidated or historical statute/regulation, the currency date shown by e-Laws, and the Ontario jurisdiction. |
| British Columbia | BC Laws and the BC Gazette or other official publication identified by the publisher | The instrument's current or point-in-time record and any official-publication caveat. |
| Alberta | Alberta King’s Printer, Alberta Gazette, Orders in Council, proclamations, or ministerial orders | The current consolidation or filing and the in-force, amendment, or proclamation record. |
| Quebec | LégisQuébec / Québec Official Publisher | Chapter, language, current or historical compilation, and chapter-specific update date. |

The source registry is not a province fallback table. Record the facility province or territory, federal or provincial context, activity date, sector, obligation domain, and selected instrument before making a dependent statement. Do not borrow Ontario, federal, or another province's requirement when the requested province is missing or unsupported; issue a coverage gap and review handoff instead.

The official systems themselves describe different currency and authority practices. Justice Laws provides current and previous federal versions and official consolidated Acts and regulations. Ontario e-Laws provides official copies and separates current, historical, repealed, and source material. BC Laws warns that its index is a convenience and points to official publications for authority. Alberta identifies the King’s Printer as the official publisher and states that Gazette regulations must be consulted when applying the law. LégisQuébec publishes official compilations and historical versions with update dates. These are source-selection facts; they do not establish that a particular plant, product, or operation is covered.

## Standards metadata and applicability

Standards are not automatically law. A record must distinguish:

- `incorporated_standard`: applicability is supported by a cited law, regulation, licence, contract, customer requirement, certification scheme, or controlled internal requirement;
- `voluntary_standard`: the publisher and edition are known, but no mandatory basis has been recorded; and
- `standards_dependent`: a task cannot reach a standards-dependent conclusion until the identifier, edition, scope, and access are resolved.

For every standard, capture the identifier, title, publisher or standards development organization, edition/revision/amendment, publication and reaffirmation dates when available, sector and product/process scope, geographic scope, incorporation basis, supersession state, access status, and rights handling. A standards-body catalogue can establish metadata; it cannot by itself establish that a standard applies to a site or is the current edition for a legal conclusion. The Standards Council of Canada coordinates the National Standards System and promotes voluntary standardization; that role does not make every CSA, ISO, IEC, ASTM, or other standard mandatory.

## Copyright and protected-standard handling

Use metadata first. Store the identifier, title, publisher, edition, access URL, rights state, and a short project-authored paraphrase. Link to the authorized copy or request authorized access when the exact clause is needed.

The allowed content states are:

| Rights state | Default content handling | Project behavior |
| --- | --- | --- |
| `OPEN_OFFICIAL` | `METADATA_AND_PARAPHRASE` | Preserve source identity, accuracy, and the publisher's conditions. |
| `PUBLIC_DOMAIN` | `FULL_TEXT_PERMITTED` only when verified | Record the basis and keep attribution. |
| `LICENSE_REQUIRED` | `METADATA_ONLY` unless a licence permits an excerpt | Do not paste, reconstruct, or distribute the standard text. |
| `USER_SUPPLIED` | `METADATA_ONLY` or `LICENSED_EXCERPT` | Treat the file as evidence supplied for the task; retain provenance and do not redistribute it. |
| `UNKNOWN` | `NO_REPRODUCTION` | Pause the dependent conclusion and request rights clarification. |

Federal guidance allows reproduction of federal enactments and consolidations under the Reproduction of Federal Law Order when accuracy is preserved and the copy is not represented as official. That rule does not generalize to provincial publications, regulator guidance, standards, manufacturer documents, or site records. Alberta's King’s Printer expressly states reproduction restrictions for legislation, and CSA catalogue pages identify DRM-protected standards and copyright terms. When in doubt, keep metadata and paraphrase only, with a link and a rights handoff.

## Freshness and version control

Use the states and policies in [source-freshness-policy.json](source-freshness-policy.json). Do not invent a universal numeric expiry period. Instead, capture both the source's own currency/effective label and the project's retrieval and verification dates.

`VERIFY_AT_USE` is required for laws, regulations, Gazettes, delegated-regulator requirements, and incorporated standards. `VERIFY_BEFORE_RELEASE` applies to guidance, voluntary standards, manufacturer specifications, and site documents before a final package or release. `SCHEDULED_REVIEW` keeps secondary sources in discovery-only use. `HISTORICAL_ONLY` requires an explicit as-of date and cannot satisfy a current claim.

Recheck when the user asks for current or in-force requirements, the activity date changes, a publisher shows an amendment/revision/proclamation/edition change, a source is stale or unresolved, a legal/safety/engineering/certification conclusion depends on it, or a known incident or change request may affect applicability. Current outputs must expose source status, as-of date, verification date, version or currency note, and a review owner or handoff.

## Sector-standard sourcing

Sector names are discovery inputs, not evidence. A sector-standard request must identify the product or process, country/province, facility or market, stage of work, standard identifier and edition, publisher, incorporation or contract basis, access rights, and unresolved applicability questions. Keep product standards, workplace requirements, environmental obligations, customer specifications, and internal procedures in separate source records. A missing standard, inaccessible licensed text, or unresolved edition is a visible coverage gap.

## Required safe output

Source-dependent output must include:

1. requested decision and scope;
2. applicable jurisdiction, sector, and activity date;
3. source keys and claim locations;
4. source status, version/currency, and as-of date;
5. rights and access limits;
6. supported statements and unresolved conflicts;
7. assumptions and exclusions; and
8. review owner or handoff.

The output must not claim legal compliance, certification, permit approval, engineering adequacy, or current applicability when the source is missing, stale, conflicting, inaccessible, or outside the project's authority.

## Acceptance scenarios

The validator requires these scenarios to remain represented in the standard:

| ID | Scenario | Expected handling |
| --- | --- | --- |
| AM07-S01 | Federal current Act | Select Justice Laws, record current verification, and preserve the federal scope. |
| AM07-S02 | Federal historical as-of request | Select the requested previous version and mark the claim historical. |
| AM07-S03 | Ontario current versus historical | Keep e-Laws current and historical records distinct. |
| AM07-S04 | British Columbia index versus official publication | Preserve the BC authority caveat and require official-source review. |
| AM07-S05 | Alberta amendment or proclamation | Check King’s Printer/Gazette and in-force status before a current claim. |
| AM07-S06 | Quebec language and chapter date | Record chapter, language, and the update date shown by LégisQuébec. |
| AM07-S07 | Incorporated standard | Require the incorporating instrument and standard edition before applying it. |
| AM07-S08 | Voluntary standard | Report metadata and applicability uncertainty; do not label it mandatory. |
| AM07-S09 | Licensed or copyrighted standard | Keep metadata and paraphrase only; request authorized access for exact clauses. |
| AM07-S10 | Stale or missing currency | Block a current conclusion and emit a recheck handoff. |
| AM07-S11 | Conflicting authoritative sources | Preserve both records and route to conflict review. |
| AM07-S12 | Unsupported province or mixed product/workplace request | Split the question, identify the coverage gap, and avoid provincial substitution. |

## Implementation boundary

AM-07 defines source records, source claims, precedence, rights, freshness, and acceptance evidence. It does not fetch sources automatically, install host tooling, select a project licence, implement legal or safety skills, or prove model behavior. AM-08 owns calculation metadata; AM-09 owns executable validation; AM-10 remains the gate for five reference skills and mass authoring.

## Reference sources reviewed

The source-selection decisions above were checked against these official pages on 2026-09-07:

- [Justice Laws Website](https://laws-lois.justice.gc.ca/eng/acts/) and [consolidated regulations](https://laws-lois.justice.gc.ca/eng/regulations/)
- [Ontario e-Laws](https://www.ontario.ca/laws)
- [BC Laws](https://www.bclaws.gov.bc.ca/)
- [Alberta King’s Printer](https://www.alberta.ca/alberta-kings-printer) and [The Alberta Gazette](https://www.alberta.ca/the-alberta-gazette.aspx)
- [LégisQuébec](https://www.legisquebec.gouv.qc.ca/?siteLocale=fr_CA)
- [Standards Council of Canada mandate](https://scc.ca/sites/default/files/SCC_NatStandards_Strategy_EN_WEB.pdf)
- [Crown copyright and federal-law reproduction guidance](https://www.canada.ca/en/canadian-heritage/services/crown-copyright-request.html)
- [CSA catalogue example and terms notice](https://www.csagroup.org/store/product/CAN-CSA-ISO-IEC%20TR%2015067-3%3A12/)
