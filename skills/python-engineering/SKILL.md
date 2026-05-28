---
name: python-engineering
description: "Handle Python runtime and typing semantics that static checks cannot fully prove: dynamic trust boundaries, exception chaining and cancellation, async/resource lifetime, Decimal/time/config/import pitfalls, dataclass mutability, and framework or SQL/JSON mapping edges. Use when changing, reviewing, or diagnosing Python code that touches these runtime or adapter semantics. Use this skill for Python-specific traps only; it does not own command routing, generic architecture, product behavior, proof selection, testing doctrine, or general structural review."
---

# Python Engineering

Owns Python-specific runtime and typing traps after this skill is selected.
Do not use it as a generic clean-code checklist.

## Contract

- Read project `AGENTS.md`, Python tooling config, and owner docs for the
  touched code. Project architecture wins over generic Python preference.
- Use `../just-recipe-routing/SKILL.md` and `../uv/SKILL.md` for commands.
  Use `../testing-best-practices/SKILL.md` when tests are touched, and
  `../systematic-debugging/SKILL.md` for symptoms or failing checks.
- For non-trivial Python work, let `../solution-shaping/SKILL.md` own the
  objective shape and current-scope disposition. This skill supplies Python
  semantics inside that shape.
- Treat Ruff, basedpyright/pyright, ty, and import checks as mechanical aid.
  Passing them does not prove runtime validation, cancellation, resource
  lifetime, Decimal rounding, clock behavior, import side effects, or adapter
  mapping correctness.

## Dynamic Boundaries

- Type hints do not validate runtime data. Raw JSON, SQL rows, environment
  values, forms, CLI args, subprocess output, third-party payloads, and
  framework objects must be decoded once at the trust boundary into an owned
  value, typed failure, or explicit contract.
- `cast(...)`, `Any`, `object`, `dict[str, object]`, and untyped containers are
  local escape hatches. Keep them inside the boundary that has the runtime
  evidence; do not let them become normal application or domain contracts.
- Prefer project-standard validators/mappers. Add `TypedDict`, dataclasses,
  Pydantic models, protocols, or enums only when they describe a real boundary;
  do not create pass-through types just to quiet the checker.
- SQLAlchemy, Pydantic/FastAPI, and JSON adapters should convert row/model
  shape at the adapter edge. Business logic should receive Python values with
  stable invariants, not framework objects or row tuples.

## Exceptions And Cancellation

- Python exception structure matters. Preserve cause with `raise ... from exc`
  when wrapping. Use `raise ... from None` only at a boundary where hiding the
  implementation detail is intentional and the caller still gets useful
  context.
- Catch the narrow exception that owns the recovery path. A broad catch is
  acceptable only at runtime, worker, CLI, cleanup, rollback, or framework
  boundaries with explicit translation, retry, cleanup, logging, or failure
  mapping.
- Do not catch `BaseException` except at process/runtime shutdown boundaries.
  Do not swallow `KeyboardInterrupt`, `SystemExit`, or `asyncio.CancelledError`.
- In async code, cancellation is part of control flow. Do not convert
  cancellation into success, retry, warning-only logs, or generic error
  results unless the runtime owner explicitly requires that policy.

## Async And Resources

- Every `asyncio.create_task`, background task registry, `gather`, timeout,
  queue, lock, client, session, or connection needs an owner for lifetime,
  cancellation, shutdown, and exception observation.
- Be suspicious of `gather(return_exceptions=True)`: each returned exception
  must be classified, surfaced, or intentionally ignored by the owner.
- Use context managers for files, temp paths, locks, transactions, network
  clients, and other resources. Cleanup may suppress only the exact cleanup
  failures it owns.
- Keep DB transaction scope explicit. Do not let helper functions commit,
  rollback, or open sessions unless they own the lifecycle by project
  convention.

## Time, Money, Config, Imports

- Use timezone-aware UTC for timestamps and monotonic clocks for durations,
  deadlines, retries, and performance timings. Inject clocks when business
  decisions or tests depend on time.
- For `Decimal`, parse from strings, integers, or already-exact values. Never
  create money or price decimals from binary floats. Put rounding and
  quantization at the owner that defines the business rule.
- Parse environment/config once into owned settings. Avoid scattered
  `os.environ`, import-time config parsing, and hidden defaults outside the
  project settings owner.
- Avoid import-time side effects: network calls, DB connections, env-dependent
  behavior, logging setup, file writes, or task creation. Keep module import
  safe for tests, tooling, CLIs, and workers.

## Python Data Model

- For dataclasses and mutable fields, use `default_factory` and decide
  deliberately on `frozen`, `slots`, equality, ordering, and hashing. Do not
  let generated methods define identity accidentally.
- Use `Enum`, `Literal`, and closed sets when Python code must reject unknown
  states. Do not normalize arbitrary strings repeatedly across layers.
- Prefer explicit `Path` and bytes/text boundaries. Do not mix raw strings,
  implicit encodings, and path operations when the owner needs filesystem
  correctness.

## Audit Output

For Python-specific audits, report only findings this skill owns:

`<owner/path>: <python trap> -> <runtime impact>; disposition=<fix-now|future|debt|no-change|blocker>; proof=<command/test/review path>`

Route generic architecture, simplicity, ownership, and test-quality findings to
their owner skills instead of restating them here.
