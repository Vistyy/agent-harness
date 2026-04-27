# Testing Strategy

Goal: protect real behavior with cheapest high-signal proof.

This is the canonical owner for touched-test remediation, layer selection,
exact-string and source/implementation-shape limits, and persistent-test proof
strength.
Planning-intake should only carry shaping and promotion pressure.

Runtime proof escalation, runtime evidence reports, visual verdict vocabulary,
and artifact promotion are owned by
`../../verification-before-completion/references/runtime-proof-escalation.md`,
`../../verification-before-completion/references/runtime-evidence-contract.md`,
and `../../verification-before-completion/references/verification-evidence.md`.

Coverage count is not goal. Bad tests are debt. Delete, shrink, rewrite, or
move them when touched.

Examples and references live in `../SKILL.md`.

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

## Persistent Proof Posture

Persistent automated proof is enough only when the claim does not depend on a
composed runtime, UI, environment, service process, or cross-process boundary.

Runtime and multi-proof class selection is owned by
`../../verification-before-completion/references/runtime-proof-escalation.md`.
When that owner requires `multi-proof-required`, this file owns whether the
persistent-test leg is valid, strong, and at the cheapest honest layer.

## Proof Strength Rules

- transaction claims prove transaction state, not helper flow or object
  identity
- provenance/ownership claims prove real owner path, not monkeypatched
  surrogate
- persistent tests must not inspect production implementation source, parsed
  source structure, private symbol names, token presence or absence, private
  dependency wiring, or private call/body shape to prove behavior, ownership,
  typing, performance, or architecture
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
- `implementation-coupled`: proves internals, private symbol names, private
  dependency wiring, private call/body shape, parsed production source
  structure, or refactor shape instead of behavior or durable public boundary
- `file-text-assertion`: proves source/file text, token presence or absence, or
  text mirrors instead of contract output, shipped artifact text, or a named
  architecture boundary surface
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

## Source And Implementation-Shape Assertions

Default: forbidden.

Persistent tests must not inspect production implementation source, parsed
source structure, private symbol names, token presence or absence, private
dependency wiring, or private call/body shape to prove behavior, ownership,
typing, performance, or architecture.

Use behavior proof, public contract proof, typecheck/lint/static architecture
checks, or review instead.

Allowed only when one of these is true:

- the inspected text or structure is itself the shipped contract or artifact
  under test
- a dedicated static architecture check enforces a named durable boundary that
  is not honestly provable by lower behavior or public contract proof

The static-architecture exception is limited to the boundary surface it owns,
such as import graph, module boundary, public API/export surface, generated
artifact, schema, manifest, or declared contract. It must not inspect arbitrary
private implementation body shape.

Every exception must name:

- the contract or durable boundary
- the exact inspected surface
- the counterfactual regression it rejects

Token deny-lists and private-symbol allow-lists are invalid persistent tests
unless the tokens are part of the public contract, shipped artifact, or named
architecture boundary surface.

## Workflow And Infra Changes

For `.github/**`, `infra/**`, deployment scripts, runtime wiring:

- prefer behavior-level integration or smoke checks
- keep text-contract assertions minimal
- use unit tests only for narrow ABI contracts
- do not snapshot command ordering, step names, or big shell fragments

## Runtime Proof Routing

Runtime-bound claims route to
`../../verification-before-completion/references/runtime-proof-escalation.md`.

This file still owns the persistent-test leg of `multi-proof-required` claims:
the test must protect a named durable boundary or regression target at the
cheapest honest layer.

Concrete browser and mobile mechanics are owned by `webapp-testing` and
`mobileapp-testing`. Project overlays own exact runtime recipes,
product-specific acceptance, and local UI verification strategy.

## CI Posture

`../../verification-before-completion/references/quality-gate-selection.md`
owns lane semantics; project overlays own stack-specific commands.

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
