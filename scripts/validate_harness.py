from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MARKDOWN_LEVEL_TWO_HEADING_PATTERN = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
INLINE_PATH_RE = re.compile(r"`((?:(?:references|assets|scripts)/|\.\./)[^`\s]+)`")
FORBIDDEN_PROJECT_OWNER_PATH_RE = re.compile(r"`(docs-ai/docs/conventions/[^`]+)`")
SKILL_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_-])\$([a-z][a-z0-9]*(?:-[a-z0-9]+)*)(?![A-Za-z0-9_-])")
BACKTICK_SKILL_REF_RE = re.compile(
    r"\b(?:use|load|apply|invoke|route(?:s|d)?|delegate(?:s|d)?)"
    r"(?:\s+[a-z]+){0,4}\s+`([a-z0-9]+(?:-[a-z0-9]+)+)`",
    re.IGNORECASE,
)
BACKTICKED_SKILL_NAME_RE = re.compile(r"`([a-z][a-z0-9]*(?:-[a-z0-9]+)*)`")
SKILL_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9_-])((?:(?:\.\./)+)?(?:skills/)?([a-z0-9]+(?:-[a-z0-9]+)*)/SKILL\.md)(?![A-Za-z0-9_-])"
)
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_DELIMITER = "---"
OPENAI_ALLOWED_TOP_LEVEL_KEYS = {"interface", "dependencies", "policy"}
OPENAI_ALLOWED_INTERFACE_KEYS = {
    "display_name",
    "short_description",
    "icon_small",
    "icon_large",
    "brand_color",
    "default_prompt",
}
PACKET_REQUIRED_SECTIONS = (
    "Objective",
    "Design Integrity",
    "Execution",
    "Readiness Claim",
)
PACKET_REQUIRED_FIELDS = {
    "Objective": (
        "original objective",
        "accepted reductions",
    ),
    "Design Integrity": (
        "owner/interface",
        "verdict",
    ),
    "Readiness Claim": (
        "exact claim",
        "claimed interface",
        "required evidence",
        "evidence status",
        "unproved boundaries",
        "residual risks",
    ),
}
TASK_CARD_STATE_FIELD = "- State:"
TASK_CARD_OWNED_SURFACES_FIELD = "- Owned surfaces:"
TASK_CARD_CHECKS_FIELD = "- Checks/artifacts:"
TASK_CARD_ALLOWED_STATES = {"blank", "done", "blocked"}
WAVE_STATUSES = {"discovery-required", "execution-ready", "done", "retired"}
# AGENTS.md and subagent-orchestration must keep explicit user authorization;
# otherwise adapter-level spawn rules can block required harness reviewers.
PREAUTHORIZED_SUBAGENT_SENTINEL = (
    "The user explicitly authorizes use of the spawn/subagent tool for these"
)
PREAUTHORIZED_SUBAGENT_END = "This preauthorization applies only to those named roles"
REMOVED_CODEX_AGENT_NAMES = {"check_runner"}
DESIGN_INTEGRITY_FILES = (
    "AGENTS.md",
    "skills/design-integrity/SKILL.md",
    "skills/work-routing/SKILL.md",
    "skills/code-review/SKILL.md",
    "skills/initiatives-workflow/references/wave-packet-contract.md",
)
DESIGN_INTEGRITY_AGENT_FILES = (
    "adapters/codex/agents/planning-critic.toml",
    "adapters/codex/agents/implementer.toml",
    "adapters/codex/agents/quality-guard.toml",
    "adapters/codex/agents/final-reviewer.toml",
)
RUNTIME_EVIDENCE_ADAPTER_FILES = (
    "adapters/codex/agents/runtime-evidence.toml",
)
RUNTIME_EVIDENCE_ADAPTER_REQUIRED_TERMS = (
    "app, service, API, or operator path",
    "binding objective",
    "accepted reductions",
    "Handoff text cannot override this role",
    "mis-scoped",
    "entrypoint fidelity",
    "reject",
    "blocked",
    "blocking",
    "accept tests/reviews as proof",
    "not overall code quality",
    "Do not use this role for visual-only UI design readiness",
    "product-grade design approval",
    "Do not take over shared or ambiguous runtime coordination",
)
PROVIDER_PROMPT_FILES = (
    "adapters/codex/README.md",
    "adapters/codex/config.toml",
    "adapters/codex/install-scope.md",
    "adapters/codex/install.sh",
)
REVIEW_ROLE_CONTRACTS = {
    "adapters/codex/agents/planning-critic.toml": (
        "binding objective",
        "accepted reductions",
        "readiness claim",
        "triggered owner skills with verdicts and blockers",
    ),
    "adapters/codex/agents/quality-guard.toml": (
        "binding objective",
        "accepted reductions",
        "Diff-only approval is invalid",
        "why inspected scope is sufficient",
        "triggered owner skills with verdicts and blockers",
    ),
    "adapters/codex/agents/final-reviewer.toml": (
        "binding objective",
        "accepted reductions",
        "Diff-only approval is invalid",
        "why it is sufficient",
        "Do not perform planning-gate review",
        "not final approval",
        "project design source",
        "project design source requirements",
        "project-local artifacts",
        "block missing, stale, blocked, rejected, or narrower",
        "Triggered owner skills",
    ),
}
REVIEW_GOVERNANCE_REQUIRED_TERMS = (
    "project design source",
    "project design source requirements",
    "project-local artifacts",
    "missing, stale, blocked, rejected, or narrower",
    "does not decide the design verdict",
)
REVIEW_VERDICT_FILES = (
    "skills/code-review/SKILL.md",
    "adapters/codex/agents/quality-guard.toml",
    "adapters/codex/agents/final-reviewer.toml",
)
CODE_REVIEW_OUTPUT_REQUIRED_TERMS = (
    "Binding objective",
    "Accepted reductions",
    "Approval boundary",
    "Boundary sufficiency",
    "Existing authority checked",
    "Authority source inspected",
    "Prompt/source mismatch",
    "Plan/design alignment",
    "Triggered owner skills",
    "Proof reviewed",
    "Issue disposition",
)
REVIEW_AUTHORITY_TERMS = (
    "Handoffs route attention; they are not authority",
    "authority source inspected",
    "prompt/source mismatch",
    "plan/design alignment",
)
REVIEW_TRIGGERED_OWNER_SKILL_TERMS = (
    "Apply every owner skill triggered by the binding objective",
    "Do not duplicate owner-skill doctrine",
    "triggered skill, verdict, and blocker",
)
DESIGN_CONTEXT_CONTRACT_REQUIRED_TERMS = (
    "project design source",
    "project design source requirements",
    "declared project design source",
    "project-local artifacts",
    "screenshot/contact-sheet",
    "Missing project design source blocks",
    "claim is explicitly narrowed",
)
UI_APPROVAL_BOUNDARY_REQUIRED_TERMS = (
    "Runtime evidence",
    "do not approve visual quality",
    "does not decide live behavior or code quality",
)
# Exact adapter-role terms protect one concrete counterexample each: reviewers
# claiming another role's authority, support roles editing, implementers
# executing without approved state, or runtime evidence reviewing code quality.
# Keep these checks narrow; do not turn them into subjective prompt-style lint.
ROLE_BOUNDARY_CONTRACTS = {
    "adapters/codex/agents/explorer.toml": (
        "Stay read-only",
        "Do not edit code or take implementation ownership.",
    ),
    "adapters/codex/agents/implementer.toml": (
        "one bounded assigned implementation slice",
        "direct-route slices",
        "Do not claim final approval.",
    ),
    "adapters/codex/agents/planning-critic.toml": (
        "Review non-trivial planning only",
        "Stay read-only and do not edit code or docs.",
        "Do not act as a final approver, implementation reviewer, or implementation owner.",
    ),
    "adapters/codex/agents/design-judge.toml": (
        "screenshot/contact-sheet",
        "binding objective",
        "accepted reductions",
        "project design source",
        "declared project design source",
        "project design source requirements",
        "Missing or contradictory declared project design source is `blocked`",
        "accepted narrowed claim",
        "run the app",
        "review code",
        "debug",
        "prove runtime behavior",
        "invent design criteria",
        "materially weaker than the target",
        "runtime-evidence-based",
        "pass",
        "reject",
        "blocked",
        "visual quality only",
        "Do not perform `runtime_evidence`, `quality_guard`, `final_reviewer`",
        "not live behavior or code quality",
    ),
}
ADAPTER_HANDOFF_CONTEXT_CONTRACTS = {
    "adapters/codex/agents/implementer.toml": ("binding objective", "accepted reductions", "readiness claim", "owned scope"),
    "adapters/codex/agents/planning-critic.toml": ("binding objective", "accepted reductions", "readiness claim"),
    "adapters/codex/agents/quality-guard.toml": ("binding objective", "accepted reductions", "readiness claim"),
    "adapters/codex/agents/final-reviewer.toml": ("binding objective", "accepted reductions", "proof artifacts"),
    "adapters/codex/agents/runtime-evidence.toml": ("binding objective", "accepted reductions", "artifacts"),
    "adapters/codex/agents/design-judge.toml": ("binding objective", "accepted reductions", "artifacts"),
}
REMOVED_WORKFLOW_SKILL_NAMES = (
    "executing-plans",
    "wave-autopilot",
    "workflow-feedback",
    "writing-plans",
)
ADVISORY_DRIFT_RE = re.compile(r"\badvisory\b", re.IGNORECASE)
NON_BLOCKING_DRIFT_RE = re.compile(r"\bnon-blocking\b", re.IGNORECASE)
ADVISORY_NEGATION_RE = re.compile(
    r"\b(?:must not|do not|not classify|not treat|never|not advisory)\b",
    re.IGNORECASE,
)
NON_BLOCKING_ALLOWED_RE = re.compile(
    r"\b(?:outside|accepted temporary debt|explicitly accepted temporary debt|NON-BLOCKING is an observation category)\b",
    re.IGNORECASE,
)
REQUIRED_GATE_CONTEXT_RE = re.compile(
    r"\b(?:required|gate|proof|review|runtime|architecture|design-integrity|validation|finding|evidence)\b",
    re.IGNORECASE,
)
QUALITY_GUARD_FINAL_APPROVAL_NEGATION_RE = re.compile(r"\bDo not\b.*\bclaim final approval\b", re.IGNORECASE)
RUNTIME_PROOF_POLICY_FILES = (
    "skills/runtime-proof/SKILL.md",
)
WEB_BROWSER_PROOF_FILES = (
    "skills/webapp-testing/references/browser-runtime-proof-workflow.md",
    "skills/webapp-testing/references/browser-proof-layering-contract.md",
)
LIVE_VALIDATION_STALE_PHRASES = (
    "Delegate isolated runtime proof only when startup/teardown is deterministic and ownership is unambiguous.",
)
STALE_ACCEPTED_DEBT_PHRASES = (
    "owner defect outside accepted debt",
)
BACKLOG_REQUIRED_HEADINGS = ("metadata", "problem", "why this bucket", "next action", "references")
BACKLOG_REQUIRED_FIELDS = (
    "status",
    "owner",
    "created",
    "bucket",
    "risk",
    "removal condition",
    "user acceptance",
    "location",
    "recommended fix",
)
BACKLOG_BUCKET_VALUES = ("discovered separate debt", "accepted temporary debt")
BACKLOG_ENTRY_TITLE_PREFIX = "# Backlog Entry:"
STAGED_REFERENCE_GATE_SKILLS = {
    "code-review",
    "design-integrity",
    "documentation-stewardship",
    "feedback-address",
    "flutter-expert",
    "harness-governance",
    "initiatives-workflow",
    "svelte-code-writer",
    "subagent-orchestration",
    "systematic-debugging",
    "testing-best-practices",
    "runtime-proof",
    "user-apps-design",
    "webapp-testing",
    "mobileapp-testing",
    "work-routing",
}
DEFERRED_REFERENCE_GATE_SKILL_GROUPS = {}
SKILL_BODY_TRIGGER_PATTERNS = (
    (re.compile(r"^##\s+Use\s+(?:When|For)\b", re.IGNORECASE | re.MULTILINE), "body-level trigger heading"),
    (re.compile(r"\bUse this skill when\b", re.IGNORECASE), "body-level trigger phrase"),
)
SKILL_REFERENCE_PATH_RE = re.compile(r"`(?:\.\./[^`]*?/)?references/[^`\s]+\.md`")
REQUIRED_REFERENCE_GATE_RE = re.compile(
    r"^\s*-?\s*Read\s+`(?:\.\./[^`]*?/)?references/[^`\s]+\.md`.*\b(?:when|before|for)\b",
    re.IGNORECASE,
)
REMOVED_HARNESS_PATHS = (
    # Current redesign-era removals that are still likely to regress through
    # stale links, live installs, or adapter drift.
    "skills/code-simplicity/SKILL.md",
    "skills/code-simplicity/agents/openai.yaml",
    "skills/code-simplicity/references/touched-component-integrity-gate.md",
    "skills/code-simplicity/references/default-simplicity-posture.md",
    "adapters/codex/agents/check-runner.toml",
    "adapters/github-copilot/README.md",
    "adapters/github-copilot/agents/check_runner.agent.md",
    "adapters/github-copilot/agents/design_judge.agent.md",
    "adapters/github-copilot/agents/explorer.agent.md",
    "adapters/github-copilot/agents/final_reviewer.agent.md",
    "adapters/github-copilot/agents/implementer.agent.md",
    "adapters/github-copilot/agents/planning_critic.agent.md",
    "adapters/github-copilot/agents/quality_guard.agent.md",
    "adapters/github-copilot/agents/runtime_evidence.agent.md",
    "skills/planning-intake/SKILL.md",
    "skills/planning-intake/agents/openai.yaml",
    "skills/planning-intake/references/intake-contract.md",
    "skills/system-boundary-architecture/references/code-shape-and-local-design.md",
    "skills/system-boundary-architecture/SKILL.md",
    "skills/system-boundary-architecture/agents/openai.yaml",
    "skills/system-boundary-architecture/references/mobile-client-boundaries.md",
    "skills/system-boundary-architecture/references/python-service-boundaries.md",
    "skills/system-boundary-architecture/references/web-boundaries.md",
    "skills/system-boundary-architecture/references/engineering-principles.md",
    "skills/system-boundary-architecture/references/migration-guardrails.md",
    "skills/system-boundary-architecture/references/python-service-and-boundary-doctrine.md",
    "skills/system-boundary-architecture/references/system-and-boundary-architecture.md",
    "skills/system-boundary-architecture/references/web-frontend-boundaries.md",
    "skills/system-boundary-architecture/references/web-route-and-state-boundary-doctrine.md",
    "skills/verification-before-completion/references/quality-gate-selection.md",
    "skills/verification-before-completion/SKILL.md",
    "skills/verification-before-completion/agents/openai.yaml",
    "skills/verification-before-completion/references/runtime-evidence-contract.md",
    "skills/verification-before-completion/references/runtime-proof-escalation.md",
    "skills/verification-before-completion/references/verification-evidence.md",
)
REMOVED_HARNESS_PATH_EXEMPTIONS = {
    "scripts/validate_harness.py",
    "tests/test_validate_harness.py",
}
OWNER_ONLY_DOCTRINE = {
    "Every durable rule has one owner.": "skills/documentation-stewardship/SKILL.md",
    "Every durable concept has one owner.": "skills/documentation-stewardship/SKILL.md",
    "Runtime evidence is blocking, not advisory.": "skills/runtime-proof/SKILL.md",
    "Task labels, packets, implementer summaries, and reviewer prompts do not replace it.": (
        "skills/code-review/SKILL.md"
    ),
    "solution correctness": "skills/design-integrity/SKILL.md",
    "`description` = trigger and routing contract.": "skills/harness-governance/references/skill-architecture.md",
    "references = mandatory purpose gates.": "skills/harness-governance/references/skill-architecture.md",
}
OWNER_ONLY_DOCTRINE_EXEMPTIONS = {
    "solution correctness": {
        "scripts/validate_harness.py",
        "tests/test_validate_harness.py",
    },
}
SOLUTION_CORRECTNESS_SCAN_PREFIXES = (
    "skills/",
    "adapters/",
)
SOLUTION_CORRECTNESS_SCAN_FILES = {
    "AGENTS.md",
}


