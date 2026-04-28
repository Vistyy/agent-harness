# Skill Ownership Audit 2026-04-27

Audit standard:
- each skill owns one coherent concept, workflow, or role surface,
- neighboring skills may be named for routing, handoff, or owner lookup,
- neighboring doctrine should not be restated,
- references should be directly discoverable from `SKILL.md`,
- frontmatter descriptions should be explicit enough for routing and no longer
  than needed.

Coverage:
- all `skills/*/SKILL.md`,
- all skill reference markdown files,
- skill markdown assets/templates/examples/evaluations,
- Codex and GitHub Copilot adapter role docs.

## Findings Addressed In This Pass

| Finding | Disposition |
|---|---|
| Live skill docs used repo-root-looking `skills/...` paths from inside skill directories. | Replaced live guidance links with skill-relative paths where the target is a bundled skill/reference. Kept repo-root paths in copied templates/examples where that is the intended project-facing form. |
| `mobile-design` stored reference docs in the skill root. | Moved mobile reference docs under `skills/mobile-design/references/` and updated `SKILL.md`. |
| `systematic-debugging` stored reference docs in the skill root. | Moved root-cause, condition-waiting, and defense-in-depth docs under `references/` and updated links. |
| `test-driven-development/references/testing-anti-patterns.md` was not directly discoverable from `SKILL.md`. | Linked it from the TDD entrypoint. |
| Several frontmatter descriptions were clear but wordier than needed. | Compacted high-token descriptions while preserving trigger terms and exclusions. |

## Skill Matrix

| Skill | Owned Concept | Disposition |
|---|---|---|
| `adversarial-review` | failure-mode review lens | Clean after description compaction; it points into review loops without owning approval. |
| `code-review` | isolated review wrapper/report shape | Clean. Review governance owns approval doctrine; subagent routing remains a role lookup, not delegation policy. |
| `code-simplicity` | simplicity lens | Clean after relative owner links. It is intentionally a cross-phase lens, not a workflow owner. |
| `documentation-stewardship` | durable doc placement and single source of truth | Clean. |
| `executing-plans` | execution of approved standalone plans | Clean after relative owner links. |
| `flutter-expert` | Flutter/Dart implementation mechanics | Clean after description compaction; routes design/mobile UX to owner skills. |
| `harness-governance` | harness architecture, skill architecture, adapter/install posture | Clean. Broad because it owns the harness repo boundary. |
| `initiatives-workflow` | wave/backlog lifecycle and packet maintenance | Clean. It references planning/review/delegation owners without restating their full doctrine. |
| `just-recipe-routing` | choosing `just` recipes and quality tiers | Clean after description compaction. |
| `mobile-design` | mobile-specific UX constraints and validation posture | Cleaned reference placement. Watch item: `mobile-backend` and `mobile-testing` references are broad but conditional; split only if they become independently triggered skills. |
| `mobileapp-testing` | deterministic mobile runtime proof mechanics | Clean. It consumes runtime-proof and evidence contracts without owning their taxonomy. |
| `planning-intake` | wave planning/intake closure | Clean after relative owner links. It necessarily references proof, workflow, and delegation owners for promotion readiness. |
| `review-address` | rigorous triage of received review feedback | Clean. |
| `subagent-orchestration` | delegation decisions, handoffs, active-worker handling | Clean. Reuse/fresh-spawn policy now defers role-specific fresh-context standards to role owners. |
| `svelte-code-writer` | Svelte docs lookup and autofixer workflow | Clean. |
| `svelte-core-bestpractices` | durable Svelte posture and anti-patterns | Clean after boundary wording and description compaction. |
| `system-boundary-architecture` | ownership, state authority, contracts, composition boundaries | Clean after description compaction. |
| `systematic-debugging` | root-cause debugging workflow | Cleaned reference placement and evaluation skill paths. |
| `tailwind-design-system` | Tailwind v4 implementation mechanics | Clean after description compaction. |
| `test-driven-development` | red-green proof workflow | Clean after moving/linking anti-pattern reference. Testing doctrine remains in `testing-best-practices`. |
| `testing-best-practices` | persistent test doctrine, layer choice, bad-test cleanup | Clean after description compaction. Runtime proof classes remain in verification owners. |
| `user-apps-design` | product-facing UI direction, parity, composition, copy posture | Clean but large. It mostly routes mechanics out instead of owning them. Future compaction could target checklist repetition, not ownership. |
| `uv` | Python command/dependency workflow through `uv` | Clean. |
| `verification-before-completion` | fresh proof before completion claims and quality gate selection | Clean. It routes runtime mechanics, testing doctrine, and review fields to owners. |
| `wave-autopilot` | executing one execution-ready wave packet | Clean after relative owner links. Its implementer/check_runner mentions are execution workflow, not role doctrine. |
| `webapp-testing` | browser-visible runtime proof mechanics | Clean. It consumes runtime-proof/evidence contracts and project runtime recipes. |
| `workflow-feedback` | project workflow issue and improvement ledger capture | Clean. Broad trigger is intentional; body stays lean and routes durable harness promotion to `harness-governance`. |
| `writing-plans` | standalone implementation plan authoring | Clean after relative owner links. |

