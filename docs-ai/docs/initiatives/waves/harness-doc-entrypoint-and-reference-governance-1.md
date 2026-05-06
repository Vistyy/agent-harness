# Wave harness-doc-entrypoint-and-reference-governance-1 - Harness documentation entrypoint and reference governance

**Status:** discovery-required

## Objective Boundary

- original objective: create reusable harness governance for documentation and
  skill references so skills are the operational entrypoints, durable docs are
  owner inputs, references are sparse and purpose-gated, completed waves are
  disposable after durable extraction, and the responsibility split between
  `harness-governance` and `documentation-stewardship` is clear enough to use.
- accepted reductions: no implementation in this session; this wave preserves
  context for a separate agent-harness session.
- residual gaps: all doctrine, audits, checks, and validation remain open.

## Context

- Project feedback from Budgeat documentation cleanup found durable docs had too
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
  imported from Budgeat;
- exact owner placement for skill entrypoints, doc owner inputs, reference
  density, and completed-wave disposal;
- completed-wave extraction targets that exclude ADRs by default, closed audit
  archives, and closed-wave indexes;
- a minimal implementation plan with touched-owner integrity for
  `harness-governance`, `documentation-stewardship`, `initiatives-workflow`,
  and any validator/check surface selected;
- proof rows for readback, governance check, targeted validation tests if
  checks change, and stale-reference scans for any deleted or moved docs.
