# Review Governance

Owner for approval boundaries, disposition, and completion claims.

## Source Of Truth Map

- This file: approval/disposition rules, review-mode deltas, completion claim contract.
- `code-review`: isolated review wrapper and report shape.
- `final_reviewer`: final isolated closeout reviewer role.
- `review-address`: pre-edit review-feedback triage.
- `code-simplicity`: simplicity lens.
- `adversarial-review`: failure-mode lens.
- `ci.md`: quality-tier semantics.
- `initiatives-workflow.md`: packet proof structure and closeout state.
- `standalone-plans.md`: standalone-plan approval record placement and schema.
- `testing-strategy.md`: proof depth and runtime evidence depth.

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
- No approval while any changed persistent test file lacks the required
  testing-strategy row or carries any testing-strategy invalid reason code.
- No approval while any changed persistent test file fails the additional
  testing-strategy gate:
  - `required-proof`: it is required to prove a changed durable boundary or
    changed regression target with no existing same-layer or lower-layer proof
    already covering that change
  - `durable-gain`: it produces an allowed durable gain for the same
    originally owned durable regression target
- Reject changed persistent tests whose strongest proof is a mutable
  fake-call kwargs bag or cast-heavy JSON spelunking; classify them as
  `mock-choreography`, `low-signal-assertion`, or
  `implementation-coupled`, and do not approve until the assertion reaches a
  public boundary or the file is deleted.
- No approval based on `better than before`, `moved to the right owner`, or
  `good enough for now`.
- Touched-test review must report each changed persistent test file as:
  `<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`.
- Reject helper-extract-only, parameter-reshape-only, file-move-only,
  fixture-churn-only, or reorganize-only persistent-test changes that are not
  required by a changed durable boundary or changed regression target and do
  not produce an allowed durable gain.
- Reject changed persistent test cleanup whose regression target, strongest
  surviving proof, proof layer, persistent-test surface, and invalid
  reason-code state are unchanged.
- Invalid approval patterns: split-only cleanup, weaker replacement of a
  removed strongest assertion, or a parameter matrix that collapses materially
  different contracts or assertion shapes.
- Invalid approval patterns for Python typing: placeholder object casts, broad
  containers or repeated casts where the shape is known, helper widening
  followed by downstream re-narrowing, framework-seam casts bleeding into
  business logic, local duplicate shapes where an imported contract exists,
  local proxy `TypedDict` or `Protocol` types or wrapper casts invented only to
  reach members or retype imported values, raw dict or list casting where a
  real adapter or model exists, `cast(object, ...)` used only to feed a
  validator or parser, sibling tests importing underscore helpers or stubs as
  public support API, or approval based only on green typecheck while the
  runtime contract stays implicit or the typed-boundary proof fails the
  testing-strategy owner rule.
- Invalid approval patterns for boundary and code-shape review: importing
  private helpers or underscore members outside their defining module,
  behavioral `dict`/`list`/`object` bags used as cross-module contracts, the
  same vendor/framework/storage payload shape parsed in more than one owner, or
  a route/service that both parses request/form input and assembles nested
  transport/domain payload dicts without being the declared contract owner,
  duplicate canonicalization for one shared external contract, production
  boundary code branching to test-only or missing-framework fallbacks,
  public helpers exposing parameters or option fields that cannot change any
  valid output,
  dependency modules defining request-scoped transactional workflow wrappers
  or execution policy,
  CLI, factory, or compose entrypoints redefining shared-home or
  runtime-local-state layout/registry policy owned by another module,
  adapters serializing one typed transport contract into raw dict/list payloads
  only for the next owner to accept or re-parse the same contract,
  a change that only relocates a broad contract or parsing problem to another
  owner while preserving the same effective behavior,
  store/runtime/adapter files importing orchestration owners for shared types,
  coordinators/controllers/services hiding cross-instance mutable cache state
  in static or module-level storage, or adapters hiding optional third-party
  dependency availability in import-time module globals.
- For boundary-changing review, reject unless the review can name one owner,
  with file evidence, for each touched role among contract,
  parsing/normalization, lifecycle/bootstrap/recovery, persistence/cache
  state, and failure policy. If a touched role has no clear owner, or the diff
  leaves two places co-owning it, reject.

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
