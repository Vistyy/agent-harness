# Testing Posture

Harness-level follow-up owner for test-suite cleanup after durable testing
doctrine is set by `testing-strategy.md`.

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
- repo-wide global test strategy, owned by `testing-strategy.md`
- runtime proof taxonomy and escalation, owned by
  `../../verification-before-completion/references/runtime-proof-escalation.md`
- concrete runtime diagnostics and artifact mechanics, owned by the active
  project overlay or separately installed surface-specific runtime-testing skill

## Follow-Up Contract

- repo-wide touched-test remediation, persistent-test proof strength, and
  cleanup doctrine stay owned by `testing-strategy.md`
- when a test family spans multiple product areas but the real problem is test
  cleanup, follow-up ownership should stay here rather than being scattered
  across product queues
- tool-selection follow-ups such as heavier mobile E2E framework evaluation
  belong here once the repo already has a baseline authoring path

## Corpus Audit Doctrine

- inventory and score suspicious clusters first
- own coherent tranches rather than isolated convenience files
- exhaust the selected tranche before moving to another
- refresh inventory after each tranche
- do not keep giant surviving suites because they pass; name the durable
  contract and the cheaper proof rejected
