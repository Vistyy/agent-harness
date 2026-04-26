# Testing Strategy

Goal: protect real behavior with cheapest high-signal proof.

This is the canonical owner for touched-test remediation, exact-string and
source-text limits, and proof-depth decisions. Planning-intake should only
carry shaping and promotion pressure.

Coverage count is not goal. Bad tests are debt. Delete, shrink, rewrite, or
move them when touched.

Examples and references live in
`../testing-best-practices/SKILL.md`.

## Hard Gate

For every changed persistent test file in the diff:

- record exactly one row:
  `<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`
- `keep` is allowed only when the row has `none`
- `shrink`, `rewrite`, and `delete` require at least one invalid reason code
- if any invalid reason code applies, `keep` is forbidden
- `better than before`, `moved to the right owner`, helper extraction,
  explanation, or reviewer preference do not override this gate
- review approval is invalid if any changed persistent test file lacks a row or
  keeps any invalid reason code
- in addition to the row gate, each changed persistent test file must satisfy
  at least one of these:
  1. `required-proof`: the file is required to prove a changed durable
     boundary or changed regression target in the same slice, no existing
     same-layer or lower-layer proof already covers that changed boundary or
     target, and the changed file rejects one named regression introduced by
     that change
  2. `durable-gain`: for the same originally owned durable regression target
     previously represented by that file, the change produces an allowed
     durable gain
     Allowed durable gains are limited to:
     - `stronger-proof`: strictly stronger surviving proof of the same target
     - `lower-layer-replacement`: replacement of a higher-layer persistent
       proof with an equally strong or stronger lower-layer proof that reduces
       higher-layer persistent-test surface
     - `smaller-surface`: fewer persistent tests or files for the same target
       and same-or-stronger surviving proof
     - `reason-code-removal`: removal of one or more invalid reason codes from
       the owned persistent-test slice
  Re-labelling the contract does not count as a changed regression target or
  as a durable gain.
  Pure helper extraction, parameter reshaping, file moves, fixture/support
  churn, or other reorganization that leaves regression target, strongest
  surviving proof, proof layer, and persistent-test surface unchanged is
  invalid.

For a new persistent test:

- add it only when a durable boundary changed, no existing same-layer or
  lower-layer proof already covers that boundary, and the new test rejects one
  named regression
- otherwise do not add it

## Proof Classes

- `automated-suite-provable`: correct persistent automated proof is enough
- `runtime-provable`: claim depends on composed runtime, UI, wiring, env, or
  process boundary
- `multi-proof-required`: persistent and runtime proof both required
- `not-reliably-provable-with-current-harness`: harness cannot honestly prove
  full claim

Rules:

- choose smallest honest class
- do not downgrade runtime or multi-proof claims for convenience
- multi-proof claims must name both legs
- weakly provable claims must narrow guarantee or schedule follow-up

## Proof Strength Rules

- transaction claims prove transaction state, not helper flow or object
  identity
- provenance/ownership claims prove real owner path, not monkeypatched
  surrogate
- do not use isinstance, hasattr, getattr, vars/__dict__, or type(x) is ...
  to recover weak contracts, repeated narrowing, or private wiring; use them
  only for real dynamic-boundary validation or explicit dispatch
- in tests, class-name/module-string assertions are valid only when that
  literal is the shipped contract; otherwise prove the public
  factory/constructor boundary or observable behavior
- do not prove a public boundary by capturing fake kwargs into a mutable bag
  and asserting the bag contents; that is mock choreography unless the bag
  itself is the shipped contract
- do not prove a typed transport contract by casting response.json() into
  broad dict/list shapes and spelunking members; assert the typed
  adapter/model boundary or move the proof to contract/integration
- if a test needs new support/capture/harness machinery and the strongest
  surviving assertion still does not prove a stronger public-boundary effect,
  delete or replace the test
- if the strongest surviving assertion is still only a call-arg bag, raw JSON
  blob, status-only, presence-only, or call-count-only check, delete or
  rewrite the test
- boundary-adoption claims must fail if code falls back to local wrapper or
  equivalent wrong owner
