# Web Boundaries

Own browser route, state-authority, UI layer, import, public-surface, and route
proof boundaries.

## Route And State Authority

- route components stay thin composition shells
- state spanning route, overlay, mutation, or lifecycle boundaries gets one
  named authority
- when orchestration grows beyond presentational glue, use a feature-local
  facade or screen model
- routes consume the facade's route-facing contract, not raw controller or
  store schema under a new name
- do not force pure query helpers, load-owned data, or page-local UI state into
  a facade for fake uniformity
- do not add a shared generic screen-model layer until multiple exemplars prove
  the same mechanics

## Layers And Imports

- routes consume patterns, components, domain, and navigation
- patterns consume components, domain, and navigation
- reusable components consume neutral components and domain contracts
- shared domain and navigation modules consume only shared peers

Blocking rules:
- shared library modules must not import route modules
- reusable components must not import feature patterns
- UI modules must not import API clients unless that boundary is explicitly
  owned
- sibling feature patterns must not import each other unless one feature is the
  declared owner
- UI-layer cycles are forbidden

Fix ownership when a rule breaks. Do not add a re-export shell, shim, bridge,
adapter, or pass-through module only to satisfy a checker.

## Shared UI

- reusable building blocks and durable surface compositions live under shared UI
- route-only orchestration wrappers stay route-owned
- shared defaults reflect generic contracts, not one current caller
- feature-specific behavior enters through explicit prop or config path
- if flags pile up and feature semantics leak through defaults, fix ownership
  instead of building a hidden workflow controller

## Public Surface

- remove dead exports, props, and wrapper plumbing in the same change
- keep no legacy public surface just in case for internal-only modules
- add no compatibility shim or alias wrapper unless explicitly approved as a
  migration bridge

## Static Checks And Tests

- fix real static boundary violations instead of suppressing them
- replace noisy or wrong static checks with more precise rules
- route tests prove composition, route-state wiring, and capability posture, not
  lower-layer internals already covered elsewhere
- component and pattern tests prove visible contract, accessibility contract,
  emitted events, and user-facing state transitions

If a small behavior change causes broad route, wrapper, or test churn, recheck
ownership split.
