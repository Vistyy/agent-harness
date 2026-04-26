quality:
    uv run python scripts/validate_harness.py

quality-fast:
    uv run python scripts/validate_harness.py

fmt:
    uv run python scripts/validate_harness.py --check-format

status:
    git status --short
