# Wave harness-mock-parity-design-workflow-1 - Harness: thin UI contract with project-local design engines

**Status:** done

## Objective Boundary

- original objective: replace the current reusable UI design workflow because
  broad UI gates still approve ugly, visibly broken, or weakly implemented UI;
  cut the global harness UI doctrine down to a lightweight reusable contract,
  preserve `design_judge`, move design methodology to project-local design
  engines such as Impeccable, and remove `runtime_evidence` from default UI
  design approval.
- accepted reductions: do not configure Impeccable in a downstream product
  project, and do not import Impeccable or require `npx impeccable` from the
  global harness.
- residual gaps: none intended after execution. Project-specific Impeccable
  installation remains project work, not harness work.

## Problem

The current workflow scatters design quality across anchors, scoring,
extra reports, runtime evidence, and final review. That creates process
without force. An implementation can keep abstract traits from a design brief or
mock while losing the visible ingredients that made the design worth building,
then `design_judge` can approve the screenshot because the handoff asks it to
judge vague anchors instead of the actual visual target.

The failed behavior to eliminate:

- mockups are treated as optional mood instead of concrete visual direction
  when the task needs a visual target;
- agents translate rich visual direction into lossy prose and then implement
  the prose, not the visible design;
- implementation can stop after a first pass, despite obvious browser-visible
  defects;
- review roles inspect reports and checklists more readily than the actual
  rendered surface;
- `runtime_evidence` adds ceremony to UI work while still missing obvious
  visual failures, because it is not a design authority and often duplicates
  browser proof mechanics.

## Impeccable Research Notes

Impeccable is useful because it changes the work order, not because it has a
longer rubric:

- `PRODUCT.md` and `DESIGN.md` are preflight context. Missing product context
  blocks design work instead of letting the agent invent taste from the prompt.
- `shape` produces a user-confirmed task brief before code. The brief covers
  purpose, audience, content ranges, states, fidelity, visual direction,
  constraints, anti-goals, and recommended design references.
- image generation is capability-gated but mandatory for ambiguous mid-fi,
  high-fi, or production-ready surfaces when the harness has native image
  generation. The generated images are direction probes or a north-star mock,
  not final UX, final copy, or rasterized UI.
- `craft` requires a mock fidelity inventory before implementation: visible
  ingredients, signature motifs, composition, nav/CTA treatment, section
  sequence, typography, density, color/material, and accepted omissions.
- implementation is not complete after first code. Browser inspection across
  relevant viewports is required, followed by at least one critique-and-fix
  pass unless no material defects exist.
- `live` mode makes visual iteration concrete: select a rendered element,
  generate distinct variants, preserve identity by default, and let the user
  accept or reject in the browser.
- deterministic anti-pattern detection catches common AI slop, while LLM
  critique covers non-deterministic taste failures. The detector is evidence,
  not design approval.

Adopt the philosophy, not the entire product. Agent Harness should not import
Impeccable as a tool dependency or copy its command taxonomy wholesale.

## Replacement Workflow Direction

The global harness should become the guardrail, not the design engine.

Global reusable contract:

1. project-local design context owns product taste, visual method, reference
   artifacts, and mock/brief semantics;
2. broad UI work must name the project design source or block/narrow the claim
   when the source is missing;
3. broad UI work must produce rendered screenshots/contact sheets for claimed
   states, viewports, and devices;
4. broad visual approval belongs to `design_judge`;
5. `design_judge` compares rendered artifacts against the binding objective,
   project design context, and approved project-local targets such as
   Impeccable shape/craft briefs, generated direction probes, visual
   inventories, or difference ledgers;
6. selectors, tests, logs, detector output, numeric scores, and runtime
   evidence do not approve visual quality;
7. global harness docs should not duplicate project-local design methodology.

Project-local design engine contract:

- projects may configure Impeccable, bespoke `PRODUCT.md` / `DESIGN.md`,
  existing design-system docs, or another local design workflow;
- the project owner decides when image generation, shape/craft, live browser
  iteration, anti-pattern detection, mock inventories, or difference ledgers
  are required;
- global closeout checks whether the declared project-local workflow was
  followed for the claim, not whether every project uses the same workflow.

## Runtime Evidence Direction

UI design approval must not require `runtime_evidence` as a separate role by
default. Replacement:

- keep `runtime-proof` policy for non-trivial runtime-visible behavior;
- use `webapp-testing` and `mobileapp-testing` mechanics to capture live
  screenshots, logs, and state artifacts in the parent or `check_runner`;
