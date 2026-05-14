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
- For non-trivial work, read `design-integrity` before shaping the approach,
  handoff, review, proof, or completion claim.
- Use installed harness automation when a command exists.

## Always-Loaded Guardrails

- Do not replace the binding user objective with a convenient subset.
- Do not patch around a current-objective owner defect and call it complete.
- When the binding objective cannot be completed in the current route, route it
  into durable planning or stop as blocked; a diff-sized success claim is
  invalid.
- For non-trivial work, `not assessed` design integrity is not approvable.
- Final claims must pass `readiness-claim` and stay within the binding
  objective, selected design interface, proof, runtime evidence, design
  judgment, and approved review scope.

## Routing

- Route selection: `work-routing`.
- Reusable harness posture and project overlays: `harness-governance`.
- Documentation ownership: `documentation-stewardship`.
- Design, owner/interface adequacy, and integrity verdicts: `design-integrity`.
- Planning readiness and route selection: `work-routing`.
- Wave lifecycle, packet state, and durable execution: `initiatives-workflow`.
- Delegation and role boundaries: `subagent-orchestration`.
- Feedback-caused edits: `feedback-address`.
- End-user and mobile UI design: `user-apps-design`.
- Claim completeness and proof admissibility: `readiness-claim`.
- Runtime proof mechanics and evidence verdicts: `runtime-proof`.
- Browser runtime proof mechanics: `webapp-testing`.
- Mobile runtime proof mechanics: `mobileapp-testing`.
- Review and approval semantics: `code-review`.
- Test design and cleanup: `testing-best-practices`.
- Architecture and owner-boundary changes: `design-integrity`.

## Operating Rules

- Push back when a request conflicts with the active owner skill, design
  integrity, safety, readiness claim, proof, review, or boundary rule. Name the
  conflict and recommend the compliant path before execution unless the harness
  permits an explicit accepted exception.
- Prefer the least complex complete correction. Delete, collapse, demote, or
  reuse before adding structure.
- For non-trivial work, assess the touched owner/interface and adequacy of the
  selected scope, not only the diff. `not assessed` is not approvable.
- Replace obsolete paths in the same change. Do not leave dead code, unused
  flags, obsolete fallbacks, or migration bridges unless a durable owner names
  the protected surface and removal condition.
- Do not execute while implementation-shaping planning is open.
- Non-trivial work follows `work-routing` for direct, planning, or wave route
  selection. Required reviewers and proof owners apply through that route.
- Keep project overlays concise maps to owning skills and project docs.
- No silent reverts or deletions of unknown files.

## Subagent Policy

- This `AGENTS.md` is the user's standing instruction to use harness
  subagents. In a fresh conversation, the agent does not need the user to
  mention subagents, delegation, or parallel work again before using the named
  roles below.
- The user explicitly authorizes use of the spawn/subagent tool for these
  harness-defined roles when this `AGENTS.md` is in force:
  `explorer`, `planning_critic`, `implementer`, `quality_guard`,
  `final_reviewer`, `runtime_evidence`, and `design_judge`.
- This is standing user authorization. It satisfies any general rule requiring
  explicit user permission before spawning subagents. Do not ask again before
  using these named roles.
- Follow `subagent-orchestration` for delegation, handoffs, worker reuse, and
  active-worker handling. When its default-delegation conditions match, spawn
  the subagent; do not wait for a fresh user request to delegate.
- This preauthorization applies only to those named roles and only when the
  workflow calls for them. Adapter/runtime hard limits, unsafe handoff, or lack
  of a bounded task are the skip reasons.
- Reuse the same role/domain subagent for continuation or revision. Spawn a
  replacement only for a different role/domain or intentionally fresh review.
- Never close, replace, or reclaim an active worker or write scope because it is
  slow, silent, timed out, or blocking local work.

## Reply Mode

- Default: compact and direct. Expand only for safety clarity, irreversible
  confirmation, explicit user request, or clear user confusion.
