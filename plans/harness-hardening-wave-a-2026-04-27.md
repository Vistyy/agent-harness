# Harness Hardening Wave A - 2026-04-27

Status: draft for planning-critic review

Linked durable follow-up state:
- `docs-ai/current-work/delivery-map.md`
- `docs-ai/current-work/backlog/harness-hardening__testing-strategy__owner-map.md`
- `docs-ai/current-work/backlog/harness-hardening__wording-compaction__bounded-trims.md`

## Scope And Execution Posture

In-scope work:
- `adapter-role-routes`
- `strict-frontmatter`
- `local-path-checks`
- `openai-metadata`
- `codex-install-smoke`

Out-of-scope work:
- wording compaction
- testing-strategy splitting
- broad `openai.yaml` regeneration
- project-overlay extraction or project-local docs

Non-obvious constraints:
- This is enforcement hardening, not skill prose rewriting.
- Do not add Python package dependencies for validation.
- Keep validation local and machine-checkable; do not build broad markdown or
  YAML implementations.

System-boundary trigger: not-triggered. This wave aligns checks and adapter
routes to existing owners; it does not change state authority, public contracts,
composition roots, storage/runtime boundaries, or product architecture.

Implementer delegation posture: parent-only.

Parent-only rationale: `shared-file-churn` and `tiny-local-followup`. A2/A3/A4
share `../scripts/validate_harness.py`, A5 wires the same gate into `justfile`, and
A1 is a small adapter route update.

Frozen decisions:
- `../scripts/validate_harness.py` remains the single harness validation entrypoint.
- New install smoke script path is `../scripts/codex_install_smoke.py`.
- `just quality` and `just quality-fast` must run both validator and install
  smoke.
- `fmt` remains validator-format only and does not run install smoke.
- Repo skill frontmatter accepts only top-level `name` and `description`.
- A4 semantic staleness review is human-audited; machine-checkable metadata
  fields are enforced by `../scripts/validate_harness.py`.

Planning exceptions: none.

## Task Plan

| Task slug | State | Dependencies | Outcome summary | Proof rows |
|---|---|---|---|---|
| `adapter-role-routes` |  | `none` | Codex role files point packet/task semantics at the packet contract and keep lifecycle routes separate. | `A1-P1` |
| `strict-frontmatter` |  | `none` | Repo skill frontmatter validation rejects prior YAML-breaking and unsupported shapes. | `A2-P1` |
| `local-path-checks` |  | `strict-frontmatter` | Validator catches missing machine-checkable local skill resource paths. | `A3-P1` |
| `openai-metadata` |  | `strict-frontmatter` | Validator enforces OpenAI metadata shape and exact `$skill` prompt invocation; human audit records semantic disposition. | `A4-P1`, `A4-P2` |
| `codex-install-smoke` |  | `none` | Install smoke proves temp `CODEX_HOME` symlinks/config and is wired into `quality` and `quality-fast`. | `A5-P1` |

### `adapter-role-routes`

- Outcome:
  - Adapter roles use current owner routes for packet/task-card schema and no
    stale project-owner or pre-split owner paths survive.
- In scope:
  - review and targeted edits to `adapters/codex/agents/*.toml`
- Out of scope:
  - changing role purpose, model selection, or role behavior beyond owner-route
    references
- Owned files and surfaces:
  - `adapters/codex/agents/check-runner.toml`
  - `adapters/codex/agents/explorer.toml`
  - `adapters/codex/agents/final-reviewer.toml`
  - `adapters/codex/agents/implementer.toml`
  - `adapters/codex/agents/planning-critic.toml`
  - `adapters/codex/agents/quality-guard.toml`
  - `adapters/codex/agents/runtime-evidence.toml`
- Locked invariants:
  - Use `wave-packet-contract.md` for packet/task-card schema.
  - Keep `initiatives-workflow.md` only for lifecycle/state maintenance.
  - Preserve role-specific boundaries and report shapes.
- Allowed local implementer decisions:
  - line wrapping and minimal phrasing needed to keep TOML readable
