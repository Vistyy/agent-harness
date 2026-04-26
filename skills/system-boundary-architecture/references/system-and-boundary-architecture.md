# System And Boundary Architecture

Own cross-stack structural and boundary-shaping decisions.

Use when work changes abstractions, state authority, composition roots,
cross-surface contracts, or ownership boundaries.

## Trigger Cases

Apply when work:

- introduces or removes non-trivial abstraction
- changes state authority or ownership boundary
- changes cross-surface contract or data-shape boundary
- changes composition-root wiring responsibilities
- changes storage, runtime, interface, or adapter boundaries
- performs structural refactor rather than local implementation edit

## Boundary Rules

- one boundary has one explicit owner
- the same vendor, framework, storage payload, or transport payload shape has
  one parsing owner only
- stores, runtime state, and adapters may not import route, screen, controller,
  or service owners just to reuse shared state or contract types
- composition roots wire dependencies and policy boundaries; they do not quietly
  own workflow logic
- dependency modules are composition-only; they may assemble services and
  adapters, but they must not define request-scoped transactional workflow
  wrappers or execution policy
- optional third-party dependencies and availability policy must be explicit at
  wiring time; adapters may not hide them in import-time module globals
- routes, screens, shells, controllers, and services may coordinate, but must
  not become hidden state machines or policy owners
- application services must not quietly own transaction lifecycle, mapping,
  exception translation, repository choreography, and workflow policy all at
  once unless that ownership is explicitly intended
- cross-surface contract changes need one named authority and one explicit
  propagation path
- state crossing route, screen, controller, or service boundaries needs declared
  authority
- shared-home, runtime-local-state, registry, or path-resolution layouts need
  one explicit owner module; CLI, factory, and compose entrypoints may consume
  that owner, but must not redefine the layout or registry policy
- one typed transport contract crosses a boundary once; adapters may not
  serialize it into raw `dict` or `list` payloads only for the next owner to
  accept or re-parse the same contract
- coordinators, controllers, and services may not hide cross-instance mutable
  cache state in static or module-level storage
- a route or service that both parses request or form input and assembles nested
  transport or domain payload dictionaries is invalid unless it is the declared
  contract owner for that payload

Boundary-tightening slices use review and testing doctrine for legacy-path
rejection. This reference owns the single-owner architecture rule.

## Stop Conditions

Stop execution and return to planning if:

- boundary changes but the new owner is ambiguous
- two plausible authorities remain for the same contract or state
- composition root would need to make policy decisions to finish the change
- refactor needs a new structural rule not already closed in planning
- local execution would need to choose public behavior, compatibility,
  migration, or runtime ownership that the governing artifact did not close

## Anti-Patterns

- route or screen shells owning URL sync, filter policy, navigation, mutation
  behavior, and view composition because it is convenient
- singleton-backed state surfaces becoming de facto lifecycle authority without
  explicit ownership rules
- backend services accreting transaction wrappers, repository calls, mapping,
  and workflow branching until boundaries are unreadable
- composition roots or factories deciding business policy instead of wiring
  declared boundaries
- adding a re-export, bridge, shim, or wrapper only to bypass a boundary rule
