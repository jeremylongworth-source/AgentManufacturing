# Capacity with mixed product cycles

Category: `unit_mismatch`
Expected routing: `implemented:calculate-production-capacity`

Prompt:

> Estimate capacity for a resource that makes two products with different cycle times and a supplied product mix. Keep the mix assumptions and limiting resource visible; do not average the rates silently.

Acceptance checks:

- Preserve product-specific cycles and mix weighting.
- Show loss assumptions, units, and limiting resource.
- Do not present the conditional estimate as guaranteed capacity.

Risk and review notes:

- Incompatible rates require an explicit mix basis.
