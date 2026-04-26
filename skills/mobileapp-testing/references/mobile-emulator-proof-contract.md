# Mobile Emulator Parallel Runtime Contract

## Purpose

Define the durable guardrails for the parallel-emulator exception path in the
engineering harness.

Run-specific evidence, troubleshooting, and host-local recovery details belong
in `docs-ai/current-work/**` or `.artifacts/runtime/**`, not here.

## Exception-Path Posture

- Prefer the repository-managed single-emulator path by default.
- Use the parallel-emulator path only when the task materially requires two
  Android instances at once.
- Keep emulator targeting explicit, ports deterministic, and emulator state
  read-only.
- Prefer direct Windows SDK binary invocation from WSL when that exception path
  is required.

## Guardrails

- Never rely on ambiguous emulator targeting.
- Avoid host-specific wrapper layers that hide the actual emulator/adb target.
- Prefer deterministic install/launch flows over concurrent ad-hoc dev sessions
  when collecting runtime proof.
- Treat host/skin-specific recovery steps as execution-local and non-durable.

## Instability Boundaries

Parallel-emulator work remains an exception path because three instability
classes can still appear:
- targeting ambiguity when emulator selection is not explicit,
- host-specific Windows/WSL toolchain friction,
- session-state volatility in adb, emulator trust posture, or app launch state.

These are execution concerns to prove in the current run, not durable truth to
archive here.