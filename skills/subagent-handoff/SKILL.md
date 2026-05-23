---
name: subagent-handoff
description: "Use when deciding whether to delegate to a subagent or reviewer, preparing a handoff, routing explorer/planning_critic/implementer/quality_guard/final_reviewer/runtime_evidence/design_judge, or handling follow-up with an active subagent."
---

# Subagent Handoff

Owns delegation decisions, role choice, handoff inputs, worker reuse, and
active-worker handling.

`../../AGENTS.md` owns standing user authorization. `../../agents/roles.md`
owns role names and missions.

## Rule

Delegate only when the handoff preserves the binding objective, accepted
reductions, target shape, selected owner/interface, evidence strategy, and
owned/read-only scope.

Handoffs are orientation packets, not authority. Parent conclusions, plans,
work notes, summaries, and implementation claims are hypotheses until checked
against the objective, repo reality, owner docs, code, tests, and evidence.

Use subagents for bounded discovery, bounded implementation, planning critique,
implementation-shape review, final review, runtime evidence, and visual design
judgment. Keep urgent blocking work local when the next step depends on it.

Use `planning_critic` before risky planning, architecture, scope expansion, or
work where the objective could be misread. Use `quality_guard` after a
non-trivial required slice has a real direction or draft diff, before that
direction hardens into dependent slices. Use `final_reviewer` after
non-trivial implementation and verification, with required-slice and
discovery-routing state, before completion is claimed.

Use `implementer` for bounded code/doc edits when the target shape,
owner/interface, evidence strategy, and write scope are clear enough to hand
off. Skip subagents for tiny local edits with direct proof and low blast radius.

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
- `planning_critic`: before risky planning, implementation, or scope expansion.
- `implementer`: executes one bounded slice after scope is clear.
- `quality_guard`: mid-slice after non-trivial required-slice implementation
  begins, before dependent work compounds a wrong shape.
- `final_reviewer`: after implementation and verification for non-trivial work,
  with required-slice and discovery-routing state.
- `runtime_evidence`: live-use behavior evidence under `verify-work`.
- `design_judge`: screenshot/contact-sheet visual-quality approval.

Normal non-trivial loop:

`shape objective -> planning_critic when risk warrants -> implementer draft or
parent draft -> quality_guard for non-trivial slices -> same implementer
revision loop -> verify work -> final_reviewer for non-trivial completion ->
closeout`

## Handoff

Pass:

- binding objective, accepted reductions, and residual gaps
- target shape, owner/interface, and rejected alternatives
- required slice, routed discovery findings, expected change surface, and
  cleanup/residual boundary
- evidence strategy and required proof artifacts
- role task and owned/read-only scope
- active durable context path when it exists
- artifacts, commands, screenshots, logs, or changed surfaces to inspect
- risks, blockers, and stop conditions

Reviewer handoffs require falsification, not validation of the parent summary.
Require the reviewer to check objective preservation, proof substitution, and
unnecessary concepts, branches, wrappers, states, defensive paths, tests, docs,
or proof entrypoints that must be deleted, collapsed, rewritten, or blocked.

Stop when delegation would narrow the objective, split one owner across
conflicting workers, require hidden material decisions, or preserve a
current-objective owner defect.
