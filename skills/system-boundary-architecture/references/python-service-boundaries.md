# Python Service Boundaries

Own Python application-service, unit-of-work, repository, dynamic-input, and
typing boundaries.

## Service Shape

- application slices use a shared unit-of-work boundary with explicit read and
  write operations
- unit of work owns transaction lifecycle, persistence dispatch strategy, and
  request user-context binding
- handlers own bounded orchestration and repository choreography
- repository construction stays explicit at the handler boundary from the
  unit-of-work connection or context
- persistence failure translation stays with the handler that knows the
  operation label
- do not let one hotspot own raw transactions, request-context binding,
  repository construction, mapping, and multi-branch workflow logic when
  focused handlers are possible
- do not turn a shared unit of work into a slice-specific service locator or
  repository bundle
- routes and dependency providers should teach focused handler shape directly,
  not preserve monolith facades

## Typing Integrity

- model dynamic input once at the first trust boundary; it leaves as a real
  typed object or typed failure
- `cast()`, `Any`, and `object` are transient only inside that boundary
  function
- do not repeat casts along one data path
- do not use `dict[str, object]`, `list[object]`, `Callable[..., object]`, a
  widened concrete model type, or a broad base model superclass as a substitute
  for a known shape
- helpers return the same contract callers use; no widen-then-re-narrow
- do not cast a strict contract back to optional or broader type only to
  preserve legacy fallback behavior
- local `TypedDict` and `Protocol` types are allowed only when they model a real
  runtime boundary shape
- private helpers and underscore members are not public seams
- validate raw values into a real adapter or model instead of cast-driven
  dictionary or list indexing
- framework-seam casts stay in adapter code; business logic must not carry them
