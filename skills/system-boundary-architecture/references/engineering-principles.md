# Engineering Principles

Standing engineering lens for implementation-shaping work.

## Principles

- prefer explicit ownership over convenience coupling
- keep systems as simple as current needs allow
- add complexity only for explicit necessity, not symmetry, future theater, or
  convenience layering
- when complexity is necessary, keep it legible and bounded
- prefer decomposition over hotspot growth
- reuse or delete before adding a layer, helper, workflow path, manager, or
  abstraction
- delete unused, unreachable, and superseded code in the same change that makes
  it dead
- keep recurring decision rules durable, not in chat or copied precedent
- escalate unresolved structural decisions back to planning
- treat review and verification as proof of the intended contract, not the
  place where design finally happens
- optimize for the next correct change, not only the current patch
- types and static contracts must model the real boundary, not just silence the
  checker
- public seams must use named contracts or adapters; importing private helpers
  or underscore members outside their defining module is invalid
- one shared external contract has one canonical normalizer or signature owner
- public helpers may not expose parameters or option fields that cannot change
  any valid output
- behavioral `dict`, `list`, or `object` bags may not cross module boundaries as
  contracts; if the bag carries behavior, make it a named contract or adapter
- production boundary modules may not branch to test-only or missing-framework
  fallback behavior

## Required Posture

- make the owner of state, contract, and policy explicit
- prefer delete, collapse, demote, and reuse before adding new structure
- every new layer must justify what existing layers cannot do cleanly
- for structural planning, record the target minimal end state and why each
  remaining complexity is necessary
- keep transport, persistence, UI glue, and workflow policy from collapsing into
  one surface
- when a surface becomes the easiest place for unrelated behavior, treat it as a
  design smell
- when a new pattern would mislead future work, persist it into doctrine, a
  plan, or backlog

## Anti-Patterns

- route shells owning URL sync, mutation orchestration, and state transitions
  together without an explicit authority
- service hotspots growing until one surface owns validation, transaction
  scope, mapping, workflow policy, and error translation
- helpers or abstractions added mainly to hide hotspot growth
- adding workflow paths before proving simpler collapse or deletion options are
  insufficient
- preserving parallel normal paths, breakglass paths, and transitional
  machinery as if they have equal standing
- keeping dead branches or just-in-case legacy fallbacks after the new owner
  path is authoritative
- singleton or controller surfaces becoming de facto cross-surface lifecycle
  owners without an explicit rule
- fixing a visible bug while leaving the same copyable smell for the next
  change
