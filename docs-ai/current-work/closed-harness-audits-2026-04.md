# Closed Harness Audits - 2026-04

This is a compact archive of completed harness audit and cleanup records.
There is no active execution plan in this file.

## Closed Records

### Terminology Audit Seed - 2026-04-27

- Added terminology and doc-writing doctrine under `documentation-stewardship`.
- Seeded terminology checks for role vocabulary, testing doctrine, entrypoint
  language, and source-of-truth/owner wording.
- No active terminology audit remains open here. Future terminology work starts
  from `documentation-stewardship`.

### OpenAI Metadata Audit - 2026-04-27

- Verified skill `agents/openai.yaml` metadata coverage.
- Updated selected prompts/descriptions for `code-review`,
  `subagent-orchestration`, Svelte guidance,
  `systematic-debugging`, and `testing-best-practices`.
- Added `workflow-feedback` metadata.
- Validation command: `uv run python scripts/validate_harness.py`.

### Skill Ownership Audit - 2026-04-27

- Audited all `skills/*/SKILL.md`, skill references/assets/templates, and
  adapter role docs for ownership clarity.
- Moved misplaced mobile and systematic-debugging references into
  `references/`.
- Normalized stale or repo-root-looking skill links.
- Later cleanup tightened the policy further: skill bodies describe their own
  capability/workflow and do not act as general routing indexes.

### Wave B Compaction Dispositions - 2026-04-27

- Compacted testing doctrine into focused references while preserving route
  discoverability from `testing-best-practices`.
- Kept browser/mobile runtime proof mechanics separate from persistent-test
  doctrine.

### Skill Description Audit - 2026-04-28

- Tightened event-shaped triggers for `systematic-debugging`,
  `subagent-orchestration`, and `code-review`.
- Confirmed no additional broad event skill was needed after
  `workflow-feedback`.

### Workflow Feedback Skill Handoff - 2026-04-28

- Removed legacy `implementation-decision-ledger` and `github-diagnostics`
  skills.
- Added lean `workflow-feedback` skill and project ledger template.
- Hardened stale skill-reference validation for removed skill paths, `$skill`
  tokens, and verb-triggered backticked skill names.
- Clarified harness subagent policy with the named preauthorized roles:
  `explorer`, `check_runner`, `planning_critic`, `implementer`,
  `quality_guard`, `final_reviewer`, and `runtime_evidence`.
- Final verification before commit passed:
  `uv run pytest tests/test_validate_harness.py`,
  `uv run python scripts/validate_harness.py`, `git diff --check`, and
  `just quality`.

## Active Queue Status

Active work remains owned by `docs-ai/current-work/delivery-map.md`.

## Follow-On Audit - Skill Routing Policy Shift

Reviewed durable docs after the policy change that skill bodies should describe
their own capability/workflow rather than acting as routing indexes.

Disposition:

- Ordinary skill entrypoints no longer contain `Related Skills`, `Owner Map`,
  `Owner Routing`, or `Cross-Skill Routing` sections.
- Remaining owner maps live in reference docs or the dedicated `work-routing`
  skill, where the map is the artifact's direct purpose.
- Added lightweight skill-eval posture later folded into
  `harness-governance/references/skill-architecture.md`.
