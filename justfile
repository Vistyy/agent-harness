quality:
    uv run python scripts/validate_harness.py --self-test
    uv run python scripts/validate_harness.py
    uv run python scripts/codex_install_smoke.py

quality-fast:
    uv run python scripts/validate_harness.py --self-test
    uv run python scripts/validate_harness.py
    uv run python scripts/codex_install_smoke.py

fmt:
    uv run python scripts/validate_harness.py --check-format

status:
    git status --short
