# Diagnostics

Use when root-cause investigation needs durable runtime context.

Diagnostics should prove where the failure enters, changes, or leaves a
boundary. They are not a substitute for root-cause analysis.

## Evidence Shape

Capture only bounded, relevant context:
- operation or component name
- stage
- status
- correlation or trace identifier when available
- sanitized error code or class
- relevant input shape, not full payload
- cwd/env/config value only when it affects the failure

Do not log secrets, credentials, cookies, auth headers, raw documents, raw
images, unbounded payloads, or PII unless a reviewed project contract explicitly
allows it.

## Correlation

Use existing project correlation/trace fields. If none exist, keep temporary
diagnostic labels local to the investigation and remove them before closeout
unless a durable observability owner accepts them.

## Testing Logs

Prefer asserting structured records directly when the project exposes them.
Avoid brittle exact-string assertions unless the message is the durable
contract.
