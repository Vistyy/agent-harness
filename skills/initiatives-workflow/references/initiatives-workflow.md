# Initiatives Workflow

Wave-first workflow. Minimal ceremony. One owner per truth class.

## Source Of Truth

- durable intent: `docs-ai/docs/**`
- queue: `docs-ai/current-work/delivery-map.md`
- planning-gate draft packet:
  `docs-ai/current-work/<wave-id>/wave-execution.draft.md`
- execution packet: `docs-ai/current-work/<wave-id>/wave-execution.md`
- backlog detail:
  `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md`

Apply `policy-single-source-of-truth.md` when overlaps appear.

## Wave ID

- legacy numeric IDs stay valid
- new IDs use lowercase ASCII `<area>-<topic>-<sequence>`
- once scheduled, ID is durable
- if merge duplicates ID, rename only branch-local conflict

## Delivery Map Rules

`delivery-map.md` is queue and delegation surface.

- order by recommended execution order
- lanes are serialized by default
- same-lane parallel work needs explicit `Parallel-safe after: ...`
- cross-lane work is parallel-safe unless stated otherwise
- execution detail stays out of map
- `discovery-required` waves are ideas only
- only `execution-ready` waves may link canonical packets
- `done` and `retired` waves leave map
- draft packets never appear in map

## Persist And Defer

Important next work must become active wave, new wave, backlog item, or mobile
parity item in the same change. Never leave it only in prose.

Rules:
- future work or debt explicitly discussed during planning/review must end as
  fixed now, active wave, new wave, mobile parity item, or backlog item
- backlog entries are short descriptions, not executable plans
- each backlog item needs one slug in a queue bucket or mobile parity queue and
  one matching detail file under `docs-ai/current-work/backlog/`
- use bucket placement for timing posture instead of extra fields
- if unclear, default to `Deferred Backlog`
- trigger bucket needs one crisp durable trigger
- `Mobile-Only Backlog` owns durable mobile-only detail; `Mobile Parity Queue`
  stays queue-only follower work
- ask the user only when the decision changes user-visible behavior, release
  priority, or a boundary/proof choice not already closed in durable doctrine
- otherwise default locally, keep the better target architecture, and phase it
  if needed
- when execution or review exposes common-cause structural debt, prefer one
  reshaped wave over stacked follow-up backlog churn

## Backlog To Wave Promotion

1. Choose owning backlog item.
2. Create wave brief under `docs-ai/docs/initiatives/waves/<wave-id>.md` with
   `**Status:** discovery-required`.
3. Add wave to ordered queue in `delivery-map.md`.
4. Remove promoted backlog slug in same change.
5. Delete the absorbed backlog detail file in same change.
6. If only part of the old backlog scope was absorbed, split the remaining
   work into one or more new backlog/mobile-parity items before deleting the
   original detail file.
7. Keep sibling follow-up work in backlog/mobile-parity state.
8. Run `planning-intake`.
9. If planning gate needs packet review, create `wave-execution.draft.md`.
10. Promote to `execution-ready` only after intake closes open questions and
    planning gate passes.
11. In same change, promote draft packet to canonical packet, update brief
    status, and link packet from map if lane uses packet links.
12. If a backlog slug or mobile-parity item was absorbed, remove it from the
    queue in the same change.

Rules:

- no item lives as both active wave and backlog slug
- no item lives as both active wave and backlog detail file
- no canonical packet while wave is `discovery-required`
- if only part is ready, split backlog item or create narrower wave
- wave briefs and feature docs must not keep absorbed backlog detail links once
  the wave becomes the active owner

## Wave Status Contract

Allowed statuses:
- `discovery-required`
- `execution-ready`
- `done`
- `retired`

Meaning:
- `discovery-required`: idea only, not executable
- `execution-ready`: planning closed enough for execution
- `done`: durably closed
- `retired`: original scope not executed; keep only the owner state still
  needed after supersession, absorption, or deferment cleanup

Rules:
- format status exactly as `**Status:** <value>`
- `execution-ready` briefs must include one plain-language
  `## User objective`, plus `## Acceptance Anchors` and
  `## Durable Audit Record`
- closed `done` and `retired` briefs should not stay as full execution-era
  briefs once their still-live history is rehomed
- closed `done` and `retired` briefs may end in one of two shapes:
  - deleted, after rehoming and reference cleanup are complete
  - slim closed brief at the same path, only when non-wave repo references
    still need the path after rehoming
- legacy full closed briefs remain temporarily valid during the historical
  cleanup migration, but they are migration debt rather than a preferred final
  state
