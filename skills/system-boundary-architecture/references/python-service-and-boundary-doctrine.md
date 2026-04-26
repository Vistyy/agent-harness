# Python Service And Boundary Doctrine

Own intended long-term Python application-service shape.

Goal: backend slices stop inferring architecture from whichever service hotspot
landed first.

## Target Shape

- application slices use a shared application unit-of-work boundary with
  explicit read and write operations
- unit of work owns transaction lifecycle, dispatch strategy for persistence,
  and request user-context binding
- handlers own bounded orchestration and repository choreography
- repository construction stays explicit at the handler boundary from the
  unit-of-work connection or context
- persistence failure translation stays in the handler that knows the operation
  label

## Rules

- do not let one hotspot own raw transactions, request-context binding,
  repository construction, mapping, and multi-branch workflow logic when
  focused handlers are possible
- keep a shared unit-of-work boundary generic
- do not turn it into a slice-specific service locator or repository bundle
- keep context surfaces small and explicit
- routes and dependency providers should teach focused handler shape directly,
  not preserve monolith facades

## Typing Integrity

- model the contract once at the first trust boundary; dynamic input leaves that
  function as a real typed object or a typed failure
- `cast()`, `Any`, and `object` are allowed only transiently inside that
  boundary function
- do not repeat casts along one data path
- do not use `dict[str, object]`, `list[object]`, `Callable[..., object]`, a
  widened concrete model type, or a broad base model superclass as a substitute
  for a known shape
- helpers and support code must return the same contract callers use; no
  widen-then-re-narrow
- do not cast a strict contract back to an optional or broader type only to
  preserve legacy fallback behavior
- use the exact imported protocol, model, request type, result type, or config
  model when it already exists
- local `TypedDict` and `Protocol` types are allowed only when they model a real
  runtime boundary shape
- private helpers and underscore members are not public seams
- when a payload shape is known, validate raw values into a real adapter or
  model instead of cast-driven dictionary or list indexing
- `cast(object, ...)` is not an allowed bridge into a validator or parser;
  validate the raw value directly or introduce a real adapter type
- framework-seam casts stay in adapter code that owns the dynamic boundary;
  business logic must not carry them

For boundary-tightening review and proof requirements, use review and testing
doctrine. This reference owns service shape and typing integrity posture.
