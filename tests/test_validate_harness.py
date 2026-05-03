from __future__ import annotations

import textwrap
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts import validate_harness


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).lstrip(), encoding="utf-8")


def add_skill(root: Path, name: str, metadata: bool = True) -> None:
    write(
        root / "skills" / name / "SKILL.md",
        f"""
        ---
        name: {name}
        description: Test skill for {name}.
        ---

        # {name}
        """,
    )
    if metadata:
        write(
            root / "skills" / name / "agents" / "openai.yaml",
            f"""
            interface:
              display_name: "{name.title()}"
              short_description: "Valid metadata helper text"
              default_prompt: "Use ${name} to do test work."
            """,
        )


def add_roles(root: Path, roles: tuple[str, ...] = ("explorer", "quality_guard")) -> None:
    role_lines = "\n".join(f"- `{role}`: test role." for role in roles)
    write(root / "agents" / "roles.md", f"# Agent Roles\n\n{role_lines}\n")
    config_blocks = ["[features]", "multi_agent = true", ""]
    for role in roles:
        config_blocks.extend(
            [
                f"[agents.{role}]",
                f'config_file = "agents/{role.replace("_", "-")}.toml"',
                "",
            ]
        )
        write(
            root / "adapters" / "codex" / "agents" / f"{role.replace('_', '-')}.toml",
            f'name = "{role}"\n# touched-component integrity gate\n',
        )
        write(
            root / "adapters" / "github-copilot" / "agents" / f"{role}.agent.md",
            f"---\nname: {role}\n---\n\nTouched-component integrity gate.\n",
        )
    write(root / "adapters" / "codex" / "config.toml", "\n".join(config_blocks))


def valid_packet() -> str:
    return """
    # Wave example Execution Packet

    ## Scope And Execution Posture

    ## Task Plan

    | Task slug | State | Dependencies | Outcome summary | Proof rows |
    | --- | --- | --- | --- | --- |
    | `example/task` |  | `none` | `Example outcome.` | `P1` |

    ### `example/task`

    - Outcome:
      - `Example outcome.`
    - In scope:
      - `Example scope.`
    - Out of scope:
      - `none`
    - Owned files and surfaces:
      - `example.md`
    - Touched owner/component integrity:
      - `acceptable`
    - Locked invariants:
      - `none`
    - Allowed local implementer decisions:
      - `parent-only`
    - Stop-and-handback triggers:
      - `parent-only`
    - Proof rows:
      - `P1`
    - Deferred follow-up:
      - `none`

    ## Proof Plan

    ```json
    {
      "proof_plan": [
        {
          "proof_id": "P1",
          "task_slug": "example/task",
          "anchor_ids": ["A1"],
          "claim": "Example claim.",
          "material_variants": ["none"],
          "proof_classification": "automated-suite-provable",
          "owner_layer": "static-check",
          "exact_proof": ["uv run python scripts/validate_harness.py"],
          "expected_evidence": ["harness validation passed"],
          "counterfactual_regression_probe": {
            "weaker_implementation": "Missing validation.",
            "failing_assertion_or_artifact": "validate_harness fails"
          },
          "status": "planned"
        }
      ]
    }
    ```

    ## Execution State
    """


def minimal_valid_root(root: Path) -> None:
    add_skill(root, "test-skill")
    add_roles(root)
    write(root / "README.md", "# Test\n")


def test_validate_accepts_minimal_valid_root(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)

    assert validate_harness.validate(tmp_path) == []


def test_validate_accepts_valid_backlog_detail(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "backlog" / "harness__example__item.md",
        """
        # Backlog Entry: harness/example/item

        ## Metadata

        - Impact: `medium`
        - Effort: `M`
        - Queue bucket: `Deferred Backlog`

        ## Problem

        Example problem.

        ## Why This Bucket

        Example bucket reason.

        ## Suggested Next Step

        - Suggested target wave (if known): none
        - Dependencies/prerequisites: none
        - Smallest next slice: define one narrow slice.
        - Promotion/removal condition: promote or delete when no longer valid.

        ## References

        - Owning durable doc: `README.md`
        - Queue/backlog source: `docs-ai/current-work/delivery-map.md`
        - Source wave/task: none
        - Files/evidence: `README.md`
        """,
    )

    assert validate_harness.validate(tmp_path) == []


