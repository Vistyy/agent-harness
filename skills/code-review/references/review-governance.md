# Review Governance

Owner for approval boundaries, disposition, and completion claims.

## Source Of Truth Map

- This file: approval/disposition rules, review-mode deltas, completion claim contract.
- `code-review`: isolated review wrapper and report shape.
- `final_reviewer`: final isolated closeout reviewer role.
- `feedback-address`: pre-edit feedback assessment and address flow.
- `code-simplicity`: canonical simplicity gate and bad-shape signal owner.
- `adversarial-review`: failure-mode lens.
- `../../verification-before-completion/references/quality-gate-selection.md`:
  quality-tier semantics.
- `../../initiatives-workflow/references/initiatives-workflow.md`:
  wave lifecycle and closeout state.
- `../../initiatives-workflow/references/wave-packet-contract.md`: packet
  schema, proof-row fields, and task state semantics.
- `../../writing-plans/references/standalone-plans.md`: standalone-plan
  approval record placement and schema.
- `../../testing-best-practices/references/touched-test-gate.md`:
  touched-test rows, invalid reason code gate, `required-proof`, and
  `durable-gain`.
- `../../testing-best-practices/references/proof-strength.md`:
  persistent-test proof validity and source/exact-string limits.
- `../../verification-before-completion/references/runtime-proof-escalation.md`:
  runtime proof escalation.
- `system-boundary-architecture`: boundary and ownership doctrine.

## Core Rules

- Default posture: skeptical. Try to disprove claims.
- No approval while any material issue lacks disposition.
- Default unresolved issue to merge-blocking.
- Compare the change against the binding user objective and any active wave or task intent.
- For non-trivial review, an objective anchor is mandatory. Use the active wave or task anchor when it exists; otherwise use the original request, issue, or review ask.
- Silence, positive tone, or "looks good" is not approval.
- Enumerate all meaningful findings. Do not stop at first blocker.
- Every finding needs exact `file/path:line` evidence.
- A finding may reject bad shape without prescribing the exact fix only when
  the evidence names the violated property, such as unstable owner, state leak,
  weaker proof, overbuilt shape, hidden boundary, awkward wiring, type trust
  loss, or visual/taste property when applicable.
- Review the touched slice as a whole: a real issue counts even if it
  predates the diff or sits outside new lines, if it is still relevant to
  approval.
- A single valid finding can expose wrong owner/component shape. If the
  observed defect is a symptom of bad design, do not approve a symptom-only fix
  without the broader fix or accepted-debt backlog link.
- If 2+ valid findings share the same controller, store, or service authority,
  name the shared cause and assess whether tactical fixes would preserve wrong
  ownership.
- If a local fix exposes a shared-cause or wrong-owner problem, do not approve
  the local fix alone; require the broader fix or a durable backlog link.
- For structural, hotspot, or state-authority slices, a declared owner map must cover every public write path and read-repair path in scope. Any surviving bypass is merge-blocking.
- No approval while any changed persistent test file fails
  `touched-test-gate.md`, including the required disposition row, invalid
  reason code gate, `required-proof`, and `durable-gain` checks.
- No approval based on `better than before`, `moved to the right owner`, or
  `good enough for now`.
- Invalid approval: the implementation matches the packet but the packet
  narrowed or weakened the binding user objective.
- Invalid approval: old complexity was removed without assessing whether the
  resulting owner/component is itself acceptable.
- Diff-myopic review is invalid for non-trivial work. Review the touched
  owner/component, not only changed lines.
- Touched owner/component means the smallest owner whose contract, state,
  lifecycle, design, workflow, or proof the change touches; expand only to
  shared authority required by the change.
- Pre-existing code is not a defense when the change touches, depends on,
  preserves, extends, or proves that owner/component.
- `unacceptable touched-component integrity` means `code-simplicity` found one
  or more must-block bad-shape signals with anchored evidence inside the
  touched owner/component and no accepted-debt backlog link covers it.
- A reviewer must ask whether the observed defect is only a symptom of
  touched-component shape. If yes, the owner/component problem is in scope.
- `not assessed` touched-component integrity is allowed only on `REJECT` or
  `BLOCKED` reports. It is never valid on approval or closeout for
  non-trivial work.
