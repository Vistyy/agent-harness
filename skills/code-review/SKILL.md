---
name: code-review
description: "Use when the user asks for code review or when verified implementation requires final isolated closeout review."
---

# Code Review

Owns isolated skeptical review and report shape.

## Contract

Review against the binding objective, accepted reductions, `design-integrity`,
and `readiness-claim`. Do not approve a narrower task summary, diff-only slice,
or handoff prompt.

Handoffs route attention; they are not authority. Review authority comes from
the binding user objective, accepted reductions, and any durable
objective/design/readiness/packet source. If the handoff narrows or conflicts
with that authority, block unless the authority was explicitly revised.

Apply every owner skill triggered by the binding objective, touched
owner/interface, readiness claim, proof path, and changed artifacts. Do not
duplicate owner-skill doctrine; report the triggered skill, verdict, and
blocker if any.

Approval is binary: `APPROVE` or `BLOCK`. Approval means no current-scope
blocker remains and reviewed evidence can support the readiness claim.

## Check

- Use fresh context and stay read-only.
- Try to falsify the readiness claim through risky paths.
- Check design integrity, stale paths, proof scope, runtime/design coverage,
  and issue disposition.
- For broad UI claims, review coverage only: project design source, project
  design source requirements, project-local artifacts, and design verdict must
  cover the same claim. Block missing, stale, blocked, rejected, or narrower
  coverage. Review does not decide the design verdict.
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
- reviewed scope and Approval boundary
- Boundary sufficiency
- Existing authority checked
- Authority source inspected
- Prompt/source mismatch
- Plan/design alignment
- Triggered owner skills
- design-integrity verdict
- readiness claim reviewed
- Proof reviewed, including runtime/design evidence when applicable
- findings with location, impact, fix, disposition
- Issue disposition
- residual risks or `none`