- Stop-and-handback triggers:
  - a route correction would require changing role responsibilities
  - stale routes appear outside adapter role files
- Proof rows:
  - `A1-P1`
- Deferred follow-up:
  - none

### `strict-frontmatter`

- Outcome:
  - Repo skills fail local validation for frontmatter shapes that Codex would
    skip or that owner docs do not bless.
- In scope:
  - `../scripts/validate_harness.py`
  - validator self-test fixtures
- Out of scope:
  - adding PyYAML or another dependency
  - accepting optional top-level frontmatter keys in repo skills
  - validating system skills outside this repo
- Owned files and surfaces:
  - `../scripts/validate_harness.py`
- Locked invariants:
  - frontmatter must start at byte zero with `---`
  - frontmatter must have a closing delimiter
  - only top-level keys `name` and `description` are accepted
  - `name` and `description` must be non-empty strings
  - `name` must be hyphen-case, <= 64 chars, and match the skill directory
  - `description` must be <= 1024 chars and contain no angle brackets
  - unquoted colon-space scalar mistakes in `description` are rejected
- Allowed local implementer decisions:
  - helper names and exact error wording
  - fixture folder names
- Stop-and-handback triggers:
  - an existing repo skill requires optional frontmatter keys
  - a valid current skill needs YAML structures beyond the locked invariants
- Proof rows:
  - `A2-P1`
- Deferred follow-up:
  - none

### `local-path-checks`

- Outcome:
  - Machine-checkable local references in skills cannot point at missing files.
- In scope:
  - `../scripts/validate_harness.py`
  - inline backticked paths beginning with `references/`, `assets/`,
    `scripts/`, or parent-directory relative prefixes
  - existing markdown-link validation
- Out of scope:
  - broad prose path mentions
  - external URLs and pure anchors
  - project-specific path validation beyond existing forbidden-term/path checks
- Owned files and surfaces:
  - `../scripts/validate_harness.py`
- Locked invariants:
  - path checks remain local and deterministic
  - source-citation exceptions remain supported
- Allowed local implementer decisions:
  - regex/helper shape
  - exact self-test fixture names
- Stop-and-handback triggers:
  - machine-checkable scope expands into fuzzy prose parsing
  - existing docs intentionally contain missing local references
- Proof rows:
  - `A3-P1`
- Deferred follow-up:
  - none

### `openai-metadata`

- Outcome:
  - `skills/*/agents/openai.yaml` files are machine-valid and semantically
    reviewed against current skill triggers without broad regeneration.
- In scope:
  - `../scripts/validate_harness.py`
  - `skills/*/agents/openai.yaml`
  - targeted metadata edits only when stale, invalid, or misleading
- Out of scope:
  - icon/brand metadata additions
  - regenerating all metadata files
  - changing skill trigger descriptions
- Owned files and surfaces:
  - `../scripts/validate_harness.py`
  - every `skills/*/agents/openai.yaml`
- Locked invariants:
  - required `interface.display_name`, `interface.short_description`, and
    `interface.default_prompt`
  - interface strings only
  - `short_description` length 25-64 characters
  - `default_prompt` must mention exact `$skill-name`
  - supported top-level keys: `interface`, `dependencies`, `policy`
  - supported `interface` keys are the `skill-creator` documented keys
  - human semantic audit must record disposition for every metadata file
- Allowed local implementer decisions:
  - exact wording for targeted metadata fixes
  - metadata report column order if it includes skill, path, display name,
    short description, default prompt, and disposition
- Stop-and-handback triggers:
  - more than five metadata files need semantic edits
  - semantic drift requires changing `SKILL.md` trigger descriptions
  - unsupported dependency/policy shapes appear and need deeper schema design
- Proof rows:
  - `A4-P1`
  - `A4-P2`
- Deferred follow-up:
  - none

### `codex-install-smoke`

- Outcome:
  - Codex install behavior is proven against temp `CODEX_HOME` and protected by
    both fast and full quality gates.
