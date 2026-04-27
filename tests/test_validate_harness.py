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
            f'name = "{role}"\n',
        )
        write(
            root / "adapters" / "github-copilot" / "agents" / f"{role}.agent.md",
            f"---\nname: {role}\n---\n",
        )
    write(root / "adapters" / "codex" / "config.toml", "\n".join(config_blocks))


def valid_packet() -> str:
    return """
    # Wave example Execution Packet

    ## Scope And Execution Posture

    ## Task Plan

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


def test_validate_requires_openai_metadata_for_every_skill(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_skill(tmp_path, "missing-metadata", metadata=False)

    errors = validate_harness.validate(tmp_path)

    assert "skills/missing-metadata missing agents/openai.yaml" in errors


def test_validate_rejects_role_parity_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    (tmp_path / "adapters" / "codex" / "agents" / "quality-guard.toml").unlink()

    errors = validate_harness.validate(tmp_path)

    assert "missing Codex agent file adapters/codex/agents/quality-guard.toml" in errors


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
