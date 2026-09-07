# Mixed product claim and workplace question

Category: `jurisdiction_conflicts`
Expected routing: `implemented:assess-made-in-canada-claim`

Prompt:

> Our Ontario plant wants to put a Made in Canada claim on a product assembled from imported components. At the same time, tell me whether the plant's workplace safety rules are federal because the customer is a federal agency. Give one combined answer.

Acceptance checks:

- Separate product-origin claim analysis from workplace-jurisdiction analysis.
- Require the product facts, facility context, and applicable sources separately.
- Do not infer federal workplace coverage from the customer's identity.

Risk and review notes:

- Product labelling and workplace jurisdiction are different obligation domains.
- Current legal and regulatory sources require review before a conclusion.
