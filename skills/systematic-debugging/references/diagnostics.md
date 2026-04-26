# Diagnostics And Structured Logging

Generic diagnostics contract for debugging and runtime evidence. Project
overlays own service-specific event names, provider fields, runtime recipes, and
artifact paths.

## Logging Pattern

Bind stable context once. Emit structured lifecycle events after.

```python
from loguru import logger

log = logger.bind(
    trace_id=trace_id,
    correlation_id=correlation_id,
    service=service_name,
    env=env,
)

log.info("operation.start", stage="worker", status="start")
# ... do work ...
log.info("operation.done", stage="worker", status="done")
```

Services bind request context fields. Minimum:

- `service`
- `env`
- `correlation_id`

## Event Naming

Pattern: `{component}.{action}`.

Reserved generic lifecycle events:

| Event | When |
| --- | --- |
| `request.completed` | request finished, success or error |
| `operation.start` | operation begins |
| `operation.done` | operation succeeds |
| `operation.error` | operation fails |
| `operation.cancelled` | async operation cancelled |

Project overlays may define domain-specific component names, but reusable
harness guidance should not require them.

## Bound Context Fields

| Field | Meaning |
| --- | --- |
| `trace_id` | distributed trace identifier |
| `correlation_id` | operator-facing request identifier |
| `service` | logical service name |
| `env` | environment name |
| `host` | host identity when available |
| `git_sha` | deployed git SHA when available |
| `image_tag` | deployed image tag when available |
| `image_digest` | deployed image digest when available |
| `stage` | current processing stage |
| `status` | event status like `start`, `done`, `error`, `cancelled` |
| `duration_ms` | elapsed milliseconds |

## Correlation Identifiers

- `correlation_id` is request-scoped operator identifier.
- `trace_id` is distributed trace identifier from tracing context.
- They are intentionally different. Never derive one from the other.

### HTTP Request Correlation

HTTP services should use header-only correlation.

- header: `X-Correlation-ID` case-insensitive
- allowed inbound chars: `[A-Za-z0-9._-]`
- allowed inbound length: `1..64`
- if inbound header is missing or invalid, generate new `correlation_id`
- echo resolved `X-Correlation-ID` on every response, success and error
- body payloads do not own `correlation_id` in HTTP contract

### Propagation Rules

- HTTP inbound: continue or start trace context and resolve `correlation_id`
- HTTP outbound: propagate trace headers and `X-Correlation-ID`
- async or background boundaries without HTTP headers: propagate trace context
  and pass `correlation_id` explicitly
- library and provider boundaries: caller supplies correlation context;
  libraries and providers must not mint `correlation_id` and must not configure
  global logging or exporter sinks

## Error Events

Required:

- same identifiers as owning event category
- stable machine-usable `error_code`

Do not log:

- sensitive exception messages
- raw payloads
- unbounded `error_reason` strings

Keep `error_reason` sanitized and bounded.

## Redaction Rules

Must never log:

- raw bytes or images
- extracted raw text or full documents
- user payload blobs
- secrets or credentials: API keys, tokens, cookies, auth headers
- PII like email, phone, or address unless another reviewed contract explicitly
  allows it

## Testing Structured Logs

Prefer capturing structured records directly. `caplog` only sees stdlib logging
unless bridged.

```python
from loguru import logger


def test_logs_operation_start() -> None:
    records: list[dict[str, object]] = []
    handler_id = logger.add(lambda msg: records.append(msg.record), level="INFO")
    try:
        # run operation
        pass
    finally:
        logger.remove(handler_id)

    assert any(record["message"] == "operation.start" for record in records)
```

Structured field assertions should read `record["extra"]`.