def test_validate_rejects_incomplete_backlog_detail(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "backlog" / "harness__example__item.md",
        """
        # Backlog Entry: harness/example/item

        ## Metadata

        - Impact: `medium`

        ## Problem

        Example problem.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/backlog/harness__example__item.md missing backlog field 'queue bucket'" in errors
    assert "docs-ai/current-work/backlog/harness__example__item.md missing backlog heading ## References" in errors


def test_validate_requires_openai_metadata_for_every_skill(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_skill(tmp_path, "missing-metadata", metadata=False)

    errors = validate_harness.validate(tmp_path)

    assert "skills/missing-metadata missing agents/openai.yaml" in errors


def test_validate_rejects_missing_skill_token_reference(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "AGENTS.md", "Use $missing-skill for missing work.\n")

    errors = validate_harness.validate(tmp_path)

    assert "AGENTS.md:1 references missing skill $missing-skill" in errors


def test_validate_rejects_missing_single_token_skill_reference(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "AGENTS.md", "Use $missing for missing work.\n")

    errors = validate_harness.validate(tmp_path)

    assert "AGENTS.md:1 references missing skill $missing" in errors


def test_validate_rejects_missing_backticked_skill_reference(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "AGENTS.md", "Missing work: use `missing-skill`.\n")

    errors = validate_harness.validate(tmp_path)

    assert "AGENTS.md:1 references missing skill `missing-skill`" in errors


def test_validate_rejects_missing_skill_path_reference(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "README.md", "See ../../skills/missing-skill/SKILL.md.\n")

    errors = validate_harness.validate(tmp_path)

    assert "README.md:1 references missing skill path ../../skills/missing-skill/SKILL.md" in errors


def test_validate_rejects_skill_body_trigger_text(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "test-skill" / "SKILL.md",
        """
        ---
        name: test-skill
        description: Test skill trigger belongs here.
        ---

        # Test Skill

        ## Use When

        - bad body trigger
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/test-skill/SKILL.md contains body-level trigger heading; ordinary trigger text belongs in frontmatter description"
        in errors
    )


def test_validate_rejects_optional_reference_wording(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "test-skill" / "SKILL.md",
        """
        ---
        name: test-skill
        description: Test skill trigger belongs here.
        ---

        # Test Skill

        ## Optional Reference
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "skills/test-skill/SKILL.md contains Optional Reference wording; references are mandatory purpose gates" in errors


def test_validate_rejects_non_gated_reference_row_in_staged_skill(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_skill(tmp_path, "code-review")
    write(tmp_path / "skills" / "code-review" / "references" / "review-governance.md", "# Review Governance\n")
    write(
        tmp_path / "skills" / "code-review" / "SKILL.md",
        """
        ---
        name: code-review
        description: Use when reviewing code.
        ---

        # Code Review

        - Shared review doctrine: `references/review-governance.md`
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/code-review/SKILL.md:8 has non-gated reference row in staged reference-gate skill; "
        "use `Read <reference> when/before/for ...`"
    ) in errors


def test_validate_rejects_removed_harness_path_outside_archive(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "README.md", "See skills/adversarial-review/SKILL.md.\n")

    errors = validate_harness.validate(tmp_path)

    assert "README.md references removed harness path skills/adversarial-review/SKILL.md" in errors


def test_validate_allows_removed_harness_path_in_closed_archive(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "closed-harness-audits-2026-04.md",
        "Archived deletion: skills/adversarial-review/SKILL.md.\n",
    )

    assert validate_harness.validate(tmp_path) == []


def test_validate_rejects_removed_harness_path_in_other_tests(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "tests" / "test_stale_path.md", "See skills/adversarial-review/SKILL.md.\n")

    errors = validate_harness.validate(tmp_path)

    assert "tests/test_stale_path.md references removed harness path skills/adversarial-review/SKILL.md" in errors


