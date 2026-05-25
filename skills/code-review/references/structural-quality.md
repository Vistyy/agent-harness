# Structural Quality

Maintainability and architecture lens for implementation quality, refactors,
added abstractions, large files, branching/control-flow changes, type
boundaries, fallback paths, wrappers, helper reuse, and architecture/ownership
drift.

Working behavior is not enough. Review whether the implementation makes the
codebase easier or harder to reason about.

## Approval Bar

Ask whether the objective can be met with fewer concepts, branches, states,
wrappers, fallback paths, public methods, defensive checks, tests, docs, or
proof entrypoints. Added surface needs a concrete owner and failure mode.

Defensive code is valid only at real boundaries: external input, auth, money,
storage, concurrency, migrations, distributed runtime, security, privacy, or
untrusted integration. Internal trusted flows stay direct.

Treat these as presumptive blockers unless the implementation gives a clear
local reason that survives objective, owner, and proof review:

- a complicated implementation where a simpler framing could delete concepts,
  branches, helpers, modes, state, or layers
- a file crossing roughly 1000 lines, or a large file absorbing a new
  responsibility instead of gaining a focused owner
- ad hoc branching, booleans, nullable modes, fallback paths, special cases, or
  temporary logic inserted into an already busy flow
- feature logic leaking into shared/general paths, or implementation details
  leaking through public APIs
- thin wrappers, identity abstractions, generic dispatchers, pass-through
  helpers, or indirection that does not reduce caller knowledge
- cast-heavy, `any`/`unknown`-heavy, loosely shaped, or unnecessarily optional
  contracts instead of explicit invariants
- bespoke helpers where the codebase already has a canonical utility
- sequential orchestration or partial-update structure that is less clear or
  less atomic than the owner path needs
- refactors that move complexity around without deleting concepts
- tests, docs, fixtures, or proof entrypoints that preserve obsolete or
  accidental API shape

Do not rubber-stamp a technically working change that makes the surrounding
code messier, harder to scan, or less natural for its owner.

## Preferred Remedies

Require structural fixes instead of cosmetic cleanup:

- delete an indirection layer instead of renaming or polishing it
- collapse duplicate branches into one clear flow
- move feature logic to the layer that owns the concept
- replace special cases with an explicit model, policy, state object, or typed
  contract
- reuse the canonical helper instead of adding a near-duplicate
- split focused modules when a file or owner is absorbing unrelated work
- make type, state, lifecycle, and ownership boundaries explicit so control
  flow gets simpler
- delete obsolete fallback paths and tests instead of carrying compatibility
  for no current owner
- parallelize independent work when doing so also makes orchestration simpler
- make related updates atomic when partial state would be harder to reason about

Do not spend attention on naming nits while structural, correctness, proof, or
owner issues remain.

## Output

Report:

- structural-quality verdict: pass, block, blocked, or not-applicable
- simplifications, deletions, decompositions, or owner moves considered
- presumptive blockers found or explicitly ruled out
- findings using the main `code-review` Finding Standard
