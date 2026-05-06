# Wave harness-doc-entrypoint-and-reference-governance-1 - Harness documentation entrypoint and reference governance

**Status:** done

## Objective Boundary

- original objective: create reusable harness governance for documentation and
  skill references so skills are the operational entrypoints, durable docs are
  owner inputs, references are sparse and purpose-gated, completed waves are
  disposable after durable extraction, and the responsibility split between
  `harness-governance` and `documentation-stewardship` is clear enough to use.
- accepted reductions: repo-wide completed-wave cleanup is deferred to later
  coherent waves; no ADR default, closed audit archive, or closed-wave index.
- residual gaps: repo-wide completed-wave cleanup is deferred to later coherent
  waves; this wave owns governance and a narrow check.

## Context

- Project feedback from documentation cleanup found durable docs had too
  many cross-references, especially to completed wave stubs.
- The desired direction is:
  - skills are always the agent workflow entrypoints;
  - durable docs are project or harness owner inputs loaded by skills;
  - docs should rarely reference skills except compact routing metadata;
  - skills may reference docs only as purpose-gated owner inputs;
  - references should matter when used, not appear as broad reference lists;
  - completed waves should not stay durable by default after closeout;
  - retained decisions/invariants from completed waves must be extracted into
    durable owners or valid backlog before wave artifacts are deleted.
- Current ambiguity: `harness-governance` owns reusable harness posture and
  skill architecture, while `documentation-stewardship` owns durable rule
  placement, one source of truth, terminology, and density. The boundary is
  usable but awkward when the work is "how skills and docs reference each
  other."
- Discussed constraints:
  - do not add an ADR default; projects with decision-record systems route
    there through their local owner;
  - do not retain closed-wave context through closed audit archives or a closed
    wave index;
  - if completed-wave context matters, extract it into the real durable owner;
  - split repo-wide completed-wave cleanup into later coherent waves.

## Planning Gaps

- Audit the agent-harness repo itself before changing rules:
  - skill-to-doc references;
  - doc-to-skill references;
  - broad reference lists in skill bodies and durable docs;
  - completed-wave retention and pointer/stub patterns;
  - duplicated or unclear ownership between `harness-governance` and
    `documentation-stewardship`.
- Decide the owner split:
  - which reusable rule belongs in `harness-governance`;
  - which durable source-of-truth/reference-density rule belongs in
    `documentation-stewardship`;
  - whether one skill should route to the other or whether wording should
    simply clarify the boundary.
- Decide completed-wave lifecycle policy and closeout requirements.
- Decide whether validation should enforce any exact high-signal rule, such as
  preventing durable docs from depending on completed wave files as doctrine.
  Keep exemptions precise for active wave planning, delivery-map state,
  tests/fixtures, and any explicitly scoped migration cleanup.
- Keep wording minimal and enforceable; avoid adding another process layer.

## Starting Points

- `AGENTS.md`
- `skills/harness-governance/SKILL.md`
- `skills/harness-governance/references/harness-contracts.md`
- `skills/harness-governance/references/skill-architecture.md`
- `skills/documentation-stewardship/SKILL.md`
- `skills/initiatives-workflow/SKILL.md`
- `docs-ai/docs/initiatives/waves/*.md`
- `docs-ai/current-work/delivery-map.md`

## Promotion Requirement

Promote only after `planning-intake`, `planning_critic`, and `quality_guard`
approve:

- an agent-harness reference audit with concrete findings, not assumptions
  imported from another project;
- exact owner placement for skill entrypoints, doc owner inputs, reference
  density, and completed-wave disposal;
- completed-wave extraction targets that exclude ADRs by default, closed audit
  archives, and closed-wave indexes;
- a minimal implementation plan with touched-owner integrity for
  `harness-governance`, `documentation-stewardship`, `initiatives-workflow`,
  and any validator/check surface selected;
- proof rows for readback, governance check, targeted validation tests if
  checks change, and stale-reference scans for any deleted or moved docs.

## Promotion Decision

- Audit found one active discovery wave and fourteen `done` wave briefs in
  `docs-ai/docs/initiatives/waves`; existing skill reference gates are already
  purpose-gated, while durable wave history carries most direct skill-path
  references.
- Execution scope is one governance/check slice. Existing done-wave cleanup is
  deferred because deleting all retained wave history is a separate tranche.
- Owner split:
  - `harness-governance`: skill entrypoints, routing, purpose-gated skill
    references, and exact harness checks.
  - `documentation-stewardship`: source of truth, retention, successor review,
    and density.
  - `initiatives-workflow`: wave lifecycle and closeout mechanics.
- Selected validation: a narrow governance check for durable docs that link to
  completed wave files as doctrine while allowing active wave planning,
  delivery-map state, tests/fixtures, and scoped migration cleanup.
- Planning gate record:
  - initial `planning_critic`: rejected; blockers were missing approval record,
    stale delivery-map state, inconsistent accepted reductions, underframed
    check semantics, and asserted touched-component integrity.
  - repaired `planning_critic`: approved; touched-component integrity
    acceptable, no must-block signals, no accepted-debt backlog link, and
    residual risk limited to keeping the check exact rather than subjective.
  - initial `quality_guard`: rejected; blockers were objective narrowing,
    missing approval record, underdeclared boundary trigger, and stale
    delivery-map state.
  - repaired `quality_guard`: blocked only because repaired
    `planning_critic` approval had not yet been recorded.
  - final `quality_guard`: approved; touched-component integrity acceptable,
    no must-block signals, no accepted-debt backlog link, and residual risk
    limited to keeping the check path/status-based.

## Closeout

- implemented reusable owner split:
  - `harness-governance` owns skill entrypoints, purpose-gated references, and
    exact governance checks;
  - `documentation-stewardship` owns durable source of truth, retention,
    successor review, and completed-wave extraction targets;
  - `initiatives-workflow` owns wave lifecycle and closeout mechanics.
- implemented `docs.completed-wave-doctrine-reference`, a path/status-based
  governance check for durable non-wave docs that reference `done` wave briefs.
- proof:
  - `uv run pytest tests/test_agent_harness_cli.py -k governance_check`: 7
    passed;
  - `agent-harness governance check --repo-root .`: passed;
  - `just quality-fast`: 85 tests passed, harness validation self-test passed,
    harness validation passed, and Codex install smoke passed.
- reviews:
  - `planning_critic`: approved promotion;
  - `quality_guard`: approved promotion and implementation;
  - `final_reviewer`: approved closeout review with no findings.
- accepted residual scope: repo-wide cleanup of existing completed wave briefs
  remains deferred to later coherent waves.
