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
    write(
        root / "agents" / "roles.md",
        f"""
        # Agent Roles

        `AGENTS.md` is the standing user authorization to use these roles in a
        fresh conversation. Agents must not wait for the user to mention
        subagents again when `subagent-handoff` says to delegate.

        {role_lines}
        """,
    )
    config_blocks = ["[features]", "multi_agent = true", ""]
    for role in roles:
        config_blocks.extend(
            [
                f"[agents.{role}]",
                f'description = "Test {role} role. Standing AGENTS.md authorization applies; do not ask the user again."',
                f'config_file = "agents/{role.replace("_", "-")}.toml"',
                "",
            ]
        )
        codex_body = f'name = "{role}"\n'
        write(
            root / "adapters" / "codex" / "agents" / f"{role.replace('_', '-')}.toml",
            codex_body,
        )
    write(root / "adapters" / "codex" / "config.toml", "\n".join(config_blocks))


def valid_context_note() -> str:
    return """
    # Active Work Note example

    ## Objective

    - original objective: `Example objective.`
    - accepted reductions: `none`
    - residual gaps: `none`
    - checkpoint: `current`

    ## Current Reality

    - repo/product state: `example`

    ## Objective Coverage

    - entrypoint/actor: `covered`
    - production trigger path: `covered`
    - state authority: `covered`
    - runtime/lifecycle owner: `covered`
    - cleanup/legacy removal: `covered`

    ## Target Shape

    - final shape: `example`

    ## Evidence And Review

    - evidence strategy: `uv run python scripts/validate_harness.py`
    - planning review: `not needed`
    - final repo-health review: `pending`
    """


def add_review_lenses_contract(root: Path) -> None:
    add_skill(root, "solution-shaping")
    write(
        root / "skills" / "solution-shaping" / "SKILL.md",
        """
        ---
        name: solution-shaping
        description: Test objective coverage skill.
        ---

        # Delivery Workflow

        solution correctness

        Read `references/review-lenses.md` before proof, review, runtime
        evidence, handoff, or completion when review-lens concerns may affect
        the claim.
        """,
    )
    write(
        root / "skills" / "solution-shaping" / "references" / "review-lenses.md",
        """
        # Review Lenses

        The material-risk lenses include security/privacy, data integrity,
        reliability, operability, observability/diagnosability,
        performance/cost, compatibility, and accessibility.

        The engineering-quality lenses include simplicity, cohesion/ownership,
        testability/provability, evolvability, maintainability/readability,
        migration/cleanup, slice integrity, and dependency/tooling fit.

        Disposition labels are `not-applicable`, `covered`, `blocked`,
        `separate debt`, and `accepted temporary debt`.

        Planning does not mark future proof as `covered`.

        Narrowed claims map to `blocked`.

        Compatibility is strict: a compatibility path is blocked unless the
        user explicitly approves the specific protected surface, owner, risk,
        and removal condition.

        Legal/licensing/compliance stays out of default scope.

        Splitting becomes valid only if the reference grows beyond compact
        review-lens disposition.
        """,
    )


def minimal_valid_root(root: Path) -> None:
    add_skill(root, "test-skill")
    add_review_lenses_contract(root)
    write(
        root / "skills" / "verify-work" / "SKILL.md",
        """
        ---
        name: verify-work
        description: Test runtime proof skill.
        ---

        # Runtime Proof

        Runtime proof validates the binding objective, rejects mis-scoped
        handoffs, reports entrypoint fidelity, and returns reject or blocked
        when proof does not cover the runtime-visible claim.

        Runtime evidence is live-use validation. It uses the app, service, API,
        or operator path through a faithful entrypoint and verifies behavior
        beyond code inspection, tests, and review approval. The tiny, local
        exemption applies only when there is no public-behavior or
        cross-boundary runtime risk.
        """,
    )
    write(
        root / "skills" / "verify-work" / "agents" / "openai.yaml",
        """
        interface:
          display_name: "Runtime Proof"
          short_description: "Valid runtime proof metadata"
          default_prompt: "Use $verify-work for runtime proof."
        """,
    )
    add_roles(root)
    write(root / "README.md", "# Test\n")


def add_repo_codex_live_install(root: Path) -> None:
    write(
        root / "AGENTS.md",
        """
        # Test Agents

        Treat project-local `AGENTS.md` as a compact first-hop map.

        ## Routing

        - Test work: `test-skill`.
        - Runtime proof: `verify-work`.

        ## Subagent Policy

        The user explicitly authorizes use of the spawn/subagent tool for these
        overlay-defined roles when this `AGENTS.md` is in force:
        `explorer` and `quality_guard`.

        This preauthorization applies only to those named roles.
        """,
    )
    codex_home = root / ".codex"
    (codex_home / "skills").mkdir(parents=True)
    (codex_home / "agents").mkdir(parents=True)
    (codex_home / "AGENTS.md").symlink_to(root / "AGENTS.md")
    for skill_dir in sorted((root / "skills").iterdir()):
        if skill_dir.is_dir():
            (codex_home / "skills" / skill_dir.name).symlink_to(skill_dir)
    for agent_file in sorted((root / "adapters" / "codex" / "agents").glob("*.toml")):
        (codex_home / "agents" / agent_file.name).symlink_to(agent_file)
    write(
        codex_home / "config.toml",
        (root / "adapters" / "codex" / "config.toml").read_text(encoding="utf-8"),
    )


