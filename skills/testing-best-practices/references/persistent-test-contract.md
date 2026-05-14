# Persistent Test Contract

Owns persistent-test admission, layer choice, touched-test disposition, and
invalid test shapes.

## Admission

A persistent test is valid only when it protects a durable behavior or contract
and rejects a named weaker implementation.

Before adding or keeping one, name:

- regression protected
- cheapest reliable layer
- failure condition
- claim boundary left outside the test

Weak answers mean delete, shrink, rewrite, or route to
`../../readiness-claim/SKILL.md`.

## Layer

Use the cheapest honest layer:

- domain invariant: unit
- schema/protocol/API/cross-module contract: contract
- architecture boundary: static check
- workflow/infra/runtime wiring: integration or smoke
- live UI/API behavior: durable spec only when regression-worthy; one-shot live
  proof stays with runtime owners

DB persistence tests prove DB contracts only. Do not put route, UI, redirect,
script, adapter, or operational proof there merely because rows are involved.

## Changed Test Disposition

For each changed persistent test file, emit:

`<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`

- `keep` requires `none`
- `shrink`, `rewrite`, or `delete` requires at least one reason code
- new tests require changed durable boundary plus named regression
- reorganization is not durable gain unless proof gets stronger, lower, smaller,
  or removes an invalid reason

Reason codes: `wrong-layer`, `implementation-coupled`, `file-text-assertion`,
`policy-mirroring`, `mock-choreography`, `snapshot-abuse`, `overscoped`,
`low-signal-assertion`, `exact-string-noncontract`, `non-hermetic`,
`order-dependent`, `flaky`, `redundant`, `assertion-thin`, `giant-suite`,
`wait-heavy`, `runner-heavy`.

## Test Strength

Persistent tests prove public behavior or durable contracts, not source shape,
private wiring, call counts, raw mock choreography, broad fixture history, or
did-not-crash presence checks.

Hand-built state proves only the constructed contract. It does not prove
workflow readiness unless `../../readiness-claim/SKILL.md` accepts producer-path
evidence too.

Exact strings are valid only for governed copy, CLI/help/diagnostic ABI,
schema/protocol literals, or consumed fields.

Material variants such as auth posture, capability gates, storage authority,
upstream source, migration path, and legacy entry path must be covered or the
claim narrowed.

Wait for assertion conditions, not guessed sleeps. Fixed delays are valid only
when timing is the contract.
