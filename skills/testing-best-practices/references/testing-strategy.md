# Testing Strategy

Goal: protect real behavior with the cheapest high-signal proof.

This is the canonical router for persistent-test doctrine. Load the focused
owner file that matches the testing question.

Runtime proof escalation, runtime evidence reports, visual verdict vocabulary,
and artifact promotion are owned by:
- `../../verification-before-completion/references/runtime-proof-escalation.md`
- `../../verification-before-completion/references/runtime-evidence-contract.md`
- `../../verification-before-completion/references/verification-evidence.md`

Coverage count is not the goal. Bad tests are debt. Delete, shrink, rewrite, or
move them when touched.

Examples and helper scripts are indexed in `../SKILL.md`.

## Owner Map

| Concern | Owner |
|---|---|
| changed persistent test file row gate | `touched-test-gate.md` |
| invalid reason codes | `touched-test-gate.md` |
| `required-proof` and `durable-gain` | `touched-test-gate.md` |
| new persistent test admission | `touched-test-gate.md` |
| persistent proof sufficiency | `proof-strength.md` |
| weakly provable claim disposition | `proof-strength.md` |
| exact string assertions | `proof-strength.md` |
| source and implementation-shape assertions | `proof-strength.md` |
| layer selection | `layer-selection.md` |
| persistence lane placement | `layer-selection.md` |
| workflow/infra proof routing | `layer-selection.md` |
| runtime proof handoff and cheapest persistent layer | `layer-selection.md` |
| arbitrary sleeps and condition-based waiting | `condition-based-waiting.md` |
| persistent-test validity/strength for `multi-proof-required` | `proof-strength.md` |
| CI posture | `layer-selection.md` |
| practical add/keep checks | `layer-selection.md` |
| corpus-wide cleanup tranches | `corpus-audit.md` |
| performance and cost posture | `corpus-audit.md` |
| test-suite cleanup posture and follow-up ownership | `corpus-audit.md` |

## Fast Route

- Touching tests in a normal implementation/review: load
  `touched-test-gate.md`, then `proof-strength.md` or `layer-selection.md` only
  if the row decision depends on proof strength or layer placement.
- Adding or defending a persistent test: load `touched-test-gate.md`,
  `proof-strength.md`, and `layer-selection.md`.
- Reviewing source-text, exact-string, private-shape, mock, or proof-strength
  concerns: load `proof-strength.md`.
- Choosing layer, persistence lane, runtime handoff, CI lane, or workflow/infra
  proof: load `layer-selection.md`.
- Replacing sleeps, fixed waits, or wait-heavy retries: load
  `condition-based-waiting.md`.
- Running a suite cleanup tranche, suspicious-cluster audit, test cost cleanup,
  or harness-level testing follow-up: load `corpus-audit.md`.
