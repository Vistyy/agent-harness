---
name: harness-governance
description: "Use for reusable agent-harness governance: skill architecture, global AGENTS/project overlays, adapter install behavior, repo posture, and checks."
---

# Harness Governance

Use this skill for the reusable agent-harness repository and for
harness-managed project overlay contracts.

## Operating Model

The global agent harness owns reusable agent workflow policy, skills, role
adapters, templates, prompts, and validation. Harness-managed projects own
product facts, architecture, roadmap, runtime topology, local command bodies,
active execution state, and project-only exceptions.

Codex is one adapter. The harness identity is generic.

Global reusable policy lives in this harness repository. Project overlays may
narrow or extend global policy only for project facts, local runtime shape, or
explicit documented exceptions. Reusable global truth must not live in a
project active-work directory.

Harness changes are reviewed and committed in the harness repository.
Project-overlay changes are reviewed in the project repository. Closeout
reports must state both repository statuses when a task touches both.

A harness change is non-trivial when it touches any of:

- `AGENTS.md`
- skills or skill metadata
- adapter prompts, role policy, or adapter config
- validation scripts or checks
- planning, review, verification, delegation, or workflow policy
- removal, replacement, or split of a workflow owner

Harness closeout adds:

- changed reusable owners
- removed obsolete routes
- new or changed routing triggers
- harness repository status
- project repository status when project overlays also changed

## Reference Loading

Load `references/harness-contracts.md` when changing project overlays,
`AGENTS.md`, repository posture, or reusable enforcement checks.

Load `references/skill-architecture.md` when authoring, splitting, installing,
or validating reusable skills.

Load `references/skill-invocation-cost.md` when auditing broad entrypoints or
proposing a new routing skill.

## Boundary

Keep this skill focused on reusable harness governance, project overlays,
adapter posture, skill architecture, and enforcement checks.

Use this skill when a workflow-feedback entry is promoted into reusable harness
policy, skill guidance, adapter posture, or validation.

## Skill Architecture

Reusable skill guidance belongs in focused skill directories.

- `SKILL.md` contains trigger description and workflow mechanics.
- Reference material should be split out only when the content is too large or
  specialized to keep in the skill body.
- Asset folders own templates copied or consumed by the skill.
- Script folders own helper scripts used by the skill.
- Agent-adapter folders own platform-specific hints.

Keep project facts out of reusable skills. Keep skill frontmatter concise and
route by description. Keep cross-skill references rare: use them only for direct
coupling, complex routing, or a dedicated routing skill. Move reusable
supporting material with the owning skill instead of leaving it in a project
documentation tree. Do not duplicate the same durable rule in multiple skills.
Keep examples generic unless the skill is explicitly project-local.

Detailed skill-authoring quality rules live in
`references/skill-architecture.md`.

## Enforcement Checks

Reusable project-overlay link validation is owned here:

```bash
python skills/harness-governance/scripts/harness_enforcement_checks.py .
```

Load `references/harness-contracts.md` before changing check semantics or
project-overlay enforcement policy.