class FrontmatterError(ValueError):
    pass


def _is_source_path_citation(line: str) -> bool:
    lowered = line.lower()
    if "source:" not in lowered and "source material:" not in lowered:
        return False
    return bool(re.search(r"`[^`]+(?:/[^`]+)+`", line))


def _iter_markdown(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)


def _validate_markdown_path(markdown_file: Path, root: Path, target: str) -> str | None:
    if "://" in target or target.startswith("#"):
        return None
    target_path = target.split("#", 1)[0]
    if not target_path:
        return None
    candidate = (markdown_file.parent / target_path).resolve()
    root_resolved = root.resolve()
    try:
        candidate.relative_to(root_resolved)
    except ValueError:
        return f"{markdown_file.relative_to(root)} reference escapes repo {target}"
    if not candidate.exists():
        return f"{markdown_file.relative_to(root)} broken reference {target}"
    return None


def _split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith(f"{FRONTMATTER_DELIMITER}\n"):
        raise FrontmatterError("frontmatter must start at byte zero")
    end = text.find(f"\n{FRONTMATTER_DELIMITER}\n", len(FRONTMATTER_DELIMITER) + 1)
    if end == -1:
        raise FrontmatterError("frontmatter missing closing delimiter")
    return text[len(FRONTMATTER_DELIMITER) + 1 : end], text[end + len(FRONTMATTER_DELIMITER) + 2 :]


def _parse_scalar(raw: str) -> tuple[object, str | None]:
    value = raw.strip()
    if not value:
        return "", None
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        quote = value[0]
        inner = value[1:-1]
        if quote == '"' and "\\" in inner:
            inner = bytes(inner, "utf-8").decode("unicode_escape")
        return inner, None
    lowered = value.lower()
    if lowered in {"true", "false"}:
        return lowered == "true", None
    if lowered in {"null", "~"}:
        return None, None
    if re.fullmatch(r"-?\d+", value):
        return int(value), None
    if re.fullmatch(r"-?\d+\.\d+", value):
        return float(value), None
    if ": " in value:
        return None, "plain scalar contains ': '; quote the value"
    if value.startswith(("{", "[", "-", "|", ">")):
        return None, "unsupported YAML value shape"
    return value, None


def _parse_simple_mapping(raw: str) -> tuple[dict[str, object], list[str]]:
    data: dict[str, object] = {}
    errors: list[str] = []
    lines = raw.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        line_number = index + 1
        index += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            errors.append(f"line {line_number}: nested YAML is not supported here")
            continue
        if ":" not in line:
            errors.append(f"line {line_number}: expected key: value")
            continue
        key, value_raw = line.split(":", 1)
        key = key.strip()
        if not key:
            errors.append(f"line {line_number}: empty key")
            continue
        if key in data:
            errors.append(f"line {line_number}: duplicate key {key!r}")
            continue
        value, error = _parse_scalar(value_raw)
        if error:
            errors.append(f"line {line_number}: {key}: {error}")
            continue
        data[key] = value
    return data, errors


