# Review Governance

Owner for approval boundaries, disposition, and completion claims.

## Source Of Truth Map

- This file: approval/disposition rules, review-mode deltas, completion claim contract.
- `code-review`: isolated review wrapper and report shape.
- `final_reviewer`: final isolated closeout reviewer role.
- `review-address`: pre-edit review-feedback triage.
- `code-simplicity`: simplicity lens.
- `adversarial-review`: failure-mode lens.
- `../../verification-before-completion/references/quality-gate-selection.md`:
  quality-tier semantics.
- `../../initiatives-workflow/references/initiatives-workflow.md`:
  wave lifecycle and closeout state.
- `../../initiatives-workflow/references/wave-packet-contract.md`: packet
  schema, proof-row fields, and task state semantics.
- `../../writing-plans/references/standalone-plans.md`: standalone-plan
  approval record placement and schema.
- `../../testing-best-practices/references/testing-strategy.md`:
  touched-test remediation and persistent-test validity.
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
- If 2+ valid findings share the same controller, store, or service authority, name the shared cause and assess whether tactical fixes would preserve wrong ownership.
- If a local fix exposes a shared-cause or wrong-owner problem, do not approve
  the local fix alone; require the broader fix or a durable backlog link.
- For structural, hotspot, or state-authority slices, a declared owner map must cover every public write path and read-repair path in scope. Any surviving bypass is merge-blocking.
- No approval while any changed persistent test file fails
  `testing-strategy.md`, including the required disposition row, invalid reason
  code gate, `required-proof`, and `durable-gain` checks.
- No approval based on `better than before`, `moved to the right owner`, or
  `good enough for now`.
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
- `Verification:` fresh proving command or artifact
- `Final review:` `APPROVED | BLOCKED | PENDING SEPARATE REVIEW`

Missing field = claim fails.
