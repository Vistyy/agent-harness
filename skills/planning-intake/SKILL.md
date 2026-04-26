---
name: planning-intake
description: "Use when the user either needs an existing wave hardened to execution-ready status or presents a vague problem that must be rigorously explored and shaped into a wave plan."
---

# Planning Intake

Discovery plus intake before wave execution.

Goal: close material decisions before execution starts.

## Stance

- Be critical.
- Do not accept requested scope at face value.
- Push on symptom-vs-root-cause mistakes.
- Start from the simplest honest solution.
- Bias hard toward deleting, collapsing, or leaving complexity manual unless a real constraint forces more.
- Prefer better long-term shape, then phase it if needed.
- Default bounded local mechanics yourself.
- Never let important deferrals stay chat-only.

## Non-Negotiables

1. No silent material assumptions.
2. Blocking user questions are only for `user-owned decisions`.
3. Every blocking question includes recommendation and short reason.
4. `agent-defaultable decisions` are decided locally.
5. Push back on weak scope or transitional architecture.
6. Run omission-class sweep before promotion.
7. Important deferred work becomes durable wave/backlog/mobile-parity state in same session.
8. Discovery work does not leak into execution.

## Decision Taxonomy

Decision authority depends on decision level.

User owns direction-setting and public-contract decisions. Agent owns execution
decisions inside an already-approved direction and contract.

### `user-owned decisions`

- product meaning, user-facing semantics, taste / visual direction, IA,
  compatibility / rollout, vendor / platform / data-model / infrastructure
  direction, or another long-lived external commitment
- release-priority tradeoff when multiple viable wave orders remain and repo
  doctrine does not already resolve the order
- architecture or scope-topology choice only when multiple plausible options
  would change long-lived ownership, compatibility, or visible semantics and no
  named durable owner doc already closes the choice
- proof posture only when multiple honest proof options materially change claim
  strength, runtime cost, or delivery timing and the proof owner doc does not
  already close the smaller honest class
- technical choice is not automatically agent-owned; if it sets direction or
  public / cross-owner contract, user owns it unless a named durable owner doc
  already closes the choice

### `agent-defaultable decisions`

- wave split / merge / ordering only when a named durable owner doc already
  forces the cleaner boundary, dependency order, or proof shape
- scope narrowing, reshaping, and extraction of follow-up waves or backlog
  items to keep one wave coherent without changing contracts, scope topology,
  or proof posture beyond what durable doctrine already requires
- naming and placement
- helper splitting
- bounded decomposition mechanics
- packet wording and placeholders
- test-module layout and local proof mechanics
- internal implementation mechanics and application of established repo
  doctrine, approved architecture, framework / language practice, correctness,
  simplicity, maintainability, or cheapest honest proof inside an approved
  direction and contract

If classification is unclear, ask only when the choice sets direction,
public / cross-owner contract, or materially changes product, taste, strategy,
reversibility, external promises, claim strength, runtime cost, or delivery
timing. Do not ask merely because competent engineers might prefer different
local implementations.

### `must-schedule-if-deferred`

- adjacent interaction completeness
- nearby worthwhile cleanup
- migration / compatibility / operational follow-up
- stronger verification follow-up

## Mandatory Sweeps

Before promotion, check:
- user objective coverage:
  - list substantive user asks in scope
  - say how each one is being handled
  - do not let material asks disappear silently
- security and trust boundaries
- failure and edge states
- migration / compatibility / rollout
- interaction completeness
- hotspot cleanup worth doing now
- operational / observability / idempotency posture
- proof ownership/allocation closed in the planning artifact
- simplicity / necessity pass:
  - target minimal end-state
  - what can be deleted
  - what can be demoted to breakglass/manual
  - what can be collapsed into one owner
  - what remaining complexity is necessary and why
  - persist this judgment in the wave brief or packet; do not leave it chat-only

## Proof Allocation

