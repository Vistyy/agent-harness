# Wave harness-strict-validation-governance-1 - Strict blocking validation governance

**Status:** done

## Problem

Harness validation roles and rules can drift into advisory or lenient posture:
reviewers may approve partial improvement, effort, plausible acceptance, or
functional success even when the binding claim is not fully supported. That
weakness affects UI design, runtime proof, code review, architecture,
planning, tests, and final closeout.

If a reusable rule is important enough to encode in the harness, failure of
that rule should normally block the claim. Non-blocking observations are valid
only outside the binding objective or as explicitly accepted debt.

## Objective

Define and enforce a compact reusable strict-validation contract for harness
gates, then update wave state so every material claim names its required gates,
proof vehicle, owner, artifacts, and blocking conditions before execution.

## Scope

In scope:

- `harness-governance` ownership of blocking gate semantics,
- general strict reviewer posture for validation roles,
- packet `Required Gates` matrix in wave state,
- pass over reusable skills and role prompts for advisory required-gate
  language,
- narrow validation checks for concrete advisory drift and required-gate matrix
  shape.

Out of scope:

- UI-specific `design_judge` role implementation,
- broad semantic lint for reviewer softness,
- project-specific overlay rewrites,
- replacing human review judgment with automated scoring.

## Candidate Task Cards

- `harness/governance/blocking-gate-contract`
- `harness/initiatives/required-gates-packet-matrix`
- `harness/review/strict-validation-posture`
- `harness/skills/remove-advisory-gate-language`
- `harness/validation/no-advisory-required-gates`

## Required Planning Questions

- closed: Reusable harness gates use `pass | reject | blocked | not-applicable`
  semantics. Required gate failures are not advisory.
- closed: `NON-BLOCKING` is valid only outside the binding objective or for
  explicitly accepted debt with owner, risk, and removal condition.
- closed: Reviewer roles default to falsifying the binding claim against
  evidence. Ambiguous or missing required evidence is `blocked`; contradictory
  evidence inside the claim is `reject`.
- closed: Wave packets need a `Required Gates` matrix so implementers,
  parent orchestration, reviewers, and final closeout know which gates must run
  and what blocks.
- closed: Automated validation should stay narrow: catch concrete dangerous
  advisory wording and missing matrix structure, not subjective tone.

## Minimum Acceptance Bar

- Harness governance owns the blocking-gate contract in one durable place.
- Review/validation consumers point to the owner and state local consequence
  without redefining the full policy.
- Wave packet contract requires a `Required Gates` matrix for material claims.
- Existing reusable skills and validation role prompts are scanned and revised
  so required gates are not framed as advisory.
- Validation catches concrete advisory drift for required gate/proof/review
  contexts and catches missing `Required Gates` matrix in execution packets.

## Planning Gate

- planning_critic: APPROVE after corrections. The two-wave split is accepted:
  this wave owns strict blocking governance and `Required Gates`; the UI wave
  remains dependent and discovery-required.
- quality_guard: APPROVE. Wave 1 has closed decisions, implementer-eligible
  task cards, owned surfaces, locked invariants, stop-and-handback triggers,
  proof rows, a `Required Gates` matrix, and acceptable touched-component
  integrity with no accepted debt.
- final_reviewer: APPROVE after fixes for runtime/design role boundary,
  non-blocking softening detection, and placeholder-only matrix validation.

## Packet

- closed after final review on 2026-05-05

## Closeout

- quality_guard: APPROVE, no findings.
- final_reviewer: APPROVE after required fixes.
- proof: focused validator tests, harness validation, governance check, and
  `just quality-fast` passed.
