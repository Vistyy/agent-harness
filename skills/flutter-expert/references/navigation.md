# Navigation (GoRouter)

Use this reference for route topology and navigation behavior.

## Route Topology

- top-level destinations: shell/tab container when persistent navigation is needed
- progressive task flows: nested stack routes
- auth/guarded areas: explicit redirect logic with deterministic conditions

## Parameter Rules

- path parameters for resource identity
- query parameters for filtering/pagination/shareable state
- `extra` only for transient in-process payloads

## Redirect Rules

- keep redirect logic centralized and side-effect free
- avoid circular redirects and hidden implicit guards
- ensure unauthorized and expired-session paths are explicit

## Back Behavior

- define expected pop behavior per route group
- align with platform/system back expectations
- avoid dead-end screens that require custom hacks to exit

## Common Failure Modes

- route graph mixed with feature business logic
- broad shell wrappers for screens that should not share nav chrome
- overuse of `extra` for data that should be in path/query/state
