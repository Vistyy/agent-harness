# Runtime Proof Escalation

Owner for runtime proof escalation, runtime evidence branch coverage, and the
boundary between reusable proof taxonomy and project-specific runtime mechanics.

Does not own:
- general test strategy, touched-test gates, proof-strength anti-patterns, or
  exact-string/source-text policy:
  `../../testing-best-practices/references/testing-strategy.md`
- browser proof mechanics:
  `../../webapp-testing/SKILL.md`
- mobile proof mechanics:
  `../../mobileapp-testing/SKILL.md`
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

## Runtime Evidence Minimum

For runtime-bound `works`, `verified`, or `done` claims, evidence must include:

1. runtime readiness proof
2. exact flow, request, screen, or state exercised
3. material branches covered or intentionally narrowed
4. reviewed artifacts, logs, screenshots, or trace pointers when applicable
5. one weaker implementation the proof would reject

## Owner Routing

- Browser-visible proof mechanics route to `../../webapp-testing/SKILL.md`.
- Mobile/device proof mechanics route to `../../mobileapp-testing/SKILL.md`.
- Artifact naming and promotion discipline route to `verification-evidence.md`.
- Project overlays provide concrete commands and runtime topology.

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
