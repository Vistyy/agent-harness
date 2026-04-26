# Verification Evidence

Runtime proof depth is owned by `runtime-proof-escalation.md`.

This reference owns evidence placement:

- run-specific runtime evidence belongs in `docs-ai/current-work/**` and
  `.artifacts/runtime/**`, not in durable docs
- raw runtime artifacts belong under `.artifacts/runtime/**`
- execution-local summaries, blocker notes, and evidence pointers belong in
  `docs-ai/current-work/**`
- durable docs keep policy and proof shape, not machine-local artifacts or
  one-off transcripts
- packet evidence pointers name the flow, state, and probe class the artifact
  proves when material to the claim

Diagnostic output such as screenshots, videos, traces, and logs becomes proof
only after it is explicitly reviewed and cited for a specific claim.
