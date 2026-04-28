---
name: code-simplicity
description: "Use as the default simplicity lens for non-trivial planning, implementation, and review; prefer deletion, collapse, demotion, and the smallest honest solution."
---

Use when:
- shaping any non-trivial solution
- implementation starts adding helpers, layers, branches, workflow steps, or heavy proof
- user explicitly asks for simplification or cutdown
- review governance requires stable-to-extend check

Use this as the default pressure toward minimum sufficient shape.

## Scope

Preserve required outcomes, not accidental structure:
- delete unnecessary code, tests, workflow steps, or proof scaffolding
- collapse ownership when one owner is enough
- reuse existing paths before adding net-new structure
- demote optional complexity to manual/breakglass when that is honest
- keep shared decisions in one canonical place

This is first-pass design pressure, implementation pressure, and review pressure. It is not post-approval polish.

Primary question:
- what is the simplest honest shape that solves the current problem?
- what can disappear if we stop preserving inherited complexity?
- would next implementer likely want to refactor this slice before extending it?
- is this the minimum sufficient design for current requirement size?

Boundary:
- changing requirements
- deleting required behavior
- correctness issues unrelated to complexity

## Rules

- default to delete, collapse, demote, or reuse before net-new structure
- complexity needs explicit justification; simplicity does not
- reorganization without material reduction is not simplification
- old and new paths must not coexist unless a real compatibility owner requires
  it; otherwise replace the old path and delete the obsolete one in the same
  change
- if a simpler honest shape exists, keeping extra helpers, layers, workflow
  steps, proof machinery, or tests is a bug, not taste
- survivors must justify survival when simpler honest shapes exist
- cleaner organization is not a defense for preserved complexity
- tests are code; slow, wrong-layer, low-signal, or complexity-inducing tests
  are deletion candidates by default
- passing test is not evidence the test deserves to survive
- existing test is not evidence it still protects value
- if a test makes production code worse just so the test can exist, the test
  loses by default
- prefer one owner, one path, one proof, one place of truth when possible
- require exact `file:line` evidence
- treat duplicate logic, fake abstractions, hotspot growth, and wrong-layer placement as blockers by default
- treat broad casts, `any`, weak local modeling, and avoidable type indirection
  as simplicity blockers when they exist mainly to prop up an overbuilt shape
- allow small safe simplifications slightly outside diff when directly impacted
- do not recommend breaking public compatibility unless explicitly approved
- follow review-governance for disposition policy
- keep follow-up recommendations bounded and backlog-linked when deferred
- `better than before` is not enough if slice is still clearly refactor-worthy

## Heuristics

- start from the direct path, then add complexity only when the direct path fails a real constraint
- pick one canonical implementation
- inline trivial pass-throughs
- prefer one linear path over flag-heavy branching
- keep exports, types, params narrow
- prefer strong local typing over escape hatches and defensive casts
- do not keep a test just because it is already there
- prefer smaller proof over higher-layer proof when both are honest
- preserve acceptance-anchor proof path when wave brief or packet exists

Common failure modes:
- preserving awkward owner split and calling it reuse
- preserving old code behind compatibility shims, feature flags, obsolete
  fallback branches, or migration bridges after the new path is ready
- extracting thin helpers that exist only to soften ugly flow
- adding proof or workflow machinery instead of reducing system shape
- keeping optional automation that could honestly stay manual
- forcing implementation seams, mocks, or indirection mainly to satisfy a test
- splitting one direct path into many “reusable” pieces before real reuse exists

## Process

1. name the required outcome and current owner/boundary in scope
2. ask what can be deleted, collapsed, demoted, or left manual
3. identify reuse targets, or say none
4. sweep for repeated decision logic, duplicated normalization, context rebuilding, and fake abstractions
5. inspect hotspot files or tests beyond changed hunk when needed
6. if implementing, proactively delete obvious owned-scope excess instead of
   waiting for reviewer rescue
7. return the simplest honest shape without hiding blockers or survivor bias

## Reporting

- Keep findings in the normal review or planning format owned by the active
  workflow.
- When this lens matters, name:
  - required outcome
  - simpler honest shape
  - what should disappear
  - top unnecessary complexity sources
- If user gave explicit simplicity directives, say how they were honored or
  why a surviving complexity still had to remain.
