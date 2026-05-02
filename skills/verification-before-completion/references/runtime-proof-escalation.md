# Runtime Proof Escalation

Owner for runtime proof escalation, runtime evidence branch coverage, and the
boundary between reusable proof taxonomy and project-specific runtime mechanics.

Does not own:
- general test strategy, touched-test gates, proof-strength anti-patterns, or
  exact-string/source/implementation-shape policy:
  `../../testing-best-practices/references/testing-strategy.md`,
  `../../testing-best-practices/references/touched-test-gate.md`, and
  `../../testing-best-practices/references/proof-strength.md`
- browser proof mechanics:
  `../../webapp-testing/SKILL.md`
- mobile proof mechanics:
  `../../mobileapp-testing/SKILL.md`
- runtime evidence report shape and visual verdict vocabulary:
  `runtime-evidence-contract.md`
- runtime artifact placement:
  `verification-evidence.md`
- exact runtime recipes, service names, ports, secrets, topology, or product
  acceptance criteria; those belong to the active project overlay.

## Runtime Proof Classes

- `runtime-provable`: the claim depends on composed runtime, UI, wiring, env,
  or a process boundary.
- `multi-proof-required`: persistent proof and runtime proof are both needed.
- `not-reliably-provable-with-current-harness`: the harness cannot honestly
  prove the full claim and the completion claim must narrow or schedule
  follow-up.

Rules:
- do not downgrade runtime or multi-proof claims for convenience
- name every material runtime branch needed for the claim
- prove actual generated, loaded, or runtime behavior, not only static text
- when runtime evidence is blocked, say `Runtime evidence: blocked` and explain
  the missing prerequisite

## Runtime Claim Map

For non-trivial runtime-visible claims, keep one compact claim map before
handoff or closeout. Tiny local claims may mark the map `not-needed` only when
there is no public-behavior or cross-boundary runtime risk.

The map names:
- final claim boundary
- user, operator, or API entrypoint
- active runtime target or recipe
- real action, request, screen, state, or flow exercised
- observable result and owning surface
- material variants, branches, auth/capability posture, and data state
- simulated, stubbed, or replaced boundaries and their claim impact
- one weaker implementation the proof rejects

Final runtime-visible wording must not exceed this map. Any unproved
user/operator entrypoint or replaced boundary must narrow the claim or become a
durable follow-up.

## Entrypoint Fidelity

Use one of these levels when reporting runtime proof coverage:

- `exact`: same command, API, UI, or operator path; same runtime topology; same
  config/env loading; same artifact or side-effect visibility path.
- `faithful-wrapper`: invokes the exact entrypoint without replacing lifecycle,
  config, topology, or visibility boundaries. Any replaced boundary is named and
  excluded from the claim.
- `simulated-boundary`: explicitly replaces a boundary. It can prove the
  downstream or upstream behavior exercised, but not the replaced boundary.
- `adjacent-only`: proves a component, artifact, helper, or neighboring path
  without exercising the claimed entrypoint. It cannot support
  readiness/end-to-end/user-flow claims.
- `not-needed`: runtime proof is not needed for the scoped claim.

Readiness, end-to-end, user-flow, or broad `works` claims cannot pass with
`adjacent-only` proof. `simulated-boundary` proof can pass only a narrowed
claim that names the unproved boundary. Artifact-only, startup-only, or
navigation-only evidence is invalid for flow-completion claims.

## Escalation Decision

Ask one question first: would the completion claim still be meaningful if no
live app, service, browser, device, generated config, or process boundary were
exercised?

- If yes, persistent static or test proof may be enough.
- If no, classify the claim as `runtime-provable` or
  `multi-proof-required`.
- If the harness cannot execute the needed runtime, classify it as
  `not-reliably-provable-with-current-harness` and narrow or defer the claim.

Do not use small diff size, passing unit tests, or reviewer confidence to
downgrade a runtime claim.

## Runtime Evidence Minimum

