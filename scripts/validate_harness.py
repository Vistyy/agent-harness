from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_TERMS = (
    "Budgeat",
    "PriceHub",
    "R2",
    "OCR",
    "brochure",
    "grocery",
    "Poland",
    "Polish",
    "PLN",
    "Biedronka",
    "Lidl",
)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
INLINE_PATH_RE = re.compile(r"`((?:(?:references|assets|scripts)/|\.\./)[^`\s]+)`")
FORBIDDEN_PROJECT_OWNER_PATH_RE = re.compile(r"`(docs-ai/docs/conventions/[^`]+)`")
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
            text = skill_file.read_text(encoding="utf-8")
            for folder in ("references", "assets", "scripts"):
                if folder in text and not (skill_dir / folder).exists():
                    errors.append(f"{skill_file.relative_to(root)} references missing {folder}/")

    _rows, openai_errors = _openai_metadata_rows(root)
    errors.extend(openai_errors)

    for markdown_file in _iter_markdown(root):
        text = markdown_file.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if _is_source_path_citation(line):
                continue
            for match in FORBIDDEN_PROJECT_OWNER_PATH_RE.finditer(line):
                errors.append(
                    f"{markdown_file.relative_to(root)}:{line_number} forbidden project owner path {match.group(1)!r}"
                )
            for term in FORBIDDEN_TERMS:
                if term in line:
                    errors.append(
                        f"{markdown_file.relative_to(root)}:{line_number} forbidden project term {term!r}"
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
        (root / "README.md").write_text("Budgeat product fact\n", encoding="utf-8")
        (root / "SOURCE.md").write_text("source: Budgeat product fact without path\n", encoding="utf-8")
        (root / "CITATION.md").write_text("source: `docs-ai/docs/example.md` Budgeat source path\n", encoding="utf-8")
        (root / "OWNER.md").write_text("See `docs-ai/docs/conventions/review-governance.md`.\n", encoding="utf-8")
        fixture_errors = validate(root)
        expected = (
            "frontmatter must start at byte zero",
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
            "README.md:1 forbidden project term",
            "SOURCE.md:1 forbidden project term",
            "OWNER.md:1 forbidden project owner path",
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
