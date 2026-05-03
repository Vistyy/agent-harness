# Proof Strength

Owner for persistent-test proof sufficiency, proof anti-patterns, weakly
provable claim disposition, exact-string limits, and source/implementation-shape
assertion policy.

Runtime proof escalation, runtime evidence reports, visual verdict vocabulary,
and evidence-of-record rules are owned by `../../runtime-proof/SKILL.md`.

## Persistent Proof Posture

Persistent automated proof is enough only when the claim does not depend on a
composed runtime, UI, environment, service process, or cross-process boundary.

Runtime and multi-proof class selection is owned by
`../../runtime-proof/SKILL.md`. This file owns whether any persistent-test leg
is valid and strong enough. Layer choice and runtime handoff belong to
`layer-selection.md`.

## Proof Strength Rules

- transaction claims prove transaction state, not helper flow or object identity
- provenance/ownership claims prove real owner path, not monkeypatched surrogate
- persistent tests must not inspect production implementation source, parsed
  source structure, private symbol names, token presence or absence, private
  dependency wiring, or private call/body shape to prove behavior, ownership,
  typing, performance, or architecture
- do not use isinstance, hasattr, getattr, vars/__dict__, or type(x) is ... to
  recover weak contracts, repeated narrowing, or private wiring; use them only
  for real dynamic-boundary validation or explicit dispatch
- in tests, class-name/module-string assertions are valid only when that literal
  is the shipped contract; otherwise prove the public factory/constructor
  boundary or observable behavior
- do not prove a public boundary by capturing fake kwargs into a mutable bag and
  asserting the bag contents; that is mock choreography unless the bag itself is
  the shipped contract
- do not prove a typed transport contract by casting response.json() into broad
  dict/list shapes and spelunking members; assert the typed adapter/model
  boundary or move the proof to contract/integration
- if a test needs new support/capture/harness machinery and the strongest
  surviving assertion still does not prove a stronger public-boundary effect,
  delete or replace the test
- if the strongest surviving assertion is still only a call-arg bag, raw JSON
  blob, status-only, presence-only, or call-count-only check, delete or rewrite
  the test
- boundary-adoption claims must fail if code falls back to local wrapper or
  equivalent wrong owner
- typed-boundary or contract-tightening claims must fail if omitted input,
  explicit `None`, downstream default/fallback, local wrapper, or equivalent
  legacy path can still reach the old behavior
- if a claim says a boundary now requires an explicit value or dependency,
  proof must cover each materially equivalent legacy entry path that could still
  preserve the old implicit behavior, or narrow the claim honestly
- if proof only shows "something equivalent happened", it is too weak for
  ownership claim
- a split is remediation only if each survivor has one owner boundary,
  support/harness/fake files stay in the same cluster, and no removed strong
  assertion is replaced by weaker status-, presence-, href-, or generic checks
- parameterize only when every case shares one contract and one assertion shape;
  otherwise split or delete
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