- slim closed briefs must keep exact status plus:
  - `## Closed Wave Pointer`
  - `## Replacement References`
  - and must not keep `## User objective`, `## Acceptance Anchors`, or
    `## Durable Audit Record`
- `## Acceptance Anchors` and `## Durable Audit Record` each contain one JSON
  fenced block
- packet-backed `execution-ready` briefs must record proof classification,
  expected evidence path, and `planning_critic` provenance inside the existing
  planning-gate object
- `discovery-required` waves may stay skeletal
- proof-gap governance waves add `## Proof-Gap Disposition Registry` before
  promotion

## Execution-Ready Gate

Do not promote while:

- material implementation-shaping decision is unresolved
- discovery/audit/disposition still leaks into execution
- two competent implementers could still choose materially different owner,
  proof, state-authority, runtime, compatibility, rollout, migration, storage,
  or public-behavior path

Treat state authority, ownership boundaries, public behavior, proof path,
migration/compatibility stance, runtime posture, forbidden legacy paths,
technology/provider choices that affect architecture or public contracts, exact
values, thresholds, MIME/format policy, bridges, cleanup ownership, and
verification scope as material unless explicitly delegated or durably deferred.

Treat local helper names, component/function decomposition, exact idiom, and
framework mechanics as implementer-local when owner skills/docs already close
the correct approach and those choices do not change a material path.

Execution-ready planning must:
- name proof class and expected evidence path for important claims
- name observability/external-dependency ownership when those are real blockers
- shape around common cause instead of keeping a wave artificially small
- close one explicit authority map for structural, hotspot, or state-authority
  work
- route non-trivial planning through `planning_critic` before planning-gate
  `quality_guard`
- record planning-gate `quality_guard` approval
- for packet-backed execution-ready planning, record `planning_critic`
  provenance inside `planning_gate.planning_critic` before planning-gate
  `quality_guard`; a packet-backed wave must not promote without both records
- keep `planning_critic` as critic pressure only; planning-gate
  `quality_guard` remains the promotion gate
- declare one packet delegation posture: `implementer-eligible` or
  `parent-only`

Non-trivial planning includes structural, hotspot, state-authority,
delegation-policy, UI / taste doctrine, proof-gap, and non-trivial wave-shaping
work. Tiny local fixes do not become heavyweight planning only because this
critic rule exists.

`implementer-eligible` is the default. `parent-only` needs one explicit reason
code in the packet:
- `packet-declared-parent-only`
- `repeated-implementer-handback`
- `tool-or-runtime-limit`
- `shared-file-churn`
- `tiny-local-followup`

Delegable task cards still need one bounded autonomy envelope with owned
surfaces, locked invariants, allowed local decisions, stop-and-handback
triggers, and proof rows.

## Packet Contract

Canonical packet:

- `docs-ai/current-work/<wave-id>/wave-execution.md`

Draft packet during planning gate:

- `docs-ai/current-work/<wave-id>/wave-execution.draft.md`

### Task State Semantics

Task state stays coarse.

Allowed packet task states:
- blank
- `done`
- `blocked`

Meaning:
- blank: task is not yet closed
- `done`: all scoped implementation obligations, cleanup/removal obligations,
  review gates, and proof rows are satisfied
- `blocked`: next required move depends on an external dependency or explicit
  user action

Rules:
- do not invent extra task states to carry nuance that belongs in proof rows,
  blocker entries, or task evidence
- do not mark task `done` while any scoped cleanup/removal/demotion item is
  still intentionally deferred
- do not mark task `done` while any required hosted/runtime proof row remains
  unsatisfied
- use `blocked` only when the next required action is truly external; otherwise
  leave the state blank and keep working
- `Execution outcome` text in task sections must match the task-row state

Draft rules:

- same layout as canonical packet
- no map links
- not active execution state
- promote to canonical only in same change that records planning approval

Use one elastic packet layout. No alternate packet shapes.

Required sections:

1. `Scope And Execution Posture`
2. `Task Plan`
3. `Proof Plan`
4. `Execution State`

Packet rules:

- keep wave-specific evidence expectations only
- raw runtime artifacts live under `.artifacts/runtime/**`
- include `System-boundary trigger` with value `triggered` or `not-triggered`
- include `Implementer delegation posture`
- include `Parent-only rationale`; use `none` unless posture is `parent-only`
- include `Planning Exceptions`; prefer `none`
- `implementer-eligible` is the preferred default; `parent-only` must record a
  concrete reason it is safer or lower-risk than delegation
- structural work must set `System-boundary trigger: triggered` and include
  `## System-Boundary Architecture Disposition`
- non-structural work sets `System-boundary trigger: not-triggered` and may
  omit the section entirely
