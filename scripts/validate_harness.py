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
BACKLOG_REQUIRED_HEADINGS = ("metadata", "problem", "next action")
BACKLOG_REQUIRED_FIELDS = (
    "status",
    "owner",
    "bucket",
    "location",
)
BACKLOG_BUCKET_VALUES = ("discovered separate debt", "accepted temporary debt")
BACKLOG_ENTRY_TITLE_PREFIX = "# Backlog Entry:"


class FrontmatterError(ValueError):
    pass


def _iter_markdown(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and not _is_codex_backup(path)
    )


def _is_codex_backup(path: Path) -> bool:
    parts = path.parts
    return ".codex" in parts and "backups" in parts


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
            and not _is_codex_backup(path)
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
                if skill_name not in skill_names:
                    errors.append(f"{rel}:{line_number} references missing skill path {raw_path}")
    return errors


def _validate_agents_instruction_map(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / "AGENTS.md"
    if not path.is_file():
        return errors
    text = path.read_text(encoding="utf-8")
    routing = _markdown_section(text, "Routing")
    if not routing:
        return errors
    skill_names = {_skill_name(skill_dir) for skill_dir in _iter_skill_dirs(root)}
    for match in BACKTICKED_SKILL_NAME_RE.finditer(routing):
        skill_name = match.group(1)
        if skill_name not in skill_names:
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
                errors.append(f"{path.relative_to(root)} is an unplanned overlay symlink to {target}")

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
            for agent_name in sorted(set(live_agents) - set(source_agents)):
                errors.append(f".codex/config.toml contains unknown agents.{agent_name} block")
            for agent_name, source_block in source_agents.items():
                live_block = live_agents.get(agent_name)
                if live_block != source_block:
                    errors.append(f".codex/config.toml missing or changed agents.{agent_name} block")
        elif source_agents:
            errors.append(".codex/config.toml missing [agents] table")

    return errors


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


def _validate_context_note(path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    try:
        _iter_json_fences(text)
    except json.JSONDecodeError as exc:
        errors.append(f"{path.relative_to(root)} invalid JSON proof fence: {exc}")
        return errors
    return errors


def _validate_memory_lifecycle(root: Path) -> list[str]:
    errors: list[str] = []
    docs_ai = root / "docs-ai"
    if not docs_ai.exists():
        return errors
    for context_path in sorted((root / "docs-ai" / "current-work" / "active").glob("*/active-work-note*.md")):
        if context_path.name not in {"active-work-note.md", "active-work-note.draft.md"}:
            continue
        errors.extend(_validate_context_note(context_path, root))

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
                if f"{folder}/" in text and not (skill_dir / folder).exists():
                    errors.append(f"{skill_file.relative_to(root)} references missing {folder}/")
        errors.extend(_validate_openai_metadata_coverage(root))

    _rows, openai_errors = _openai_metadata_rows(root)
    errors.extend(openai_errors)
    errors.extend(_validate_skill_references(root))
    errors.extend(_validate_agents_instruction_map(root))
    errors.extend(_validate_role_parity(root))
    errors.extend(_validate_repo_codex_live_install(root))
    errors.extend(_validate_memory_lifecycle(root))
    errors.extend(_validate_backlog_detail_contract(root))

    for markdown_file in _iter_markdown(root):
        text = markdown_file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            if error := _validate_markdown_path(markdown_file, root, match.group(1)):
                errors.append(error)
        for match in INLINE_PATH_RE.finditer(text):
            if error := _validate_markdown_path(markdown_file, root, match.group(1)):
                errors.append(error)

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
        invalid_context = """# Work Note invalid Context Note

```json
{"proof_plan": [}
```
"""
        (root / "docs-ai" / "current-work" / "work-notes").mkdir(parents=True)
        (root / "docs-ai" / "current-work" / "active" / "invalid").mkdir(parents=True)
        (root / "docs-ai" / "current-work" / "active" / "invalid" / "active-work-note.md").write_text(
            invalid_context,
            encoding="utf-8",
        )
        (root / "docs-ai" / "current-work" / "work-notes" / "invalid.md").write_text(
            "# Work Note invalid\n",
            encoding="utf-8",
        )
        (root / "docs-ai" / "current-work" / "work-notes" / "ready.md").write_text(
            "# Work Note ready\n",
            encoding="utf-8",
        )
        (root / "docs-ai" / "current-work" / "work-notes" / "done.md").write_text(
            "# Work Note done\n",
            encoding="utf-8",
        )
        (root / "docs-ai" / "current-work" / "active" / "done").mkdir(parents=True)
        (root / "docs-ai" / "current-work" / "active" / "done" / "active-work-note.draft.md").write_text(
            invalid_context,
            encoding="utf-8",
        )
        (root / "docs-ai" / "current-work" / "delivery-map.md").write_text(
            "\n".join(
                [
                    "# Delivery Map",
                    "",
                    "- [invalid](work-notes/invalid.md)",
                    "- [ready](work-notes/ready.md)",
                    "- [done](work-notes/done.md)",
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
            "invalid JSON proof fence",
            "adapters/codex/config.toml missing agents.quality_guard",
            "explorer.toml name must be 'explorer'",
            "missing Codex agent file adapters/codex/agents/quality-guard.toml",
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
