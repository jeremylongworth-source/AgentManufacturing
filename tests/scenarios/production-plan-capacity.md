# Capacity-limited production plan

Category: `correct_invocation`
Expected routing: `implemented:build-production-plan`

Prompt:

> Draft a production plan for this horizon: demand is 120 units due Friday, and the supplied line capacity is 80 units. Show the feasible allocation, unmet demand, binding constraint, assumptions, and review handoff. Do not invent overtime or release an order.

Acceptance checks:

- Allocate no more than the supplied 80 units.
- Report 40 units as unmet demand and identify capacity as the binding constraint.
- Do not invent a shift, inventory, material, labor, or customer commitment.

Risk and review notes:

- This is a planning draft, not a live ERP/MES action or customer promise.
- Production planning must review priorities, dates, and any later capacity evidence.
