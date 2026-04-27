# Mobile Backend Patterns

Use when backend decisions directly shape mobile reliability or UX.

## Priorities

Design for:
- unreliable network
- resumable flows
- low-latency payloads
- safe auth/session renewal
- field-debuggable failures

## Push Notifications

Required:
- token lifecycle: create, refresh, revoke
- APNs and FCM differences handled explicitly
- taxonomy for transactional, reminder, informational notifications

Guardrails:
- never assume token permanence
- duplicate delivery must be idempotent
- server controls frequency and targeting

## Offline Sync And Conflicts

Define sync model per domain:
- authoritative server plus merge rules
- last-write-wins only when data loss is acceptable
- explicit conflict flow for high-value user-editable data

Required mechanics:
- queued local ops with retry policy
- stable operation IDs for idempotency
- deterministic conflict metadata for diagnostics

## API Shape

Payload rules:
- avoid overfetch
- support cursor pagination for growing datasets
- include stable identifiers and timestamps for reconciliation

Performance rules:
- compress and cache when appropriate
- prefer incremental updates over full replacement

## Version And Capability Control

Backend should support:
- minimum supported app version
- optional capability negotiation
- controlled deprecation windows

Do not silently break old clients without explicit policy path.

## Authentication

Required:
- short-lived access tokens with safe refresh flow
- explicit refresh failure and expiry handling
- device/session revocation support

Security:
- never log sensitive token material
- support server-side anomaly detection for suspicious token use

## Error Contract

Errors should be:
- categorizable
- user-message friendly or mappable
- traceable with request/correlation identifiers

Include retry guidance when meaningful.

## Media And Binary Flows

- support chunking or resume for large transfers
- enforce size and type constraints server-side
- expose progress-friendly contracts

## Security And Abuse

- device-level throttling where risk warrants
- request signing or attestation where risk warrants
- replay mitigation on sensitive endpoints

## Observability

Capture per request:
- app version
- platform
- non-PII device/app context
- correlation IDs
- error class
- retry outcome

Use logs and metrics to detect:
- version-specific spikes
- platform-specific regressions
- sync-conflict trends

## Readiness Check

- [ ] offline and retry behavior is explicit
- [ ] idempotency is defined for mutable ops
- [ ] pagination and payload shape fit mobile
- [ ] auth refresh and revocation are tested
- [ ] error contract supports safe recovery
- [ ] observability captures platform and version diagnostics
