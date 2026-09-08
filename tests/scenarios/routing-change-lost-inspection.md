# routing change lost inspection

Category: `missing_inputs`
Expected routing: `implemented:review-routing-change`

Prompt:

> Review a routing change removing an operation that contained the final inspection gate. No replacement control basis is supplied.

Acceptance checks:

- The lost inspection control is explicitly recorded.
- The routing revision is not activated.

Risk and review notes:

- Expected routing is not observed behavior. Responsible owners retain disposition and approval authority.
