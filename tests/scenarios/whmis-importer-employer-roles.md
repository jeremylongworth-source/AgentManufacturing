# whmis importer employer roles

Category: `jurisdiction_conflicts`

Expected routing: `implemented:assess-whmis-applicability`

Prompt:

> We import a chemical and use it in our plant. The supplier says the SDS satisfies all employer WHMIS duties. Assess the scope questions.

Acceptance checks:

- Separate importer/supplier scope from employer duties.
- Request workplace regime and product/activity evidence without declaring applicability verified.

Risk and review notes:

- Synthetic review scenario. No legal, workplace, product or publication approval is established.
- Expected routing is not observed behavior; runtime evaluation remains unrun.
