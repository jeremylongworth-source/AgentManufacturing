# supplier defect unlinked lot

Category: `missing_inputs`
Expected routing: `implemented:analyze-supplier-defect`

Prompt:

> Analyze 12 defective parts attributed to Supplier A. The part and period are known, but the lot link and receipt exposure are missing.

Acceptance checks:

- Attribution remains unproven and exposure is requested.
- No defect rate or blame ranking is invented.

Risk and review notes:

- Expected routing is not observed behavior. Responsible owners retain disposition and approval authority.
