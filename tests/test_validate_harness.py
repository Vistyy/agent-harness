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
        subagents again when `subagent-orchestration` says to delegate.

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
        if role == "quality_guard":
            codex_body = (
                f'name = "{role}"\n'
                "# design integrity gate\n"
                "# active `execution-ready` packet\n# binding objective\n# accepted reductions\n# readiness claim\n# artifacts\n# final approval\n"
                "# Do not claim final approval.\n"
                "# Diff-only approval is invalid\n"
                "# why inspected scope is sufficient\n"
            )
        elif role == "explorer":
            codex_body = (
                f'name = "{role}"\n'
                "# design integrity gate\n"
                "# Stay read-only\n# Do not edit code or take implementation ownership.\n"
            )
        else:
            codex_body = f'name = "{role}"\n# design integrity gate\n'
        write(
            root / "adapters" / "codex" / "agents" / f"{role.replace('_', '-')}.toml",
            codex_body,
        )
    write(root / "adapters" / "codex" / "config.toml", "\n".join(config_blocks))


def valid_packet() -> str:
    return """
    # Wave example Execution Packet

    ## Objective

    - original objective: `Example objective.`
    - accepted reductions: `none`
    - residual gaps: `none`
    - checkpoint: `current`

    ## Design Integrity

    - owner/interface: `example`
    - key decisions: `none`
    - verdict: `acceptable`
    - accepted temporary debt: `none`

    ## Execution

    ### `example/task`

    - State: `blank`
    - Owned surfaces: `example.md`
    - Checks/artifacts: `uv run python scripts/validate_harness.py`

    - blockers/decisions: `none`

    ## Readiness Claim

    - exact claim: `Example claim.`
    - claimed interface: `example interface`
    - required evidence: `uv run python scripts/validate_harness.py`
    - evidence status: `planned`
    - unproved boundaries: `none`
    - residual risks: `none`
    """


