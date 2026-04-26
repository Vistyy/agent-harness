# Repository Operating Posture

Default posture when no user instruction or project owner doc overrides it:

- Treat a project as pre-release unless a durable owner marks a surface live or
  release-critical.
- Treat a project as single-developer unless a durable owner names other
  stakeholders.
- For internal-only surfaces, avoid compatibility shims, migration bridges,
  rollback ceremony, and approval choreography unless a real owner contract
  requires them.
- For released or externalized surfaces, assess compatibility, migration,
  rollout, and user impact explicitly.

Prefer the simplest operational path that honestly serves the current posture.
