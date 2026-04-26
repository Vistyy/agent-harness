# Python Package Setup

Use this reference when shaping Python package and workspace setup in a `uv`
project.

## Layout

- Keep reusable library code, application/service entry points, provider or
  plugin packages, tests, and operational scripts in explicit top-level
  ownership areas.
- Treat scripts as first-class Python modules when static analysis includes
  them.
- Do not let operational helpers become an untyped bypass around package
  boundaries.

## uv Workspace

- Use `uv.toml` or `pyproject.toml` workspace configuration when multiple
  Python packages are developed together.
- Keep dev tooling shared when it must run consistently across packages.
- Keep runtime dependencies package-scoped.
- Prefer editable installs for local development and CI unless release
  packaging needs a different mode.
- Run quality, test, and tooling flows through `uv run` so local and CI
  environments use the locked dependency graph.

## `pyproject.toml` Rules

- Declare supported Python versions explicitly.
- Keep package dependencies minimal and owned by the package that imports them.
- Keep lint, format, and type-check configuration where `uv run` can discover
  it without command-specific path hacks.
- Register plugin/provider entry points in the package that provides them.
- Do not import optional providers directly from orchestration code; resolve
  declared entry points at startup when a plugin model is required.

## Verification Posture

- Use project quality wrappers when present; otherwise run the relevant
  formatter, linter, type checker, and tests through `uv run`.
- Package or provider changes should preserve format, lint, type, import
  boundary, and relevant unit/contract/integration coverage.
- Merge readiness requires the owning quality gate to be green.

## Provider Wiring Checklist

1. Add the provider package with its own `pyproject.toml` and entry-point
   declaration.
2. Import shared contracts from the contract package, not from core
   implementation modules.
3. Register a stable provider identifier and route aliases through explicit
   startup configuration.
4. Extend contract or integration tests for provider-specific behavior.
