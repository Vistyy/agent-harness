# Web Route And State Boundary Doctrine

Own intended long-term web route, state-authority, and screen-facing boundary
shape.

Goal: stop inferring architecture from whichever route shell, singleton store,
or controller hotspot happened to land first.

## Target Shape

- route components stay thin composition shells
- state spanning route, overlay, mutation, or lifecycle boundaries gets one
  named authority
- when orchestration grows beyond presentational glue, prefer a feature-local
  facade or screen model
- feature-local facades may delegate to smaller domain modules
- shared generic base abstraction is not required
- backend or API contracts may change only when cleanup directly requires it,
  with full propagation in the same slice

## Rules

- route shells must not own URL sync, filter policy, mutation sequencing,
  lifecycle transitions, and view composition at the same time
- singleton stores and controllers must not silently become cross-surface
  authority
- use a feature-local facade or screen model when a route would otherwise become
  workflow owner or a controller would become hidden state machine
- when a facade exists, the route consumes the facade's route-facing contract,
  not a raw controller or store schema under a new name
- screen-facing read state should also be owned by the facade or screen model
- keep facades explicit and feature-local
- do not add a shared generic screen-model layer until multiple exemplars prove
  the same mechanics
- do not force pure route-query helpers, load-owned data, or page-local UI state
  into a facade for fake uniformity
- preserve user-visible behavior semantics during doctrine-alignment refactors
  unless a tiny direct correction is explicitly recorded
- browser-visible structural refactors need persistent proof and live runtime
  proof when claims are materially interactive

Runtime proof ownership remains outside this structural skill. Use
verification and web testing doctrine for proof depth and browser mechanics.