- typed-boundary or contract-tightening claims must fail if omitted input,
  explicit `None`, downstream default/fallback, local wrapper, or equivalent
  legacy path can still reach the old behavior
- if a claim says a boundary now requires an explicit value or dependency,
  proof must cover each materially equivalent legacy entry path that could
  still preserve the old implicit behavior, or narrow the claim honestly
- if proof only shows "something equivalent happened", it is too weak for
  ownership claim
- a split is remediation only if each survivor has one owner boundary,
  support/harness/fake files stay in the same cluster, and no removed strong
  assertion is replaced by weaker status-, presence-, href-, or generic checks
- parameterize only when every case shares one contract and one assertion
  shape; otherwise split or delete
- if changed behavior differs by auth posture, capability gate, storage/state
  authority, or upstream data source, proof must name those material variants
  and cover each one or narrow claim honestly
- anonymous or guest proof does not prove authenticated or server-owned branch;
  authenticated proof does not prove guest-local branch
- when write authority moved across process/storage boundary, proof must include
  one real mutation plus follow-up read/reload in same authority path
- stale history is not proof; a test that can pass by replaying old events,
  broad fixture state, or pre-existing rows without proving the current action
  is too weak

## Invalid Reason Codes

Any one of these makes `keep` invalid:

- `wrong-layer`: a lower owner can prove the same regression
- `implementation-coupled`: proves internals or refactor shape
- `file-text-assertion`: proves source or file text instead of contract output
- `policy-mirroring`: duplicates another owner's inventory, metadata, or
  denylist instead of generated, loaded, or runtime behavior
- `mock-choreography`: proves call wiring more than behavior
- `snapshot-abuse`: broad snapshot or golden as primary proof
- `overscoped`: file covers more than one owner boundary or feature family
- `low-signal-assertion`: the file contains no assertion stronger than
  status-only, presence-only, call-count-only, or did-not-crash proof
- `exact-string-noncontract`: incidental wording treated as contract
- `non-hermetic`: depends on ambient machine, time, network, or shared state
- `order-dependent`: outcome depends on suite order or leaked state
- `flaky`: outcome is unstable for the same code
- `redundant`: adds no independent regression signal
- `assertion-thin`: file has more tests than behavior assertions
- `giant-suite`: file exceeds `300` non-comment lines or `15` tests
- `wait-heavy`: file uses more than `2` waits, settles, polls, or retry loops
- `runner-heavy`: subprocess, browser, container, or full runtime without a
  boundary reason

## Weakly Provable Claim Disposition

Pick one:

- `operationalize now`
- `require multi-proof`
- `narrow the claim`
- `schedule follow-up`

Current broad deferred families:

- security-sensitive claims
- concurrency-sensitive claims
- performance-sensitive claims

Do not overclaim these from happy-path intuition.

## Touched-Test Remediation

For each changed persistent test file, choose one:

- `keep`
- `shrink`
- `rewrite`
- `delete`

Reason codes:

- `wrong-layer`
- `implementation-coupled`
- `file-text-assertion`
- `policy-mirroring`
- `mock-choreography`
- `snapshot-abuse`
- `overscoped`
- `low-signal-assertion`
- `exact-string-noncontract`
- `non-hermetic`
- `order-dependent`
- `flaky`
- `redundant`
- `assertion-thin`
- `giant-suite`
- `wait-heavy`
- `runner-heavy`
- `valuable-high-layer`
- `benchmark-good-fit`

Defaults:

- no real regression protected -> delete
- behavior belongs lower -> move down
- high layer still matters -> shrink to minimum durable surface
- if a test can pass without the current action proving a fresh effect -> rewrite
  or delete
- any invalid reason code -> `keep` is forbidden

## Corpus-Wide Audit Mode

Touched-only remediation is the floor, not the ceiling.

When a wave or cleanup program owns a broader suite slice:

- audit the full owned tranche, not a hand-picked sample
- rank suspicious clusters first, then exhaust each owned tranche before moving
  on
- default the tranche unit to a coherent cluster such as one directory, route
  family, controller family, or provider family rather than one convenience
  file