Execution-ready planning must record in the wave brief or packet:
- proof class using `skills/testing-best-practices/references/testing-strategy.md`
- owner layer
- success condition
- exact command/artifact or `not-required`
- one weaker implementation the proof must reject
- for typed-boundary or contract-tightening claims, each materially equivalent
  legacy path the proof must reject

Shape work around outcomes and proof, not command lists. A plan or task card
states the success condition, the proof that rejects a weaker implementation,
and then the expected command or artifact.

## Blocking Question Format

Use only for `user-owned decisions`.

```md
**Question:** <single decision question>

**Recommended:** Option A - <short reason>

| Option | Description |
|--------|-------------|
| A | ... |
| B | ... |
| C | ... |

Reply with A/B/C, or say "yes" to accept recommendation.
```

## Intake Gate

Promotion needs all four:

1. `scope closed`
2. `decisions closed`
3. `proof allocated`
4. `deferrals persisted`

If any fail, keep questioning.

## Promotion Rules

- no `execution-ready` while any material implementation-shaping question remains open
- local defaults must not decide unresolved user-visible semantics,
  compatibility / rollout posture, or a materially contested proof /
  architecture tradeoff that durable doctrine does not already resolve
- no `execution-ready` promotion when a substantive user ask was silently
  omitted, downplayed, or converted to a narrower scope without explicit record
- packet must be implementation-only
- if two competent implementers could still choose materially different owner,
  proof, state-authority, runtime, compatibility, migration, or public-behavior
  paths, planning is still open
- local framework mechanics stay implementer-local only when owner skills/docs
  already close the correct approach and no material path changes
- do not authorize material implementation from memory-only plans on
  non-trivial work
- route non-trivial planning through `planning_critic` before planning-gate
  `quality_guard`; if the critic finds a material gap, planning is still open
- record `planning_critic` provenance in the planning artifact before
  requesting planning-gate `quality_guard`
- `planning_critic` is mandatory critic pressure, not a final approver and not
  a replacement for planning-gate `quality_guard`
- non-trivial planning includes structural, hotspot, state-authority,
  delegation-policy, UI / taste doctrine, proof-gap, typed-boundary,
  ownership, contract-tightening, and non-trivial wave-shaping work
- tiny local fixes do not require heavyweight planning solely because this rule
  exists

## Doctrine Routing

- apply standing engineering-principles lens:
  `skills/system-boundary-architecture/references/engineering-principles.md`
- apply standing code-shape lens:
  `skills/system-boundary-architecture/references/code-shape-and-local-design.md`
- apply `skills/code-simplicity/SKILL.md` as the default shaping lens for
  non-trivial planning
- if work changes boundaries or ownership, load `skills/system-boundary-architecture/SKILL.md`
- structural slices need explicit `System-Boundary Architecture Disposition`

## Anti-Misdirection Check

Ask:
- Are we treating symptom as root cause?
- Is there smaller or higher-leverage fix?
- Is requested implementation mode wrong?
- Would targeted research change scope?
- Are we removing complexity or only moving it?
- Does the claimed stricter boundary still leave the old behavior reachable
  through a surviving legacy path?
- Which current path, layer, or artifact can disappear if the redesign is
  honest?

If yes and a `user-owned decision` is exposed, ask the blocking question and
reframe scope.
If yes but a named durable owner doc already closes the better shape, decide
locally and persist the reshape.

For each substantive user ask, answer:
- is planning keeping it as-is, shrinking it, rewriting the approach, or deferring it?
- if not keeping it as-is, why is that still faithful to the user objective?

## Outputs

1. `docs-ai/current-work/delivery-map.md`
2. `docs-ai/docs/initiatives/waves/<wave-id>.md`
3. `docs-ai/current-work/<wave-id>/wave-execution.draft.md` when planning gate needs packet-shaped review
4. `docs-ai/current-work/<wave-id>/wave-execution.md` only after promotion
5. `docs-ai/current-work/backlog/<initiative>__<feature>__<item>.md` when deferral needs backlog state
6. `docs-ai/docs/roadmap.md` only when initiative/feature status changes materially
