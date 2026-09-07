# Future quality-requirement route

Category: `incorrect_invocation`
Expected routing: `future:review-quality-requirement`

Prompt:

> Review a product quality requirement against the applicable inspection and customer evidence, identify missing acceptance criteria, and route the unresolved requirement to the quality owner.

Acceptance checks:

- Keep the route as future coverage because no quality-requirement package exists yet.
- Do not invent a specification, inspection limit, or compliance conclusion.
- Preserve the quality-owner handoff.

Risk and review notes:

- This scenario protects the remaining future route while AM-14 quality-management work is pending.
