---
name: uv
description: Use for Python command execution, dependencies, or tooling in uv-managed projects; prefer project just commands first, otherwise use uv instead of raw python, pip, pytest, or manual virtualenvs.
---

# uv

Runs Python work through `uv` in uv-managed projects.

## Detect

uv-managed indicators: `pyproject.toml`, `uv.lock`, or uv-generated
requirements. Do not switch Poetry or PDM projects to uv.

## Rule

Prefer project owner commands first, especially `just ...` recipes that already
wrap uv. Otherwise run Python tools through `uv`.

In uv projects, do not use raw:
- `python`
- `python -m pytest`
- `pytest`
- `pip`
- manual virtualenv activation

Use:
- `uv run python ...`
- `uv run pytest`
- `uv run ruff check`
- `uv sync`
- `uv add <pkg>`
- `uv remove <pkg>`

## Scripts And Tools

- standalone script: `uv run script.py`
- script with transient dependency: `uv run --with requests script.py`
- trusted one-off tool: `uvx ruff`

Use `uvx` only for trusted external tool packages. Use `uv tool install` only
when the user explicitly asks.

## Legacy Pip Interface

Use only when the project is clearly legacy and no uv-managed path exists:

```bash
uv venv
uv pip install -r requirements.txt
uv pip compile requirements.in -o requirements.txt
uv pip sync requirements.txt
```

## Package Layout

Read `references/python-package-setup.md` only when shaping Python package,
workspace, dependency, lint, format, type-check, or test layout.

Official docs: `https://docs.astral.sh/uv/llms.txt`
