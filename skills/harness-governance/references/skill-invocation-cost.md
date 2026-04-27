# Skill Invocation Cost

Load this reference when auditing broad skill entrypoints or proposing a new
routing skill. Keep it as durable policy and concise audit disposition, not a
run log.

## Policy

- Prefer a short skill hot path plus explicit `load when` gates for detailed
  references.
- Add a router only when observed flows repeatedly load the wrong broad skill or
  require an expensive owner only for a narrow decision.
- Do not add a routing hop for possible prompt-size savings alone.
- Preserve invariants in the hot path when extracting detail: owner boundary,
  stop conditions, proof requirements, and review requirements.
- Store raw one-off audit evidence in current-work. Keep only durable
  threshold, rationale, and disposition here.

## 2026-04-27 Audit Disposition

Measured hot-path bodies before and after the audit:

| Skill | Before lines / bytes | After lines / bytes | Disposition |
| --- | ---: | ---: | --- |
| `planning-intake` | 175 / 6375 | 96 / 3771 | Extracted detailed intake mechanics to `../../planning-intake/references/intake-contract.md`. |
| `verification-before-completion` | 106 / 4570 | 102 / 4299 | Reused existing `quality-gate-selection.md`; no completion router. |
| `harness-governance` | 143 / 5805 | 83 / 3373 | Extracted overlay/posture/enforcement detail to `harness-contracts.md`. |
| `user-apps-design` | 126 / 5272 | unchanged | No split; trigger is already UI-direction-specific. |
| `mobile-design` | 127 / 4262 | unchanged | No split; used only after `user-apps-design` for mobile constraints. |
| `webapp-testing` | 156 / 6443 | unchanged | No split; runtime proof mechanics need a single owner. |
| `mobileapp-testing` | 94 / 4091 | unchanged | No split; mobile runtime proof trigger is already narrow. |

Rejected splits:

- `ui-routing`: no observed repeated misroute across `user-apps-design`,
  `mobile-design`, `webapp-testing`, and `mobileapp-testing`.
- `completion-routing`: no observed friction beyond a small duplicated gate
  table, now removed from the hot path.

Future split threshold: name the overloaded flow, current owner skill loaded,
smaller intended route, invariants that remain with the original owner, and
observed friction that a reference extraction cannot solve.
