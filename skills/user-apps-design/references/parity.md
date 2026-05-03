# Parity

Owner for end-user web/mobile parity meaning.

## Rule

Same product, different surfaces.

Parity means matching product capability, behavior, state semantics, user
outcome, copy meaning, component semantics, interaction posture, and visual
tone. Layout, navigation container, density, and platform affordances may
diverge unless explicitly locked.

Functional parity wins when visual parity conflicts with behavior and no
product decision says otherwise.

## Required Matrix

For parity work, record:

- must match: capability, behavior, state, copy meaning, component semantics,
  interaction posture, destructive/read-only/auth posture
- allowed divergence: layout, navigation structure, density, platform
  interaction form
- prohibited mirror moves
- evidence for each client
- shared-logic equivalence proof when separate codebases implement the same
  domain behavior

Missing matrix means the work is not execution-ready.

## Blockers

Do not claim parity from screenshots alone when behavior, state, capability, or
shared logic can drift.

Do not duplicate browser history, system back, or native navigation with in-UI
navigation unless it serves a product purpose or the platform cannot represent
the transition.

Do not accept "mobile works differently" without brief-level rationale naming
the preserved product behavior.