- Accepted touched-component debt requires explicit user acceptance after the
  blocker, risk, recommended reshape, and proposed backlog path were presented.
  The approval or closeout record must link the backlog item.
- Boundary, typing, and code-shape approval must satisfy the applicable
  `system-boundary-architecture` owner docs. For boundary-changing review,
  reject unless the review can name one owner, with file evidence, for each
  touched role among contract, parsing/normalization,
  lifecycle/bootstrap/recovery, persistence/cache state, and failure policy.

## Review Modes

All modes below inherit the core rules. Mode sections add cadence, scope, and required inputs only.

### 0. Planning Gate `quality_guard`

Use before promoting a wave from `discovery-required` to `execution-ready`.

Rules:
- run after discovery says material questions are closed,
- reject while any implementation-shaping decision is still open, implied, or silently delegated,
- approve only when execution can proceed without broad design discretion,
- reject structural, hotspot, or state-authority waves that lack a closed authority map naming owner, write paths, read-repair paths, forbidden bypasses, rejected alternatives, and why scope is not artificially narrowed.

Required inputs:
- wave brief,
- packet draft or equivalent execution breakdown,
- explicit starting points and frozen decisions,
- `Proof Plan`,
- touched owner/component integrity assessment for non-trivial work,
- authority map when structural, hotspot, or state-authority trigger applies.

Promotion rule:
- no explicit `quality_guard` approval, no promotion.

### 1. In-Thread `quality_guard`

Deep iterative review inside the implementation thread.

Rules:
- run after each meaningful implementation chunk or completed task card,
- do not save the first `quality_guard` pass for thread end when work spans multiple task cards, public surfaces, or owner-boundary changes,
- return `APPROVE` or `REJECT`,
- reject while any material issue remains,
- reject structural, hotspot, or state-authority chunks when the authority map is missing, stale, or still leaves one public write or read-repair bypass,
- if review exposes a common-cause boundary flaw, stop tactical patching and route back through planning or authority-map update before more chunk execution.

Required inputs:
- reviewed diff or scope,
- chunk or task-card boundary being reviewed,
- changed public surfaces,
- proof artifacts reviewed,
- touched owner/component, highest inspected scope, integrity verdict,
  must-block signals, and accepted-debt backlog link if any,
- authority map when structural, hotspot, or state-authority trigger applies,
- explicit approve or reject ask.

Invalid approval patterns:
- no explicit verdict,
- parent self-assigns `quality_guard` result,
- first review arrives only after several materially different task clusters already landed,
- narrow file glance while cross-surface behavior changed,
- implied concerns left unstated.

### 2. Final Isolated Review `final_reviewer`

Separate breadth-first review outside the implementation loop.

Rules:
- use `final_reviewer` by default when a subagent is available,
- review the whole slice as one change,
- focus on breadth, cross-surface interaction, architecture coherence, and plan alignment,
- enumerate all meaningful findings,
- include touched owner/component integrity in the closeout verdict,
- if the diff changed after an earlier blocked review, restart from fresh context,
- treat planning-gate and in-thread `quality_guard` approvals as history, not
  final approval,
- when wave or task artifacts exist, cite the plan anchor or user objective reviewed,
- return a closeout verdict.

## Completion Rule

Completion requires the applicable approval surfaces above and acceptance-anchor re-check when wave artifacts exist.

Wave closeout rule:
- `Final review: PENDING SEPARATE REVIEW` is a valid progress state, not approval.
- Do not mark the wave done, delete the packet, or clear the delivery-map entry while final review is pending.
- Closeout needs final separate review `APPROVED`.

Any message claiming done, complete, ready, or approved must include:
- `In-thread quality_guard:` actual verdict plus reviewed scope
- `Touched component integrity:` `acceptable | unacceptable | not assessed`,
  with touched owner/component, highest inspected scope, must-block signals, and
  accepted-debt backlog link when present
- `Verification:` fresh proving command or artifact
- `Final review:` `APPROVED | BLOCKED | PENDING SEPARATE REVIEW`
- For non-trivial work, changed surfaces, required `planning_critic` verdict,
  and residual risks.

Missing field = claim fails.
