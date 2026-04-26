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
FRONTMATTER_RE = re.compile(r"^---\nname: .+\ndescription: .+\n---\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
INLINE_PATH_RE = re.compile(r"`((?:references|assets|scripts)/[^`]+)`")


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
    if not (markdown_file.parent / target_path).exists():
        return f"{markdown_file.relative_to(root)} broken reference {target}"
    return None


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        errors.append("missing skills/ directory")
    else:
        for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.is_file():
                errors.append(f"{skill_dir.relative_to(root)} missing SKILL.md")
                continue
            text = skill_file.read_text(encoding="utf-8")
            if not FRONTMATTER_RE.match(text):
                errors.append(f"{skill_file.relative_to(root)} missing required frontmatter")
            for folder in ("references", "assets", "scripts"):
                if folder in text and not (skill_dir / folder).exists():
                    errors.append(f"{skill_file.relative_to(root)} references missing {folder}/")

    for markdown_file in _iter_markdown(root):
        text = markdown_file.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if _is_source_path_citation(line):
                continue
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
        (root / "README.md").write_text("Budgeat product fact\n", encoding="utf-8")
        (root / "SOURCE.md").write_text("source: Budgeat product fact without path\n", encoding="utf-8")
        (root / "CITATION.md").write_text("source: `docs-ai/docs/example.md` Budgeat source path\n", encoding="utf-8")
        fixture_errors = validate(root)
        expected = (
            "missing required frontmatter",
            "broken reference references/foo.md",
            "README.md:1 forbidden project term",
            "SOURCE.md:1 forbidden project term",
        )
        for marker in expected:
            if not any(marker in error for error in fixture_errors):
                errors.append(f"self-test did not reject {marker}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check-format", action="store_true")
    args = parser.parse_args()

    errors = run_self_test() if args.self_test else validate(ROOT)
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
