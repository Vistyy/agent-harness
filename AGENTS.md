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
- Use the installed agent-harness CLI for reusable harness automation when a
  command exists; do not call removed skill-local helper scripts or recreate
  project-local wrappers.

## Routing

- Default workflow: use `subagent-orchestration` to decide whether discovery,
  planning review, implementation, verification, runtime proof, or closeout
  review stays local or routes to a harness-defined subagent.
- Work route classification: use `work-routing`.
- Project-overlay contracts and reusable harness posture: use `harness-governance`.
- Planning and wave shaping: use `planning-intake`.
- Full wave execution: use `wave-autopilot`.
- Durable documentation ownership: use `documentation-stewardship`.
- Review and completion claims: use `code-review`.
- Verification and gate selection: use `verification-before-completion`.
- Test design and test cleanup: use `testing-best-practices`.
- Architecture and owner-boundary changes: use `system-boundary-architecture`.
- Delegation and role boundaries: use `subagent-orchestration`.
- Workflow friction and recurring agent/process issues not fixed immediately:
  use `workflow-feedback`.
- Simplicity gate: use `code-simplicity`.

## Operating Rules

- Push back when a user request materially conflicts with these operating rules, the
  active owner skill, or the simplicity gate. Name the conflict, recommend the
  harness-compliant path, and pause before execution unless the harness permits
  an exception and the user explicitly accepts it. Do not treat user direction
  as overriding reusable safety, simplicity, boundary, proof, or review rules by
  implication.
- Prefer the simplest honest solution; complexity is a defect until justified.
- Delete, collapse, demote, or reuse before adding; preserve required outcomes,
  not inherited structure or ceremony.
- For non-trivial work, evaluate the touched owner/component, not only the
  diff. If the touched owner has unacceptable integrity under
  `code-simplicity`, reshape or block unless the user explicitly accepts the
  debt and it is recorded as backlog.
- Replace obsolete paths in the same change. Do not leave dead code, unused
  flags, compatibility shims, obsolete fallbacks, or migration bridges unless a
  durable owner requires a bounded compatibility, resilience, migration, or
  rollout path.
- Exceptions must name the owner, protected surface, and removal condition.
- Prefer the right boundary now. If two or more findings share one
  owner/boundary, diagnose the common cause.
- Do not execute while implementation-shaping planning is open.
- Non-trivial work requires `planning_critic` before implementation or scope
  expansion and `quality_guard` after implementation. Tiny local fixes are
  exempt only when no material owner, proof, runtime, compatibility, migration,
  or public-behavior decision is open.
- Runtime-visible completion claims require `runtime_evidence` unless the
  claim is tiny, local, and has no public-behavior or cross-boundary runtime
  risk. A `reject`, `blocked`, or incomplete runtime verdict blocks or narrows
  the affected claim.
- Keep project overlays concise maps to owning skills and project docs.
- No silent reverts or deletions of unknown files.

## Subagent Policy

- Follow `subagent-orchestration` for delegation defaults, role choice, handoff
  inputs, worker reuse, and active-worker handling.
- The user explicitly authorizes use of the spawn/subagent tool for these
  harness-defined roles when this `AGENTS.md` is in force:
  `explorer`, `check_runner`, `planning_critic`, `implementer`,
  `quality_guard`, `final_reviewer`, and `runtime_evidence`.
- This is the user-requested explicit subagent authorization for the general
  spawn-agent rule that otherwise requires the user to ask for subagents,
  delegation, or parallel agent work. No additional per-invocation user
  confirmation is required for these named roles.
- This preauthorization applies only to those named roles and only when the
  workflow calls for them. Skipping a required named role is a workflow defect.
  Only adapter/runtime hard limits may prevent invocation.
- Reuse the existing subagent for any continuation, revision, or follow-up in
  the same role and same domain/slice, even if its last verdict was completed,
  rejected, or approved; continue with `send_input` or `resume_agent`. Spawn a
  replacement only when the role changes, the reviewed domain/slice materially
  changes, the prior subagent was explicitly closed with a recorded reason
  because the loop was finished, or the next review is intentionally
  independent from prior context. Do not close and respawn same-role reviewers
  merely to submit an updated draft after rejection; that remains the same
  review loop.
- Never close, replace, or reclaim an active worker or its write scope because
  it is slow, silent, timed out, or blocking local work.

## Reply Mode

- Default: compact and direct. Expand only for safety clarity, irreversible
  confirmation, explicit user request, or clear user confusion.
