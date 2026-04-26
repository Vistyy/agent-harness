# Defense In Depth

One validation point is not enough. Different paths, refactors, mocks, and tests bypass single checks.

Goal: make bug structurally impossible.

## Layers

1. Entry validation
   Reject obviously invalid input at boundary.
2. Business validation
   Reject values that are invalid for operation semantics.
3. Environment guards
   Block dangerous operations in special contexts like tests or local tooling.
4. Debug instrumentation
   Capture context so failures are diagnosable when other layers miss.

## Why

- entry validation catches common bad input
- business validation catches semantic misuse
- environment guards catch context-specific damage
- instrumentation shortens forensic loop

## Workflow

When bug comes from invalid data:
1. trace data flow from source to failure
2. map every checkpoint bad value crosses
3. add validation at each relevant layer
4. test bypass paths, not only happy path

## Example Pattern

Bug:
- empty `projectDir` reached `git init`
- result: git repo initialized in wrong directory

Layered fix:
- entry: reject empty or missing directory
- business: reject missing project dir in workspace creation
- environment: in tests, refuse `git init` outside temp dirs
- instrumentation: log directory, cwd, stack before dangerous op

## Rule

Do not stop after first guard passes tests.
Keep adding barriers until bad state cannot reach dangerous operation through any supported path.
