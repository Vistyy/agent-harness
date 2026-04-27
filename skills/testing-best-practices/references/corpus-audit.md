# Corpus Audit

Owner for corpus-wide test cleanup tranches, suspicious cluster selection, and
performance/cost posture for persistent tests.

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
