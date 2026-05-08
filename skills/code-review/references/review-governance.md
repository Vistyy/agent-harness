# Review Governance

Owns code-review approval, review modes, issue disposition, and review
coverage. `../../verification-before-completion/SKILL.md` owns final completion
claims.

## Approval Contract

Review approval is binary: `APPROVE` or `BLOCK`.

`APPROVE` means the binding objective, accepted reductions, touched
owner/component, proof, and required gates survive skeptical inspection. Missing
or vague approval evidence is `BLOCK`.

For non-trivial review, approval is invalid unless the report names:
- binding objective and accepted reductions
- reviewed scope and approval boundary
- why that boundary is sufficient
- existing authority checked before approving new behavior
- touched-owner integrity
- proof reviewed
- issue disposition, or `none`

Review the binding objective, not task labels, packets, summaries, or narrow
handoffs. Reject smaller invented objectives, shallow breadth, patch-over
fixes, diff-only review, unassessed touched-owner integrity, and approval whose
highest inspected scope is narrower than the approval boundary.

## Issue Disposition

Every concrete issue found during review is fixed, routed, tracked, or dropped.

- current-scope blocker: fix directly or route through `work-routing`; never
  ordinary backlog
- small safe separate issue: fix when repair stays inside the current route and
  proof burden
- large, risky, or separately owned issue outside the approval boundary: track
  as discovered separate debt through `initiatives-workflow`
- accepted temporary debt inside the approval boundary: requires explicit user
  acceptance, owner, risk, removal condition, and backlog link
- taste, speculation, or unevidenced concern: drop

Findings cite exact `file/path:line`, problem, impact, and required fix.

## Review Modes

`quality_guard` applies this contract to planning readiness and implementation
chunks. Reject when one more concrete fix, simplification, proof correction, or
current-scope owner repair is required.

`final_reviewer` applies this contract to the whole changed slice after
implementation and fresh verification. Earlier `quality_guard` approvals are
history, not final approval.

Reviewers verify required runtime and design gate coverage; they do not replace
runtime proof or product design judgment. Broad UI closeout requires
`design_judge` coverage for the declared project design source, project design
source requirements, applicable project-local artifacts, and the same claim;
block missing, stale, blocked, rejected, or narrower coverage. Final review
verifies coverage and does not decide the design verdict.

## Completion Interface

Review approval is evidence for completion, not completion itself.

Reports state reviewed scope, approval boundary, verdict, touched
owner/component and integrity, proof reviewed, issue disposition, final review
status when applicable, and residual risks or `none`.
