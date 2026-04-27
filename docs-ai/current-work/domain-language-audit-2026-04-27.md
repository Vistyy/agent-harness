# Domain Language Audit Seed - 2026-04-27

Scope: doctrine placement plus seed terminology audit. This is not a completed
harness-wide terminology audit.

Doctrine added:
- `../../skills/documentation-stewardship/references/domain-language.md`
- `../../skills/documentation-stewardship/references/doc-writing-contract.md`
  now points durable docs at canonical domain language.

## Evidence-Backed Seed Rows

| Domain | Canonical terms checked | Alias candidates searched | Evidence | Classification |
|---|---|---|---|---|
| Role vocabulary | `explorer`, `check_runner`, `planning_critic`, `implementer`, `quality_guard`, `final_reviewer`, `runtime_evidence` | `planning-critic`, `final-reviewer`, `quality-guard`, `check-runner`, `runtime-evidence` | `rg -n "planning_critic|planning-critic|final_reviewer|final-reviewer|quality_guard|quality-guard|check_runner|check-runner|runtime_evidence|runtime-evidence" skills adapters AGENTS.md` shows canonical ids in role owners and adapter filename aliases where provider files require hyphenated names. | `document-alias`: provider filename aliases are acceptable; role ids stay canonical. |
| Testing doctrine | `testing-strategy.md`, `touched-test-gate.md`, `proof-strength.md`, `layer-selection.md`, `corpus-audit.md` | broad `testing-strategy.md` links for specific touched-test/proof/layer concerns | `rg -n "testing-strategy.md|touched-test-gate|proof-strength|layer-selection|corpus-audit" skills/code-review skills/verification-before-completion skills/webapp-testing skills/mobileapp-testing skills/testing-best-practices` shows specific consumers now point at focused owners or intentionally use the router. | `leave`: Wave B already normalized this domain. |
| Router vs entrypoint | `SKILL.md` entrypoint, reference router | `entry point`, `entrypoint`, `router` | `skill-architecture.md` owns `SKILL.md` as workflow entrypoint; `testing-strategy.md` uses router for a reference that dispatches to focused owner docs. | `leave`: related but different concepts. |
| Source of truth vs owner | source-of-truth placement, owner doc | `source of truth`, `source-of-truth`, `owner` | `policy-single-source-of-truth.md` owns placement; owner-doc language identifies the document responsible for a durable rule. They are complementary: placement says where truth belongs; owner says which doc owns a rule or term. | `leave`: intentional distinction, no backlog. |

Future audit method is owned by
`../../skills/documentation-stewardship/references/domain-language.md`.