## Reference And Adapter Disposition

| Surface | Disposition |
|---|---|
| `code-review/references/review-governance.md` | Clean. It owns review modes/approval semantics; role names are part of that topology. |
| `documentation-stewardship/references/**` | Clean. Owns single-source and domain-language doctrine. |
| `flutter-expert/references/**` | Clean. Flutter-specific mechanics only. |
| `harness-governance/references/skill-architecture.md` | Clean. Owns skill-authoring policy. |
| `initiatives-workflow/references/**` and assets | Clean but naturally template-heavy. Assets intentionally use project-facing repo-root examples. |
| `mobile-design/references/**` | Cleaned placement. Content is conditional; no immediate split unless backend/testing/performance use independently. |
| `subagent-orchestration/references/coding-agent-topology.md` | Clean after relative link normalization. Owns role vocabulary/boundaries only. |
| `svelte-core-bestpractices/references/**` | Clean. Svelte-specific and conditional. |
| `system-boundary-architecture/references/**` | Clean. Broad but coherent around ownership/boundary doctrine. |
| `systematic-debugging/references/**`, `examples/**`, `evaluations/**` | Cleaned placement and stale evaluation paths. Evaluations remain explicitly non-runtime. |
| `testing-best-practices/references/**` | Clean. Internal testing owner map separates proof strength, layer choice, corpus audit, and touched-test gate. |
| `user-apps-design/references/**` | Clean. UI-specific parity, composition, and text constraints. |
| `verification-before-completion/references/**` | Clean. Runtime proof escalation and evidence contract are correctly owned here; browser/mobile mechanics route out. |
| `webapp-testing/references/**`, examples, scripts | Clean. Browser proof mechanics and helper references are directly named from `SKILL.md`. |
| `writing-plans/references/**` and assets | Clean. Standalone plan policy/templates are owned here. |
| Adapter role docs under `adapters/codex/agents/**` and `adapters/github-copilot/agents/**` | Acceptable duplication. They are provider-facing role adapters and must carry compact self-contained role instructions; some also point back to global skill owners. |

## Watch Items

1. `mobile-design` remains the broadest conceptual bundle. Keep it as one skill
   while references are conditional and always mobile-specific. Split only if
   `mobile-backend`, `mobile-testing`, or `mobile-performance` starts being
   useful without mobile UX/design routing.
2. `user-apps-design` is the largest entrypoint. It is not currently leaking
   another owner's doctrine, but a future terseness pass could collapse checklist
   repetition after confirming no trigger clarity is lost.
3. Adapter role docs intentionally repeat compact role constraints. Do not
   apply the no-duplication rule mechanically there; provider role files need
   self-contained safety posture.
