# Wave harness-design-preservation-anchor-gate-1 - Harness: design preservation anchor gate discovery

**Status:** done

## Problem

A project UI defect fix can drift into a generic replacement when
`design_judge` only checks final screenshots for cleanliness. Changed UI with a
project-defined visual language or product-defining UI pattern needs
preservation anchors so a cleaner but generic replacement is rejected unless
the project explicitly approved a visual-language replacement.

## Objective

Discover the smallest reusable harness change that makes visual-language
preservation enforceable for changed UI with a project-defined visual language
or product-defining UI pattern without adding project-specific style rules or
broad packet taxonomy.

## Scope

In scope:

- `skills/user-apps-design/references/design-quality-rubric.md` preservation-anchor rule shape,
- `adapters/github-copilot/agents/design_judge.agent.md` role contract parity,
- `adapters/codex/agents/design-judge.toml` role contract parity,
- final-review coverage check owner and wording, if needed,
- validation/readback proof for adapter parity and blocking semantics.

Out of scope:

- project-specific visual style such as paper tabs, fonts, or Szopping identity,
- pixel-diff tooling,
- broad wave-packet taxonomy for defect correction vs visual-system replacement unless discovery proves it is necessary,
- changing project overlays or product docs.

## Discovery Questions

- closed: `skills/user-apps-design/references/design-quality-rubric.md` owns
  the reusable preservation-anchor rule. Adapter prompts repeat only local
  verdict, handoff, and output consequences.
- closed: final-review coverage semantics belong in
  `skills/code-review/references/review-governance.md`. `final_reviewer`
  adapter prompts carry local input/check consequences and must not replace
  `design_judge`.
- closed: Codex role files are maintained as adapter source files under
  `adapters/codex/agents/`. Install tooling copies/symlinks them from that
  source; no generator owns `adapters/codex/agents/design-judge.toml`.
- closed: parity proof is the harness validator plus focused tests
  that require equivalent preservation-anchor terms in both Codex and Copilot
  `design_judge` adapters.

## Promotion Requirements

A promoted packet must include proof/counterfactual rows for:

- changed UI surfaces that require preservation anchors cause `design_judge` `blocked` when those anchors are missing,
- visibly generic replacement without approved replacement objective causes `design_judge` `reject`,
- controlled project-approved visual-language traits are not rejected solely because they use asymmetry, rotation, or other project-approved identity cues,
- final reviewer catches a broad UI closeout where `design_judge` passed without covering required preservation anchors,
- Codex and Copilot `design_judge` adapters carry equivalent preservation-anchor obligations.

## Planning Gate

- draft packet created for planning review; promotion requires
  `planning_critic` approval and planning `quality_guard` approval.
- planning `quality_guard`: APPROVE after proof design and owner placement
  repairs.
- `planning_critic`: APPROVE after system-boundary disposition and P8 proof
  ownership repairs.

## Packet

- closed after final review on 2026-05-05

## Closeout

- planning: `planning_critic` and planning `quality_guard` approved after
  proof-shape, owner-placement, system-boundary, and P8 ownership repairs.
- implementation `quality_guard`: APPROVE after stale closeout state and
  delivery-map task drift were repaired.
- final_reviewer: APPROVE after approved-identity-cue proof narrowing and
  Codex/Copilot preservation-anchor validator assertions were repaired.
- proof: focused design-judge/validator tests, harness validator readback,
  `just fmt`, and `just quality-fast` passed.

## Notes

This wave was created from project shell-nav drift. The project owns its
specific navigation invariant; this harness wave owns only the reusable
preservation-anchor gate.
