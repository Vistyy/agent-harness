---
name: subagent-orchestration
description: "Use when subagents should be invoked or routed: delegation decisions, handoff inputs, active-worker handling, and implementer routes."
---

# Subagent Orchestration

Owns delegation decisions, role choice, handoff inputs, worker reuse, and
active-worker handling.

`../../AGENTS.md` owns the explicit user preauthorization allowlist.
`../../agents/roles.md` owns harness role names and missions.

## Rule

`../../AGENTS.md` is standing user authorization for the named harness
subagents. Do not ask for additional delegation permission when this skill says
to delegate.

Treat this as the fresh-conversation authorization source. The parent agent
does not need the user to mention subagents, delegation, or parallel work in
the current conversation before using a named harness role.

Delegate only when the handoff preserves the binding objective, accepted
reductions, selected design owner/interface, and readiness claim.

Use subagents for parallel bounded work, isolated review, live-use runtime
proof, broad design judgment, or bounded discovery. Keep urgent blocking work
local when the next step depends on it.

Default to `implementer` for non-trivial code/doc edits when design integrity,
readiness claim, and owned scope are clear enough to hand off. A durable packet
is not required for a direct-route implementation slice. Keeping the work local
requires a concrete reason: next-step blocking dependency, unclear owned scope,
unsafe split, or an active-worker/write-scope conflict.

Default to `explorer` for non-trivial repository discovery when the parent can
ask a bounded question instead of reading broad file sets locally.

## Roles

- `explorer`: read-only repository discovery and context compression.
- `planning_critic`, `quality_guard`, `final_reviewer`: review only.
- `implementer`: one bounded approved implementation slice.
- `runtime_evidence`: live-use behavior evidence under `readiness-claim` and
  `runtime-proof`.
- `design_judge`: screenshot/contact-sheet visual-quality approval.

## Handoff

Pass:

- active packet path when durable state exists
- binding objective, accepted reductions, residual gaps
- design owner/interface
- readiness claim
- role task and owned/read-only scope
- artifacts, commands, screenshots, or logs to inspect
- risks or blockers

Do not substitute a task label, packet summary, implementer summary, or narrow
review prompt for the original objective.

Stop when delegation would narrow the objective, split one owner across
conflicting workers, require hidden material decisions, or preserve a
current-objective owner defect.

## Active Workers

Reuse the same role/domain subagent for continuation, revision, or follow-up.
Spawn a replacement only when role/domain changes or fresh independent review
is required.

Never close, replace, or reclaim an active worker or write scope because it is
slow, silent, timed out, or blocking local work.
