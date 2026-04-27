# Agent Harness Global Instructions

Reusable cross-project baseline. Project-local `AGENTS.md` files own project
facts and may add stricter rules.

Precedence:
1. User instruction.
2. Project-local `AGENTS.md` loaded after this file.
3. Global `AGENTS.md` and skills.

## Scope

- Keep project identity, product facts, runtime topology, and active queue state
  in the target project.

## Map First

- Treat project-local `AGENTS.md` as a compact first-hop map, not a doctrine
  dump.
- Start from the matching owner skill or project owner doc.
- Read only what the current task needs.

## Routing

- Task-size routing and project-overlay contracts: use `harness-governance`.
- Planning and wave shaping: use `planning-intake`.
- Full wave execution: use `wave-autopilot`.
- Durable documentation ownership: use `documentation-stewardship`.
- Review and completion claims: use `code-review`.
- Verification and gate selection: use `verification-before-completion`.
- Test design and test cleanup: use `testing-best-practices`.
- Architecture and owner-boundary changes: use `system-boundary-architecture`.
- Delegation and role boundaries: use `subagent-orchestration`.
- Simplicity lens: use `code-simplicity`.

## Operating Rules

- Prefer the simplest honest solution; complexity is a defect until justified.
- Delete, collapse, demote, or reuse before adding; preserve required outcomes,
  not inherited structure or ceremony.
- Replace obsolete paths in the same change. Do not leave dead code, unused
  flags, compatibility shims, obsolete fallbacks, or migration bridges unless a
  durable owner requires a bounded compatibility, resilience, migration, or
  rollout path.
- Exceptions must name the owner, protected surface, and removal condition.
- Prefer the right boundary now. If two or more findings share one
  owner/boundary, diagnose the common cause.
- Do not execute while implementation-shaping planning is open; non-trivial work
  needs critic-first review and a durable plan.
- Keep project overlays concise maps to owning skills and project docs.
- No silent reverts or deletions of unknown files.

## Subagent Policy

- Reuse subagents only for the same role on the same domain/slice. If the next
  step needs a different role, use a worker with that role.
- Never close, replace, or reclaim an active worker or its write scope because
  it is slow, silent, timed out, or blocking local work.

## Reply Mode

- Default: compact and direct. Expand only for safety clarity, irreversible
  confirmation, explicit user request, or clear user confusion.
