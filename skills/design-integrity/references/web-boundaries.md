# Web Boundaries

Use only when the touched owner is a browser route, page, shared UI module,
facade, or screen model.

## Rules

- Routes compose; they do not become hidden state machines.
- State crossing route, overlay, mutation, or lifecycle boundaries has one
  named authority.
- Shared UI exposes generic contracts, not one caller's workflow hidden behind
  defaults.
- Feature-specific behavior enters through explicit props/config or stays
  feature-owned.
- Shared modules must not import routes; reusable components must not import
  feature patterns; UI cycles are forbidden.
- Do not add re-export shells, shims, or pass-through modules to satisfy an
  import checker. Fix ownership instead.

Tests and proof use the public UI contract: visible state, accessibility,
events, route-state wiring, and capability posture.