def test_validate_rejects_missing_relative_skill_path_reference(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "skills" / "test-skill" / "references" / "owner.md", "See ../missing-skill/SKILL.md.\n")

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/test-skill/references/owner.md:1 references missing skill path ../missing-skill/SKILL.md"
        in errors
    )


def test_validate_rejects_role_parity_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    (tmp_path / "adapters" / "codex" / "agents" / "quality-guard.toml").unlink()

    errors = validate_harness.validate(tmp_path)

    assert "missing Codex agent file adapters/codex/agents/quality-guard.toml" in errors


def test_validate_rejects_preauthorized_subagent_allowlist_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "AGENTS.md",
        """
        ## Subagent Policy

        - The user explicitly authorizes use of the spawn/subagent tool for these
          harness-defined roles when this `AGENTS.md` is in force:
          `explorer`.
        - This preauthorization applies only to those named roles and only when the
          workflow calls for them.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "AGENTS.md preauthorized subagents ['explorer'] do not match agents/roles.md roles "
        "['explorer', 'quality_guard']"
    ) in errors


def test_validate_rejects_topology_role_table_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "subagent-orchestration" / "references" / "coding-agent-topology.md",
        """
        # Coding Agent Topology

        | Role | Mission |
        | --- | --- |
        | `explorer` | discovery |
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/subagent-orchestration/references/coding-agent-topology.md role table ['explorer'] "
        "does not match agents/roles.md roles ['explorer', 'quality_guard']"
    ) in errors


def test_validate_rejects_binding_simplicity_lens_language(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "AGENTS.md", "Simplicity lens: use `code-simplicity`.\n")

    errors = validate_harness.validate(tmp_path)

    assert "AGENTS.md must call code-simplicity a gate, not a lens" in errors


def test_validate_rejects_agent_missing_touched_component_gate(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "quality-guard.toml",
        'name = "quality_guard"\n',
    )

    errors = validate_harness.validate(tmp_path)

    assert "adapters/codex/agents/quality-guard.toml missing touched-component integrity gate" in errors


def test_validate_rejects_incomplete_touched_owner_definition(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "skills" / "planning-intake" / "SKILL.md", "Touched owner uses contract, state, lifecycle, or proof.\n")

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/planning-intake/SKILL.md has incomplete touched-owner definition; include design and workflow"
        in errors
    )


def test_validate_rejects_runtime_evidence_project_doc_leakage(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "runtime-evidence.toml",
        'name = "runtime_evidence"\nSee docs-ai/docs/project.md.\n',
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/agents/runtime-evidence.toml must not hard-code project-local docs-ai/docs/ paths"
        in errors
    )


def test_validate_requires_microsoft_playwright_cli_anchor(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "webapp-testing" / "references" / "browser-runtime-proof-workflow.md",
        "Use a browser CLI.\n",
    )
    write(
        tmp_path / "skills" / "webapp-testing" / "references" / "browser-proof-layering-contract.md",
        "One-shot browser proof.\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/webapp-testing browser proof docs must identify Microsoft playwright-cli "
        "(`microsoft/playwright-cli`, `@playwright/cli`) as the one-shot channel"
    ) in errors