def minimal_valid_root(root: Path) -> None:
    add_skill(root, "test-skill")
    write(
        root / "skills" / "runtime-proof" / "SKILL.md",
        """
        ---
        name: runtime-proof
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
        root / "skills" / "runtime-proof" / "agents" / "openai.yaml",
        """
        interface:
          display_name: "Runtime Proof"
          short_description: "Valid runtime proof metadata"
          default_prompt: "Use $runtime-proof for runtime proof."
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
        - Runtime proof: `runtime-proof`.

        ## Subagent Policy

        The user explicitly authorizes use of the spawn/subagent tool for these
        harness-defined roles when this `AGENTS.md` is in force:
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


def test_validate_rejects_stale_repo_codex_live_install(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_repo_codex_live_install(tmp_path)
    (tmp_path / ".codex" / "skills" / "code-simplicity").symlink_to(
        tmp_path / "skills" / "code-simplicity"
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
        + '\n[agents.check_runner]\ndescription = "Removed check runner"\nconfig_file = "agents/check-runner.toml"\n',
        encoding="utf-8",
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        ".codex/agents/quality-guard.toml is not a symlink to "
        "adapters/codex/agents/quality-guard.toml"
    ) in errors
    assert any(".codex/skills/code-simplicity is a stale harness symlink" in error for error in errors)
    assert ".codex/config.toml missing or changed agents.quality_guard block" in errors
    assert ".codex/config.toml contains removed agents.check_runner block" in errors


def test_validate_accepts_valid_backlog_detail(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "backlog" / "harness__example__item.md",
        """
        # Backlog Entry: harness/example/item

        ## Metadata

        - Status: `open`
        - Owner: `README.md`
        - Created: `2026-05-09`
        - Bucket: `discovered separate debt`
        - Risk: `medium`
        - Removal condition: `fixed or no longer relevant`
        - User acceptance: `none`
        - Location: `README.md`
        - Recommended fix: define one narrow slice.

        ## Problem

        Example problem.

        ## Why This Bucket

        Example bucket reason.

        ## Next Action

        Define one narrow slice.

        ## References

        - `README.md`
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
    assert "docs-ai/current-work/backlog/harness__example__item.md missing backlog heading ## References" in errors


def test_validate_rejects_invalid_backlog_bucket(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "backlog" / "harness__example__item.md",
        """
        # Backlog Entry: harness/example/item

        ## Metadata

        - Status: `open`
        - Owner: `README.md`
        - Created: `2026-05-09`
        - Bucket: `later`
        - Risk: `medium`
        - Removal condition: `fixed or no longer relevant`
        - User acceptance: `none`
        - Location: `README.md`
        - Recommended fix: define one narrow slice.

        ## Problem

        Example problem.

        ## Why This Bucket

        Example bucket reason.

        ## Next Action

        Define one narrow slice.

        ## References

        - `README.md`
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
        - Created: `2026-05-09`
        - Bucket: `accepted temporary debt`
        - Risk: `medium`
        - Removal condition: `none`
        - User acceptance: `none`
        - Location: `README.md`
        - Recommended fix: define one narrow slice.

        ## Problem

        Example problem.

        ## Why This Bucket

        Example bucket reason.

        ## Next Action

        Define one narrow slice.

        ## References

        - `README.md`
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
        - Created: `2026-05-09`
        - Bucket: `accepted temporary debt`
        - Risk: `medium`
        - Removal condition: `<condition | none>`
        - User acceptance: `<required for accepted temporary debt | none>`
        - Location: `README.md`
        - Recommended fix: define one narrow slice.

        ## Problem

        Example problem.

        ## Why This Bucket

        Example bucket reason.

        ## Next Action

        Define one narrow slice.

        ## References

        - `README.md`
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/backlog/harness__example__item.md missing backlog field 'removal condition'" in errors
    assert "docs-ai/current-work/backlog/harness__example__item.md missing backlog field 'user acceptance'" in errors
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

        - Full wave execution: `wave-autopilot`.
        - Missing route: `missing-skill`.
        - Runtime proof policy: `runtime-proof`.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "AGENTS.md routes to removed workflow skill 'wave-autopilot'" in errors
    assert "AGENTS.md routes to missing skill 'missing-skill'" in errors


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
    add_skill(tmp_path, "design-integrity")
    write(tmp_path / "skills" / "design-integrity" / "references" / "web-boundaries.md", "# Web Boundaries\n")
    write(
        tmp_path / "skills" / "design-integrity" / "SKILL.md",
        """
        ---
        name: design-integrity
        description: Use when reviewing design integrity.
        ---

        # Design Integrity

        - Web boundary detail: `references/web-boundaries.md`
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/design-integrity/SKILL.md:8 has non-gated reference row in staged reference-gate skill; "
        "use `Read <reference> when/before/for ...`"
    ) in errors


def test_validate_rejects_removed_harness_path_outside_archive(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "README.md",
        """
        See skills/adversarial-review/SKILL.md.
        See skills/user-apps-design/references/atomic-design.md.
        See skills/user-apps-design/references/parity-dimensions.md.
        See skills/user-apps-design/references/ui-direction-workflow.md.
        See skills/testing-best-practices/references/condition-based-waiting.md.
        See skills/testing-best-practices/references/corpus-audit.md.
        See skills/testing-best-practices/references/layer-selection.md.
        See skills/testing-best-practices/references/proof-strength.md.
        See skills/testing-best-practices/references/touched-test-gate.md.
        See skills/initiatives-workflow/assets/wave-brief.example.md.
        See skills/webapp-testing/examples/console_logging.py.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "README.md references removed harness path skills/adversarial-review/SKILL.md" in errors
    assert (
        "README.md references removed harness path skills/user-apps-design/references/atomic-design.md"
        in errors
    )
    assert (
        "README.md references removed harness path skills/user-apps-design/references/parity-dimensions.md"
        in errors
    )
    assert (
        "README.md references removed harness path skills/user-apps-design/references/ui-direction-workflow.md"
        in errors
    )
    assert (
        "README.md references removed harness path skills/testing-best-practices/references/condition-based-waiting.md"
        in errors
    )
    assert (
        "README.md references removed harness path skills/testing-best-practices/references/corpus-audit.md"
        in errors
    )
    assert (
        "README.md references removed harness path skills/testing-best-practices/references/layer-selection.md"
        in errors
    )
    assert (
        "README.md references removed harness path skills/testing-best-practices/references/proof-strength.md"
        in errors
    )
    assert (
        "README.md references removed harness path skills/testing-best-practices/references/touched-test-gate.md"
        in errors
    )
    assert (
        "README.md references removed harness path skills/initiatives-workflow/assets/wave-brief.example.md"
        in errors
    )
    assert (
        "README.md references removed harness path skills/webapp-testing/examples/console_logging.py"
        in errors
    )


def test_validate_rejects_owner_only_doctrine_duplicates(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "documentation-stewardship" / "SKILL.md",
        """
        ---
        name: documentation-stewardship
        description: Test owner.
        ---

        Every durable rule has one owner.
        """,
    )
    write(
        tmp_path / "README.md",
        """
        Every durable rule has
        one owner.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "README.md duplicates owner-only doctrine 'Every durable rule has one owner.'; "
        "owner is skills/documentation-stewardship/SKILL.md"
    ) in errors


def test_validate_rejects_removed_harness_path_in_closed_archive(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "closed-harness-audits-2026-04.md",
        "Archived deletion: skills/adversarial-review/SKILL.md.\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "docs-ai/current-work/closed-harness-audits-2026-04.md references removed harness path "
        "skills/adversarial-review/SKILL.md"
    ) in errors


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


def test_validate_rejects_obsolete_role_packet_proof_row_term(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    roles_path = tmp_path / "agents" / "roles.md"
    roles_path.write_text(
        roles_path.read_text(encoding="utf-8")
        + "\nAdapter migrations update every consumer and proof row together.\n",
        encoding="utf-8",
    )

    errors = validate_harness.validate(tmp_path)

    assert "agents/roles.md contains obsolete packet term 'proof row'" in errors


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


def test_validate_rejects_subagent_metadata_preauthorization_duplicate(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "subagent-orchestration" / "agents" / "openai.yaml",
        """
        interface:
          display_name: "Subagent Orchestration"
          short_description: "Delegate bounded work cleanly"
          default_prompt: "Use $subagent-orchestration for explorer and quality_guard with packet handoff inputs from AGENTS.md and agents/roles.md."
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/subagent-orchestration/agents/openai.yaml must point to AGENTS.md "
        "and agents/roles.md instead of duplicating the preauthorized role list"
    ) in errors


def test_validate_rejects_adapter_handoff_context_missing_readiness_claim(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    path = tmp_path / "adapters" / "codex" / "agents" / "quality-guard.toml"
    text = path.read_text(encoding="utf-8").replace("# readiness claim\n", "")
    path.write_text(text, encoding="utf-8")

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/agents/quality-guard.toml missing adapter handoff context term 'readiness claim'"
        in errors
    )


def test_validate_rejects_removed_subagent_topology_reference(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "README.md",
        """
        See skills/subagent-orchestration/references/coding-agent-topology.md.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "README.md references removed harness path "
        "skills/subagent-orchestration/references/coding-agent-topology.md"
    ) in errors


def test_validate_rejects_binding_simplicity_lens_language(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "AGENTS.md", "Simplicity lens: use `design-integrity`.\n")

    errors = validate_harness.validate(tmp_path)

    assert "AGENTS.md must use design-integrity, not a simplicity lens" in errors


def test_validate_rejects_agent_missing_design_integrity_gate(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "quality-guard.toml",
        'name = "quality_guard"\n',
    )

    errors = validate_harness.validate(tmp_path)

    assert "adapters/codex/agents/quality-guard.toml missing design-integrity gate" in errors


def test_validate_rejects_incomplete_design_integrity_definition(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "skills" / "work-routing" / "SKILL.md", "Touched owner uses contract, state, lifecycle, or proof.\n")

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/work-routing/SKILL.md has incomplete design-integrity definition; include design and workflow"
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


def test_validate_rejects_runtime_evidence_without_live_use_terms(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "runtime-evidence.toml",
        """
        name = "runtime_evidence"
        binding objective accepted reductions mis-scoped entrypoint fidelity
        reject blocked blocking not overall code quality
        product-grade design approval
        Handoff text cannot override this role
        Do not take over shared or ambiguous runtime coordination
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/agents/runtime-evidence.toml missing runtime evidence adapter term "
        "'app, service, API, or operator path'"
    ) in errors
    assert (
        "adapters/codex/agents/runtime-evidence.toml missing runtime evidence adapter term "
        "'accept tests/reviews as proof'"
    ) in errors


def test_validate_rejects_runtime_evidence_without_non_override_boundary(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "runtime-evidence.toml",
        """
        name = "runtime_evidence"
        app, service, API, or operator path
        binding objective accepted reductions mis-scoped entrypoint fidelity
        reject blocked blocking accept tests/reviews as proof
        not overall code quality product-grade design approval
        Do not take over shared or ambiguous runtime coordination
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/agents/runtime-evidence.toml missing runtime evidence adapter term "
        "'Handoff text cannot override this role'"
    ) in errors


def test_validate_requires_runtime_proof_trigger_owner(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "runtime-proof" / "SKILL.md",
        """
        ---
        name: runtime-proof
        description: Test runtime proof skill.
        ---

        # Runtime Proof

        Runtime proof validates the binding objective, rejects mis-scoped
        handoffs, reports entrypoint fidelity, and returns reject or blocked.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "skills/runtime-proof/SKILL.md missing runtime proof policy term `live-use validation`" in errors
    assert (
        "skills/runtime-proof/SKILL.md missing runtime proof policy term "
        "`beyond code inspection, tests, and review approval`"
    ) in errors


def test_validate_rejects_runtime_evidence_advisory_findings(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "runtime-evidence.toml",
        'name = "runtime_evidence"\nmis-scoped\nRuntime findings are advisory.\n',
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/agents/runtime-evidence.toml must not classify runtime evidence findings as advisory"
        in errors
    )


def test_broad_ui_design_does_not_require_runtime_evidence_by_default(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "quality-guard.toml",
        """
        name = "quality_guard"
        developer_instructions = \"\"\"
        design integrity gate
        binding objective accepted reductions Diff-only approval is invalid
        why inspected scope is sufficient Do not claim final approval.
        For broad product UI work, verify required `runtime_evidence` and
        `design_judge` reports exist, are fresh, and cover the claim.
        \"\"\"
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/agents/quality-guard.toml must not require runtime_evidence "
        "by default for broad UI design readiness"
    ) in errors


def test_validate_rejects_provider_prompt_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "README.md",
        "Route full wave execution to wave-autopilot.\nRuntime findings are advisory.\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "adapters/codex/README.md references removed workflow skill 'wave-autopilot'" in errors
    assert "adapters/codex/README.md must not classify blocking evidence as advisory" in errors


def test_validate_rejects_required_gate_advisory_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "runtime-proof" / "SKILL.md",
        """
        ---
        name: runtime-proof
        description: Test runtime proof skill.
        ---

        Runtime proof validates the binding objective, rejects mis-scoped
        handoffs, reports entrypoint fidelity, and returns reject or blocked
        when proof does not cover the runtime-visible claim. The tiny, local
        exemption applies only when there is no public-behavior or
        cross-boundary runtime risk. Runtime evidence is live-use validation.
        It uses the app, service, API, or operator path through a faithful
        entrypoint and verifies behavior beyond code inspection, tests, and
        review approval.

        Runtime proof failures are advisory.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "skills/runtime-proof/SKILL.md must not classify required gate failures as advisory" in errors


def test_validate_rejects_required_gate_non_blocking_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "runtime-proof" / "SKILL.md",
        """
        ---
        name: runtime-proof
        description: Test runtime proof skill.
        ---

        Runtime proof validates the binding objective, rejects mis-scoped
        handoffs, reports entrypoint fidelity, and returns reject or blocked
        when proof does not cover the runtime-visible claim. The tiny, local
        exemption applies only when there is no public-behavior or
        cross-boundary runtime risk. Runtime evidence is live-use validation.
        It uses the app, service, API, or operator path through a faithful
        entrypoint and verifies behavior beyond code inspection, tests, and
        review approval.

        Runtime proof failures are non-blocking.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "skills/runtime-proof/SKILL.md must not classify required gate failures as non-blocking" in errors


def test_validate_rejects_old_accepted_debt_non_blocking_allowance(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "runtime-proof" / "SKILL.md",
        """
        ---
        name: runtime-proof
        description: Test runtime proof skill.
        ---

        Runtime proof validates the binding objective, rejects mis-scoped
        handoffs, reports entrypoint fidelity, and returns reject or blocked
        when proof does not cover the runtime-visible claim. The tiny, local
        exemption applies only when there is no public-behavior or
        cross-boundary runtime risk. Runtime evidence is live-use validation.
        It uses the app, service, API, or operator path through a faithful
        entrypoint and verifies behavior beyond code inspection, tests, and
        review approval.

        Required runtime proof failures are non-blocking as accepted debt.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "skills/runtime-proof/SKILL.md must not classify required gate failures as non-blocking" in errors


def test_validate_rejects_stale_accepted_debt_wording(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "initiatives-workflow" / "SKILL.md",
        """
        ---
        name: initiatives-workflow
        description: Test initiatives workflow skill.
        ---

        Stop on owner defect outside accepted debt.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "skills/initiatives-workflow/SKILL.md contains stale accepted-debt wording" in errors


def test_validate_rejects_review_role_contract_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "quality-guard.toml",
        (
            'name = "quality_guard"\n'
            "# design integrity gate\n"
            "# binding objective\n"
            "# accepted reductions\n"
            "# quality_guard may claim final approval\n"
        ),
    )

    errors = validate_harness.validate(tmp_path)

    assert "adapters/codex/agents/quality-guard.toml missing quality_guard final-approval negation" in errors
    assert (
        "adapters/codex/agents/quality-guard.toml missing review role contract term "
        "'Diff-only approval is invalid'"
    ) in errors
    assert (
        "adapters/codex/agents/quality-guard.toml missing review role contract term "
        "'why inspected scope is sufficient'"
    ) in errors


def test_validate_rejects_final_reviewer_scope_contract_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "final-reviewer.toml",
        (
            'name = "final_reviewer"\n'
            "# binding objective\n"
            "# accepted reductions\n"
            "# Do not perform planning-gate review\n"
            "# final_reviewer is not final approval\n"
        ),
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/agents/final-reviewer.toml missing review role contract term "
        "'Diff-only approval is invalid'"
    ) in errors
    assert (
        "adapters/codex/agents/final-reviewer.toml missing review role contract term "
        "'why it is sufficient'"
    ) in errors
    assert (
        "adapters/codex/agents/final-reviewer.toml missing review role contract term "
        "'project design source'"
    ) in errors
    assert (
        "adapters/codex/agents/final-reviewer.toml missing review role contract term "
        "'project design source requirements'"
    ) in errors
    assert (
        "adapters/codex/agents/final-reviewer.toml missing review role contract term "
        "'block missing, stale, blocked, rejected, or narrower'"
    ) in errors
    assert (
        "adapters/codex/agents/final-reviewer.toml missing review role contract term "
        "'project-local artifacts'"
    ) in errors


def test_validate_rejects_missing_code_review_project_artifact_coverage(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "code-review" / "SKILL.md",
        """
        ---
        name: code-review
        description: Review code.
        ---

        # Code Review

        Reject UI readiness closeout when `design_judge` is missing, rejected,
        blocked, stale, or narrower than the final claim.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/code-review/SKILL.md missing review governance "
        "contract term 'project design source'"
    ) in errors
    assert (
        "skills/code-review/SKILL.md missing review governance "
        "contract term 'missing, stale, blocked, rejected, or narrower'"
    ) in errors
    assert (
        "skills/code-review/SKILL.md missing review governance "
        "contract term 'project design source requirements'"
    ) in errors


def test_validate_rejects_stale_non_blocking_review_verdict(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "final-reviewer.toml",
        """
        name = "final_reviewer"
        description = "Final isolated closeout review after implementation and verification."

        developer_instructions = '''
        binding objective
        accepted reductions
        Diff-only approval is invalid
        why it is sufficient
        Do not perform planning-gate review
        not final approval
        project design source
        project design source requirements
        project-local artifacts
        block missing, stale, blocked, rejected, or narrower
        Overall: `BLOCK | NON-BLOCKING | APPROVE`
        '''
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "adapters/codex/agents/final-reviewer.toml uses stale NON-BLOCKING review verdict" in errors


def test_validate_rejects_missing_code_review_approval_evidence_fields(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "code-review" / "SKILL.md",
        """
        ---
        name: code-review
        description: Test code review skill.
        ---

        # Code Review

        ## Output

        - Base branch: `<name>`
        - Touched owner/component: `<owner>`
        - Overall: `BLOCK | APPROVE`
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "skills/code-review/SKILL.md missing review output term 'Approval boundary'" in errors
    assert "skills/code-review/SKILL.md missing review output term 'Existing authority checked'" in errors
    assert "skills/code-review/SKILL.md missing review output term 'Issue disposition'" in errors


def test_validate_rejects_missing_ui_approval_context_terms(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "user-apps-design" / "SKILL.md",
        """
        ---
        name: user-apps-design
        description: Test user apps design.
        ---

        # User Apps Design

        Before broad UI work, name visual goals.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/user-apps-design/SKILL.md "
        "missing UI approval context term 'project design source'"
    ) in errors
    assert (
        "skills/user-apps-design/SKILL.md "
        "missing UI approval context term 'project design source requirements'"
    ) in errors
    assert (
        "skills/user-apps-design/SKILL.md "
        "missing UI approval context term 'declared project design source'"
    ) in errors
    assert (
        "skills/user-apps-design/SKILL.md "
        "missing UI approval context term 'project-local artifacts'"
    ) in errors
    assert (
        "skills/user-apps-design/SKILL.md "
        "missing UI approval context term 'screenshot/contact-sheet'"
    ) in errors


def test_validate_rejects_missing_ui_approval_boundary_terms(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "user-apps-design" / "SKILL.md",
        """
        ---
        name: user-apps-design
        description: Test user apps design.
        ---

        # User Apps Design

        Before broad UI work, name project design source, project-local
        artifacts, screenshot/contact-sheet, Missing project design source
        blocks, and claim is explicitly narrowed.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/user-apps-design/SKILL.md "
        "missing UI approval boundary term 'Runtime evidence'"
    ) in errors
    assert (
        "skills/user-apps-design/SKILL.md "
        "missing UI approval boundary term 'does not decide live behavior or code quality'"
    ) in errors


def test_validate_rejects_role_boundary_contract_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "adapters" / "codex" / "agents" / "explorer.toml",
        'name = "explorer"\n# design integrity gate\n# Stay read-only\n',
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/agents/explorer.toml missing role boundary contract term "
        "'Do not edit code or take implementation ownership.'"
    ) in errors


def test_validate_rejects_design_judge_contract_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_roles(tmp_path, ("explorer", "quality_guard", "design_judge"))
    write(
        tmp_path / "adapters" / "codex" / "agents" / "design-judge.toml",
        'name = "design_judge"\n# screenshot/contact-sheet\n',
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/agents/design-judge.toml missing role boundary contract term "
        "'runtime-evidence-based'"
    ) in errors
    assert (
        "adapters/codex/agents/design-judge.toml missing role boundary contract term "
        "'not live behavior or code quality'"
    ) in errors
    assert (
        "adapters/codex/agents/design-judge.toml missing role boundary contract term "
        "'declared project design source'"
    ) in errors
    assert (
        "adapters/codex/agents/design-judge.toml missing role boundary contract term "
        "'materially weaker than the target'"
    ) in errors
    assert (
        "adapters/codex/agents/design-judge.toml missing role boundary contract term "
        "'invent design criteria'"
    ) in errors
    assert (
        "adapters/codex/agents/design-judge.toml missing role boundary contract term "
        "'visual quality only'"
    ) in errors


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


def test_validate_rejects_packet_missing_required_section(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "bad-wave" / "wave-execution.md",
        """
        # Wave bad-wave Execution Packet

        ## Objective

        ## Design Integrity

        ## Execution
        """,
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "bad-wave.md",
        "# Wave bad-wave\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/bad-wave/wave-execution.md missing section 'Readiness Claim'" in errors


def test_validate_rejects_wave_task_card_missing_owned_surfaces_or_checks(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "bad-wave" / "wave-execution.md",
        """
        # Wave bad-wave Execution Packet

        ## Objective

        - original objective: `Example objective.`

        ## Design Integrity

        - owner/interface: `example`
        - verdict: `acceptable`

        ## Execution

        ### `example/task`

        - State: `blank`

        ## Readiness Claim

        - exact claim: `Example claim.`
        - Follow-up:
          - `none`
        """,
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "bad-wave.md",
        "# Wave bad-wave\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/bad-wave/wave-execution.md task card '`example/task`' missing - Owned surfaces:" in errors
    assert "docs-ai/current-work/bad-wave/wave-execution.md task card '`example/task`' missing - Checks/artifacts:" in errors


def test_validate_rejects_wave_task_card_missing_or_invalid_state(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    packet = valid_packet().replace("    - State: `blank`\n", "")
    write(tmp_path / "docs-ai" / "current-work" / "missing-state" / "wave-execution.md", packet)
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "missing-state.md",
        "# Wave missing-state\n\n**Status:** execution-ready\n",
    )

    invalid_packet = valid_packet().replace("`blank`", "`reviewing`", 1)
    write(tmp_path / "docs-ai" / "current-work" / "invalid-state" / "wave-execution.md", invalid_packet)
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "invalid-state.md",
        "# Wave invalid-state\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/missing-state/wave-execution.md task card '`example/task`' missing state" in errors
    assert (
        "docs-ai/current-work/invalid-state/wave-execution.md task card '`example/task`' "
        "invalid state 'reviewing'; expected one of ['blank', 'blocked', 'done']"
    ) in errors


def test_validate_rejects_wave_packet_missing_readiness_claim(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    packet = """
    # Wave bad-wave Execution Packet

    ## Objective

    - original objective: `Example objective.`

    ## Design Integrity

    - owner/interface: `example`
    - verdict: `acceptable`

    ## Execution

    - blockers/decisions: `none`
    """
    write(tmp_path / "docs-ai" / "current-work" / "bad-wave" / "wave-execution.md", packet)
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "bad-wave.md",
        "# Wave bad-wave\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/bad-wave/wave-execution.md missing section 'Readiness Claim'" in errors


def test_validate_rejects_wave_packet_missing_core_fields(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    packet = valid_packet().replace("    - accepted reductions: `none`\n", "", 1).replace(
        "    - evidence status: `planned`\n",
        "",
        1,
    )
    write(tmp_path / "docs-ai" / "current-work" / "bad-wave" / "wave-execution.md", packet)
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "bad-wave.md",
        "# Wave bad-wave\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/bad-wave/wave-execution.md section 'Objective' missing field 'accepted reductions'" in errors
    assert "docs-ai/current-work/bad-wave/wave-execution.md section 'Readiness Claim' missing field 'evidence status'" in errors


def test_validate_rejects_wave_packet_obsolete_top_level_ceremony(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    packet = valid_packet().replace(
        "    ## Execution",
        "    ## Work Context\n\n    old duplicate context\n\n    ## Required Gates\n\n    | Claim | Required gate | Owner | Proof/artifacts | Blocks when |\n    | --- | --- | --- | --- | --- |\n    | old | old | old | old | old |\n\n    ## Execution",
        1,
    )
    write(tmp_path / "docs-ai" / "current-work" / "bad-wave" / "wave-execution.md", packet)
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "bad-wave.md",
        "# Wave bad-wave\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/bad-wave/wave-execution.md contains obsolete top-level section 'Work Context'" in errors
    assert "docs-ai/current-work/bad-wave/wave-execution.md contains obsolete top-level section 'Required Gates'" in errors


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


def test_validate_rejects_closed_wave_left_in_delivery_map(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "done-wave.md",
        "# Wave done-wave\n\n**Status:** done\n",
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "retired-wave.md",
        "# Wave retired-wave\n\n**Status:** retired\n",
    )
    write(
        tmp_path / "docs-ai" / "current-work" / "delivery-map.md",
        """
        # Delivery Map (Waves + Backlog)

        ## Wave Plan

        ### Wave done-wave - Done Wave

        - `initiative/feature/task`

        - [retired](../docs/initiatives/waves/retired-wave.md)
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/delivery-map.md lists done wave done-wave" in errors
    assert "docs-ai/current-work/delivery-map.md lists retired wave retired-wave" in errors
