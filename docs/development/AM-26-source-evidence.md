# AM-26 federal source evidence

Access date: 2026-09-08. Scope: source discovery and bounded observations for Family 20 evidence-review packages.

## Observations

- `AM26-WORKPLACE`: The list identifies workplaces and differentiates Code-part coverage; undertaking context is needed for authority research. [Employment and Social Development Canada: List of federally regulated industries and workplaces](https://www.canada.ca/en/services/jobs/workplace/federally-regulated-industries.html).
- `AM26-WHMIS`: Supplier HPA/HPR guidance separates its scope from employer requirements administered under the applicable workplace jurisdiction. [Health Canada: Guidance on the WHMIS supplier requirements](https://www.canada.ca/en/health-canada/services/environmental-workplace-health/occupational-health-safety/workplace-hazardous-materials-information-system/supplier-hazard-communication-requirements-whmis/guidance.html).
- `AM26-WHMIS-TRANSITION`: The newsletter records the amended-HPR transition ending on 2025-12-14; it is not permission to continue using pre-amendment documents. [Health Canada: December 2025 issue: Workplace Hazardous Products Program newsletter](https://www.canada.ca/en/health-canada/services/environmental-workplace-health/occupational-health-safety/workplace-hazardous-materials-information-system/program-newsletter/december-2025.html).
- `AM26-ORIGIN`: The guidance distinguishes Made in Canada (51% Canadian direct costs, last substantial transformation in Canada and qualifying wording) from Product of Canada (98% and last substantial transformation in Canada). It does not approve or certify claims. [Competition Bureau Canada: Made in Canada claims](https://competition-bureau.canada.ca/en/deceptive-marketing-practices/made-canada-claims).
- `AM26-LABELLING`: The overview addresses prepackaged non-food consumer products, identifies product/channel exclusions, and names identity, quantity and dealer information as basic label evidence areas. [Competition Bureau Canada: Packaging and labelling requirements](https://competition-bureau.canada.ca/en/labelling/prepackaged-non-food-consumer-products/packaging-and-labelling-requirements).
- `AM26-HPA`: Landing page identifies R.S.C., 1985, c. H-3, currency to 2026-06-21 and last amendment 2023-01-14. [Justice Canada: Hazardous Products Act](https://laws-lois.justice.gc.ca/eng/acts/H-3/).
- `AM26-HPR`: Landing page identifies SOR/2015-17, currency to 2026-06-21 and last amendment 2022-12-15. [Justice Canada: Hazardous Products Regulations](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2015-17/).
- `AM26-CPLA`: Landing page identifies R.S.C., 1985, c. C-38, currency to 2026-06-21 and last amendment 2019-01-15. [Justice Canada: Consumer Packaging and Labelling Act](https://laws-lois.justice.gc.ca/eng/acts/C-38/).
- `AM26-CPLR`: Landing page identifies C.R.C., c. 417, currency to 2026-06-21 and last amendment 2019-06-17. [Justice Canada: Consumer Packaging and Labelling Regulations](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._417/).

## Currency and evidence limits

The four Justice landing pages display currency to 2026-06-21. Their AM-07 source records are `PENDING_REVIEW` for a claim as of 2026-09-08: later amendments, commencement and the intervening period have not been verified. The verification date records checking the displayed metadata, not legal currency through that date. A recently accessed official page must not be promoted to `CURRENT` on that basis alone.

The Competition Bureau pages were found through web search and retrieved successfully with PowerShell Invoke-WebRequest after the browser fetch timed out. The origin page displayed modification date 2026-06-14; the label overview displayed 2022-06-23. Health Canada guidance and newsletter, ESDC list, and Justice metadata were read through the web tool. Only the bounded observations above are stored; no protected standard text or full-page reproduction is included.

## Use in the packages

[AM-07-compatible records](../architecture/am26-federal-source-records.json) preserve source class, authority, rights, freshness, and scope. Guidance is `CURRENT_ON_ACCESS`, not a legal applicability finding. The newsletter records a historical transition event; any decision for a later date requires current governing evidence. No automatic origin-claim verdict, WHMIS applicability conclusion, provincial substitution, or packaging release is implemented.

Runtime model behavior remains `NOT_RUN`; validation of these files checks record structure and coverage, not live source freshness.
