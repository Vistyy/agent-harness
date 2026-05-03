# Delegation Policy

Delegate for parallel bounded work, isolated review, runtime proof, or bulky
diagnostics. Keep urgent blocking work local when the next step depends on it.

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
