---
name: system-boundary-architecture
description: "Use when work changes abstractions, ownership boundaries, cross-surface contracts, composition roots, state authority, or storage/runtime/interface boundaries."
---

# System-Boundary Architecture

Owns structural stop gates and boundary-shaping doctrine.

## Boundary Rules

- one boundary, contract, state authority, registry, runtime-local-state,
  shared-home, or path-resolution layout has one explicit owner
- one vendor, framework, storage payload, or transport payload shape has one
  parsing or normalization owner
- stores, runtime state, and adapters must not import route, screen,
  controller, or service owners only to reuse state or contract types
- composition roots and dependency modules wire declared dependencies and
  policy boundaries; they do not own request-scoped workflow wrappers,
  execution policy, or business workflow logic
- optional dependency availability policy is explicit at wiring time, not
  hidden in import-time globals
- routes, screens, shells, controllers, services, coordinators, and caches must
  not become hidden state machines, policy owners, or cross-instance mutable
  state holders
- typed contracts cross boundaries as named contracts or adapters, not raw
  `dict`, `list`, or object bags that the next owner must re-parse
- cross-surface contract changes need one named authority and one propagation
  path
- static architecture checks need a durable owner and one forbidden dependency,
  import, state-authority, or data-flow shape; aspirational target shapes stay
  planning or backlog until explicit

Apply `../code-simplicity/SKILL.md` for owner-correct repair and local shape.
Keep runtime proof taxonomy and project runtime recipes out of this skill.

## Reference Gates

- Read `references/web-boundaries.md` when browser route, page, component,
  shared UI, import direction, public-surface, route-state, facade, or
  screen-model boundaries matter.
- Read `references/python-service-boundaries.md` when Python application
  service, unit-of-work, repository construction, dynamic input, cast, `Any`, or
  typed-contract boundaries matter.

## Workflow

1. Confirm the change is structural, not merely local implementation.
2. Load only matched reference gates.
3. Check whether the governing plan/packet already closes owner, authority,
   proof, runtime, compatibility, rollout, migration, storage, and
   public-behavior decisions.
4. If the structural decision is open, stop and route back to planning.
5. If closed, apply the relevant rules and keep the governing artifact's
   structural disposition aligned.

## Stop Conditions

Stop execution and return to planning when:
- the new owner is ambiguous
- two plausible authorities remain for the same contract, state, or policy
- a composition root would need to decide policy to finish the change
- the fix needs a new structural rule not closed by the governing artifact or
  durable doctrine
- a local tactical patch would preserve a wrong ownership boundary
- an adapter, store, dependency module, route, service, or cache would become
  hidden authority to make the change fit

## Structural Smells

- route, screen, shell, service, or controller becomes a hidden state machine
- shared contract is parsed or normalized independently by multiple owners
- one nullable or dynamic shape carries multiple meanings across boundaries
- service owns transaction lifecycle, mapping, repository choreography,
  workflow policy, and error translation at once
- shared component or facade gains caller-specific behavior by default
- composition root starts deciding workflow policy instead of wiring declared
  boundaries
