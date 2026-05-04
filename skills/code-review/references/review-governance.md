# Review Governance

Owns approval boundaries, review modes, disposition, and review coverage.
`../../verification-before-completion/SKILL.md` owns final completion claims.

## Core Rules

- Review skeptically. Try to disprove the claim.
- Do not approve from politeness, momentum, effort, partial improvement, or
  plausible acceptance. Approval means the binding claim survives review
  against required evidence.
- Required gates are blocking under `harness-governance`: missing evidence is
  `blocked`; contradictory evidence inside the claim is `reject`.
- Pressure-test realistic non-happy paths: hidden assumptions, invalid or stale
  inputs, partial updates, retries/races, boundary misuse, unsafe defaults, and
  proof that covers only the nominal path.
- Binding objective = original user objective plus explicitly accepted
  reductions. Task labels, packets, implementer summaries, and reviewer prompts
  do not replace it.
- Reject when implementation, proof, review request, or closeout satisfies a
  smaller invented objective.
- Reject mis-scoped review requests. A reviewer approves against the binding
  objective, not the prompt they were handed. Missing binding objective or
  accepted reductions is blocking for non-trivial review.
- Reject shallow breadth implementation when the objective required owner-depth.
  Touching many requested areas lightly is not completion evidence.
- Reject patch-over fixes that preserve a current-objective owner defect.
- Default unresolved material issues to blocking.
- Enumerate material findings with exact `file/path:line` evidence.
- Non-trivial review assesses the touched owner/component, not only the diff.
- Touched owner/component is the smallest owner whose contract, state,
  lifecycle, design, workflow, or proof the change touches; expand only to
  required shared authority.
- `not assessed` touched-component integrity is never valid on approval.
- Accepted debt needs explicit user acceptance plus backlog owner, risk, and
  removal condition.
- `NON-BLOCKING` is only for residuals outside the binding claim.

## Review Modes

### Planning Gate `quality_guard`

Approves execution readiness only after discovery/planning closes scope,
decisions, proof, deferrals, and touched-owner integrity.

Required inputs:
- binding objective, accepted reductions, residual gaps
- plan/wave/packet anchor
- proof plan
- touched owner/component integrity
- authority map when structural, hotspot, or state-authority work is in scope

No explicit approval, no promotion.

### In-Thread `quality_guard`

Approves or rejects meaningful implementation chunks.

Required inputs:
- reviewed diff or scope
- binding objective, accepted reductions, residual gaps
- changed public surfaces
- proof artifacts
- touched owner/component integrity
- explicit approve/reject ask

Reject when one more material fix, simplification, proof correction, or
current-objective owner repair is justified now.

### Final Isolated Review `final_reviewer`

Reviews the whole changed slice after implementation and fresh verification.

Required inputs:
- binding objective, accepted reductions, residual gaps
- changed surfaces and base/diff range
- proof artifacts and runtime evidence when applicable
- in-thread `quality_guard` history
- touched owner/component integrity

Treat earlier approvals as history, not final approval. Reject if the handoff
omits the binding objective or final wording exceeds proof/review scope.
Reject mis-scoped handoffs that ask review to approve less than the binding
objective without an accepted reduction.

## Review Coverage For Completion

Review approval is an input to completion, not the completion gate.

Review reports define:
- reviewed scope
- approval scope
- proof and runtime evidence reviewed
- residual risks

## Report Minimum

Approval or closeout reports name:
- reviewed scope
- verdict
- touched owner/component and integrity
- proof reviewed
- final review status
- residual risks or `none`
