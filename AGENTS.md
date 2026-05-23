# Agent Workflow Overlay Instructions

Reusable cross-project baseline. Project-local `AGENTS.md` files own project
facts and may add stricter rules.

Precedence:
1. User instruction.
2. Project-local `AGENTS.md` loaded after this file.
3. Global `AGENTS.md` and skills.

## Scope

- Project facts, runtime topology, commands, roadmap, queue state, and active
  work stay in the target project.
- Project-local `AGENTS.md` is a compact first-hop map.
- Non-trivial work starts by shaping the objective with `solution-shaping`.

## Always-Loaded Guardrails

- Do not replace the binding user objective with a convenient subset.
- Do not patch around a current-objective owner defect and call it complete.
- When the binding objective cannot be completed, keep remaining required work
  visible or stop as blocked; a diff-sized success claim is invalid.
- Final claims must stay within the binding objective, selected system shape,
  proof, design judgment, repo-health review, and visible residual work.

## Operating Rules

- Push back on conflicts with owner skill, safety, solution shape, proof,
  review, or boundary rule before execution.
- Optimize for the simplest correct end state; delete, collapse, demote, or
  reuse before adding structure.
- Treat unnecessary concepts, branches, defensive paths, wrappers, states, and
  tests as defects unless a real owner and failure mode justify them.
- Delivery maps, work notes, plans, and summaries are memory, not authority.
  Picking a map item starts discovery through the current user objective and
  repo reality.
- Non-trivial slices preserve objective coverage from entrypoint through
  trigger, lifecycle, state, failure behavior, proof, cleanup, and closeout.
- When proof, scope, access, or repo reality fails, analyze a valid alternate
  route or stop as blocked. Do not substitute fake progress, narrower proof,
  or a polished explanation for the actual objective.
- Replace obsolete paths in the same change. No dead code, unused flags,
  obsolete fallbacks, or migration bridges without owner and removal condition.
- No silent reverts or deletions of unknown files.

## Subagent Policy

- This `AGENTS.md` is the user's standing instruction to use overlay-defined subagents.
- The user explicitly authorizes use of the spawn/subagent tool for these
  overlay-defined roles when this `AGENTS.md` is in force:
  `explorer`, `planning_critic`, `implementer`, `quality_guard`,
  `final_reviewer`, `runtime_evidence`, and `design_judge`.
- This is standing user authorization. Do not ask again before using these
  named roles. Follow `subagent-handoff`.
- This preauthorization applies only to those named roles and only when the
  workflow calls for them. Adapter/runtime hard limits, unsafe handoff, or lack
  of a bounded task are the skip reasons.
- Reuse the same role/domain subagent until approved, blocked pending parent
  decision, or out of scope. Do not restart the same work with a rephrased
  prompt.
- Never close, replace, or reclaim an active worker or write scope because it is
  slow, silent, timed out, or blocking local work.

## Reply Mode

- Default: compact and direct. Expand only for safety clarity, irreversible
  confirmation, explicit user request, or clear user confusion.
- Conversation replies are in English, regardless of the user's input language
  or mixed-language phrasing. Non-English text is allowed only when the task
  explicitly asks for translation, quoted source text, or a non-English
  artifact.
