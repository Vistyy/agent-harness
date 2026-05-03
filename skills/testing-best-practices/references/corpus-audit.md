# Corpus Audit

Owner for corpus-wide test cleanup tranches, suspicious cluster selection,
performance/cost posture, and harness-level follow-up ownership for persistent
tests.

## Scope

Included:
- discovery and follow-up ownership for low-signal, oversized, or weakly owned
  test families
- follow-up shaping for shrinking broad route/status/snapshot suites toward
  narrower semantic proofs
- evaluation of repo-owned UI/mobile automation tool choices after baseline
  adoption
- backlog shaping for cross-domain test cleanup motivated by harness doctrine
  rather than by a product feature

Excluded:
- feature-specific product correctness decisions, owned by the relevant product
  initiative
- repo-wide testing strategy router, owned by `../SKILL.md`
- runtime proof taxonomy and escalation, owned by
  `../../verification-before-completion/references/runtime-proof-escalation.md`
- concrete runtime diagnostics and artifact mechanics, owned by the active
  project overlay or separately installed surface-specific runtime-testing skill

## Follow-Up Contract

- repo-wide touched-test remediation stays owned by `touched-test-gate.md`
- proof strength stays owned by `proof-strength.md`
- cleanup doctrine stays here
- when a test family spans multiple product areas but the real problem is test
  cleanup, follow-up ownership should stay here rather than being scattered
  across product queues
- tool-selection follow-ups such as heavier mobile E2E framework evaluation
  belong here once the repo already has a baseline authoring path

## Corpus-Wide Audit Mode

Touched-only remediation is the floor, not the ceiling.

When a wave or cleanup program owns a broader suite slice:
- audit the full owned tranche, not a hand-picked sample
- rank suspicious clusters first, then exhaust each owned tranche before moving
  on
- default the tranche unit to a coherent cluster such as one directory, route
  family, controller family, or provider family rather than one convenience file
- giant surviving suites need explicit justification; "it still passes" is not
  justification
- if a cluster still obviously wants delete, split, move, or rewrite today, the
  tranche is not done

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
- clusters whose assertion surface is thin relative to setup, mocked wiring, or
  scenario churn

Performance cleanup defaults:
- delete redundant expensive tests before optimizing them
- move behavior downward before trying to speed up the wrong layer
- split giant mixed-purpose files into smaller honest owners only when the
  survivors are still worth keeping
- if a test remains expensive, the retained contract must be named explicitly
  and the cheaper rejected proof should be obvious