- In scope:
  - `../scripts/codex_install_smoke.py`
  - `justfile`
- Out of scope:
  - changing `adapters/codex/install.sh` unless smoke exposes a real install bug
  - touching the user's live Codex home
  - changing adapter config semantics
- Owned files and surfaces:
  - `../scripts/codex_install_smoke.py`
  - `justfile`
- Locked invariants:
  - smoke runs installer with temp `CODEX_HOME` and `--apply`
  - smoke asserts `$CODEX_HOME/AGENTS.md` symlink
  - smoke asserts `$CODEX_HOME/skills/webapp-testing` symlink
  - smoke asserts `$CODEX_HOME/agents/runtime-evidence.toml` symlink
  - smoke asserts `[features] multi_agent = true`
  - smoke asserts every agent block from `adapters/codex/config.toml` appears
  - smoke asserts repo root does not acquire a `.codex` regular file stub
  - smoke is idempotent by running install twice in the same temp home
  - temp files are cleaned up by default
- Allowed local implementer decisions:
  - Python helper names and assertion formatting
  - whether `just quality` calls the smoke directly or through `quality-fast`
- Stop-and-handback triggers:
  - smoke requires writing outside temp `CODEX_HOME`
  - idempotency requires replacing non-temp live targets
  - installer behavior is ambiguous enough to require user policy
- Proof rows:
  - `A5-P1`
- Deferred follow-up:
  - none

## Proof Plan

