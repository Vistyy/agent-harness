# Harness Design Context Contract

**Status:** done

Superseded by later UI workflow compaction: global context/register and taste
contracts were collapsed into a generic project design source requirement in
`skills/user-apps-design/SKILL.md`.

## Objective Boundary

- original objective: enhance the harness design workflow with the useful ideas
  from Impeccable, going beyond instructions when it truly helps output.
- accepted reductions: do not port Impeccable wholesale or implement live mode
  in this wave; keep those as future work unless this slice exposes an owner
  defect that requires them now.
- residual gaps: anti-pattern automation and command/workflow specialization
  are deferred to backlog; live visual iteration remains outside this wave by
  accepted reduction.

## Scope

- superseded scope: reusable `user-apps-design` context/register contract,
  register-aware taste pressure, screenshot-led `design_judge`
  handoff consequences, and focused validation that prevents adapter drift.
- out of scope: importing Impeccable as a dependency, adding a browser
  extension, implementing HMR live variants, project-specific product/design
  files, or adding a broad design-command language.

## Alternatives And Deferrals

- adopt Impeccable wholesale: rejected because it would duplicate harness
  skill ownership, import a second command router, and make Impeccable's taste
  the global authority instead of project design truth.
- start with anti-pattern automation: deferred because detector rules need the
  design-context/register contract first to avoid false global bans such as
  rejecting system fonts in product UI.
- start with a broad command vocabulary: deferred because the harness already
  routes by owner skills; command specialization needs the context/register
  owner before adding entrypoints.
- start with live visual iteration: out of scope for this wave because the
  user accepted not porting live mode now; it remains a possible future product
  investment, not a prerequisite for the first workflow improvement.

## Closed Decisions

- `user-apps-design` owns reusable design context and register semantics.
- Projects own product facts, visual systems, and exact file locations; the
  harness may recognize `PRODUCT.md` and `DESIGN.md` as portable aliases.
- superseded: broad UI work named a context source, register, and taste
  posture before claiming visual approval.
- Missing or contradictory design context blocks broad visual claims unless the
  user explicitly narrows the claim to avoid the missing truth.
- `design_judge` verifies design-context/register coverage from handoff
  artifacts; it does not run discovery or invent product truth.

## Proof Plan

- focused contract tests: `uv run pytest tests/test_validate_harness.py -q`
- harness validation: `uv run python scripts/validate_harness.py`
- governance check: `agent-harness governance check --repo-root .`
- quality fast: `just quality-fast`

## Planning Gate

- `planning_critic`: APPROVE. The repaired draft preserves the binding
  objective and accepted reductions, names the smaller first slice, tracks
  anti-pattern automation and command specialization in backlog, triggers the
  system-boundary disposition, and gives bounded proof through exact test and
  fixture artifacts.
- `quality_guard`: APPROVE. Later compaction moved the canonical reusable UI
  approval owner to `skills/user-apps-design/SKILL.md`, keeps project truth out
  of global harness policy, includes the required system-boundary disposition,
  and strengthens proof rows to cover blocking behavior and adapter handoff
  coverage.

## Packet

- closed after final review on 2026-05-05.

## Closeout

- planning_critic: APPROVE after the packet was demoted, boundary-triggered,
  given exact proof artifacts, and durable Impeccable-derived deferrals were
  added.
- planning quality_guard: APPROVE after the canonical owner, boundary
  disposition, and proof rows were repaired.
- implementation quality_guard: APPROVE with no material findings.
- final_reviewer: APPROVE with acceptable touched-component integrity and no
  findings.
- proof: focused design-context tests, validate-harness tests, harness
  validation, governance check, and `just quality-fast` passed.