- make screenshot/contact-sheet sufficiency part of the UI design workflow and
  `design_judge` handoff, not a `runtime_evidence` pass;
- reserve `runtime_evidence` for exceptional non-trivial live behavior claims
  where an independent verifier is valuable: auth/session, checkout/payment,
  destructive flows, mobile install/deep links/offline, queues/sync,
  notifications, tenant/data-dependent behavior, and release smoke checks.

## Scope

In scope:

- `skills/user-apps-design/**` lightweight UI contract and reference
  ownership;
- `adapters/codex/agents/design-judge.toml` and
  `adapters/github-copilot/agents/design_judge.agent.md`;
- `skills/runtime-proof/**`, `skills/webapp-testing/**`,
  `skills/mobileapp-testing/**`, and `runtime_evidence` adapters to remove
  default UI-design approval responsibility and keep only exceptional live
  behavior use;
- `skills/verification-before-completion/**`,
  `skills/code-review/references/review-governance.md`, quality/final reviewer
  prompts, and validation only where they enforce the new closeout boundary;
- stale-proof cleanup for old UI fixture/evaluator/test layers so validation
  and quality proof stay focused on retained harness contracts.

Out of scope:

- project-specific product style rules or project-local Impeccable setup;
- importing Impeccable or requiring `npx impeccable`;
- pixel-perfect visual diff as the first implementation;
- making generated mockups durable project truth;
- replacing user/project design truth with generated images;
- removing runtime proof for real runtime behavior without a successor owner.

## Closed Decisions

- Global `user-apps-design` keeps only reusable UI guardrails. Project-local
  design docs own visual method and product taste.
- `harness-governance` already owns the project overlay boundary. This wave
  adds no new global project-design-engine contract. If the `user-apps-design`
  pointer is insufficient, execution stops and returns to planning instead of
  expanding overlay policy.
- Broad UI design readiness must not require `runtime_evidence` by default.
  Validation should fail stale default UI/runtime coupling in global docs and
  adapter prompts.
- No static design-judge fixture is required. It was removed as low-value
  schema proof that did not exercise the judge.

## Promotion Requirements

Closed by `planning-intake`, `planning_critic`, and `quality_guard`.
The execution packet includes proof rows for:

- broad UI work blocks when project design context or declared local workflow
  is missing and the claim cannot be narrowed honestly;
- global docs avoid defining Impeccable-like design methodology and instead
  require a project-owned design source;
- `design_judge` prompts require screenshot/contact-sheet visual approval and
  block attempts to substitute selectors, tests, logs, runtime evidence, or
  code review;
- closeout rejects missing or stale browser screenshots/contact sheets,
  project-local design artifacts when required by that project, or
  design-judge handoffs narrower than the UI claim;
- broad UI design readiness does not require `runtime_evidence` by default,
  while exceptional live behavior claims still route to runtime proof.

## Starting Points

- Impeccable research from `pbakaus/impeccable`: core skill preflight,
  `shape`, `craft`, `live`, `critique`, and deterministic anti-pattern
  detector. Treat as external research, not a durable local dependency.
- `skills/user-apps-design/SKILL.md`
- `adapters/codex/agents/design-judge.toml`
- `adapters/github-copilot/agents/design_judge.agent.md`
- `adapters/codex/agents/runtime-evidence.toml`
- `adapters/github-copilot/agents/runtime_evidence.agent.md`
- `skills/runtime-proof/SKILL.md`
- `skills/verification-before-completion/SKILL.md`

## Planning Gate

- planning_critic: APPROVE on 2026-05-06. Final packet closes prior blockers:
  no hidden `harness-governance` project-design-engine expansion, exact P2
  runtime-evidence validation proof, and explicit Codex/Copilot reviewer
  prompt surfaces.
- planning quality_guard: APPROVE on 2026-05-06. Packet preserves the binding
  objective, keeps global UI doctrine thin, routes design method to
  project-local owners, preserves `design_judge`, removes `runtime_evidence`
  from default UI design approval, keeps runtime proof for exceptional live
  behavior claims, and has acceptable touched-component integrity.

## Closeout

- implementation `quality_guard`: APPROVE on 2026-05-06 after stale
  design-anchor, runtime visual-approval, deleted-rubric, and direct-consumer
  owner references were repaired.
- final_reviewer: APPROVE on 2026-05-06 after stale proof and ownership
  blockers were repaired.
- proof: `just quality-fast` passed with 82 tests, harness validation
  self-test, harness validation, and Codex install smoke.
