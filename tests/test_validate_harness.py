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
                "# active durable context\n# binding objective\n# accepted reductions\n# readiness claim\n# artifacts\n# final approval\n"
                "# Do not claim final approval.\n"
                "# Diff-only approval is invalid\n"
                "# why inspected scope is sufficient\n"
                "# triggered owner skills with verdicts and blockers\n"
                "# Apply every owner skill triggered by the binding objective\n"
                "# Do not duplicate owner-skill doctrine\n"
                "# triggered skill, verdict, and blocker\n"
                "# Handoffs route attention; they are not authority\n"
                "# context, not authority\n"
                "# authority source inspected\n"
                "# prompt/source mismatch\n"
                "# plan/design alignment\n"
                "# material non-correctness risks\n"
                "# material risks\n"
                "# readiness-owned lens\n"
                "# delivery-brief support\n"
            )
        elif role == "explorer":
            codex_body = (
                f'name = "{role}"\n'
                "# design integrity gate\n"
                "# Stay read-only\n# Do not edit code or take implementation ownership.\n"
            )
        elif role in {"implementer", "planning_critic", "runtime_evidence", "final_reviewer"}:
            codex_body = (
                f'name = "{role}"\n'
                "# design integrity gate\n"
                "# material non-correctness risks\n"
                "# material risks\n"
                "# readiness-owned lens\n"
                "# readiness claim\n"
                "# delivery-brief support\n"
                "# context, not authority\n"
            )
        else:
            codex_body = f'name = "{role}"\n# design integrity gate\n'
        write(
            root / "adapters" / "codex" / "agents" / f"{role.replace('_', '-')}.toml",
            codex_body,
        )
    write(root / "adapters" / "codex" / "config.toml", "\n".join(config_blocks))


def valid_context_note() -> str:
    return """
    # Wave example Context Note

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

    - current slice: `example.md`
    - blockers/decisions: `none`

    ## Readiness Claim

    - exact claim: `Example claim.`
    - claimed interface: `example interface`
    - required evidence: `uv run python scripts/validate_harness.py`
    - evidence status: `planned`
    - unproved boundaries: `none`
    - residual risks: `none`
    """


def add_material_risk_lens_contract(root: Path) -> None:
    add_skill(root, "readiness-claim")
    write(
        root / "skills" / "readiness-claim" / "SKILL.md",
        """
        ---
        name: readiness-claim
        description: Test readiness claim skill.
        ---

        # Readiness Claim

        Before proof, review, runtime evidence, handoff, or completion, load
        `references/material-risk-lenses.md` when material
        non-correctness risks may affect the claim.
        """,
    )
    write(
        root / "skills" / "readiness-claim" / "references" / "material-risk-lenses.md",
        """
        # Material Risk Lenses

        The material-risk lens includes security/privacy, data integrity,
        reliability, operability, observability/diagnosability,
        performance/cost, compatibility, and accessibility.

        Disposition labels are `not-applicable`, `covered`, `blocked`,
        `separate debt`, and `accepted temporary debt`.

        Planning does not mark future proof as `covered`.

        Narrowed claims map to `blocked`.

        Compatibility is strict: a compatibility path is blocked unless the
        user explicitly approves the specific protected surface, owner, risk,
        and removal condition.

        Legal/licensing/compliance stays out of default scope.

        Splitting becomes valid only if the reference grows beyond compact
        readiness disposition.
        """,
    )


