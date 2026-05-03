---
name: subagent-orchestration
description: "Use when subagents should be invoked or routed: delegation decisions, handoff inputs, active-worker handling, and implementer routes."
---

# Subagent Orchestration

Owns delegation defaults, role choice, handoff inputs, worker reuse, and
active-worker handling.

The user explicitly authorizes use of the spawn/subagent tool for these
harness-defined roles when this skill is in force:
`explorer`, `check_runner`, `planning_critic`, `implementer`,
`quality_guard`, `final_reviewer`, and `runtime_evidence`.

This preauthorization applies only to those named roles and only when the
workflow calls for them.

## Rule

Delegate only when the handoff can preserve the binding objective. Reviewer,
worker, or runtime-evidence prompts must not replace the original objective
with a smaller task summary.

Delegate for parallel bounded work, isolated review, runtime proof, or bulky
diagnostics. Keep urgent blocking work local when the next step depends on it.

Read `references/coding-agent-topology.md` when choosing a role or preparing a
handoff.

## Handoff Contract

Pass:
- original user objective
- accepted scope reductions and residual gaps
- exact role task
- owned files/surfaces or read-only scope
- artifacts, proof rows, commands, screenshots, or logs to inspect
- known risks and stop conditions

Do not substitute a task label, packet summary, implementer summary, or narrow
review prompt for the original objective.

## Implementer Rules

- Assign one bounded approved wave task card.
- Name owned files/surfaces.
- Tell workers they are not alone in the codebase and must not revert others'
  changes.
- Parent owns shared runtime, integration, queue/packet state, quality gates,
  and final synthesis.

## Reuse And Active Workers

- Reuse the same role/domain subagent for continuation, revision, or follow-up.
- Spawn a replacement only when role or reviewed domain materially changes, or a
  fresh independent review is the point.
- Never close, replace, or reclaim an active worker or write scope because it is
  slow, silent, timed out, or blocking local work.

## Stop

Stop or reroute when delegation would narrow the objective, split one owner
across conflicting workers, require hidden material decisions, or preserve a
current-objective owner defect for someone else.