- giant surviving suites need explicit justification; "it still passes" is not
  justification
- if a cluster still obviously wants delete, split, move, or rewrite today,
  the tranche is not done

Recommended audit loop:

1. inventory the corpus
2. score suspicious clusters
3. take the highest-value tranche
4. assign `keep | shrink | rewrite | delete` dispositions across the tranche
5. refresh the inventory before choosing the next tranche

Do not hide repo-wide ballast behind "untouched files" once the cleanup itself
is the owned work.

## Performance And Cost Rules

Slow tests are debt unless their signal clearly earns the cost.

Pressure points that are suspicious by default:

- giant single-file suites with many unrelated scenarios
- unit or component tests that spend more effort on mocks, waits, pumps, or
  orchestration than on durable assertions
- low-layer tests that invoke subprocesses, containers, browsers, or other
  runtime-heavy machinery without a boundary reason
- UI tests with repeated wait loops, broad pump-and-settle posture, or large
  state setup just to reach one narrow assertion
- clusters whose assertion surface is thin relative to the amount of setup,
  mocked wiring, or scenario churn

Performance cleanup defaults:

- delete redundant expensive tests before optimizing them
- move behavior downward before trying to speed up the wrong layer
- split giant mixed-purpose files into smaller honest owners only when the
  survivors are still worth keeping
- if a test remains expensive, the retained contract must be named explicitly
  and the cheaper rejected proof should be obvious

## Layer Selection

Choose layer first.

| Change type | Preferred layer | Notes |
|---|---|---|
| Pure domain logic/invariants | `unit` | assert outputs/behavior, not call order |
| Cross-module interfaces / schema compatibility | `contract` | keep contract explicit |
| Same feature logic on web and mobile | `unit` parity fixtures in both clients | assert same semantic outcome |
| Infra/workflow/deploy orchestration | `integration` + smoke | unit alone is weak |
| Runtime API/UI behavior across process boundary | smoke/e2e + live runtime proof when required | in-process harness does not replace runtime wiring proof |
| Static architecture boundaries | static checks | prefer dedicated tools |

Wrong-layer warning:
- subprocess-heavy, shell-heavy, or slow workflow proofs are usually not `unit`
  tests even if stored under `tests/unit/**`

Web boundary owner:

- project overlay frontend-boundary doctrine

## Persistence Lane Rule

Persistence lane is for DB contract only.

Valid owners:

- schema constraints/defaults/indexes/foreign keys/cascades
- supported migration/seed contracts
- repository/query semantics
- RLS, role-context, user-scope behavior
- DB-level idempotency or concurrency

Wrong for persistence lane:

- route/view/action/endpoint tests
- HTML, redirect, query-param, workflow-state assertions
- service/adapter/script tests whose main contract is not DB
- storage wiring tests that only happen to persist rows
- operational drills or harness proof

If removing persistence-marked test from lane:

- delete if low-value
- or move to correct layer

## Exact String Rule

Allowed only for:

- governed end-user copy
- stable CLI/help/diagnostic ABI
- schema keys and protocol literals
- DOM/API field names consumed literally by callers

Forbidden:

- HTML snippets or rendered fragments
- incidental error wording
- source/workflow/script text

If production does not depend on the literal wording, do not assert wording.

## Source-Text Assertions

Default: forbidden.

Allowed only when the file text itself is the shipped contract:

- protocol or schema literal registries
- stable CLI/help fixture text
- governed end-user copy sources

Everything else is forbidden.

## Workflow And Infra Changes

For `.github/**`, `infra/**`, deployment scripts, runtime wiring:

- prefer behavior-level integration or smoke checks
- keep text-contract assertions minimal
- use unit tests only for narrow ABI contracts
- do not snapshot command ordering, step names, or big shell fragments

## Runtime Artifact Discipline

- persistent tests should not emit screenshot/video/trace archives by default
- runtime screenshots are durable only when screenshot review is part of claim
- failure artifacts are diagnostics unless explicitly reviewed and promoted
- durable runtime artifacts live under `.artifacts/runtime/**`
- disposable bundles stay diagnostic-only

