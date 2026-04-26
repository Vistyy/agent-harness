# Code Shape And Local Design

Own local design posture inside files, modules, classes, functions, and
controllers.

`engineering-principles.md` says broad posture. This reference says what healthy
local shape looks like.

## Decomposition

- split by concern before one file, class, or controller becomes the default
  landing zone for every new step
- repeated branching, mutation stages, or adapter choreography means hotspot
  pressure
- prefer one clear extracted unit over a growing coordinator that owns
  everything end to end
- do not keep adding unrelated behavior because a file already has context
- if a clearer local boundary fits the current change without distorting scope,
  make it now

## Helpers And Abstractions

- add helpers only when they clarify ownership and behavior, not just line count
- reject helpers that hide the same hotspot behind another name
- prefer fewer, sharper units over wrapper stacks
- optional branches and mode flags inside an abstraction are smell

## State And Mutation

- keep mutation obvious
- readers should see where state is initialized, changed, and cleared
- prefer one visible mutation path per concern
- keep mutable authority close to the behavior that needs it
- do not let stores, caches, or controllers accumulate unrelated lifecycle rules
- when consumers need the same semantic meaning from low-level flags, publish
  semantic state at the authority boundary
- repeated consumer-side recomposition of readiness, phase, ownership, or
  permission is boundary smell

## Control Flow

- happy path, guard clauses, and failure paths should be obvious at a glance
- prefer early exit and narrow branches over deep nesting
- keep optional behavior explicit
- do not hide major path differences behind loose booleans or nullable
  parameter combinations
- split a function before unrelated phases become hard to reason about

## Test Seam Posture

- shape code so dependencies, mutation points, and side-effect boundaries are
  visible
- prefer seams that fall out of good design, not seams bolted on after tests
  hurt
- keep units small enough that tests can target one responsibility at a time

This reference owns code shape that supports testability. Test-layer choice and
proof depth stay with testing and verification doctrine.

## Belongs Elsewhere

- broad engineering posture: [engineering-principles.md](./engineering-principles.md)
- architectural ownership and cross-boundary authority:
  [system-and-boundary-architecture.md](./system-and-boundary-architecture.md)
- migration guardrails: [migration-guardrails.md](./migration-guardrails.md)