- the canonical packet template keeps one conditional
  `System-Boundary Architecture Disposition` appendix slot for that triggered
  case
- structural, hotspot, or state-authority work must include the authority map
  fields: changed authorities/contracts, single owner after change, public
  write paths, read-repair paths, forbidden bypass paths, rejected
  alternatives, why scope is not artificially narrowed, and stable-to-extend
  expectation
- `implementer-eligible` packets must keep allowed implementer decisions minor
  and local to one task card envelope
- allowed local decisions must not include state-authority shape, owner
  boundary, public behavior, proof path, migration/compatibility stance,
  runtime posture, forbidden legacy path, or material technology/provider
  choice
- implementer-eligible task cards require the material handoff boundary:
  outcome, scope, owned files/surfaces, locked invariants, allowed local
  implementer decisions, stop-and-handback triggers, proof rows, and deferred
  follow-up disposition
- starting files/symbols, existing patterns, and implementation notes are
  optional execution hints; include them when they reduce ambiguity, but do not
  require them as ceremony
- task cards are outcome-and-proof shaped, not command lists: state the success
  condition, the proof that rejects a weaker implementation, and then expected
  commands or artifacts
- multi-task execution must chunk task cards so `quality_guard` can review each
  meaningful boundary or public-surface change separately; do not hide several
  materially different task clusters inside one first review pass
- proof rows assigned to a task define the implementer's task-local verification
  obligations; handback should leave those checks green or return an explicit
  blocker
- structural, hotspot, or state-authority task plans must migrate every listed
  write/read-repair path to the declared owner before follow-on cleanup or
  proof-polish tasks
- task plans must not intentionally leave already-visible owned-scope hygiene,
  decomposition, awkward-wiring, or type-rigor debt for a later pass unless
  packet records explicit user-approved durable exception
- `proof_plan` records only important claims materially advanced by wave
- each proof row includes:
  - `proof_id`
  - `task_slug`
  - `anchor_ids`
  - `claim`
  - `material_variants`
  - `proof_classification`
  - `owner_layer`
  - `exact_proof`
  - `expected_evidence`
  - `counterfactual_regression_probe`
  - `status`

Packet gating:

- `discovery-required`: no canonical packet
- `execution-ready`: packet required
- `done` and `retired`: no packet

## Closeout

- keep packet until final execution window, proof, and required review loops
  are done
- update packet with final evidence before closeout
- reconcile or remove the durable brief in same closeout window
- `Final review: PENDING SEPARATE REVIEW` is not closeable
- delete packet only as last closeout act
- no wave is `done` while required review or verification is pending or blocked
- do not report a wave closed while
  `docs-ai/current-work/<wave-id>/wave-execution.md` still exists

When wave closes:

- remove delivery-map entry
- delete packet
- rehome any still-live user objective, acceptance-anchor outcomes, durable
  audit rationale, and follow-up state into the real owner doc or backlog item
  before slimming or deleting the closed brief
- run a repo-wide exact-path scan for
  `docs-ai/docs/initiatives/waves/<wave-id>.md`
  - preferred helper: `just wave-brief-refs <wave-id>`
- if non-wave references still remain after rehoming, replace the full closed
  brief with a slim closed brief at the same path
- otherwise delete the closed brief
- wave-only references never justify keeping a full closed brief; update or
  remove them in the same change
- `done` and `retired` follow the same delete-or-slim rule; `retired` no
  longer implies history is kept by default
- until the historical cleanup pass finishes, older full closed briefs may
  remain temporarily; treat them as migration debt, not as the preferred
  closeout shape

All three happen in same change.

Slim closed brief shape:

```md
# Wave <wave-id> — <wave-title>

**Status:** done

## Closed Wave Pointer

<one short sentence covering outcome and why this path still exists>

## Replacement References

- <owner doc / successor wave / backlog item>
```

Rerun-safe rule:

- execution-ready wave keeps one queue entry and one packet path
- failed verification or pending review resumes from same state
- partial closeout cleanup is forbidden
- interrupted delegated verification is `incomplete` and must be rerun

## Task Sizing

If task is too large or ambiguous, split it or reshape it through
`planning-intake`. Do not pick worse architecture just to keep a wave small,
and do not reintroduce per-task spec/plan artifacts.

## Taxonomy Maintenance

- keep work under existing feature when it fits durable contract
- split/add feature when repeated waves/backlog keep forcing awkward placement
- prefer rehome under existing initiative before creating new initiative
- new initiative only for real long-lived ownership boundary

If audit finds missing durable owner boundary, update taxonomy and rehome work
in same change.

`Later` without repo state is incomplete. No silent debt acceptance.