## Runtime Proof Depth

For runtime-bound `works`, `verified`, or `done` claims, evidence must include:

1. runtime readiness proof
2. candidate discovery for data-dependent flows before main proof
3. real user action or real request for each changed critical path
4. outcome proof tied to action
5. screenshot review when UI quality is part of claim
6. request/response and logs when cross-layer behavior matters

Data-dependent flow rule:

- inspect active runtime data with the supported repo path; do not guess probe
  inputs
- exact runtime recipe belongs in the owning runtime-testing skill or surface
  doc, not here
- treat flow as candidate discovery, then proof
- if runtime lacks suitable data, report `Runtime evidence: blocked` with the
  failed probe and next repo-supported action

Runtime proof overlay:

- interactive UI needs interaction completeness, not only action fired
- failure/edge-state claims need actual failure/edge probes
- shared controls/filter/handoff flows need one-source-of-truth checks across
  UI, request shape, query, and downstream handoff
- if branch behavior differs by auth posture, capability, or state authority,
  runtime proof must state exact branch exercised and why remaining branches are
  either covered separately or out of claim
- `multi-proof-required` still needs persistent-test leg
- weakly provable claims must be narrowed or deferred honestly

Artifact-only, startup-only, or navigation-only evidence is invalid for
flow-completion claims.

## Runtime UI Evidence

For browser/device-visible UI changes:

- execute changed flow live
- execute every material claimed branch live, not only easiest branch
- capture required viewports
- open and inspect screenshots
- review each touched screen/state that matters
- name screenshots reviewed, states covered, viewport used, checks performed
- name user posture and authority posture used for each reviewed flow

Merge-blocking UI evidence failures:

- overlapping controls
- clipped or unreadable primary labels
- broken responsive layout
- broken hierarchy or action placement
- missing/broken media on visual surfaces
- screenshot quality not acceptable as product evidence

Element/text presence alone is not enough for overlay/floating interactions.

UI risk-class owner:

- this reference owns proof taxonomy and escalation requirements only
- concrete browser/device proof mechanics are supplied by the active project
  overlay or by a separately installed runtime-testing skill
- project overlays own exact runtime recipes, product-specific acceptance, and
  any local UI verification strategy

## Shared Flow Functional Parity

When end-user flow exists on both web and mobile:

- verify edited client
- verify counterpart still matches same functional contract
- or schedule owning follow-up in same change

If a feature intentionally ships on one client first, record that rollout policy
or follow-up in the project overlay. The global harness does not decide product
delivery order.

## Backend Runtime Claims

Backend-only changes still need live runtime proof when claim depends on
process boundary:

- HTTP/API behavior
- auth/session/RLS
- env/config/runtime wiring
- background worker or cross-service behavior
- observability/diagnostic claims

Minimum live evidence:

1. start affected service with repo runtime recipe
2. execute real request/flow for each changed critical path
3. capture request/response, relevant logs, required side-effect evidence

For observability/diagnostic claims, evidence must also cite selected
`correlation_id` or `trace_id` values plus the linked log/trace artifact, or
explicit `none observed` when the packet has already narrowed the claim to
allow that outcome.

Mutating flows need at least one real runtime mutation plus verified outcome.
Offline/retry claims need degraded-condition evidence plus recovery evidence.

If delegated runtime worker is interrupted or closed before final verdict, that
proof leg is incomplete and must be rerun.

## CI Posture

`quality-gate-selection.md` owns lane semantics; project overlays own stack-specific commands.

Rule here:

- do not promote broad smoke/e2e into faster shared lanes unless flow is
  stable, repeatedly valuable, and proportionate in cost

## Practical Checks

Before adding test:

1. What regression does this catch?
2. Why is this cheapest reliable layer?
3. What stronger layer did we skip, and why?
4. If behavior exists on web and mobile, where is counterpart proof?
5. If UI-related, does proof match chosen UI risk class?

Before keeping test:

1. Would we add it today?
2. Does it assert real contract or implementation shape?
3. Would harmless refactor break it for bad reason?

Weak answers mean shrink, rewrite, or delete.
