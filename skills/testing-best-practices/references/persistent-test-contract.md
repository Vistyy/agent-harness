# Persistent Test Contract

Owns persistent-test admission, layer choice, proof strength, touched-test
disposition, and invalid proof shapes.

## Admission

A persistent test is valid only when it protects a durable boundary and rejects
a named weaker implementation.

Before adding or keeping one, name the regression, cheapest reliable layer,
failure condition, and runtime/platform/completion claim left outside the test.

Weak answers mean delete, rewrite, shrink, or route to the real proof owner.

Meaningful persistent red evidence happens before implementation when a
behavior change needs a failing persistent test or static/contract check. If no
meaningful failing check exists, stop, clarify, or narrow the claim. Do not fake
a test.

## Layer

Choose the cheapest honest persistent layer:

| Change | Default persistent layer |
| --- | --- |
| domain logic or invariant | unit |
| schema, protocol, API, or cross-module contract | contract |
| static architecture boundary | static check with named owner |
| workflow, infra, deploy, or runtime wiring | integration or smoke |
| UI/API behavior across live process boundary | durable spec only when regression-worthy; live proof stays with runtime owners |

Runtime-bound claims route to `../../runtime-proof/SKILL.md`. Browser and
mobile mechanics route to `../../webapp-testing/SKILL.md` and
`../../mobileapp-testing/SKILL.md`.

Persistence-lane tests are for DB contracts only: schema constraints,
migrations/seeds, repository/query semantics, RLS/user scope, DB idempotency, or
DB concurrency. Route/view/action/endpoint, HTML, redirect, query-param,
workflow-state, script, adapter, and operational proof do not belong there just
because they touch rows.

Workflow, infra, deploy, and runtime-wiring tests prefer behavior-level
integration or smoke proof. Keep text assertions minimal; do not snapshot
command ordering, step names, or large shell fragments.

## Touched Test Disposition

For every changed persistent test file, emit exactly one row:

`<path>: <keep|shrink|rewrite|delete> [reason-codes|none]`

Rules:

- `keep` requires `none`
- any invalid reason code forbids `keep`
- `shrink`, `rewrite`, and `delete` require at least one reason code
- new tests require changed durable boundary plus named regression
- each changed persistent test file needs `required-proof` or `durable-gain`
- relabeling, helper extraction, file moves, fixture churn, or reorganization
  without stronger proof, smaller surface, lower layer, or invalid-reason
  removal is not durable gain

`required-proof`: needed for a changed durable boundary or regression target,
not already covered at the same or lower layer, and rejects one named regression
introduced by the change.

`durable-gain`: same durable regression target, with `stronger-proof`,
`lower-layer-replacement`, `smaller-surface`, or `reason-code-removal`.

## Invalid Reason Codes

Use the smallest accurate set: `wrong-layer`, `implementation-coupled`,
`file-text-assertion`, `policy-mirroring`, `mock-choreography`,
`snapshot-abuse`, `overscoped`, `low-signal-assertion`,
`exact-string-noncontract`, `non-hermetic`, `order-dependent`, `flaky`,
`redundant`, `assertion-thin`, `giant-suite`, `wait-heavy`, `runner-heavy`.

Defaults: no real regression protected -> delete; behavior belongs lower ->
move down; high layer still matters -> shrink; test can pass without proving
the current action -> rewrite or delete.

## Proof Strength

Persistent tests prove public behavior or durable contracts. They must not use
production source shape, private names/wiring, call/body shape, call counts, or
fake captured kwargs as proof.

Source/shape inspection is allowed only for shipped contracts/artifacts or a
named static architecture check enforcing one durable boundary: import graph,
public API, schema, manifest, or generated artifact.

Exact strings are valid only for governed copy, CLI/help/diagnostic ABI,
schema/protocol literals, or literally consumed fields. Incidental wording,
HTML fragments, and source text are not contracts.

Mocks are support, not proof. Call order/count, raw JSON spelunking,
status-only, presence-only, did-not-crash, or mock choreography is too weak as
the strongest assertion.

Typed transport is proved at the typed adapter/model boundary, not by casting
`response.json()` into broad dict/list shapes and spelunking members.

Material variants matter. Auth posture, capability gates, storage/state
authority, upstream data source, migration path, and legacy entry path must be
covered or the claim narrowed.

Boundary tightening must cover materially equivalent legacy paths: omitted
input, explicit `None`, downstream defaults, local wrappers, old fallback
routes, and old implicit behavior.

Anonymous proof does not prove authenticated behavior; authenticated proof does
not prove guest/local behavior. Server-owned write authority needs one real
mutation plus follow-up read or reload through the same authority path.
Stale history is not proof: old events, broad fixtures, or pre-existing rows
without current action proof are too weak.

## Waiting

Guessed sleeps are invalid persistent-test proof.

Wait for the assertion condition: event arrived, state ready, count reached,
file exists, UI action available, or async operation settled. Wait helpers need
bounded timeout, modest polling, fresh condition evaluation, and a failure
message naming the timed-out condition.

Fixed delays are valid only when timing itself is the contract, such as
debounce, throttle, expiry, or timeout behavior.
