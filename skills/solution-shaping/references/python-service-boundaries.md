# Python Service Boundaries

Use when the touched owner is a Python service, unit of work, repository,
handler, or dynamic input boundary.

- One boundary owns transaction lifecycle, request context, and persistence
  dispatch.
- Handlers own focused orchestration; do not preserve monolith facades just to
  avoid choosing a service interface.
- Repository construction stays explicit at the handler/unit-of-work boundary.
- Raw dynamic input is modeled once at the first trust boundary and leaves as a
  typed object or typed failure.
- `Any`, `object`, broad dict/list shapes, and casts are temporary inside that
  boundary only.
- Framework casts stay in adapters; business logic receives real contracts.

If a service owns transaction lifecycle, repository choreography, mapping,
workflow policy, and error translation at once, recheck interface depth.