def test_validate_rejects_stale_runtime_optional_helper_wording(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "subagent-orchestration" / "SKILL.md",
        """
        Delegate isolated runtime proof only when startup/teardown is
        deterministic and ownership is unambiguous.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/subagent-orchestration/SKILL.md contains stale optional-helper runtime proof wording"
        in errors
    )


def test_validate_rejects_packet_missing_required_section_and_proof_field(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "bad-wave" / "wave-execution.md",
        """
        # Wave bad-wave Execution Packet

        ## Scope And Execution Posture

        ## Task Plan

        ## Proof Plan

        ```json
        {"proof_plan": [{"proof_id": "P1"}]}
        ```
        """,
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "bad-wave.md",
        "# Wave bad-wave\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/bad-wave/wave-execution.md missing section 'Execution State'" in errors
    assert "docs-ai/current-work/bad-wave/wave-execution.md proof_plan row 1 missing task_slug" in errors


def test_validate_rejects_wave_task_card_missing_touched_integrity(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "bad-wave" / "wave-execution.md",
        """
        # Wave bad-wave Execution Packet

        ## Scope And Execution Posture

        ## Task Plan

        ### `example/task`

        - Outcome:
          - `Example outcome.`
        - In scope:
          - `Example scope.`
        - Out of scope:
          - `none`
        - Owned files and surfaces:
          - `example.md`
        - Locked invariants:
          - `none`
        - Allowed local implementer decisions:
          - `parent-only`
        - Stop-and-handback triggers:
          - `parent-only`
        - Proof rows:
          - `P1`
        - Deferred follow-up:
          - `none`

        ## Proof Plan

        ```json
        {
          "proof_plan": [
            {
              "proof_id": "P1",
              "task_slug": "example/task",
              "anchor_ids": ["A1"],
              "claim": "Example claim.",
              "material_variants": ["none"],
              "proof_classification": "automated-suite-provable",
              "owner_layer": "static-check",
              "exact_proof": ["uv run python scripts/validate_harness.py"],
              "expected_evidence": ["harness validation passed"],
              "counterfactual_regression_probe": {
                "weaker_implementation": "Missing validation.",
                "failing_assertion_or_artifact": "validate_harness fails"
              },
              "status": "planned"
            }
          ]
        }
        ```

        ## Execution State
        """,
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "bad-wave.md",
        "# Wave bad-wave\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "docs-ai/current-work/bad-wave/wave-execution.md task card '`example/task`' missing touched owner/component integrity"
        in errors
    )


def test_validate_rejects_wave_packet_with_proof_rows_but_no_task_cards(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "bad-wave" / "wave-execution.md",
        """
        # Wave bad-wave Execution Packet

        ## Scope And Execution Posture

        ## Task Plan

        | Task slug | State | Dependencies | Outcome summary | Proof rows |
        | --- | --- | --- | --- | --- |
        | `example/task` |  | `none` | `Example outcome.` | `P1` |

        ## Proof Plan

        ```json
        {
          "proof_plan": [
            {
              "proof_id": "P1",
              "task_slug": "example/task",
              "anchor_ids": ["A1"],
              "claim": "Example claim.",
              "material_variants": ["none"],
              "proof_classification": "automated-suite-provable",
              "owner_layer": "static-check",
              "exact_proof": ["uv run python scripts/validate_harness.py"],
              "expected_evidence": ["harness validation passed"],
              "counterfactual_regression_probe": {
                "weaker_implementation": "Missing validation.",
                "failing_assertion_or_artifact": "validate_harness fails"
              },
              "status": "planned"
            }
          ]
        }
        ```

        ## Execution State
        """,
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "bad-wave.md",
        "# Wave bad-wave\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/bad-wave/wave-execution.md missing task cards" in errors
    assert (
        "docs-ai/current-work/bad-wave/wave-execution.md proof_plan row 1 task_slug 'example/task' has no matching task card"
        in errors
    )


def test_validate_enforces_wave_lifecycle_from_status_and_packet_existence(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "discovery.md",
        "# Wave discovery\n\n**Status:** discovery-required\n",
    )
    write(tmp_path / "docs-ai" / "current-work" / "discovery" / "wave-execution.md", valid_packet())
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "ready.md",
        "# Wave ready\n\n**Status:** execution-ready\n",
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "done.md",
        "# Wave done\n\n**Status:** done\n",
    )
    write(tmp_path / "docs-ai" / "current-work" / "done" / "wave-execution.draft.md", valid_packet())

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/docs/initiatives/waves/discovery.md is discovery-required but canonical packet exists" in errors
    assert "docs-ai/docs/initiatives/waves/ready.md is execution-ready but canonical packet is missing" in errors
    assert "docs-ai/docs/initiatives/waves/done.md is done but current-work packet exists" in errors