def test_validate_accepts_minimal_valid_root(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)

    assert validate_harness.validate(tmp_path) == []


def test_validate_accepts_repo_codex_live_install(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_repo_codex_live_install(tmp_path)

    assert validate_harness.validate(tmp_path) == []


def test_validate_rejects_drifted_repo_codex_live_install(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_repo_codex_live_install(tmp_path)
    (tmp_path / ".codex" / "skills" / "extra-skill").symlink_to(
        tmp_path / "skills" / "extra-skill"
    )
    quality_guard = tmp_path / ".codex" / "agents" / "quality-guard.toml"
    quality_guard.unlink()
    write(quality_guard, 'name = "quality_guard"\n')
    config_path = tmp_path / ".codex" / "config.toml"
    config_path.write_text(
        config_path.read_text(encoding="utf-8").replace(
            'description = "Test quality_guard role. Standing AGENTS.md authorization applies; do not ask the user again."',
            'description = "Stale quality guard role. Standing AGENTS.md authorization applies; do not ask the user again."',
        )
        + '\n[agents.extra_agent]\ndescription = "Extra agent"\nconfig_file = "agents/extra-agent.toml"\n',
        encoding="utf-8",
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        ".codex/agents/quality-guard.toml is not a symlink to "
        "adapters/codex/agents/quality-guard.toml"
    ) in errors
    assert any(".codex/skills/extra-skill is an unplanned overlay symlink" in error for error in errors)
    assert ".codex/config.toml missing or changed agents.quality_guard block" in errors
    assert ".codex/config.toml contains unknown agents.extra_agent block" in errors


def test_validate_accepts_valid_backlog_detail(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "backlog" / "harness__example__item.md",
        """
        # Backlog Entry: harness/example/item

        ## Metadata

        - Status: `open`
        - Owner: `README.md`
        - Bucket: `discovered separate debt`
        - Location: `README.md`

        ## Problem

        Example problem.

        ## Next Action

        Define one narrow slice.
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

        - Status: `open`

        ## Problem

        Example problem.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/backlog/harness__example__item.md missing backlog field 'bucket'" in errors
    assert "docs-ai/current-work/backlog/harness__example__item.md missing backlog heading ## Next Action" in errors


def test_validate_rejects_invalid_backlog_bucket(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "backlog" / "harness__example__item.md",
        """
        # Backlog Entry: harness/example/item

        ## Metadata

        - Status: `open`
        - Owner: `README.md`
        - Bucket: `later`
        - Location: `README.md`

        ## Problem

        Example problem.

        ## Next Action

        Define one narrow slice.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/backlog/harness__example__item.md has invalid backlog bucket 'later'" in errors


def test_validate_rejects_accepted_temporary_debt_without_acceptance(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "backlog" / "harness__example__item.md",
        """
        # Backlog Entry: harness/example/item

        ## Metadata

        - Status: `open`
        - Owner: `README.md`
        - Bucket: `accepted temporary debt`
        - Removal condition: `none`
        - User acceptance: `none`
        - Location: `README.md`

        ## Problem

        Example problem.

        ## Next Action

        Define one narrow slice.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/backlog/harness__example__item.md accepted temporary debt missing user acceptance" in errors
    assert "docs-ai/current-work/backlog/harness__example__item.md accepted temporary debt missing removal condition" in errors


def test_validate_rejects_accepted_temporary_debt_placeholders(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "backlog" / "harness__example__item.md",
        """
        # Backlog Entry: harness/example/item

        ## Metadata

        - Status: `open`
        - Owner: `README.md`
        - Bucket: `accepted temporary debt`
        - Removal condition: `<condition | none>`
        - User acceptance: `<required for accepted temporary debt | none>`
        - Location: `README.md`

        ## Problem

        Example problem.

        ## Next Action

        Define one narrow slice.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/backlog/harness__example__item.md accepted temporary debt missing user acceptance" in errors
    assert "docs-ai/current-work/backlog/harness__example__item.md accepted temporary debt missing removal condition" in errors


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


def test_validate_rejects_agents_route_map_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "AGENTS.md",
        """
        Treat project-local `AGENTS.md` as a compact first-hop map.

        ## Routing

        - Missing route: `missing-skill`.
        - Runtime proof policy: `verify-work`.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "AGENTS.md routes to missing skill 'missing-skill'" in errors


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
