# State And Providers

Use this reference for Riverpod/provider design decisions.

## Provider Selection

- simple local mutable state: `StateProvider`
- computed values without mutation: `Provider`
- async read model: `FutureProvider`
- stream-driven model: `StreamProvider`
- behavior-rich domain state: `NotifierProvider` / `AsyncNotifierProvider`

Prefer the least powerful primitive that matches the required behavior.

## Notifier Rules

- keep mutation logic in notifier methods, not widgets
- produce new immutable state values
- keep side effects explicit and traceable
- separate transient UI state from domain state

## Rebuild Control

- use selective watching (`select`) for high-frequency updates
- avoid watching broad objects when only one field is needed
- split large providers when change frequency differs by concern

## Async State Handling

- model loading, success, and error explicitly
- include retry path for recoverable failures
- avoid hiding errors with silent fallback state

## Common Failure Modes

- provider owns too many responsibilities
- widget watches broad provider and rebuilds excessively
- async mutation overwrites state without guarding in-flight operations
- state shared globally when scope should be feature-local
