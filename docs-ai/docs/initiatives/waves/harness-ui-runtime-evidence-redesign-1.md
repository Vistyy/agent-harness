# Wave harness-ui-runtime-evidence-redesign-1 - UI runtime evidence and design approval redesign

**Status:** done

Superseded by later UI workflow compaction: `runtime_evidence` is no longer a
default broad UI design-readiness gate. Current visual approval is
screenshot/contact-sheet based and owned by `design_judge`.

## Problem

The current UI runtime evidence flow can pass a visibly poor product UI when
the implementation satisfies selector-level claims. A triggering runtime proof
approved a screenshot that a human review immediately rejected as visually
unacceptable: oversized low-information rows, detached search block, weak
composition, awkward cost slab, and generic scaffolding despite a `20/20`
design-fidelity score.

This is a harness workflow failure, not only a project implementation defect.
Runtime evidence behaved as a claim-fulfillment auditor and produced no
separate design-gate handoff capable of rejecting non-shippable UI.

## Objective

Redesign the reusable harness flow so broad UI work cannot be approved by
runtime checklist fulfillment alone. Runtime evidence must prove live behavior
and artifact sufficiency; UI approval must require a separate screenshot-led
design judgment with constructive findings and an explicit ship-quality verdict.

## Scope

In scope:

- runtime evidence contract for broad visual claims,
- relationship between `runtime-proof`, `webapp-testing`/`mobileapp-testing`,
  `user-apps-design`, `code-review`, and final closeout,
- a dedicated `design_judge` role with reject authority,
- pre-selection role registration, authorization, and adapter routing for
  `design_judge`,
- screenshot/contact-sheet inspection requirements,
- hard visual rejection conditions for non-shippable UI,
- constructive feedback requirements when rejecting or approving with issues,
- executable eval or regression fixture where a functional but ugly UI must
  reject.

Out of scope:

- project-specific redesign implementation,
- replacing product design ownership with generic harness taste,
- backend/runtime correctness proof unrelated to visual approval.

## Candidate Task Cards

- `harness/runtime-evidence/ui-design-gate-boundary-contract`
- `harness/runtime-evidence/screenshot-artifact-sufficiency-gate`
- `harness/review/final-ui-closeout-screenshot-inspection-contract`
- `harness/evals/regression-case-bad-ui-must-reject`

## Required Planning Questions

- closed: UI design approval is a separate blocking gate owned by
  `user-apps-design`; `runtime_evidence` owns live behavior and screenshot
  artifact sufficiency, not product-grade visual approval by score.
- closed: `design_judge` is the executable screenshot-led product UI design
  approval gate for broad product-facing UI chunks. It does not run the app,
  review code, or replace runtime evidence.
- closed: `quality_guard` remains the implementation quality gate. It verifies
  required runtime/design gates exist and cover the claim; it does not perform
  runtime proof or visual design judgment.
- closed: UI design verdicts are `pass`, `reject`, and `blocked`; only
  `design_judge` `pass` can support broad UI completion.
- closed: A UI-design pass requires inspected screenshot/contact-sheet
  artifacts for the claimed surface, state, viewport/device, and interaction
  posture. DOM assertions, snapshots, logs, or selector checks are insufficient.
- superseded: hard visual blockers are now owned by the current
  `design_judge` prompt and project design source, not this historical wave.
- closed: Final review must name the screenshot/contact-sheet paths it
  inspected and cite any visible blockers or explicitly state `none observed`;
  missing inspection blocks UI closeout.
- closed: Runtime and design reports stay bounded by requiring artifact paths,
  verdict, blockers, and at most `3-5` concrete repair findings unless the
  gate rejects and more detail is necessary to unblock repair.
- superseded: later compaction removed the static bad-UI fixture and score-like
  proof language. Current `design_judge` approval is screenshot/contact-sheet
  based and scoped by project design source.

## Minimum Acceptance Bar

- A UI runtime evidence `pass` must be impossible without screenshot/contact
  sheet artifact sufficiency for `design_judge` handoff.
- Broad UI completion must require `design_judge` `pass`; `quality_guard` and
  `final_reviewer` may only verify gate coverage, not replace it.
- Functional assertions, absence of console errors, and DOM order cannot by
  themselves satisfy broad visual approval.
- Runtime evidence is not the default visual approval gate; screenshot capture
  mechanics feed `design_judge` when broad visual approval is claimed.
- `design_judge` must reject when artifacts show generic, visually incoherent,
  scaffold-like, ugly, or non-shippable UI, and include concrete visible
  findings with enough direction for repair.
- Final closeout for UI redesign must inspect the reviewed screenshots or
  explicitly block.
- Superseded: the static regression/eval requirement was removed as low-value
  schema proof.

## Origin Evidence

- Triggering artifact:
  runtime report and screenshot from the project worktree that exposed the
  failed approval.
- Human rejection context:
  A screenshot was rejected after runtime evidence reported `pass` and `20/20`;
  the workflow produced no meaningful constructive visual critique until the
  user intervened.

## Planning Gate

Reopened after user feedback: design judgment must be isolated in a dedicated
role, not folded into `quality_guard`. The earlier planning approvals are stale
for the revised role-boundary model. Fresh planning critic approval is required
before execution-ready promotion. This wave depends on
`harness-strict-validation-governance-1` for blocking gate semantics and
`harness-runtime-evidence-live-use-contract-1` for runtime evidence role
semantics.

Planning critic blocked promotion on missing durable state promotion,
pre-selection `design_judge` routing/authorization, and non-durable bad-UI
proof. The draft packet now requires those fixes before execution-ready
promotion.

- planning_critic: APPROVE after packet repairs for stale dependency state,
  pre-selection `design_judge` routing/authorization, adapter callability proof,
  executable bad-UI rejection proof, and boundary write paths.
- planning quality_guard: APPROVE for execution-ready promotion. Scope, role
  boundaries, Required Gates, task cards, proof rows, stop conditions, and
  touched-owner integrity are execution-ready.

## Packet

- closed after final review on 2026-05-05

## Closeout

- superseded: static bad-UI fixture proof was later removed as low-value
  schema proof that did not exercise `design_judge`.
- quality_guard: APPROVE for implementation state and honest blocker handling.
- final_reviewer: APPROVE after live `design_judge` proof resolved P1.
- proof: focused validator/design tests, harness validation, and
  `just quality-fast` passed.
