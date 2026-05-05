---
name: subagent-orchestration
description: "Use when subagents should be invoked or routed: delegation decisions, handoff inputs, active-worker handling, and implementer routes."
---

# Subagent Orchestration

Owns delegation defaults, role choice, handoff inputs, worker reuse, and
active-worker handling.

`../../agents/roles.md` owns harness role names and missions. This skill owns
how those roles are invoked and handed work.

The user explicitly authorizes use of the spawn/subagent tool for these
harness-defined roles when this skill is in force:
`explorer`, `check_runner`, `planning_critic`, `implementer`,
`quality_guard`, `final_reviewer`, `runtime_evidence`, and `design_judge`.

This preauthorization applies only to those named roles and only when the
workflow calls for them.

## Rule

Delegate only when the handoff can preserve the binding objective. Reviewer,
worker, or runtime-evidence prompts must not replace the original objective
with a smaller task summary.

Runtime-evidence handoffs cannot command the role to skip live use, accept
tests/reviews as proof, edit, debug, design-judge, code-review, or narrow the
claim without accepted reduction.

Design-judge handoffs cannot command the role to skip screenshot/contact-sheet
inspection, accept selectors/tests/scores as UI approval, run the app, review
code, or narrow the design claim without accepted reduction.

Delegate for parallel bounded work, isolated review, live-use runtime proof, or
bulky diagnostics. Keep urgent blocking work local when the next step depends
on it.

Use `../../agents/roles.md` when choosing a role.

Role boundaries:
- parent owns orchestration, integration, shared runtime lifecycle, final
  synthesis, and queue/packet state
- `explorer` and `check_runner` are read-only/support roles
- `planning_critic`, `quality_guard`, and `final_reviewer` review; they do not
  implement
- `runtime_evidence` uses the app/service beyond tests and reviews to prove
  handed-off live behavior under `runtime-proof` verdict policy
- `design_judge` inspects screenshots/contact sheets against design anchors and
  returns product UI design `pass`, `reject`, or `blocked`
- `implementer` executes only an approved wave task card

## Handoff Contract

Slice scope is execution scope only. It is not the success claim. A handoff may
narrow work; only the user or durable planning state may narrow success.

Pass:
- original user objective
- accepted scope reductions and residual gaps
- exact role task
- owned files/surfaces or read-only scope
- artifacts, proof rows, commands, screenshots, or logs to inspect
- known risks and stop conditions

Do not substitute a task label, packet summary, implementer summary, or narrow
review prompt for the original objective.

If a non-trivial handoff omits the binding objective or accepted reductions, or
cannot state how the slice preserves them, stop and return to planning.

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
