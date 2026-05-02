# Skill Invocation Cost

Load this reference when auditing broad skill entrypoints, reference reading
cost, or proposed routing/splitting changes. Keep it as durable policy and
concise audit disposition, not a run log.

## Policy

- Prefer a short skill hot path plus explicit `load when` gates for conditional
  references.
- Broad-trigger authoring rules live in `skill-architecture.md`.
- Add a router only when observed flows repeatedly load the wrong broad skill or
  require an expensive owner only for a narrow decision.
- Do not add a routing hop, extraction, or split for possible prompt-size
  savings alone.
- Preserve invariants in the hot path when extracting detail: owner boundary,
  stop conditions, proof requirements, and review requirements.
- Treat length as reading-cost evidence, not sufficient proof that a skill or
  reference should split.
- When sections are needed together to preserve one contract, prefer a heading
  map, tighter wording, owner links, or stale-material deletion.
- Store raw one-off audit evidence in current-work. Keep only durable
  threshold, rationale, and disposition here.

## Split Or Router Threshold

Before proposing a router, extraction, or split, name:

- overloaded flow
- current owner skill or reference loaded
- smaller intended route or extracted target
- invariants that remain with the original owner
- separability proof: distinct trigger, load gate, input/output, proof/review
  owner, or independent consumer
- observed friction that a heading map, tighter wording, owner link, or stale
  deletion cannot solve

## Prior Rejected Split Classes

- `ui-routing`: no observed repeated misroute across `user-apps-design`,
  `mobile-design`, `webapp-testing`, and `mobileapp-testing`.
- `completion-routing`: no observed friction beyond a small duplicated gate
  table that justified a smaller hot path, not a router.
