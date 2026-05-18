---
name: code-review
description: "Use when the user asks for code review or when verified implementation requires final isolated closeout review."
---

# Code Review

Owns isolated skeptical review and report shape.

## Contract

Review against the binding objective, accepted reductions, simplest correct end
state, `design-integrity`, and `readiness-claim`. Do not approve a narrower
task summary, finding, file, diff-only slice, implementer summary, prior
correction, handoff prompt, plan, durable context, or brief.

Plans, waves, context notes, and briefs are context only; their validity is not
evidence that the change is good.

Handoffs route attention; they are not authority. Review authority comes from
the binding user objective, accepted reductions, repo reality, durable context
when useful, readiness claim, design source, and relevant owner docs. If the
handoff narrows, summarizes, or conflicts with that authority, review against
the authority or `BLOCK` for prompt/source mismatch.

Approval is binary: `APPROVE` or `BLOCK`. Approval means:

- the claim-relevant changed surface was reviewed deeply enough to support the
  authoritative claim
- the final shape is the simplest coherent implementation of the objective
- reviewed evidence can support the readiness claim
- no current-scope blocker remains
- delivery-brief support is credible for non-trivial completion

Claim-relevant changed surface means edited paths plus unedited
owner/interface paths needed to judge the authoritative claim and selected
design interface. It is not diff-only, and it is not an unbounded repository
scan.

Apply every owner skill triggered by the binding objective, touched
owner/interface, readiness claim, proof path, and changed artifacts. Do not
duplicate owner-skill doctrine; report the triggered skill, verdict, and
blocker if any.

When `readiness-claim` material risks are in scope, review the readiness-owned
material-risk disposition as claim support. Block unassessed, mis-disposed, or
contradicted current-scope material risk without redefining the lens semantics.

## Check

- Use fresh context and stay read-only.
- Try to falsify the readiness claim through risky paths.
- Ask what the change deleted, collapsed, reused, or avoided; added code, tests,
  docs, or process state must be justified by the objective and owner.
- Check design integrity, stale paths, proof scope, runtime/design coverage,
  readiness-owned material-risk disposition, delivery-brief support, and issue
  disposition.
- Approve only after credible, current-scope, claim-relevant failure paths have
  been pursued or dropped with a stated reason.
- Cite exact `file/path:line` findings.

## Issue Disposition

Every concrete issue is fixed, routed, tracked, or dropped.

- Current-scope blocker: fix now or route through `work-routing`.
- Separate debt outside approval boundary: track through `initiatives-workflow`.
- Accepted temporary debt: requires explicit user acceptance, owner, risk,
  removal condition, and backlog link.
- Taste, speculation, or unevidenced concern: drop.

## Output

Report:

- verdict: `APPROVE` or `BLOCK`
- Binding objective
- Accepted reductions
- Reviewed scope against authoritative claim
- Reviewed-scope sufficiency for `APPROVE`/`BLOCK`
- Existing authority checked
- Authority source inspected
- Prompt/source mismatch
- Plan/design alignment
- Triggered owner skills
- design-integrity verdict
- readiness claim reviewed
- Proof reviewed, including runtime/design evidence when applicable
- Delivery brief support: outcome, end-state shape, evidence map, residuals,
  and context closeout
- findings with location, impact, fix, disposition
- Issue disposition
- residual risks or `none`
