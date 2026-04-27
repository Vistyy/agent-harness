# Layer Selection

Owner for choosing the cheapest honest persistent-test layer, persistence-lane
placement, workflow/infra proof routing, testing-side runtime routing, CI
posture, and practical add/keep checks.

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

## Workflow And Infra Changes

For `.github/**`, `infra/**`, deployment scripts, runtime wiring:
- prefer behavior-level integration or smoke checks
- keep text-contract assertions minimal
- use unit tests only for narrow ABI contracts
- do not snapshot command ordering, step names, or big shell fragments

## Runtime Proof Routing

Runtime-bound claims route to
`../../verification-before-completion/references/runtime-proof-escalation.md`.

For `multi-proof-required` claims, this file owns runtime handoff and cheapest
honest persistent layer selection. `proof-strength.md` owns whether the
persistent-test leg is valid and strong enough.

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
