---
name: subagent-orchestration
description: "Use when subagents should be invoked or routed: delegation decisions, handoff inputs, active-worker handling, and implementer routes."
---

# Subagent Orchestration

Owns delegation decisions, role choice, handoff inputs, worker reuse, and
active-worker handling.

`../../AGENTS.md` owns standing user authorization. `../../agents/roles.md`
owns role names and missions.

## Rule

Delegate only when the handoff preserves the binding objective, accepted
reductions, simplest correct end state, selected owner/interface, readiness
claim, and owned/read-only scope.

Handoffs preserve context. They do not narrow the reviewer question or turn a
plan, durable note, brief, task label, or implementer summary into authority.

Use subagents for bounded discovery, bounded implementation, strategy review,
implementation-shape review, final merge review, runtime evidence, and visual
design judgment. Keep urgent blocking work local when the next step depends on
it.

Default to `explorer` for non-trivial repository discovery when the parent can
ask one bounded question instead of reading broad file sets locally.

Default to `implementer` for non-trivial code/doc edits when the end state,
owner/interface, readiness claim, and owned scope are clear enough to hand off.
A durable context note is not required for a direct-route implementation slice.

## Active Subagents

For any active role/domain, use one loop:

1. Parent gives the smallest complete handoff.
2. Subagent returns work, evidence, approval, rejection, or blocker.
3. Parent integrates only enough to preserve objective, end state, scope,
   durable context, and routing.
4. Follow-up issues return to the same role/domain subagent until approved,
   explicitly blocked pending parent decision, or explicitly out of scope.

Do not spawn a replacement with a rephrased version of the same task to get a
fresh answer. Never close, replace, or reclaim an active worker or write scope
because it is slow, silent, timed out, or blocking local work.

## Role Timing

- `explorer`: before or during planning when repo reality is unclear.
- `planning_critic`: before non-trivial execution or scope expansion; judges
  whether the proposed route/end state should exist.
- `implementer`: executes one bounded slice after scope is clear.
- `quality_guard`: during planning or implementation while work is cheap to
  reshape; judges whether current work advances the end state.
- `final_reviewer`: after implementation and local verification; judges merge
  readiness for the whole changed slice.
- `runtime_evidence`: live-use behavior evidence under `readiness-claim` and
  `runtime-proof`.
- `design_judge`: screenshot/contact-sheet visual-quality approval.

Normal non-trivial implementation loop:

`parent route/end state -> planning_critic when needed -> implementer ->
quality_guard -> same implementer revision loop -> local verification ->
final_reviewer -> delivery brief`

## Handoff

Pass:

- binding objective, accepted reductions, residual gaps
- simplest correct end state and rejected alternatives
- design owner/interface
- readiness claim and required evidence
- role task and owned/read-only scope
- active durable context path when it exists
- artifacts, commands, screenshots, logs, or changed surfaces to inspect
- risks, blockers, and stop conditions

Never ask a reviewer only whether a context note, task label, plan, or diff is well
formed. Ask whether the route or change is the simplest correct way to satisfy
the objective, what smells, and what should be deleted, collapsed, reused,
rewritten, simplified, or blocked.

Stop when delegation would narrow the objective, split one owner across
conflicting workers, require hidden material decisions, or preserve a
current-objective owner defect.
