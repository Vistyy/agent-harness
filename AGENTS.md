# Agent Harness Global Instructions

Reusable cross-project baseline. Project-local `AGENTS.md` files own project
facts and may add stricter rules.

Precedence:
1. User instruction.
2. Project-local `AGENTS.md` loaded after this file.
3. Global `AGENTS.md` and skills.

## Scope

- Keep project identity, product facts, runtime topology, local command bodies,
  roadmap, queue state, and active execution state in the target project.
- Treat project-local `AGENTS.md` as a compact first-hop map, not a doctrine
  dump.
- Start from the matching owner skill or project owner doc; read only what the
  current task needs.
- Use installed harness automation when a command exists.

## Always-Loaded Guardrails

- Do not replace the binding user objective with a convenient subset.
- Do not patch around a current-objective owner defect and call it complete.
- For non-trivial work, `not assessed` touched-owner integrity is not
  approvable.
- Final claims must stay within owner-selected proof, runtime evidence, and
  approved review scope.

## Routing

- Route selection: `work-routing`.
- Reusable harness posture and project overlays: `harness-governance`.
- Documentation ownership: `documentation-stewardship`.
- Simplicity and touched-owner integrity: `code-simplicity`.
- Planning, wave shaping, and non-trivial durable planning: `planning-intake`.
- Wave lifecycle, packet state, and durable execution: `initiatives-workflow`.
- Delegation and role boundaries: `subagent-orchestration`.
- Feedback-caused edits: `feedback-address`.
- End-user and mobile UI design: `user-apps-design`.
- Verification and completion claims: `verification-before-completion`.
- Runtime proof policy and evidence verdicts: `runtime-proof`.
- Browser runtime proof mechanics: `webapp-testing`.
- Mobile runtime proof mechanics: `mobileapp-testing`.
- Review and approval semantics: `code-review`.
- Test design and cleanup: `testing-best-practices`.
- Architecture and owner-boundary changes: `system-boundary-architecture`.

## Operating Rules

- Push back when a request conflicts with the active owner skill, simplicity
  gate, safety, proof, review, or boundary rule. Name the conflict and recommend
  the compliant path before execution unless the harness permits an explicit
  accepted exception.
- Prefer the least complex complete correction. Delete, collapse, demote, or
  reuse before adding structure.
- For non-trivial work, assess the touched owner/component, not only the diff.
  `not assessed` is not approvable.
- Replace obsolete paths in the same change. Do not leave dead code, unused
  flags, obsolete fallbacks, or migration bridges unless a durable owner names
  the protected surface and removal condition.
- Do not execute while implementation-shaping planning is open.
- Non-trivial work follows `work-routing` for direct, planning, or wave route
  selection. Required reviewers and proof owners apply through that route.
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
  the same role and same domain/slice. Spawn a replacement only when the role or
  reviewed domain materially changes, or when a fresh independent review is the
  point.
- Never close, replace, or reclaim an active worker or its write scope because
  it is slow, silent, timed out, or blocking local work.

## Reply Mode

- Default: compact and direct. Expand only for safety clarity, irreversible
  confirmation, explicit user request, or clear user confusion.