```json
{
  "proof_plan": [
    {
      "proof_id": "A1-P1",
      "task_slug": "adapter-role-routes",
      "anchor_ids": ["AA1"],
      "claim": "Codex role files route packet/task schema to the packet owner and lifecycle to the lifecycle owner.",
      "material_variants": ["all adapters/codex/agents/*.toml"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "static-check",
      "exact_proof": [
        "rg -n \"initiatives-workflow\\\\.md for packet|packet/task semantics|docs-ai/docs/conventions\" adapters/codex/agents",
        "rg -n \"wave-packet-contract|initiatives-workflow\\\\.md\" adapters/codex/agents"
      ],
      "expected_evidence": [
        "first scan returns no stale-route hits",
        "second scan shows intentional owner split"
      ],
      "counterfactual_regression_probe": {
        "weaker_implementation": "A role still sends agents to initiatives-workflow.md for packet/task semantics.",
        "failing_assertion_or_artifact": "The stale-route rg scan prints that role line."
      },
      "status": "planned"
    },
    {
      "proof_id": "A2-P1",
      "task_slug": "strict-frontmatter",
      "anchor_ids": ["AA2"],
      "claim": "Repo skill frontmatter rejects prior YAML-breaking shapes and required-field/type/key mistakes.",
      "material_variants": ["invalid colon", "missing keys", "non-string values", "unexpected keys", "bad delimiters", "dir/name mismatch"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "static-check",
      "exact_proof": [
        "uv run python scripts/validate_harness.py --self-test",
        "uv run python scripts/validate_harness.py"
      ],
      "expected_evidence": ["both commands pass"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Unquoted colon-space description or extra frontmatter key still passes.",
        "failing_assertion_or_artifact": "Self-test reports missing rejection marker."
      },
      "status": "planned"
    },
    {
      "proof_id": "A3-P1",
      "task_slug": "local-path-checks",
      "anchor_ids": ["AA3"],
      "claim": "Machine-checkable local skill resource references cannot point to missing files.",
      "material_variants": ["markdown links", "backticked resource paths", "relative owner-doc paths"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "static-check",
      "exact_proof": [
        "uv run python scripts/validate_harness.py --self-test",
        "uv run python scripts/validate_harness.py"
      ],
      "expected_evidence": ["both commands pass"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Backticked ../verification-before-completion/references/missing.md passes.",
        "failing_assertion_or_artifact": "Self-test reports missing broken-reference rejection."
      },
      "status": "planned"
    },
    {
      "proof_id": "A4-P1",
      "task_slug": "openai-metadata",
      "anchor_ids": ["AA4"],
      "claim": "OpenAI metadata has required interface fields, valid lengths, supported keys, and exact $skill-name prompt invocation.",
      "material_variants": ["every skills/*/agents/openai.yaml"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "static-check",
      "exact_proof": [
        "uv run python scripts/validate_harness.py --self-test",
        "uv run python scripts/validate_harness.py",
        "uv run python scripts/validate_harness.py --openai-metadata-report .tmp/harness-openai-metadata.tsv"
      ],
      "expected_evidence": [
        "validator passes",
        ".tmp/harness-openai-metadata.tsv exists with one row per skill metadata file"
      ],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Wrong $skill name or invalid short_description length passes.",
        "failing_assertion_or_artifact": "Self-test reports missing metadata rejection marker."
      },
      "status": "planned"
    },
    {
      "proof_id": "A4-P2",
      "task_slug": "openai-metadata",
      "anchor_ids": ["AA4"],
      "claim": "Targeted human review finds no misleading metadata, or edits only justified stale metadata.",
      "material_variants": ["every skills/*/agents/openai.yaml against its SKILL.md trigger and body"],
      "proof_classification": "not-reliably-provable-with-current-harness",
      "owner_layer": "doc-only",
      "exact_proof": [
        "review .tmp/harness-openai-metadata.tsv against each corresponding SKILL.md",
        "closeout table columns: skill | metadata_path | disposition | changed file | reason",
        "closeout table must include exactly one disposition row for every .tmp/harness-openai-metadata.tsv data row, including no-change cases"
      ],
      "expected_evidence": [
        "closeout includes one disposition row per metadata file and changed-file reasons for any edits"
      ],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Syntactically valid but stale UI metadata remains unreviewed.",
        "failing_assertion_or_artifact": "Closeout lacks a disposition for that skill."
      },
      "status": "planned"
    },
    {
      "proof_id": "A5-P1",
      "task_slug": "codex-install-smoke",
      "anchor_ids": ["AA5"],
      "claim": "Codex installer creates expected temp-home symlinks and agent config without writing a repo-local .codex regular file stub, and both quality gates run the smoke.",
      "material_variants": ["temp CODEX_HOME", "--apply", "second idempotency run", "quality", "quality-fast"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "integration",
      "exact_proof": [
        "uv run python scripts/codex_install_smoke.py",
        "just quality-fast",
        "just quality"
      ],
      "expected_evidence": ["all commands pass"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Installer misses agent config block, symlink, idempotency, or quality-fast wiring.",
        "failing_assertion_or_artifact": "Smoke or quality-fast exits nonzero."
      },
      "status": "planned"
    }
  ]
}
```

## Execution State

### Decisions And Blockers

| Type | Item | Action | Owner |
|---|---|---|---|
| decision | Optional repo skill frontmatter keys | Reject all keys except `name` and `description` for this repo. | agent |
| decision | A4 semantic staleness proof | Use exact TSV inventory plus closeout disposition table; do not claim machine proof for semantic quality. | agent |
| blocker | none | none | none |

### Technical Debt And Deferred Follow-Up

- `harness-hardening__testing-strategy__owner-map`
- `harness-hardening__wording-compaction__bounded-trims`

## Acceptance Anchors

- `AA1`: Adapter role route owners are current and unambiguous.
- `AA2`: Skill frontmatter validation catches the prior Codex parsing failure
  class before install/runtime loading.
- `AA3`: Skill local reference checks catch missing machine-checkable resource
  paths.
- `AA4`: OpenAI UI metadata is machine-valid and semantically reviewed without
  broad churn.
- `AA5`: Codex adapter install behavior is protected by repeatable temp-home
  smoke and quality gates.

## Completion Bar

Wave A is complete only when:
- planning-critic approves this scope or all material findings are addressed,
- implementation passes `just quality-fast` and `just quality`,
- the OpenAI metadata audit disposition is included in closeout,
- a final isolated review approves the changed slice,
- deferred Wave B/wording work remains in workflow-owned backlog state.