For non-trivial runtime-bound `works`, `verified`, or `done` claims, route
`runtime_evidence` unless the claim is tiny, local, and has no public-behavior
or cross-boundary runtime risk. If in doubt, route it.

Evidence must include:

1. runtime readiness proof
2. candidate discovery for data-dependent flows before main proof
3. exact flow, request, screen, or state exercised
4. real user action or real request for each changed critical path
5. outcome proof tied to action
6. material branches covered or intentionally narrowed
7. reviewed artifacts, logs, screenshots, or trace pointers when applicable
8. one weaker implementation the proof would reject

Artifact-only, startup-only, or navigation-only evidence is invalid for
flow-completion claims; classify those cases as `adjacent-only` unless they
exercise the mapped entrypoint and observable result.

`reject`, `blocked`, or incomplete runtime evidence blocks or narrows the
affected claim.

Data-dependent flows:
- inspect active runtime data with the supported repo path before choosing
  probes
- treat flow setup as candidate discovery, then proof
- if runtime lacks suitable data, report `Runtime evidence: blocked` with the
  failed probe and next repo-supported action
- do not fabricate fixture expectations after seeing convenient data

Branch coverage:
- interactive UI needs interaction completeness, not only action fired
- failure and edge-state claims need actual failure or edge probes
- shared controls, filters, and handoff flows need one-source-of-truth checks
  across visible state, request shape, query, and downstream handoff
- if behavior differs by auth posture, capability, or state authority, state
  the exact branch exercised and why remaining branches are covered separately
  or out of claim
- `multi-proof-required` still needs testing owners:
  `../../testing-best-practices/references/layer-selection.md` for runtime
  handoff and cheapest persistent layer, and
  `../../testing-best-practices/references/proof-strength.md` for validity and
  strength of the persistent-test leg
- weakly provable claims must be narrowed or deferred honestly

## Runtime UI Claims

For browser/device-visible UI changes:
- execute the changed flow live
- execute every material claimed branch live, not only the easiest branch
- capture required viewports or device postures
- open and inspect screenshots when UI quality is part of the claim
- review each touched screen/state that matters
- name user posture and authority posture for each reviewed flow

Visual verdict vocabulary and reject floor live in
`runtime-evidence-contract.md`.

Element/text presence alone is not enough for overlay, floating, hit-test, or
transition interactions.

UI quality claims also need design anchors or an explicit underspecified
posture. A runtime pass for behavior does not prove visual quality by itself.

## Shared Flow Functional Parity

When an end-user flow exists on both web and mobile:
- verify the edited client
- verify the counterpart still matches the same functional contract
- or schedule owning follow-up in the same change

If a feature intentionally ships on one client first, record that rollout policy
or follow-up in the project overlay. The global harness does not decide product
delivery order.

## Backend Runtime Claims

Backend-only changes still need live runtime proof when the claim depends on a
process boundary:
- HTTP/API behavior
- auth/session/RLS
- env/config/runtime wiring
- background worker or cross-service behavior
- observability/diagnostic claims

Minimum live evidence:
1. start affected service with repo runtime recipe
2. execute real request/flow for each changed critical path
3. capture request/response, relevant logs, and required side-effect evidence

For observability or diagnostic claims, cite selected `correlation_id` or
`trace_id` values plus linked log/trace artifacts, or explicit `none observed`
when the claim allows that outcome.

Mutating flows need at least one real runtime mutation plus verified outcome.
Offline/retry claims need degraded-condition evidence plus recovery evidence.
Interrupted delegated runtime proof is incomplete and must be rerun.

## Escalation Triggers

Escalate from static or unit proof to runtime proof when the claim depends on:

- browser or device-visible behavior
- HTTP/API behavior across a process boundary
- auth/session/capability state
- generated runtime config or environment wiring
- service startup, readiness, or lifecycle
- uploads, downloads, object storage, or external side effects
- visual/layout quality visible to a user or operator

Mutating flows need at least one real runtime mutation plus verified outcome
unless the claim is explicitly narrowed.
