# Mobile Client Boundaries

Use only when the touched owner is a mobile client/backend contract.

## Rules

Mobile reliability belongs at explicit interfaces, not inside UI screens or
runtime proof scripts.

Name the owner for any changed:

- offline/sync authority, operation IDs, retry, conflict, and recovery behavior
- API payload identity, pagination, timestamps, and reconciliation fields
- app version/capability negotiation and deprecation
- auth expiry, refresh, revocation, and safe logging
- push token lifecycle and notification targeting
- media limits, resumability, and progress contracts
- error categories, retry posture, user mapping, correlation IDs, and
  observability

Stop when local client code would invent one of these contracts without an
owner.