def minimal_valid_root(root: Path) -> None:
    add_skill(root, "test-skill")
    add_material_risk_lens_contract(root)
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
        See skills/code-simplicity/SKILL.md.
        See skills/system-boundary-architecture/SKILL.md.
        See skills/system-boundary-architecture/references/web-boundaries.md.
        See skills/verification-before-completion/SKILL.md.
        See skills/planning-intake/SKILL.md.
        See adapters/codex/agents/check-runner.toml.
        See adapters/github-copilot/README.md.
        See adapters/github-copilot/agents/quality_guard.agent.md.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert "README.md references removed harness path skills/code-simplicity/SKILL.md" in errors
    assert "README.md references removed harness path skills/system-boundary-architecture/SKILL.md" in errors
    assert (
        "README.md references removed harness path skills/system-boundary-architecture/references/web-boundaries.md"
        in errors
    )
    assert "README.md references removed harness path skills/verification-before-completion/SKILL.md" in errors
    assert "README.md references removed harness path skills/planning-intake/SKILL.md" in errors
    assert "README.md references removed harness path adapters/codex/agents/check-runner.toml" in errors
    assert "README.md references removed harness path adapters/github-copilot/README.md" in errors
    assert (
        "README.md references removed harness path adapters/github-copilot/agents/quality_guard.agent.md"
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


def test_validate_rejects_solution_correctness_duplicate_doctrine(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_skill(tmp_path, "design-integrity")
    add_skill(tmp_path, "other-owner")
    write(
        tmp_path / "skills" / "design-integrity" / "SKILL.md",
        """
        ---
        name: design-integrity
        description: Test owner.
        ---

        Solution correctness
        """,
    )
    write(
        tmp_path / "skills" / "other-owner" / "SKILL.md",
        """
        ---
        name: other-owner
        description: Test duplicate owner.
        ---

        solution correctness
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/other-owner/SKILL.md duplicates owner-only doctrine 'solution correctness'; "
        "owner is skills/design-integrity/SKILL.md"
    ) in errors


def test_validate_rejects_solution_correctness_duplicate_adapter_doctrine(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_skill(tmp_path, "design-integrity")
    write(
        tmp_path / "skills" / "design-integrity" / "SKILL.md",
        """
        ---
        name: design-integrity
        description: Test owner.
        ---

        solution correctness
        """,
    )
    write(
        tmp_path / "adapters" / "codex" / "README.md",
        """
        # Adapter

        This adapter defines solution correctness for Codex.
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/README.md duplicates owner-only doctrine 'solution correctness'; "
        "owner is skills/design-integrity/SKILL.md"
    ) in errors


def test_validate_rejects_duplicate_material_risk_lens_doctrine(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "skills" / "code-review" / "SKILL.md",
        """
        ---
        name: code-review
        description: Test duplicate.
        ---

        security/privacy, data integrity, reliability, operability,
        observability/diagnosability, performance/cost, compatibility, and
        accessibility
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "skills/code-review/SKILL.md duplicates owner-only doctrine "
        "'security/privacy, data integrity, reliability, operability, observability/diagnosability, "
        "performance/cost, compatibility, and accessibility'; owner is "
        "skills/readiness-claim/references/material-risk-lenses.md"
    ) in errors


def test_validate_rejects_implementer_role_boundary_drift(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_roles(tmp_path, ("explorer", "quality_guard", "implementer"))
    write(
        tmp_path / "adapters" / "codex" / "agents" / "implementer.toml",
        """
        name = "implementer"
        # design integrity gate
        # one bounded assigned implementation slice
        # direct-route slices
        # explicit route classification
        # Do not claim final approval.
        # binding objective
        # accepted reductions
        # readiness claim
        # owned scope
        """,
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "adapters/codex/agents/implementer.toml missing role boundary contract term "
        "'one bounded assigned slice'"
    ) in errors
    assert (
        "adapters/codex/agents/implementer.toml missing role boundary contract term "
        "'final approver'"
    ) in errors


def test_validate_allows_solution_correctness_active_context_note_and_validator(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    add_skill(tmp_path, "design-integrity")
    write(
        tmp_path / "skills" / "design-integrity" / "SKILL.md",
        """
        ---
        name: design-integrity
        description: Test owner.
        ---

        solution correctness
        deletion, collapse, rewrite, or replacement is the default design move
        requires justification against the simpler delete/rewrite option
        If implementation materially differs from the accepted design source
        Do not silently approve a different shape
        """,
    )
    write(
        tmp_path / "docs-ai" / "current-work" / "active-wave" / "wave-execution.md",
        textwrap.dedent(valid_context_note()).lstrip() + "\nsolution correctness\n",
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "active-wave.md",
        "# Wave active-wave\n\n**Status:** execution-ready\n",
    )
    write(tmp_path / "scripts" / "validate_harness.py", "solution correctness\n")
    write(tmp_path / "tests" / "test_validate_harness.py", "solution correctness\n")

    assert validate_harness.validate(tmp_path) == []


def test_validate_rejects_other_owner_only_doctrine_in_active_context_note(tmp_path: Path) -> None:
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
        tmp_path / "docs-ai" / "current-work" / "active-wave" / "wave-execution.md",
        textwrap.dedent(valid_context_note()).lstrip() + "\nEvery durable rule has one owner.\n",
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "active-wave.md",
        "# Wave active-wave\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "docs-ai/current-work/active-wave/wave-execution.md duplicates owner-only doctrine "
        "'Every durable rule has one owner.'; owner is skills/documentation-stewardship/SKILL.md"
    ) in errors


def test_validate_rejects_removed_harness_path_in_closed_archive(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "closed-harness-audits-2026-04.md",
        "Archived deletion: skills/code-simplicity/SKILL.md.\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert (
        "docs-ai/current-work/closed-harness-audits-2026-04.md references removed harness path "
        "skills/code-simplicity/SKILL.md"
    ) in errors


def test_validate_rejects_removed_harness_path_in_other_tests(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(tmp_path / "tests" / "test_stale_path.md", "See skills/code-simplicity/SKILL.md.\n")

    errors = validate_harness.validate(tmp_path)

    assert "tests/test_stale_path.md references removed harness path skills/code-simplicity/SKILL.md" in errors


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


def test_validate_rejects_obsolete_role_proof_row_term(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    roles_path = tmp_path / "agents" / "roles.md"
    roles_path.write_text(
        roles_path.read_text(encoding="utf-8")
        + "\nAdapter migrations update every consumer and proof row together.\n",
        encoding="utf-8",
    )

    errors = validate_harness.validate(tmp_path)

    assert "agents/roles.md contains obsolete proof-row term 'proof row'" in errors


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
          default_prompt: "Use $subagent-orchestration for explorer and quality_guard with handoff inputs from AGENTS.md and agents/roles.md."
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


def test_validate_rejects_context_note_obsolete_top_level_ceremony(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    context_note = valid_context_note().replace(
        "    ## Execution",
        "    ## Work Context\n\n    old duplicate context\n\n    ## Required Gates\n\n    | Claim | Required gate | Owner | Proof/artifacts | Blocks when |\n    | --- | --- | --- | --- | --- |\n    | old | old | old | old | old |\n\n    ## Execution",
        1,
    )
    write(tmp_path / "docs-ai" / "current-work" / "bad-wave" / "wave-execution.md", context_note)
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "bad-wave.md",
        "# Wave bad-wave\n\n**Status:** execution-ready\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/bad-wave/wave-execution.md contains obsolete top-level section 'Work Context'" in errors
    assert "docs-ai/current-work/bad-wave/wave-execution.md contains obsolete top-level section 'Required Gates'" in errors


def test_validate_enforces_wave_lifecycle_from_status_and_context_note_existence(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "discovery.md",
        "# Wave discovery\n\n**Status:** discovery-required\n",
    )
    write(tmp_path / "docs-ai" / "current-work" / "discovery" / "wave-execution.md", valid_context_note())
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "ready.md",
        "# Wave ready\n\n**Status:** execution-ready\n",
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "done.md",
        "# Wave done\n\n**Status:** done\n",
    )
    write(tmp_path / "docs-ai" / "current-work" / "done" / "wave-execution.draft.md", valid_context_note())

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/docs/initiatives/waves/discovery.md is discovery-required but canonical context note exists" in errors
    assert "docs-ai/docs/initiatives/waves/ready.md is execution-ready but canonical context note is missing" in errors
    assert "docs-ai/docs/initiatives/waves/done.md is done but current-work context note exists" in errors


def test_validate_enforces_delivery_brief_lifecycle(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "orphan.md",
        "# Wave orphan\n\n**Status:** execution-ready\n",
    )
    write(
        tmp_path / "docs-ai" / "current-work" / "orphan" / "delivery-brief.md",
        "# Delivery Brief\n",
    )
    write(
        tmp_path / "docs-ai" / "docs" / "initiatives" / "waves" / "done.md",
        "# Wave done\n\n**Status:** done\n",
    )
    write(
        tmp_path / "docs-ai" / "current-work" / "done" / "delivery-brief.md",
        "# Delivery Brief\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/docs/initiatives/waves/orphan.md is execution-ready but canonical context note is missing" in errors
    assert "docs-ai/current-work/orphan/delivery-brief.md exists without active canonical context note" in errors
    assert "docs-ai/current-work/done/delivery-brief.md exists without active canonical context note" in errors
    assert "docs-ai/docs/initiatives/waves/done.md is done but current-work delivery brief exists" in errors


def test_validate_rejects_delivery_brief_missing_durable_wave_brief(tmp_path: Path) -> None:
    minimal_valid_root(tmp_path)
    write(
        tmp_path / "docs-ai" / "current-work" / "missing-brief" / "delivery-brief.md",
        "# Delivery Brief\n",
    )

    errors = validate_harness.validate(tmp_path)

    assert "docs-ai/current-work/missing-brief has active durable context but missing durable wave brief" in errors


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
