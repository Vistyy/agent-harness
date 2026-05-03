# Mobile Client Boundaries

Owner for mobile backend, offline, sync, API, version, auth, notification, and
observability contracts when they shape app behavior.

## Rule

Mobile reliability rules live at explicit boundaries, not inside UI design or
runtime proof mechanics.

## Contracts

- Push notification token lifecycle covers create, refresh, revoke, duplicate
  delivery, frequency, and targeting.
- Offline and sync flows define authority, queued operation IDs, retry policy,
  conflict metadata, and user recovery for destructive or high-value data.
- Mobile API payloads avoid overfetch, support pagination for growing data, and
  expose stable IDs and timestamps for reconciliation.
- Version/capability policy names minimum supported app version, capability
  negotiation, and deprecation path.
- Auth covers short-lived access, refresh failure, expiry, revocation, and safe
  logging.
- Error contracts are categorizable, user-mappable, retry-aware, and traceable
  with correlation IDs.
- Media/binary flows define size/type limits, resumability when needed, and
  progress-friendly contracts.
- Observability captures platform, app version, non-PII context, correlation
  IDs, error class, and retry outcome.

## Stop

Stop when mobile UI, runtime proof, or local client code would invent one of
these contracts without a project or boundary owner.
