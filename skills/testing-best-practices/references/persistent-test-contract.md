# Persistent Test Contract

Owner for normal persistent-test edits: layer choice, admission, proof strength,
touched-test disposition, and invalid proof shapes.

## Admission

A persistent test is valid only when it protects a durable boundary and rejects
a named weaker implementation.

Before adding or keeping one, answer:

- What regression does it catch?
- Why is this the cheapest reliable persistent layer?
- What would make it fail?
- What runtime, platform, or completion claim remains outside this test?

Weak answers mean delete, rewrite, shrink, or route to the real proof owner.

Meaningful persistent red evidence happens before implementation when a
behavior change needs a failing persistent test or persistent static/contract
check. If no meaningful failing check exists, stop, clarify, or narrow the
claim. Do not fake a test.

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

Do not promote broad smoke/e2e proof into fast shared lanes unless the flow is
stable, repeatedly valuable, and proportionate in cost.

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

`required-proof` means the file is needed to prove a changed durable boundary or
changed regression target in this slice, no existing same-layer or lower-layer
proof already covers it, and the file rejects one named regression introduced
by the change.

`durable-gain` means the same original durable regression target was previously
represented by the file, and the change creates one of:

- `stronger-proof`
- `lower-layer-replacement`
- `smaller-surface`
- `reason-code-removal`

## Invalid Reason Codes

Use the smallest accurate set:

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

Defaults:

- no real regression protected -> delete
- behavior belongs lower -> move down
- high layer still matters -> shrink to minimum durable surface
- test can pass without proving the current action -> rewrite or delete

## Proof Strength

Persistent tests prove public behavior or durable contracts. They must not
inspect production source, parsed source shape, private symbol names, token
presence, private dependency wiring, private call/body shape, call counts, or
fake captured kwargs to prove behavior.

Allowed source or shape inspection only when the inspected surface is the
shipped contract/artifact, or a named static architecture check enforces one
durable boundary such as import graph, public API, schema, manifest, or
generated artifact.

Exact strings are valid only for governed copy, CLI/help/diagnostic ABI,
schema/protocol literals, or fields consumed literally. Incidental wording,
HTML fragments, and source text are not contracts.

Mocks are support, not proof. A test whose strongest assertion is call order,
call count, raw JSON spelunking, status-only, presence-only, did-not-crash, or
mock choreography is too weak.

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

Stale history is not proof. A test that can pass by replaying old events,
broad fixture state, or pre-existing rows without proving the current action is
too weak.

## Waiting

Guessed sleeps are invalid persistent-test proof.

Wait for the condition the assertion needs: event arrived, state ready, count
reached, file exists, UI action available, or async operation settled.

Every wait helper needs bounded timeout, modest polling, fresh condition
evaluation, and a failure message naming the timed-out condition.

Fixed delays are valid only when timing itself is the contract, such as
debounce, throttle, expiry, or timeout behavior.
