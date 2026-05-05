# Harness Design Anti-Pattern Gate

**Status:** done

Superseded by later UI workflow compaction: global report contracts were
removed. Current reusable visual approval ownership lives in
`skills/user-apps-design/SKILL.md` and `design_judge`.

## Objective Boundary

- original objective: continue the Impeccable-derived design workflow
  improvements by adding the deferred anti-pattern gate.
- accepted reductions: do not import Impeccable or require `npx impeccable`;
  this wave defines a harness-native report contract first.
- residual gaps: command/workflow specialization remains in backlog.

## Scope

- superseded scope: register-aware report semantics in `user-apps-design`,
  design-judge/runtime-evidence consumption rules, and focused fixture proof.
- out of scope: browser extension, HMR live variants, full deterministic
  detector implementation, and project-specific style bans.

## Closed Decisions

- superseded: `user-apps-design` owned a report contract that was later
  removed.
- The report is evidence, not approval; `design_judge` still owns UI design
  verdicts and `runtime_evidence` still owns live behavior/artifact
  sufficiency.
- Register matters: product UI may use familiar/system patterns when project
  truth supports them; brand UI has a stronger distinctiveness bar.
- Detector findings are inputs. Project-approved taste can override them;
  unsupported generic patterns can block/reject broad visual approval.

## Planning Gate

- `planning_critic`: APPROVE. Packet preserves the accepted reductions, keeps
  detector implementation out of scope, includes `harness-governance`, and
  names real owner layers in proof rows.
- planning `quality_guard`: APPROVE. Packet has implementer-eligible posture,
  bounded owner authority, valid deferrals, and proof rows that cover bypasses
  and adapter parity risks.

## Packet

- closed after final review on 2026-05-05.

## Closeout

- planning_critic: APPROVE after owner layers, `harness-governance`, bypass
  fixtures, and adapter parity variants were repaired.
- planning quality_guard: APPROVE after delegation posture, touched-owner
  integrity, and adapter parity proof were tightened.
- implementation quality_guard: APPROVE with no material findings.
- final_reviewer: APPROVE after stale backlog state and report-shape proof
  blockers were repaired.
- proof: focused anti-pattern tests, validate-harness tests, harness
  validation, governance check, and `just quality-fast` passed.
