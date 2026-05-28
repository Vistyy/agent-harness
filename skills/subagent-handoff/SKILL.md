---
name: subagent-handoff
description: "Route and manage bounded subagent delegation or reviewer handoffs. Use when deciding whether to delegate, preparing handoffs, routing explorer/planning_critic/implementer/quality_guard/final_reviewer/runtime_evidence/design_judge, or handling active-subagent follow-up. Use this skill for delegation mechanics only; it does not replace parent ownership of objective, integration, or final claims."
---

# Subagent Handoff

Owns delegation decisions, role choice, handoff inputs, worker reuse, and
active-worker handling.

`../../AGENTS.md` owns standing user authorization. `../../agents/roles.md`
owns role names and missions.

## Rule

Delegate only when the handoff preserves the binding objective, accepted
reductions, target shape, selected owner/interface, atomic claim boundaries,
evidence strategy, and owned/read-only scope.

Handoffs are orientation packets, not authority. Parent conclusions, plans,
work notes, summaries, and implementation claims are hypotheses until checked
against the objective, repo reality, owner docs, code, tests, and evidence.
Reference existing artifacts instead of duplicating them, name suggested
owners/skills and stop conditions, and do not include secrets or sensitive
context.

Use subagents for bounded discovery, bounded implementation, planning critique,
implementation-shape review, final review, runtime evidence, and visual design
judgment. Keep urgent blocking work local when the next step depends on it.

Use `explorer` only for discovery, inventory, context mapping, and open
questions. Explorer output is context, not review evidence. Never substitute
`explorer` for `quality_guard` because a review task is read-only. If a
bounded surface needs code review, use `quality_guard` by default; if
`quality_guard` is unavailable, stop or ask instead of downgrading to
discovery.

Use `planning_critic` before risky planning, architecture, scope expansion, or
work where the objective could be misread. It reconstructs objective, target
state, owner model, and atomic claim boundaries. Use `quality_guard` after a
non-trivial required claim has a real direction or draft diff, before bugs,
drift, unreadable code, or bad structure compound. It reconstructs the assigned
claim and enough lifecycle context to judge implementation quality and plan
validity; dependent work should not continue until current-scope findings are
fixed, routed, or explicitly blocked for parent decision. Use `final_reviewer`
after non-trivial implementation and verification, with required-claim,
discovery-routing, proof, cleanup, artifact-disposition, and
finding-disposition state, before completion is claimed.

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

- `explorer`: before or during planning when repo reality is unclear; returns
  maps and questions, not code-review findings or approve/block verdicts.
- `planning_critic`: before risky planning, implementation, or scope expansion;
  reconstructs objective, target state, owner model, and atomic claim
  boundaries.
- `implementer`: executes one bounded slice after scope is clear.
- `quality_guard`: default bounded code-review role and early code-quality gate
  after non-trivial required-claim implementation begins; reconstructs the
  assigned claim and blocks continuation on current-scope correctness, quality,
  objective, proof, owner, or simplicity defects.
- `final_reviewer`: final merge-readiness gate after implementation and
  verification for non-trivial work; reconstructs whole objective coverage from
  required claims, discovery-routing, prior-finding, proof, cleanup, artifact
  disposition, and residual-work state.
- `runtime_evidence`: live-use behavior evidence under `verify-work`.
- `design_judge`: screenshot/contact-sheet visual-quality approval.

Normal non-trivial loop:

`probe/shape/slice objective -> explorer when repo reality is unclear ->
planning_critic when risk warrants -> implementer draft or parent draft ->
quality_guard for non-trivial claims -> same implementer revision loop ->
verify work -> final_reviewer for non-trivial completion -> closeout`

## Handoff

Pass:

- binding objective, accepted reductions, and residual gaps
- target shape, owner/interface, and rejected alternatives
- required atomic claim, routed discovery findings, expected change surface, and
  cleanup/residual boundary
- evidence strategy, required proof, and any available proof artifacts
- role task and owned/read-only scope
- active durable context path when it exists
- artifacts, commands, screenshots, logs, or changed surfaces to inspect
- risks, blockers, and stop conditions

Reviewer handoffs require independent reconstruction and convergence, not
validation of the parent summary. Require the reviewer to reconstruct the
role-bounded objective/claim/proof context from repo evidence, compare it with
the parent story, and return a convergence verdict. Require checks for
objective preservation, proof substitution, current-scope bugs, implementation
quality, pre-existing issue disposition, missed simplification/unification, and
unnecessary concepts, branches, wrappers, states, defensive paths, tests, docs,
or proof entrypoints that must be deleted, collapsed, rewritten, fixed, routed,
or blocked.

Stop when delegation would narrow the objective, split one owner across
conflicting workers, require hidden material decisions, or preserve a
current-objective owner defect.