def _parse_openai_yaml(raw: str) -> tuple[dict[str, object], list[str]]:
    data: dict[str, object] = {}
    errors: list[str] = []
    current_section: str | None = None
    lines = raw.splitlines()
    for line_number, line in enumerate(lines, start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0:
            if not line.endswith(":"):
                errors.append(f"line {line_number}: expected top-level section")
                current_section = None
                continue
            current_section = line[:-1].strip()
            if current_section in data:
                errors.append(f"line {line_number}: duplicate top-level key {current_section!r}")
            data[current_section] = {}
            continue
        if current_section is None:
            errors.append(f"line {line_number}: nested value without section")
            continue
        if current_section == "interface":
            if indent != 2 or ":" not in line:
                errors.append(f"line {line_number}: unsupported interface shape")
                continue
            key, value_raw = line.strip().split(":", 1)
            section = data[current_section]
            assert isinstance(section, dict)
            if key in section:
                errors.append(f"line {line_number}: duplicate interface key {key!r}")
                continue
            value, error = _parse_scalar(value_raw)
            if error:
                errors.append(f"line {line_number}: interface.{key}: {error}")
                continue
            section[key] = value
            continue
        if current_section in {"dependencies", "policy"}:
            continue
        errors.append(f"line {line_number}: unsupported section content under {current_section!r}")
    return data, errors


def _validate_skill_frontmatter(skill_dir: Path, skill_file: Path, root: Path) -> list[str]:
    errors: list[str] = []
    text = skill_file.read_text(encoding="utf-8")
    try:
        raw, _body = _split_frontmatter(text)
    except FrontmatterError as exc:
        return [f"{skill_file.relative_to(root)} invalid frontmatter: {exc}"]
    frontmatter, parse_errors = _parse_simple_mapping(raw)
    for error in parse_errors:
        errors.append(f"{skill_file.relative_to(root)} invalid frontmatter: {error}")
    allowed = {"name", "description"}
    for key in sorted(set(frontmatter) - allowed):
        errors.append(f"{skill_file.relative_to(root)} unexpected frontmatter key {key!r}")
    for key in ("name", "description"):
        if key not in frontmatter:
            errors.append(f"{skill_file.relative_to(root)} missing {key!r} in frontmatter")
    name = frontmatter.get("name")
    if name is not None:
        if not isinstance(name, str):
            errors.append(f"{skill_file.relative_to(root)} frontmatter 'name' must be a string")
        else:
            stripped = name.strip()
            if not stripped:
                errors.append(f"{skill_file.relative_to(root)} frontmatter 'name' must be non-empty")
            if len(stripped) > 64:
                errors.append(f"{skill_file.relative_to(root)} frontmatter 'name' exceeds 64 characters")
            if not SKILL_NAME_RE.fullmatch(stripped):
                errors.append(f"{skill_file.relative_to(root)} frontmatter 'name' must be hyphen-case")
            if stripped != skill_dir.name:
                errors.append(
                    f"{skill_file.relative_to(root)} frontmatter 'name' {stripped!r} does not match directory {skill_dir.name!r}"
                )
    description = frontmatter.get("description")
    if description is not None:
        if not isinstance(description, str):
            errors.append(f"{skill_file.relative_to(root)} frontmatter 'description' must be a string")
        else:
            stripped = description.strip()
            if not stripped:
                errors.append(f"{skill_file.relative_to(root)} frontmatter 'description' must be non-empty")
            if len(stripped) > 1024:
                errors.append(f"{skill_file.relative_to(root)} frontmatter 'description' exceeds 1024 characters")
            if "<" in stripped or ">" in stripped:
                errors.append(f"{skill_file.relative_to(root)} frontmatter 'description' cannot contain angle brackets")
    return errors


def _iter_skill_dirs(root: Path) -> list[Path]:
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        return []
    return sorted(path for path in skills_dir.iterdir() if path.is_dir())


def _validate_skill_markdown_layout(skill_dir: Path, root: Path) -> list[str]:
    allowed_roots = {"references", "assets", "examples", "evaluations", "agents"}
    errors: list[str] = []
    for markdown_file in sorted(skill_dir.rglob("*.md")):
        rel = markdown_file.relative_to(skill_dir)
        if rel.name == "SKILL.md" and len(rel.parts) == 1:
            continue
        if rel.parts[0] not in allowed_roots:
            errors.append(
                f"{markdown_file.relative_to(root)} should live under references/, assets/, examples/, or evaluations/"
            )
    return errors


def _openai_metadata_rows(root: Path) -> tuple[list[dict[str, str]], list[str]]:
    rows: list[dict[str, str]] = []
    errors: list[str] = []
    for skill_dir in _iter_skill_dirs(root):
        metadata_file = skill_dir / "agents" / "openai.yaml"
        if not metadata_file.is_file():
            continue
        text = metadata_file.read_text(encoding="utf-8")
        parsed, parse_errors = _parse_openai_yaml(text)
        rel = str(metadata_file.relative_to(root))
        for error in parse_errors:
            errors.append(f"{rel} invalid openai.yaml: {error}")
        for key in sorted(set(parsed) - OPENAI_ALLOWED_TOP_LEVEL_KEYS):
            errors.append(f"{rel} unsupported top-level key {key!r}")
        interface = parsed.get("interface")
        if not isinstance(interface, dict):
            errors.append(f"{rel} missing interface section")
            interface = {}
        for key in sorted(set(interface) - OPENAI_ALLOWED_INTERFACE_KEYS):
            errors.append(f"{rel} unsupported interface key {key!r}")
        required = ("display_name", "short_description", "default_prompt")
        for key in required:
            if key not in interface:
                errors.append(f"{rel} missing interface.{key}")
        display_name = interface.get("display_name", "")
        short_description = interface.get("short_description", "")
        default_prompt = interface.get("default_prompt", "")
        for key, value in (
            ("display_name", display_name),
            ("short_description", short_description),
            ("default_prompt", default_prompt),
        ):
            if not isinstance(value, str):
                errors.append(f"{rel} interface.{key} must be a string")
        if isinstance(short_description, str) and not (25 <= len(short_description) <= 64):
            errors.append(f"{rel} interface.short_description must be 25-64 characters")
        prompt_pattern = rf"(?<![A-Za-z0-9_-])\${re.escape(skill_dir.name)}(?![A-Za-z0-9_-])"
        if isinstance(default_prompt, str) and not re.search(prompt_pattern, default_prompt):
            errors.append(f"{rel} interface.default_prompt must mention ${skill_dir.name}")
        rows.append(
            {
                "skill": skill_dir.name,
                "path": rel,
                "display_name": display_name if isinstance(display_name, str) else "",
                "short_description": short_description if isinstance(short_description, str) else "",
                "default_prompt": default_prompt if isinstance(default_prompt, str) else "",
            }
        )
    return rows, errors


def _skill_name(skill_dir: Path) -> str:
    return skill_dir.name


def _validate_openai_metadata_coverage(root: Path) -> list[str]:
    errors: list[str] = []
    for skill_dir in _iter_skill_dirs(root):
        metadata_file = skill_dir / "agents" / "openai.yaml"
        if not metadata_file.is_file():
            errors.append(f"{skill_dir.relative_to(root)} missing agents/openai.yaml")
    return errors


def _validate_skill_references(root: Path) -> list[str]:
    errors: list[str] = []
    skill_names = {_skill_name(skill_dir) for skill_dir in _iter_skill_dirs(root)}
    text_files: list[Path] = []
    for path in root.rglob("*"):
        if (
            path.is_file()
            and path.suffix in {".md", ".yaml", ".yml", ".toml", ".txt"}
            and ".git" not in path.parts
        ):
            text_files.append(path)
    for path in sorted(set(text_files)):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in SKILL_TOKEN_RE.finditer(line):
                skill_name = match.group(1)
                if "-" not in skill_name and not re.search(rf"\bUse\s+`?\${re.escape(skill_name)}\b", line):
                    continue
                if skill_name not in skill_names:
                    errors.append(f"{rel}:{line_number} references missing skill ${skill_name}")
            for match in BACKTICK_SKILL_REF_RE.finditer(line):
                skill_name = match.group(1)
                if re.search(rf"\bdo not\s+use\s+`{re.escape(skill_name)}`", line, re.IGNORECASE):
                    continue
                if skill_name not in skill_names:
                    errors.append(f"{rel}:{line_number} references missing skill `{skill_name}`")
            for match in SKILL_PATH_RE.finditer(line):
                raw_path = match.group(1)
                skill_name = match.group(2)
                if _is_removed_path_scan_exempt(path, root) and raw_path in REMOVED_HARNESS_PATHS:
                    continue
                if skill_name not in skill_names:
                    errors.append(f"{rel}:{line_number} references missing skill path {raw_path}")
    return errors


def _iter_non_fenced_lines(text: str, start_line: int = 1) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    in_fence = False
    for line_number, line in enumerate(text.splitlines(), start=start_line):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append((line_number, line))
    return lines


def _validate_skill_body_contracts(root: Path) -> list[str]:
    errors: list[str] = []
    for skill_dir in _iter_skill_dirs(root):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            continue
        rel = skill_file.relative_to(root)
        text = skill_file.read_text(encoding="utf-8")
        try:
            _frontmatter, body = _split_frontmatter(text)
        except FrontmatterError:
            continue
        body_start_line = text[: text.index(body)].count("\n") + 1
        for pattern, label in SKILL_BODY_TRIGGER_PATTERNS:
            if pattern.search(body):
                errors.append(f"{rel} contains {label}; ordinary trigger text belongs in frontmatter description")
        if re.search(r"\boptional references?\b", body, re.IGNORECASE):
            errors.append(f"{rel} contains Optional Reference wording; references are mandatory purpose gates")

        if skill_dir.name not in STAGED_REFERENCE_GATE_SKILLS:
            continue
        for line_number, line in _iter_non_fenced_lines(body, body_start_line):
            if not SKILL_REFERENCE_PATH_RE.search(line):
                continue
            if REQUIRED_REFERENCE_GATE_RE.search(line):
                continue
            errors.append(
                f"{rel}:{line_number} has non-gated reference row in staged reference-gate skill; "
                "use `Read <reference> when/before/for ...`"
            )
    return errors


def _is_removed_path_scan_exempt(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    return rel in REMOVED_HARNESS_PATH_EXEMPTIONS


def _validate_removed_harness_paths(root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(root.rglob("*")):
        if (
            not path.is_file()
            or path.suffix not in {".md", ".yaml", ".yml", ".toml", ".txt"}
            or ".git" in path.parts
            or _is_removed_path_scan_exempt(path, root)
        ):
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)
        for removed_path in REMOVED_HARNESS_PATHS:
            if removed_path in text:
                errors.append(f"{rel} references removed harness path {removed_path}")
    return errors


def _validate_owner_only_doctrine(root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml", ".toml", ".txt"} or ".git" in path.parts:
            continue
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        normalized_text = " ".join(text.split())
        normalized_lower_text = normalized_text.lower()
        for phrase, owner in OWNER_ONLY_DOCTRINE.items():
            normalized_phrase = " ".join(phrase.split())
            exemptions = OWNER_ONLY_DOCTRINE_EXEMPTIONS.get(phrase, set())
            is_active_packet = (
                phrase == "solution correctness"
                and rel.startswith("docs-ai/current-work/")
                and rel.endswith("/wave-execution.md")
            )
            if phrase == "solution correctness":
                is_scanned_counterexample = rel in SOLUTION_CORRECTNESS_SCAN_FILES or rel.startswith(
                    SOLUTION_CORRECTNESS_SCAN_PREFIXES
                )
                if rel == owner and normalized_phrase not in normalized_lower_text:
                    errors.append(f"{rel} missing owner-only doctrine {phrase!r}")
                    continue
                if not is_scanned_counterexample:
                    continue
                has_phrase = normalized_phrase in normalized_lower_text
            else:
                has_phrase = normalized_phrase in normalized_text
            if rel != owner and rel not in exemptions and not is_active_packet and has_phrase:
                errors.append(f"{rel} duplicates owner-only doctrine {phrase!r}; owner is {owner}")
    return errors


def _validate_agents_instruction_map(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / "AGENTS.md"
    if not path.is_file():
        return errors
    text = path.read_text(encoding="utf-8")
    if "compact first-hop map" not in text:
        errors.append("AGENTS.md must describe project overlays as a compact first-hop map")
    routing = _markdown_section(text, "Routing")
    if not routing:
        errors.append("AGENTS.md missing ## Routing skill map")
        return errors
    skill_names = {_skill_name(skill_dir) for skill_dir in _iter_skill_dirs(root)}
    for match in BACKTICKED_SKILL_NAME_RE.finditer(routing):
        skill_name = match.group(1)
        if skill_name in REMOVED_WORKFLOW_SKILL_NAMES:
            errors.append(f"AGENTS.md routes to removed workflow skill {skill_name!r}")
        elif skill_name not in skill_names:
            errors.append(f"AGENTS.md routes to missing skill {skill_name!r}")
    return errors


def _parse_roles_markdown(root: Path) -> tuple[set[str], list[str]]:
    roles_path = root / "agents" / "roles.md"
    if not roles_path.is_file():
        return set(), ["agents/roles.md missing"]
    roles: set[str] = set()
    for line in roles_path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*- `([a-z0-9_]+)`:", line)
        if match:
            roles.add(match.group(1))
    if not roles:
        return roles, ["agents/roles.md defines no roles"]
    return roles, []


def _extract_preauthorized_roles(path: Path, root: Path) -> tuple[set[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    if PREAUTHORIZED_SUBAGENT_SENTINEL not in text:
        return set(), [f"{path.relative_to(root)} missing named preauthorized subagent allowlist"]
    start = text.index(PREAUTHORIZED_SUBAGENT_SENTINEL)
    end = text.find(PREAUTHORIZED_SUBAGENT_END, start)
    if end == -1:
        return set(), [f"{path.relative_to(root)} missing preauthorized subagent boundary text"]
    block = text[start:end]
    roles = set(re.findall(r"`([a-z0-9_]+)`", block))
    if not roles:
        return roles, [f"{path.relative_to(root)} preauthorized subagent allowlist is empty"]
    return roles, []


def _validate_subagent_allowlist(root: Path, roles: set[str]) -> list[str]:
    errors: list[str] = []
    if not roles:
        return errors
    agents_path = root / "AGENTS.md"
    if agents_path.is_file():
        preauthorized, source_errors = _extract_preauthorized_roles(agents_path, root)
        errors.extend(source_errors)
        if preauthorized and preauthorized != roles:
            errors.append(
                f"AGENTS.md preauthorized subagents {sorted(preauthorized)} "
                f"do not match agents/roles.md roles {sorted(roles)}"
            )
    metadata_path = root / "skills" / "subagent-orchestration" / "agents" / "openai.yaml"
    if metadata_path.is_file():
        metadata_text = metadata_path.read_text(encoding="utf-8")
        metadata_role_mentions = sorted(role for role in roles if role in metadata_text)
        if len(metadata_role_mentions) > 1:
            errors.append(
                "skills/subagent-orchestration/agents/openai.yaml must point to AGENTS.md "
                "and agents/roles.md instead of duplicating the preauthorized role list"
            )
        metadata_normalized = " ".join(metadata_text.split())
        for term in ("AGENTS.md", "agents/roles.md", "packet"):
            if term not in metadata_normalized:
                errors.append(f"skills/subagent-orchestration/agents/openai.yaml missing subagent metadata owner pointer {term!r}")
    subagent_path = root / "skills" / "subagent-orchestration" / "SKILL.md"
    if subagent_path.is_file():
        normalized_text = " ".join(subagent_path.read_text(encoding="utf-8").split())
        for term in (
            "AGENTS.md` owns the explicit user preauthorization allowlist",
            "standing user authorization",
            "Do not ask for additional delegation permission",
            "fresh-conversation authorization source",
            "Active Subagents",
            "same `implementer` until `quality_guard` approves",
            "Do not spawn a new subagent with a rephrased version of the same task",
            "Handoffs route attention; they are not authority",
            "Include authority sources when durable state exists",
            "agents/roles.md` owns harness role names and missions",
            "active packet path",
        ):
            if " ".join(term.split()) not in normalized_text:
                errors.append(f"skills/subagent-orchestration/SKILL.md missing subagent context contract term {term!r}")
    roles_path = root / "agents" / "roles.md"
    if roles_path.is_file():
        normalized_roles_text = " ".join(roles_path.read_text(encoding="utf-8").split())
        for term in (
            "standing user authorization",
            "fresh conversation",
            "must not wait for the user to mention subagents again",
        ):
            if term not in normalized_roles_text:
                errors.append(f"agents/roles.md missing subagent authorization term {term!r}")
        for stale_term in ("proof row", "proof rows"):
            if stale_term in normalized_roles_text:
                errors.append(f"agents/roles.md contains obsolete packet term {stale_term!r}")

    return errors


def _load_toml(path: Path, root: Path) -> tuple[dict[str, object], list[str]]:
    try:
        return tomllib.loads(path.read_text(encoding="utf-8")), []
    except tomllib.TOMLDecodeError as exc:
        return {}, [f"{path.relative_to(root)} invalid TOML: {exc}"]


def _validate_role_parity(root: Path) -> list[str]:
    errors: list[str] = []
    roles, role_errors = _parse_roles_markdown(root)
    errors.extend(role_errors)
    if not roles:
        return errors
    errors.extend(_validate_subagent_allowlist(root, roles))

    config_path = root / "adapters" / "codex" / "config.toml"
    config, config_errors = _load_toml(config_path, root) if config_path.is_file() else ({}, ["adapters/codex/config.toml missing"])
    errors.extend(config_errors)
    config_agents = config.get("agents", {})
    if not isinstance(config_agents, dict):
        errors.append("adapters/codex/config.toml missing [agents] table")
        config_agents = {}

    codex_agent_dir = root / "adapters" / "codex" / "agents"
    for role in sorted(roles):
        codex_filename = f"{role.replace('_', '-')}.toml"
        codex_agent_path = codex_agent_dir / codex_filename
        if role not in config_agents:
            errors.append(f"adapters/codex/config.toml missing agents.{role}")
        else:
            block = config_agents[role]
            if not isinstance(block, dict):
                errors.append(f"adapters/codex/config.toml agents.{role} must be a table")
            else:
                expected_config_file = f"agents/{codex_filename}"
                if block.get("config_file") != expected_config_file:
                    errors.append(
                        f"adapters/codex/config.toml agents.{role}.config_file must be {expected_config_file!r}"
                    )
                description = str(block.get("description", ""))
                for term in ("Standing AGENTS.md authorization applies", "do not ask the user again"):
                    if term not in description:
                        errors.append(f"adapters/codex/config.toml agents.{role}.description missing {term!r}")
        if not codex_agent_path.is_file():
            errors.append(f"missing Codex agent file {codex_agent_path.relative_to(root)}")
        else:
            agent_toml, agent_errors = _load_toml(codex_agent_path, root)
            errors.extend(agent_errors)
            if agent_toml and agent_toml.get("name") != role:
                errors.append(f"{codex_agent_path.relative_to(root)} name must be {role!r}")

    for role in sorted(set(config_agents) - roles):
        errors.append(f"adapters/codex/config.toml has unknown agents.{role}")
    for path in sorted(codex_agent_dir.glob("*.toml")):
        role = path.stem.replace("-", "_")
        if role not in roles:
            errors.append(f"{path.relative_to(root)} has no matching agents/roles.md role")
    return errors


def _resolved_symlink_target(path: Path) -> Path:
    target = path.readlink()
    if not target.is_absolute():
        target = path.parent / target
    return target.resolve(strict=False)


def _target_is_inside_root(target: Path, root: Path) -> bool:
    try:
        target.resolve(strict=False).relative_to(root.resolve())
    except ValueError:
        return False
    return True


def _validate_repo_codex_live_install(root: Path) -> list[str]:
    errors: list[str] = []
    codex_home = root / ".codex"
    if not codex_home.is_dir():
        return errors

    def require_symlink(relative_path: str, expected_target: Path) -> None:
        path = codex_home / relative_path
        if not path.is_symlink():
            errors.append(f".codex/{relative_path} is not a symlink to {expected_target.relative_to(root)}")
            return
        actual_target = _resolved_symlink_target(path)
        if actual_target != expected_target.resolve(strict=False):
            errors.append(
                f".codex/{relative_path} points to {actual_target}, expected {expected_target.resolve(strict=False)}"
            )

    require_symlink("AGENTS.md", root / "AGENTS.md")

    planned_skills = {
        path.name: path
        for path in sorted((root / "skills").iterdir())
        if path.is_dir()
    } if (root / "skills").is_dir() else {}
    planned_agents = {
        path.name: path
        for path in sorted((root / "adapters" / "codex" / "agents").glob("*.toml"))
    }

    for name, source in planned_skills.items():
        require_symlink(f"skills/{name}", source)
    for name, source in planned_agents.items():
        require_symlink(f"agents/{name}", source)

    for directory_name, planned_names in (
        ("skills", set(planned_skills)),
        ("agents", set(planned_agents)),
    ):
        directory = codex_home / directory_name
        if not directory.is_dir():
            errors.append(f".codex/{directory_name} is missing")
            continue
        for path in sorted(directory.iterdir()):
            if path.name == ".system" or not path.is_symlink():
                continue
            target = _resolved_symlink_target(path)
            if _target_is_inside_root(target, root) and path.name not in planned_names:
                errors.append(f"{path.relative_to(root)} is a stale harness symlink to {target}")

    source_config_path = root / "adapters" / "codex" / "config.toml"
    live_config_path = codex_home / "config.toml"
    if source_config_path.is_file():
        live_config, live_config_errors = (
            _load_toml(live_config_path, root)
            if live_config_path.is_file()
            else ({}, [".codex/config.toml missing"])
        )
        source_config, source_config_errors = _load_toml(source_config_path, root)
        errors.extend(live_config_errors)
        errors.extend(source_config_errors)
        source_agents = source_config.get("agents", {}) if isinstance(source_config, dict) else {}
        live_agents = live_config.get("agents", {}) if isinstance(live_config, dict) else {}
        if live_config and live_config.get("features", {}).get("multi_agent") is not True:
            errors.append(".codex/config.toml missing [features] multi_agent = true")
        if isinstance(source_agents, dict) and isinstance(live_agents, dict):
            for agent_name in sorted(REMOVED_CODEX_AGENT_NAMES):
                if agent_name in live_agents:
                    errors.append(f".codex/config.toml contains removed agents.{agent_name} block")
            for agent_name, source_block in source_agents.items():
                live_block = live_agents.get(agent_name)
                if live_block != source_block:
                    errors.append(f".codex/config.toml missing or changed agents.{agent_name} block")
        elif source_agents:
            errors.append(".codex/config.toml missing [agents] table")

    return errors


def _heading_names(text: str, level: int) -> set[str]:
    prefix = "#" * level
    return {
        match.group(1).strip()
        for match in re.finditer(rf"^{re.escape(prefix)}\s+(.+?)\s*$", text, re.MULTILINE)
    }


def _iter_json_fences(text: str) -> list[object]:
    values: list[object] = []
    for match in re.finditer(r"```json\s*\n(.*?)\n```", text, re.DOTALL):
        values.append(json.loads(match.group(1)))
    return values


def _markdown_section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return ""
    next_match = re.search(r"^##\s+", text[match.end() :], re.MULTILINE)
    if not next_match:
        return text[match.end() :]
    return text[match.end() : match.end() + next_match.start()]


def _markdown_subsection(text: str, heading: str) -> str:
    match = re.search(rf"^###\s+{re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return ""
    next_match = re.search(r"^###\s+", text[match.end() :], re.MULTILINE)
    if not next_match:
        return text[match.end() :]
    return text[match.end() : match.end() + next_match.start()]


def _task_card_sections(text: str) -> list[tuple[str, str]]:
    execution = _markdown_section(text, "Execution")
    cards: list[tuple[str, str]] = []
    matches = list(re.finditer(r"^###\s+(.+?)\s*$", execution, re.MULTILINE))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(execution)
        cards.append((match.group(1).strip(), execution[match.end() : end]))
    return cards


def _task_card_field_value(task_body: str, field: str) -> str | None:
    field_name = field.removeprefix("- ").removesuffix(":")
    match = re.search(
        rf"(?m)^-\s+{re.escape(field_name)}:[ \t]*(?:`([^`]+)`|([^\n`]*))?"
        rf"(?:\n\s+-\s*(?:`([^`]+)`|([^\n`]*)))?",
        task_body,
    )
    if not match:
        return None
    for group in match.groups():
        if group is not None and group.strip():
            return group.strip()
    return ""


def _packet_field_present(section_body: str, field: str) -> bool:
    return re.search(rf"(?m)^\s*-\s+{re.escape(field)}\s*:", section_body) is not None


def _validate_wave_packet(path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    headings = _heading_names(text, 2)
    for section in PACKET_REQUIRED_SECTIONS:
        if section not in headings:
            errors.append(f"{path.relative_to(root)} missing section {section!r}")
            continue
        section_body = _markdown_section(text, section)
        for field in PACKET_REQUIRED_FIELDS.get(section, ()):
            if not _packet_field_present(section_body, field):
                errors.append(f"{path.relative_to(root)} section {section!r} missing field {field!r}")
    for obsolete_section in ("Work Context", "Task Plan", "Execution State", "Required Gates", "Proof Plan"):
        if obsolete_section in headings:
            errors.append(f"{path.relative_to(root)} contains obsolete top-level section {obsolete_section!r}")
    try:
        _iter_json_fences(text)
    except json.JSONDecodeError as exc:
        errors.append(f"{path.relative_to(root)} invalid JSON proof fence: {exc}")
        return errors

    task_cards = _task_card_sections(text)
    for task_title, task_body in task_cards:
        state = _task_card_field_value(task_body, TASK_CARD_STATE_FIELD)
        if state is None:
            errors.append(f"{path.relative_to(root)} task card {task_title!r} missing state")
        elif state not in TASK_CARD_ALLOWED_STATES:
            errors.append(
                f"{path.relative_to(root)} task card {task_title!r} invalid state {state!r}; "
                f"expected one of {sorted(TASK_CARD_ALLOWED_STATES)}"
            )
        for field in (TASK_CARD_OWNED_SURFACES_FIELD, TASK_CARD_CHECKS_FIELD):
            if field not in task_body:
                errors.append(f"{path.relative_to(root)} task card {task_title!r} missing {field}")
    return errors


def _wave_status(brief_path: Path, root: Path) -> tuple[str | None, str | None]:
    text = brief_path.read_text(encoding="utf-8")
    match = re.search(r"^\*\*Status:\*\*\s*([a-z-]+)\s*$", text, re.MULTILINE)
    if not match:
        return None, f"{brief_path.relative_to(root)} missing **Status:**"
    status = match.group(1)
    if status not in WAVE_STATUSES:
        return status, f"{brief_path.relative_to(root)} invalid status {status!r}"
    return status, None


def _validate_wave_lifecycle(root: Path) -> list[str]:
    errors: list[str] = []
    docs_ai = root / "docs-ai"
    if not docs_ai.exists():
        return errors
    for packet_path in sorted((root / "docs-ai" / "current-work").glob("*/wave-execution*.md")):
        if packet_path.name not in {"wave-execution.md", "wave-execution.draft.md"}:
            continue
        errors.extend(_validate_wave_packet(packet_path, root))

    wave_ids: set[str] = set()
    brief_dir = root / "docs-ai" / "docs" / "initiatives" / "waves"
    if brief_dir.is_dir():
        wave_ids.update(path.stem for path in brief_dir.glob("*.md"))
    current_work = root / "docs-ai" / "current-work"
    if current_work.is_dir():
        for child in current_work.iterdir():
            if child.is_dir() and ((child / "wave-execution.md").exists() or (child / "wave-execution.draft.md").exists()):
                wave_ids.add(child.name)
    delivery_map = current_work / "delivery-map.md"
    delivery_map_wave_ids: set[str] = set()
    if delivery_map.is_file():
        map_text = delivery_map.read_text(encoding="utf-8")
        delivery_map_wave_ids.update(
            re.findall(r"docs-ai/docs/initiatives/waves/([A-Za-z0-9_-]+)\.md", map_text)
        )
        delivery_map_wave_ids.update(
            re.findall(r"\.\./docs/initiatives/waves/([A-Za-z0-9_-]+)\.md", map_text)
        )
        delivery_map_wave_ids.update(
            re.findall(r"docs-ai/current-work/([A-Za-z0-9_-]+)/wave-execution(?:\.draft)?\.md", map_text)
        )
        delivery_map_wave_ids.update(re.findall(r"^###\s+Wave\s+([A-Za-z0-9_-]+)\b", map_text, re.MULTILINE))
        wave_ids.update(delivery_map_wave_ids)

    for wave_id in sorted(wave_ids):
        brief_path = brief_dir / f"{wave_id}.md"
        canonical_packet = current_work / wave_id / "wave-execution.md"
        draft_packet = current_work / wave_id / "wave-execution.draft.md"
        if not brief_path.is_file():
            if canonical_packet.exists() or draft_packet.exists():
                errors.append(f"docs-ai/current-work/{wave_id} has packet but missing durable wave brief")
            continue
        status, status_error = _wave_status(brief_path, root)
        if status_error:
            errors.append(status_error)
            continue
        if status == "discovery-required" and canonical_packet.exists():
            errors.append(f"{brief_path.relative_to(root)} is discovery-required but canonical packet exists")
        if status == "execution-ready" and not canonical_packet.exists():
            errors.append(f"{brief_path.relative_to(root)} is execution-ready but canonical packet is missing")
        if status in {"done", "retired"} and (canonical_packet.exists() or draft_packet.exists()):
            errors.append(f"{brief_path.relative_to(root)} is {status} but current-work packet exists")
        if status in {"done", "retired"} and wave_id in delivery_map_wave_ids:
            errors.append(f"docs-ai/current-work/delivery-map.md lists {status} wave {wave_id}")
    return errors


def _validate_design_integrity_gate(root: Path) -> list[str]:
    errors: list[str] = []
    for relative_path in DESIGN_INTEGRITY_FILES:
        path = root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        normalized_text = " ".join(text.split())
        if re.search(r"\b[Ss]implicity lens\b", text):
            errors.append(f"{relative_path} must use design-integrity, not a simplicity lens")
        if "contract, state, lifecycle, or proof" in text:
            errors.append(f"{relative_path} has incomplete design-integrity definition; include design and workflow")
        if relative_path == "skills/design-integrity/SKILL.md":
            for term in (
                "deletion, collapse, rewrite, or replacement is the default design move",
                "requires justification against the simpler delete/rewrite option",
                "If implementation materially differs from the accepted design source",
                "Do not silently approve a different shape",
            ):
                if " ".join(term.split()) not in normalized_text:
                    errors.append(f"{relative_path} missing design-integrity authority term {term!r}")
    for relative_path in DESIGN_INTEGRITY_AGENT_FILES:
        path = root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if "design integrity" not in text.lower():
            errors.append(f"{relative_path} missing design-integrity gate")
        if "contract, state, lifecycle, or proof" in text:
            errors.append(f"{relative_path} has incomplete design-integrity definition; include design and workflow")
    return errors


def _validate_live_validation_contracts(root: Path) -> list[str]:
    errors: list[str] = []

    for relative_path in RUNTIME_EVIDENCE_ADAPTER_FILES:
        path = root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if "docs-ai/docs/" in text:
            errors.append(f"{relative_path} must not hard-code project-local docs-ai/docs/ paths")
        for term in RUNTIME_EVIDENCE_ADAPTER_REQUIRED_TERMS:
            if term not in text:
                errors.append(f"{relative_path} missing runtime evidence adapter term {term!r}")
        for line in text.splitlines():
            if ADVISORY_DRIFT_RE.search(line) and not ADVISORY_NEGATION_RE.search(line):
                errors.append(f"{relative_path} must not classify runtime evidence findings as advisory")
                break

    for relative_path in RUNTIME_PROOF_POLICY_FILES:
        path = root / relative_path
        if not path.is_file():
            errors.append(f"{relative_path} missing runtime proof policy owner")
            continue
        text = path.read_text(encoding="utf-8")
        required_terms = (
            "binding objective",
            "mis-scoped",
            "reject",
            "blocked",
            "live-use validation",
            "operator path",
            "beyond code inspection, tests, and review approval",
            "faithful entrypoint",
            "entrypoint fidelity",
        )
        for term in required_terms:
            if term not in text:
                errors.append(f"{relative_path} missing runtime proof policy term `{term}`")

    web_texts: list[str] = []
    for relative_path in WEB_BROWSER_PROOF_FILES:
        path = root / relative_path
        if path.is_file():
            web_texts.append(path.read_text(encoding="utf-8"))
    if web_texts:
        combined = "\n".join(web_texts)
        if "microsoft/playwright-cli" not in combined or "@playwright/cli" not in combined:
            errors.append(
                "skills/webapp-testing browser proof docs must identify Microsoft playwright-cli "
                "(`microsoft/playwright-cli`, `@playwright/cli`) as the one-shot channel"
            )

    scan_files = [
        root / "AGENTS.md",
        root / "agents" / "roles.md",
        root / "skills" / "subagent-orchestration" / "SKILL.md",
        root / "skills" / "runtime-proof" / "SKILL.md",
        root / "skills" / "readiness-claim" / "SKILL.md",
    ]
    for path in scan_files:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        normalized_text = " ".join(text.split())
        for phrase in LIVE_VALIDATION_STALE_PHRASES:
            if " ".join(phrase.split()) in normalized_text:
                errors.append(f"{path.relative_to(root)} contains stale optional-helper runtime proof wording")

    return errors


def _normalize_heading(raw: str) -> str:
    return raw.strip().rstrip("#").strip().lower()


def _backlog_field_value(text: str, field: str) -> str | None:
    match = re.search(
        rf"^\s*-\s+{re.escape(field)}(?:\s+\([^)]+\))?\s*:(?P<inline>.*)$",
        text,
        re.IGNORECASE | re.MULTILINE,
    )
    if match is None:
        return None
    value = match.group("inline").strip()
    if value:
        return value.removeprefix("`").removesuffix("`").strip()
    following = [line for line in text[match.end() :].splitlines() if line.strip()]
    if following and following[0].startswith("  "):
        return following[0].strip().removeprefix("`").removesuffix("`").strip()
    return None


def _is_backlog_placeholder(value: str) -> bool:
    stripped = value.strip()
    return stripped.startswith("<") and stripped.endswith(">")


def _has_backlog_field_value(text: str, field: str) -> bool:
    value = _backlog_field_value(text, field)
    if value is None:
        return False
    return bool(value) and not _is_backlog_placeholder(value)


def _validate_backlog_detail_contract(root: Path) -> list[str]:
    errors: list[str] = []
    backlog_root = root / "docs-ai/current-work/backlog"
    if not backlog_root.is_dir():
        return errors
    for path in sorted(backlog_root.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or not lines[0].startswith(BACKLOG_ENTRY_TITLE_PREFIX):
            errors.append(f"{path.relative_to(root)} missing {BACKLOG_ENTRY_TITLE_PREFIX!r} title")
        headings = {_normalize_heading(match.group(1)) for match in MARKDOWN_LEVEL_TWO_HEADING_PATTERN.finditer(text)}
        for heading in BACKLOG_REQUIRED_HEADINGS:
            if heading not in headings:
                errors.append(f"{path.relative_to(root)} missing backlog heading ## {heading.title()}")
        for field in BACKLOG_REQUIRED_FIELDS:
            if not _has_backlog_field_value(text, field):
                errors.append(f"{path.relative_to(root)} missing backlog field {field!r}")
        bucket = (_backlog_field_value(text, "bucket") or "").lower()
        if bucket and bucket not in BACKLOG_BUCKET_VALUES:
            errors.append(f"{path.relative_to(root)} has invalid backlog bucket {bucket!r}")
        if bucket == "accepted temporary debt":
            user_acceptance = (_backlog_field_value(text, "user acceptance") or "").lower()
            removal_condition = (_backlog_field_value(text, "removal condition") or "").lower()
            if user_acceptance in {"", "none", "n/a", "na"} or _is_backlog_placeholder(user_acceptance):
                errors.append(f"{path.relative_to(root)} accepted temporary debt missing user acceptance")
            if removal_condition in {"", "none", "n/a", "na"} or _is_backlog_placeholder(removal_condition):
                errors.append(f"{path.relative_to(root)} accepted temporary debt missing removal condition")
    return errors


def _validate_stale_accepted_debt_phrases(root: Path) -> list[str]:
    errors: list[str] = []
    scan_roots = [
        root / "skills",
        root / "adapters" / "codex" / "agents",
    ]
    for scan_root in scan_roots:
        if not scan_root.is_dir():
            continue
        for path in sorted(scan_root.rglob("*")):
            if path.suffix not in {".md", ".toml"}:
                continue
            normalized_text = " ".join(path.read_text(encoding="utf-8").split()).lower()
            for phrase in STALE_ACCEPTED_DEBT_PHRASES:
                if phrase in normalized_text:
                    errors.append(f"{path.relative_to(root)} contains stale accepted-debt wording")
                    break
    return errors


def write_openai_metadata_report(root: Path, report_path: Path) -> list[str]:
    rows, errors = _openai_metadata_rows(root)
    lines = ["skill\tpath\tdisplay_name\tshort_description\tdefault_prompt"]
    for row in rows:
        lines.append(
            "\t".join(
                row[key].replace("\t", " ").replace("\n", " ")
                for key in ("skill", "path", "display_name", "short_description", "default_prompt")
            )
        )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return errors


def _validate_provider_prompt_contracts(root: Path) -> list[str]:
    errors: list[str] = []
    for relative_path in PROVIDER_PROMPT_FILES:
        path = root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for skill_name in REMOVED_WORKFLOW_SKILL_NAMES:
            if skill_name in text:
                errors.append(f"{relative_path} references removed workflow skill {skill_name!r}")
        for line in text.splitlines():
            if ADVISORY_DRIFT_RE.search(line) and not ADVISORY_NEGATION_RE.search(line):
                errors.append(f"{relative_path} must not classify blocking evidence as advisory")
                break
    return errors


def _has_advisory_negation(lines: list[str], index: int) -> bool:
    window = " ".join(lines[max(0, index - 1) : min(len(lines), index + 2)])
    return ADVISORY_NEGATION_RE.search(window) is not None


def _has_non_blocking_allowance(lines: list[str], index: int) -> bool:
    window = " ".join(lines[max(0, index - 1) : min(len(lines), index + 2)])
    return NON_BLOCKING_ALLOWED_RE.search(window) is not None


def _required_gates_has_data_row(section: str) -> bool:
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        if stripped == REQUIRED_GATES_HEADER or re.fullmatch(r"\|(?:\s*-+\s*\|)+", stripped):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        unquoted_cells = [cell.removeprefix("`").removesuffix("`") for cell in cells]
        if (
            len(cells) == 6
            and all(cells)
            and not any(cell.startswith("<") and cell.endswith(">") for cell in unquoted_cells)
        ):
            return True
    return False


def _validate_required_gate_advisory_drift(root: Path) -> list[str]:
    errors: list[str] = []
    scan_roots = [
        root / "skills",
        root / "adapters" / "codex" / "agents",
    ]
    for scan_root in scan_roots:
        if not scan_root.is_dir():
            continue
        for path in sorted(scan_root.rglob("*")):
            if path.suffix not in {".md", ".toml"}:
                continue
            relative_path = str(path.relative_to(root))
            lines = path.read_text(encoding="utf-8").splitlines()
            for index, line in enumerate(lines):
                if not ADVISORY_DRIFT_RE.search(line):
                    continue
                if not REQUIRED_GATE_CONTEXT_RE.search(line):
                    continue
                if _has_advisory_negation(lines, index):
                    continue
                errors.append(f"{relative_path} must not classify required gate failures as advisory")
                break
            for index, line in enumerate(lines):
                if not NON_BLOCKING_DRIFT_RE.search(line):
                    continue
                if not REQUIRED_GATE_CONTEXT_RE.search(line):
                    continue
                if _has_non_blocking_allowance(lines, index):
                    continue
                errors.append(f"{relative_path} must not classify required gate failures as non-blocking")
                break
    return errors


def _validate_review_role_contracts(root: Path) -> list[str]:
    errors: list[str] = []
    for relative_path in REVIEW_VERDICT_FILES:
        path = root / relative_path
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            normalized_line = line.upper()
            is_verdict_line = "OVERALL" in normalized_line or "VERDICT" in normalized_line
            has_review_verdicts = "APPROVE" in normalized_line and "BLOCK" in normalized_line
            if is_verdict_line and has_review_verdicts and "NON-BLOCKING" in normalized_line:
                errors.append(f"{relative_path} uses stale NON-BLOCKING review verdict")
                break

    code_review = root / "skills" / "code-review" / "SKILL.md"
    if code_review.is_file():
        text = code_review.read_text(encoding="utf-8")
        normalized_text = " ".join(text.split())
        for term in CODE_REVIEW_OUTPUT_REQUIRED_TERMS:
            if " ".join(term.split()) not in normalized_text:
                errors.append(f"skills/code-review/SKILL.md missing review output term {term!r}")
        for term in REVIEW_GOVERNANCE_REQUIRED_TERMS:
            if " ".join(term.split()) not in normalized_text:
                errors.append(f"skills/code-review/SKILL.md missing review governance contract term {term!r}")
    for relative_path, required_terms in REVIEW_ROLE_CONTRACTS.items():
        path = root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        normalized_text = " ".join(text.split())
        normalized_lower_text = normalized_text.lower()
        for term in required_terms:
            if " ".join(term.split()) not in normalized_text:
                errors.append(f"{relative_path} missing review role contract term {term!r}")
        for term in REVIEW_TRIGGERED_OWNER_SKILL_TERMS:
            if " ".join(term.split()) not in normalized_text:
                errors.append(f"{relative_path} missing triggered owner skill review term {term!r}")
        for term in REVIEW_AUTHORITY_TERMS:
            if " ".join(term.lower().split()) not in normalized_lower_text:
                errors.append(f"{relative_path} missing review authority term {term!r}")
        if "quality-guard" in relative_path or "quality_guard" in relative_path:
            if not QUALITY_GUARD_FINAL_APPROVAL_NEGATION_RE.search(text):
                errors.append(f"{relative_path} missing quality_guard final-approval negation")
    return errors


def _validate_ui_approval_contract(root: Path) -> list[str]:
    errors: list[str] = []
    relative_path = "skills/user-apps-design/SKILL.md"
    path = root / relative_path
    if not path.is_file():
        return errors
    text = path.read_text(encoding="utf-8")
    normalized_text = " ".join(text.split())
    for term in DESIGN_CONTEXT_CONTRACT_REQUIRED_TERMS:
        if " ".join(term.split()) not in normalized_text:
            errors.append(f"{relative_path} missing UI approval context term {term!r}")
    for term in UI_APPROVAL_BOUNDARY_REQUIRED_TERMS:
        if " ".join(term.split()) not in normalized_text:
            errors.append(f"{relative_path} missing UI approval boundary term {term!r}")
    return errors


def _validate_role_boundary_contracts(root: Path) -> list[str]:
    errors: list[str] = []
    for relative_path, required_terms in ROLE_BOUNDARY_CONTRACTS.items():
        path = root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        normalized_text = " ".join(text.split())
        for term in required_terms:
            if " ".join(term.split()) not in normalized_text:
                errors.append(f"{relative_path} missing role boundary contract term {term!r}")
    for relative_path, required_terms in ADAPTER_HANDOFF_CONTEXT_CONTRACTS.items():
        path = root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        normalized_text = " ".join(text.split())
        for term in required_terms:
            if " ".join(term.split()) not in normalized_text:
                errors.append(f"{relative_path} missing adapter handoff context term {term!r}")
    return errors


def _validate_runtime_evidence_ui_default_contract(root: Path) -> list[str]:
    errors: list[str] = []
    stale_patterns = (
        "required `runtime_evidence` and `design_judge`",
        "matching `runtime_evidence` and `design_judge`",
        "runtime evidence or `design_judge` is missing",
    )
    checked_files = (
        "skills/user-apps-design/SKILL.md",
        "skills/runtime-proof/SKILL.md",
        "skills/readiness-claim/SKILL.md",
        "skills/code-review/SKILL.md",
        "adapters/codex/agents/quality-guard.toml",
        "adapters/codex/agents/final-reviewer.toml",
    )
    for relative_path in checked_files:
        path = root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        normalized_text = " ".join(text.split())
        for pattern in stale_patterns:
            if pattern in normalized_text:
                errors.append(
                    f"{relative_path} must not require runtime_evidence by default for broad UI design readiness"
                )
                break
    return errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        errors.append("missing skills/ directory")
    else:
        for skill_dir in _iter_skill_dirs(root):
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.is_file():
                errors.append(f"{skill_dir.relative_to(root)} missing SKILL.md")
                continue
            errors.extend(_validate_skill_frontmatter(skill_dir, skill_file, root))
            errors.extend(_validate_skill_markdown_layout(skill_dir, root))
            text = skill_file.read_text(encoding="utf-8")
            for folder in ("references", "assets", "scripts"):
                if folder in text and not (skill_dir / folder).exists():
                    errors.append(f"{skill_file.relative_to(root)} references missing {folder}/")
        errors.extend(_validate_openai_metadata_coverage(root))

    _rows, openai_errors = _openai_metadata_rows(root)
    errors.extend(openai_errors)
    errors.extend(_validate_skill_references(root))
    errors.extend(_validate_skill_body_contracts(root))
    errors.extend(_validate_removed_harness_paths(root))
    errors.extend(_validate_owner_only_doctrine(root))
    errors.extend(_validate_agents_instruction_map(root))
    errors.extend(_validate_role_parity(root))
    errors.extend(_validate_repo_codex_live_install(root))
    errors.extend(_validate_wave_lifecycle(root))
    errors.extend(_validate_backlog_detail_contract(root))
    errors.extend(_validate_design_integrity_gate(root))
    errors.extend(_validate_live_validation_contracts(root))
    errors.extend(_validate_provider_prompt_contracts(root))
    errors.extend(_validate_required_gate_advisory_drift(root))
    errors.extend(_validate_stale_accepted_debt_phrases(root))
    errors.extend(_validate_ui_approval_contract(root))
    errors.extend(_validate_review_role_contracts(root))
    errors.extend(_validate_role_boundary_contracts(root))
    errors.extend(_validate_runtime_evidence_ui_default_contract(root))

    for markdown_file in _iter_markdown(root):
        text = markdown_file.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if _is_source_path_citation(line):
                continue
            for match in FORBIDDEN_PROJECT_OWNER_PATH_RE.finditer(line):
                errors.append(
                    f"{markdown_file.relative_to(root)}:{line_number} forbidden project owner path {match.group(1)!r}"
                )
        for match in LINK_RE.finditer(text):
            if error := _validate_markdown_path(markdown_file, root, match.group(1)):
                errors.append(error)
        for match in INLINE_PATH_RE.finditer(text):
            if error := _validate_markdown_path(markdown_file, root, match.group(1)):
                errors.append(error)

    if (root / "docs").exists():
        errors.append("plugin-level docs/ directory is not allowed")

    return errors


def run_self_test() -> list[str]:
    errors: list[str] = []
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        (root / "skills" / "bad-skill").mkdir(parents=True)
        (root / "skills" / "bad-skill" / "SKILL.md").write_text("no frontmatter\n", encoding="utf-8")
        (root / "skills" / "missing-ref").mkdir(parents=True)
        (root / "skills" / "missing-ref" / "references").mkdir()
        (root / "skills" / "missing-ref" / "SKILL.md").write_text(
            "---\nname: missing-ref\ndescription: Missing reference test.\n---\n\nSee `references/foo.md`.\n",
            encoding="utf-8",
        )
        (root / "skills" / "bad-colon").mkdir(parents=True)
        (root / "skills" / "bad-colon" / "SKILL.md").write_text(
            "---\nname: bad-colon\ndescription: Bad colon: unquoted value.\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "missing-name").mkdir(parents=True)
        (root / "skills" / "missing-name" / "SKILL.md").write_text(
            "---\ndescription: Missing name.\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "missing-description").mkdir(parents=True)
        (root / "skills" / "missing-description" / "SKILL.md").write_text(
            "---\nname: missing-description\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "non-string-name").mkdir(parents=True)
        (root / "skills" / "non-string-name" / "SKILL.md").write_text(
            "---\nname: 42\ndescription: Numeric name.\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "non-string-description").mkdir(parents=True)
        (root / "skills" / "non-string-description" / "SKILL.md").write_text(
            "---\nname: non-string-description\ndescription: true\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "unexpected-key").mkdir(parents=True)
        (root / "skills" / "unexpected-key" / "SKILL.md").write_text(
            "---\nname: unexpected-key\ndescription: Extra key.\nmetadata: value\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "wrong-name").mkdir(parents=True)
        (root / "skills" / "wrong-name" / "SKILL.md").write_text(
            "---\nname: other-name\ndescription: Wrong name.\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "malformed").mkdir(parents=True)
        (root / "skills" / "malformed" / "SKILL.md").write_text(
            "---\nname: malformed\ndescription: No close.\n",
            encoding="utf-8",
        )
        (root / "skills" / "relative-missing").mkdir(parents=True)
        (root / "skills" / "relative-missing" / "SKILL.md").write_text(
            "---\nname: relative-missing\ndescription: Missing relative path.\n---\n\nSee `../missing/owner.md`.\n",
            encoding="utf-8",
        )
        (root / "skills" / "extensionless-missing").mkdir(parents=True)
        (root / "skills" / "extensionless-missing" / "SKILL.md").write_text(
            "---\nname: extensionless-missing\ndescription: Extensionless missing path.\n---\n\nSee `scripts/run`.\n",
            encoding="utf-8",
        )
        (root / "skills" / "escape-ref").mkdir(parents=True)
        (root / "outside.md").write_text("outside repo\n", encoding="utf-8")
        (root / "skills" / "escape-ref" / "SKILL.md").write_text(
            "---\nname: escape-ref\ndescription: Escaping relative path.\n---\n\nSee `../../../outside.md`.\n",
            encoding="utf-8",
        )
        (root / "skills" / "bare-escape").mkdir(parents=True)
        (root / "skills" / "bare-escape" / "SKILL.md").write_text(
            "---\nname: bare-escape\ndescription: Bare parent escape.\n---\n\nSee `../../../`.\n",
            encoding="utf-8",
        )
        (root / "skills" / "metadata-skill").mkdir(parents=True)
        (root / "skills" / "metadata-skill" / "SKILL.md").write_text(
            "---\nname: metadata-skill\ndescription: Metadata skill.\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "metadata-skill" / "agents").mkdir()
        (root / "skills" / "metadata-skill" / "agents" / "openai.yaml").write_text(
            'interface:\n  display_name: "Metadata Skill"\n  short_description: "Valid metadata skill helper"\n  default_prompt: "Use $wrong-skill to do metadata work."\n',
            encoding="utf-8",
        )
        (root / "skills" / "short-metadata").mkdir(parents=True)
        (root / "skills" / "short-metadata" / "SKILL.md").write_text(
            "---\nname: short-metadata\ndescription: Short metadata.\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "short-metadata" / "agents").mkdir()
        (root / "skills" / "short-metadata" / "agents" / "openai.yaml").write_text(
            'interface:\n  display_name: "Short Metadata"\n  short_description: "Too short"\n  default_prompt: "Use $short-metadata to do metadata work."\n',
            encoding="utf-8",
        )
        (root / "skills" / "uv").mkdir(parents=True)
        (root / "skills" / "uv" / "SKILL.md").write_text(
            "---\nname: uv\ndescription: Prefix collision metadata.\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "uv" / "agents").mkdir()
        (root / "skills" / "uv" / "agents" / "openai.yaml").write_text(
            'interface:\n  display_name: "uv"\n  short_description: "Manage Python workflows with uv"\n  default_prompt: "Use $uvicorn to do metadata work."\n',
            encoding="utf-8",
        )
        (root / "skills" / "loose-md").mkdir(parents=True)
        (root / "skills" / "loose-md" / "SKILL.md").write_text(
            "---\nname: loose-md\ndescription: Loose markdown.\n---\n",
            encoding="utf-8",
        )
        (root / "skills" / "loose-md" / "extra.md").write_text("loose markdown\n", encoding="utf-8")
        (root / "README.md").write_text("Harness fixture text\n", encoding="utf-8")
        (root / "OWNER.md").write_text("See `docs-ai/docs/conventions/review-governance.md`.\n", encoding="utf-8")
        (root / "agents").mkdir()
        (root / "agents" / "roles.md").write_text(
            "# Agent Roles\n\n- `explorer`: read-only discovery.\n- `quality_guard`: quality review.\n",
            encoding="utf-8",
        )
        (root / "adapters" / "codex" / "agents").mkdir(parents=True)
        (root / "adapters" / "codex" / "config.toml").write_text(
            '[features]\nmulti_agent = true\n\n[agents.explorer]\nconfig_file = "agents/explorer.toml"\n',
            encoding="utf-8",
        )
        (root / "adapters" / "codex" / "agents" / "explorer.toml").write_text(
            'name = "wrong_name"\n',
            encoding="utf-8",
        )
        invalid_packet = """# Wave invalid Execution Packet

## Work Context

## Task Plan

## Proof Plan

```json
{"proof_plan": [{"proof_id": "P1"}]}
```
"""
        (root / "docs-ai" / "docs" / "initiatives" / "waves").mkdir(parents=True)
        (root / "docs-ai" / "current-work" / "invalid").mkdir(parents=True)
        (root / "docs-ai" / "current-work" / "invalid" / "wave-execution.md").write_text(
            invalid_packet,
            encoding="utf-8",
        )
        (root / "docs-ai" / "docs" / "initiatives" / "waves" / "invalid.md").write_text(
            "# Wave invalid\n\n**Status:** discovery-required\n",
            encoding="utf-8",
        )
        (root / "docs-ai" / "docs" / "initiatives" / "waves" / "ready.md").write_text(
            "# Wave ready\n\n**Status:** execution-ready\n",
            encoding="utf-8",
        )
        (root / "docs-ai" / "docs" / "initiatives" / "waves" / "done.md").write_text(
            "# Wave done\n\n**Status:** done\n",
            encoding="utf-8",
        )
        (root / "docs-ai" / "current-work" / "done").mkdir(parents=True)
        (root / "docs-ai" / "current-work" / "done" / "wave-execution.draft.md").write_text(
            invalid_packet,
            encoding="utf-8",
        )
        (root / "docs-ai" / "current-work" / "delivery-map.md").write_text(
            "\n".join(
                [
                    "# Delivery Map (Waves + Backlog)",
                    "",
                    "- [invalid](../docs/initiatives/waves/invalid.md)",
                    "- [ready](../docs/initiatives/waves/ready.md)",
                    "- [done](../docs/initiatives/waves/done.md)",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        fixture_errors = validate(root)
        expected = (
            "frontmatter must start at byte zero",
            "missing agents/openai.yaml",
            "broken reference references/foo.md",
            "bad-colon/SKILL.md invalid frontmatter",
            "missing 'name' in frontmatter",
            "missing 'description' in frontmatter",
            "frontmatter 'name' must be a string",
            "frontmatter 'description' must be a string",
            "unexpected frontmatter key",
            "does not match directory",
            "frontmatter missing closing delimiter",
            "broken reference ../missing/owner.md",
            "broken reference scripts/run",
            "reference escapes repo ../../../outside.md",
            "reference escapes repo ../../../",
            "interface.default_prompt must mention $metadata-skill",
            "interface.short_description must be 25-64 characters",
            "interface.default_prompt must mention $uv",
            "loose-md/extra.md should live under references/",
            "OWNER.md:1 forbidden project owner path",
            "adapters/codex/config.toml missing agents.quality_guard",
            "explorer.toml name must be 'explorer'",
            "missing Codex agent file adapters/codex/agents/quality-guard.toml",
            "wave-execution.md missing section 'Readiness Claim'",
            "invalid.md is discovery-required but canonical packet exists",
            "ready.md is execution-ready but canonical packet is missing",
            "done.md is done but current-work packet exists",
            "delivery-map.md lists done wave done",
        )
        for marker in expected:
            if not any(marker in error for error in fixture_errors):
                errors.append(f"self-test did not reject {marker}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check-format", action="store_true")
    parser.add_argument("--openai-metadata-report", type=Path)
    args = parser.parse_args()

    errors = run_self_test() if args.self_test else validate(ROOT)
    if args.openai_metadata_report:
        errors.extend(write_openai_metadata_report(ROOT, args.openai_metadata_report))
    if args.check_format:
        errors.extend(validate(ROOT))
    if errors:
        for error in errors:
            print(error)
        return 1
    print("harness validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
