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
reductions, objective coverage, target shape, selected owner/interface, evidence
strategy, and owned/read-only scope.
The target shape must still be the simplest correct end state for the binding
objective.

Handoffs preserve context. They are orientation packets, not authority. Pass
the smallest context needed to start; do not pre-decide the answer. Parent
conclusions, plans, work notes, task labels, delivery-map items, summaries, and
implementation claims are hypotheses until checked against the binding
objective, repo reality, owner docs, code, tests, and evidence.

Use subagents for bounded discovery, bounded implementation, strategy review,
implementation-shape review, final merge review, runtime evidence, and visual
design judgment. Keep urgent blocking work local when the next step depends on
it.

Default to `explorer` for non-trivial repository discovery when the parent can
ask one bounded question instead of reading broad file sets locally.

Default to `planning_critic` before non-trivial implementation or scope
expansion. Skip only when the work is local/trivial, the parent cannot form a
bounded handoff yet, or adapter/runtime limits block delegation.

Default to `implementer` for non-trivial code/doc edits when the objective
coverage, target shape, owner/interface, evidence strategy, and owned scope are
clear enough to hand off. A durable note is not required for a small in-thread
implementation slice.

Parent direct implementation of non-trivial work needs a named reason, such as
tight coupling to immediate local investigation, ambiguous write ownership,
adapter/runtime limits, or a slice small enough that delegation adds no value.
Direct parent implementation remains bound by `../delivery-workflow/SKILL.md`
implementation-slice and blocker rules.

Default to `quality_guard` while non-trivial shape or implementation is still
cheap to change.

Default to `final_reviewer` after non-trivial implementation and local
verification, before completion is claimed.

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
  whether the active note/plan correctly interprets the objective.
- `implementer`: executes one bounded slice after scope is clear.
- `quality_guard`: during planning or implementation while work is cheap to
  reshape; judges whether current work advances the end state.
- `final_reviewer`: after implementation and local verification; judges merge
  readiness for the whole changed slice.
- `runtime_evidence`: live-use behavior evidence under `delivery-workflow` and
  `runtime-proof`.
- `design_judge`: screenshot/contact-sheet visual-quality approval.

Normal non-trivial implementation loop:

`parent objective coverage/target shape -> planning_critic when needed -> implementer ->
quality_guard -> same implementer revision loop -> local verification ->
final_reviewer -> closeout`

## Handoff

Pass:

- binding objective, accepted reductions, residual gaps
- objective coverage, target shape, and rejected alternatives
- design owner/interface
- valid slice, expected change surface, and cleanup/residual boundary for
  implementation handoffs
- evidence strategy and required proof artifacts
- role task and owned/read-only scope
- active durable context path when it exists
- artifacts, commands, screenshots, logs, or changed surfaces to inspect
- risks, blockers, and stop conditions

Never ask a reviewer only whether a context note, task label, plan, or diff is
well formed. Ask whether the note correctly interprets the objective, whether
the change is the simplest coherent way to satisfy it, what proof could pass
while behavior is absent, and what should be deleted, collapsed, reused,
rewritten, simplified, or blocked.

Reviewer handoffs must ask for falsification, not validation of the parent
summary. If the handoff narrows or pre-decides the answer, the reviewer reports
prompt/source mismatch and reviews against higher authority.

Stop when delegation would narrow the objective, split one owner across
conflicting workers, require hidden material decisions, or preserve a
current-objective owner defect.
