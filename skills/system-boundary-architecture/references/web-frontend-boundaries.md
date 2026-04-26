# Web Frontend Boundaries

Own frontend layer ownership, import direction, public-surface hygiene, and
boundary test shape.

General testing policy stays with testing doctrine.

## Layers

| Layer | Owns | Must not become |
| --- | --- | --- |
| route or page modules | screen and route composition | reusable helper home for shared library code |
| feature-specific pattern modules | composed user flows | source of reusable component defaults or feature leaks into primitives |
| reusable component modules | behavior-neutral UI blocks | importer of feature patterns or routes |
| shared domain, app, and navigation modules | route-free domain and helper logic | importer of route modules |

## Route Ownership And Atomic Design

Atomic design governs reusable UI. It does not mean every component extraction
belongs in shared UI space.

Required split:

- reusable building blocks and durable surface compositions live under shared UI
  modules,
- route-only orchestration wrappers stay route-owned,
- do not move route-owned orchestration into a shared pattern only because it is
  a component,
- do not hide feature-boundary mistakes by relabeling route orchestration as a
  shared pattern.

Heuristic:

- reusable without one route state machine: maybe shared UI space,
- mainly coordinates one route's overlays, branches, or cross-feature wiring:
  keep route-owned.

## Dependency Directions

Allowed direction:

- routes consume patterns, components, domain, and navigation
- patterns consume components, domain, and navigation
- components consume other neutral components and domain contracts
- shared domain and navigation modules consume only shared domain and navigation
  peers

Blocking rules:

- shared library modules must not import route modules
- reusable components must not import feature patterns
- UI modules must not import API clients directly unless that boundary is
  explicitly owned
- sibling feature patterns must not import each other unless one feature is the
  declared owner
- UI-layer cycles are forbidden

When a rule breaks, fix ownership. Do not add a re-export shell, shim, bridge,
or adapter only to satisfy a static check.

## Shared Primitive Neutrality

Reusable components and shared patterns stay neutral by default.

Required:

- caller opts into surface-specific behavior
- shared defaults reflect generic contract, not one current caller
- feature-specific affordance enters through explicit prop or config path
- if flags pile up and feature semantics still leak through default behavior,
  fix ownership split instead of building a hidden workflow controller

## Public Surface Hygiene

Dead exports, props, and wrapper plumbing are architecture debt.

Required:

- remove dead exports in the same change
- remove behaviorally dead props through all wrappers in the same change
- keep no legacy public surface just in case for internal-only modules
- add no compatibility shim or alias wrapper unless explicitly approved as a
  migration bridge

## Static Enforcement

Static checks should enforce local layer violations, structural graph rules,
cycle detection, and dead public surface.

Policy:

- if a rule finds a real problem, fix code instead of suppressing the rule
- if a rule is noisy or models the wrong boundary, replace it with a more
  precise rule
- do not add naming indirection or pass-through modules only to appease a
  checker

## Test Contract

Static boundary checks and runtime tests do different jobs.

Required test shape:

- domain and controller tests prove semantic outputs, state transitions, and
  invariants
- component and pattern tests prove visible contract, accessibility contract,
  emitted events, and user-facing state transitions
- route tests prove composition, route-state wiring, and capability posture, not
  lower-layer internals already covered elsewhere

Avoid:

- tests proving helper path or fetch path instead of visible contract
- route tests coupled to pattern or component internals
- runtime tests used as the main proof of static boundary correctness

If a small behavior change causes broad route, wrapper, or test churn, treat
that as boundary smell and recheck ownership split.

## Exceptions

Exceptions must be explicit and durable:

- record the exception in owning durable doctrine or an approved governing
  artifact
- keep it narrow and time-bounded
- state why the normal boundary is insufficient
