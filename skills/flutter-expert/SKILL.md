---
name: flutter-expert
description: "Use when implementing or debugging Flutter/Dart mobile code: repo-consistent architecture, state management, navigation, widget composition, and performance."
---

# Flutter Expert

Owns Flutter/Dart implementation and debugging mechanics.

Does not own mobile UX design or emulator/device runtime proof.

## Implementation Loop

1. clarify feature boundary and runtime surface
2. choose smallest viable state/navigation shape
3. implement with rebuild-safe composition
4. verify with tests and runtime checks
5. optimize only when evidence shows risk

## Feature Shape

- define feature boundary and ownership before adding structure
- extend existing feature boundaries before introducing new top-level folders
- wire routes in one place with explicit entry points
- register providers close to feature scope unless sharing is intentional
- add dependencies only for a concrete use case
- avoid overlapping libraries for one concern
- keep bootstrap and router/provider setup order explicit
- avoid hidden global initialization side effects

## State And Providers

- use the least powerful provider primitive that matches required behavior
- keep mutation logic in notifier methods, not widgets
- produce new immutable state values
- separate transient UI state from domain state
- model loading, success, and error explicitly
- include retry paths for recoverable failures
- guard async mutations that can race or overwrite in-flight state
- avoid watching broad provider objects when one field is needed
- keep rebuild scopes narrow with selective watching and focused widgets

## Navigation

- use shell or tab containers only when persistent navigation is needed
- use nested stack routes for progressive task flows
- keep auth and guard redirect logic centralized and side-effect free
- use path parameters for resource identity
- use query parameters for filtering, pagination, and shareable state
- use `extra` only for transient in-process payloads
- define expected pop behavior per route group
- align system back with platform expectations

## Widgets And Performance

- use `const` for static values
- keep widgets focused and composable
- use stable keys in dynamic or reorderable collections
- avoid heavy computation inside `build`
- use builder or sliver patterns for large datasets
- isolate high-churn subtrees
- offload CPU-heavy transforms from the UI isolate
- constrain image decode sizes when possible
- profile before adding `RepaintBoundary` or other jank fixes
- revalidate behavior on the same scenario after performance changes

## Stop

- avoid global mutable shortcuts
- prefer clear composition over clever abstractions
- do not add a new state/navigation framework pattern without a migration plan
- do not let shared folders become dumping grounds for one-off widgets
- do not claim runtime behavior from static inspection alone
