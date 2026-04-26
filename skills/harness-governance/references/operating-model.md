# Harness Operating Model

The global agent harness owns reusable agent workflow policy, skills, role
adapters, templates, prompts, and validation.

Harness-managed projects own product facts, architecture, roadmap, runtime
topology, local command bodies, active execution state, and project-only
exceptions.

Codex is one adapter. The harness identity is generic.

## Ownership

- Global reusable policy lives in this harness repository.
- Project overlays live in the project repository.
- A project overlay may narrow or extend global policy only for project facts,
  local runtime shape, or explicitly documented exceptions.
- Reusable global truth must not live in a project active-work directory.

## Git Discipline

Harness changes are reviewed and committed in the harness repository.
Project-overlay changes are reviewed in the project repository.
Closeout reports must state both repository statuses when a task touches both.
