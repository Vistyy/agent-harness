# Harness Hardening Wave B - 2026-04-27

Status: draft for planning-critic review

Backlog absorbed:
- `harness-hardening__testing-strategy__owner-map`
- `harness-hardening__wording-compaction__bounded-trims`

## Scope And Execution Posture

In-scope work:
- split `testing-strategy.md` into a lean router plus focused owner references
- update direct consumers to point at focused testing owners where useful
- apply bounded wording compaction only where the split makes text redundant
- remove absorbed backlog items from the delivery map after implementation

Out-of-scope work:
- changing testing doctrine meaning
- broad skill rewrite or style polish
- changing frontmatter `description` fields unless a direct trigger mismatch is
  found and reviewed
- changing runtime proof doctrine, browser/mobile mechanics, or review approval
  semantics beyond updated owner links

Non-obvious constraints:
- Preserve all existing testing policy.
- Prefer fewer focused references over many tiny shards.
- Keep `testing-strategy.md` as the stable entrypoint for broad consumers.
- Any compacted wording needs a before/after owner claim and a preserved-meaning
  disposition.

System-boundary trigger: not-triggered. This wave reorganizes documentation
ownership and references only; it does not change runtime architecture, state
authority, product behavior, or public contracts.

Implementer delegation posture: parent-only.

Parent-only rationale: `shared-file-churn`. The split touches one doctrine
cluster and its consumers; keeping it local avoids cross-worker reference drift.

Frozen decisions:
- `testing-strategy.md` remains the canonical broad entrypoint.
- Focused references live under `skills/testing-best-practices/references/`.
- Split targets:
  - `touched-test-gate.md`
  - `proof-strength.md`
  - `layer-selection.md`
  - `corpus-audit.md`
- The wording-compaction backlog is satisfied only by the predeclared trim
  candidates in this plan. No opportunistic compaction.

Planning exceptions: none.

## Split-Shape Decision

Rejected alternatives:
- No split / router-only cleanup: preserves current single 415-line reference,
  so every focused testing question still loads all touched-test, proof,
  layer, corpus, performance, runtime-routing, and CI posture details.
- Workflow-phase split: attractive for task flow, but the existing doctrine is
  organized by policy owner rather than chronological workflow. It would mix
  hard-gate rows, proof-strength rules, layer selection, and corpus cleanup
  into phase files and make exact owner lookup weaker.
- More granular split: would reduce file size further but create too many
  owner documents and increase route friction for agents.

Chosen shape:
- Four focused owner references plus a lean router. This maps to stable
  doctrine families agents ask for directly: touched-test gate, proof strength,
  layer selection/runtime routing, and corpus/performance cleanup.

## Section Owner Map

| Current `testing-strategy.md` section | New owner | Notes |
|---|---|---|
| `# Testing Strategy` intro | `testing-strategy.md` | Keep goal and owner map only. |
| `## Hard Gate` | `touched-test-gate.md` | Owns row gate, `required-proof`, `durable-gain`, new-test rule. |
| `## Persistent Proof Posture` | `proof-strength.md` | Owns persistent proof sufficiency and points runtime handoff to `layer-selection.md`. |
| `## Proof Strength Rules` | `proof-strength.md` | Owns anti-patterns and branch/authority proof strength. |
| `## Invalid Reason Codes` | `touched-test-gate.md` | Owns invalid-code list because the hard gate consumes it. |
| `## Weakly Provable Claim Disposition` | `proof-strength.md` | Owns disposition for weak proof families. |
| `## Touched-Test Remediation` | `touched-test-gate.md` | Owns keep/shrink/rewrite/delete workflow and reason-code reuse. |
| `## Corpus-Wide Audit Mode` | `corpus-audit.md` | Owns tranche workflow. |
| `## Performance And Cost Rules` | `corpus-audit.md` | Owns audit cost/performance posture. |
| `## Layer Selection` | `layer-selection.md` | Owns preferred proof layer table. |
| `## Persistence Lane Rule` | `layer-selection.md` | Owns persistence lane placement. |
| `## Exact String Rule` | `proof-strength.md` | Owns exact-string proof validity. |
| `## Source And Implementation-Shape Assertions` | `proof-strength.md` | Owns source/private-shape proof validity. |
| `## Workflow And Infra Changes` | `layer-selection.md` | Owns infra/workflow proof layer routing. |
| `## Runtime Proof Routing` | `layer-selection.md` and `proof-strength.md` | `layer-selection.md` owns runtime handoff and cheapest persistent layer; `proof-strength.md` owns persistent-test validity/strength. |
| `## CI Posture` | `layer-selection.md` | Owns quality lane posture as testing-side route. |
| `## Practical Checks` | `layer-selection.md` | Owns add/keep test triage prompts. |

## Predeclared Compaction Candidates

| Surface | Before owner claim | After owner claim | Preserved meaning | Counterfactual trigger check |
|---|---|---|---|---|
| `testing-strategy.md` | Full doctrine owner and all detailed rules. | Broad router plus owner map to focused references. | All rules move to focused owners named above. | Agent can still find every previous section from the owner map. |
| `testing-best-practices/SKILL.md` | Entry skill repeats non-negotiables, audit loop, failure modes, exact-string mini-rule. | Entry skill keeps trigger, fast routing, and output contract; detailed doctrine routes to references. | Trigger and touched-test row requirement remain explicit. | Agent still knows to emit one row per changed persistent test file. |
| `review-governance.md` testing reference sentence | Names broad `testing-strategy.md` plus row/gate/proof concepts. | Points approval gate to `touched-test-gate.md` and proof validity to `proof-strength.md`. | Review still rejects changed persistent tests that fail row/gate/proof checks. | Reviewer still knows no approval while changed tests fail testing doctrine. |
| `runtime-proof-escalation.md` testing route | Routes broad testing concerns to `testing-strategy.md`. | Routes multi-proof persistent-test concerns to `layer-selection.md` for runtime handoff/cheapest layer and `proof-strength.md` for validity/strength. | Runtime owner still does not absorb testing doctrine. | Runtime proof still requires testing owners for persistent leg. |
| `webapp-testing` / `mobileapp-testing` proof notes | Mentions `testing-strategy.md` only for persistent-test strategy. | Either keep broad router or point persistent-test leg to focused owner without extra doctrine text. | Browser/mobile mechanics stay separate from persistent-test doctrine. | These skills do not start restating testing policy. |

## Task Plan

| Task slug | State | Dependencies | Outcome summary | Proof rows |
|---|---|---|---|---|
| `testing-owner-map-split` |  | `none` | Testing doctrine owner map is split into focused references without meaning loss. | `B1-P1`, `B1-P2` |
| `consumer-reference-update` |  | `testing-owner-map-split` | Consumers route to focused owners where they name a specific testing concern. | `B2-P1` |
| `bounded-wording-compaction` |  | `testing-owner-map-split` | Redundant wording is trimmed with explicit preserved-meaning dispositions. | `B3-P1`, `B3-P2` |
| `backlog-closeout-state` |  | `bounded-wording-compaction` | Absorbed backlog state is deleted from active workflow state. | `B4-P1` |

### `testing-owner-map-split`

- Outcome:
  - `testing-strategy.md` becomes a lean router and the owner map is explicit.
- In scope:
  - `skills/testing-best-practices/references/testing-strategy.md`
  - new focused references under `skills/testing-best-practices/references/`
- Out of scope:
  - changing any testing rule, reason code, gate, or exception semantics
  - adding new test doctrine
- Owned files and surfaces:
  - `skills/testing-best-practices/references/testing-strategy.md`
  - `skills/testing-best-practices/references/touched-test-gate.md`
  - `skills/testing-best-practices/references/proof-strength.md`
  - `skills/testing-best-practices/references/layer-selection.md`
  - `skills/testing-best-practices/references/corpus-audit.md`
- Locked invariants:
  - hard gate, invalid reason codes, `required-proof`, and `durable-gain` live
    in `touched-test-gate.md`
  - proof strength, weakly provable claims, exact-string rules, and
    source/implementation-shape assertions live in `proof-strength.md`
  - layer selection, persistence lane, workflow/infra, runtime proof routing,
    CI posture, and practical checks live in `layer-selection.md`
  - corpus-wide audit and performance/cost rules live in `corpus-audit.md`
  - `testing-strategy.md` names the owner map and routes readers to focused
    files; it does not duplicate full policy bodies
- Allowed local implementer decisions:
  - section ordering inside focused references when it does not change the
    section owner map
  - brief bridge sentences needed after moving content
- Stop-and-handback triggers:
  - a rule cannot be moved without changing meaning
  - one existing rule seems to belong to multiple focused owners with material
    ambiguity
  - split creates circular or unclear owner routing
- Proof rows:
  - `B1-P1`
  - `B1-P2`
- Deferred follow-up:
  - none

### `consumer-reference-update`

- Outcome:
  - Consumers keep broad links when broad strategy is intended and point to
    focused references when they name a specific testing concern.
- In scope:
  - `skills/code-review/references/review-governance.md`
  - `skills/verification-before-completion/references/runtime-proof-escalation.md`
  - `skills/webapp-testing/SKILL.md`
  - `skills/mobileapp-testing/SKILL.md`
  - `skills/testing-best-practices/SKILL.md`
- Out of scope:
  - changing consumer skill behavior beyond reference routing
- Owned files and surfaces:
  - the files listed above
- Locked invariants:
  - code-review approval gate must still mention touched-test row, invalid
    reason code gate, `required-proof`, and `durable-gain`
  - runtime proof escalation must still route persistent-test concerns back to
    testing owners
  - browser/mobile testing skills must not absorb persistent-test doctrine
- Allowed local implementer decisions:
  - whether a consumer link stays broad or points at a focused reference, based
    on the specificity of the surrounding sentence
- Stop-and-handback triggers:
  - a consumer needs policy text copied instead of linked
  - a reference update would change trigger behavior
- Proof rows:
  - `B2-P1`
- Deferred follow-up:
  - none

### `bounded-wording-compaction`

- Outcome:
  - Token reduction is achieved only where the split removes the need to repeat
    detailed policy in entrypoints or consumers.
- In scope:
  - only the five surfaces listed in `Predeclared Compaction Candidates`
- Out of scope:
  - broad skill compaction outside the testing-doctrine route
  - compacting frontmatter descriptions
- Owned files and surfaces:
  - `skills/testing-best-practices/references/testing-strategy.md`
  - `skills/testing-best-practices/SKILL.md`
  - `skills/code-review/references/review-governance.md`
  - `skills/verification-before-completion/references/runtime-proof-escalation.md`
  - `skills/webapp-testing/SKILL.md`
  - `skills/mobileapp-testing/SKILL.md`
- Locked invariants:
  - each compaction has a before/after owner claim in closeout
  - no trigger or policy strength weakens
  - compacted entrypoints still tell agents when to load focused references
- Allowed local implementer decisions:
  - sentence-level trims inside the predeclared candidates that preserve owner
    claims
- Stop-and-handback triggers:
  - a trim removes an explicit trigger or enforcement rule
  - compaction requires changing multiple unrelated skill surfaces
- Proof rows:
  - `B3-P1`
  - `B3-P2`
- Deferred follow-up:
  - none

### `backlog-closeout-state`

- Outcome:
  - The two absorbed backlog items no longer remain active backlog after Wave B.
- In scope:
  - `docs-ai/current-work/delivery-map.md`
  - `docs-ai/current-work/backlog/harness-hardening__testing-strategy__owner-map.md`
  - `docs-ai/current-work/backlog/harness-hardening__wording-compaction__bounded-trims.md`
- Out of scope:
  - creating further backlog unless implementation exposes new material debt
- Owned files and surfaces:
  - the files listed above
- Locked invariants:
  - no item lives as both active wave work and backlog detail after closeout
  - absorbed backlog detail files are deleted in the same change
  - any new material follow-up must be recorded in delivery-map/backlog state
- Allowed local implementer decisions:
  - none; delete absorbed backlog details and remove delivery-map entries
- Stop-and-handback triggers:
  - new follow-up scope is user-visible or changes owner/proof direction
- Proof rows:
  - `B4-P1`
- Deferred follow-up:
  - none expected

## Proof Plan

```json
{
  "proof_plan": [
    {
      "proof_id": "B1-P1",
      "task_slug": "testing-owner-map-split",
      "anchor_ids": ["BB1"],
      "claim": "Every current testing-strategy section has exactly one planned focused owner or the router owner.",
      "material_variants": ["all current section headings listed in Section Owner Map"],
      "proof_classification": "multi-proof-required",
      "owner_layer": "doc-only + static-check",
      "exact_proof": [
        "rg -n \"^# |^## \" skills/testing-best-practices/references/testing-strategy.md skills/testing-best-practices/references/touched-test-gate.md skills/testing-best-practices/references/proof-strength.md skills/testing-best-practices/references/layer-selection.md skills/testing-best-practices/references/corpus-audit.md",
        "human compare heading inventory against Section Owner Map"
      ],
      "expected_evidence": ["each current section heading appears under its planned owner; testing-strategy.md contains only intro/router sections, not duplicated full policy bodies"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "One current section is omitted, duplicated, or moved to a different owner than the Section Owner Map.",
        "failing_assertion_or_artifact": "Heading inventory or human comparison shows mismatch."
      },
      "status": "planned"
    },
    {
      "proof_id": "B1-P2",
      "task_slug": "testing-owner-map-split",
      "anchor_ids": ["BB1"],
      "claim": "The split preserves all testing doctrine meaning.",
      "material_variants": ["all moved sections from testing-strategy.md"],
      "proof_classification": "not-reliably-provable-with-current-harness",
      "owner_layer": "doc-only",
      "exact_proof": [
        "human diff review of old testing-strategy sections against new focused references",
        "final_reviewer review"
      ],
      "expected_evidence": ["no final-review findings on omitted or weakened testing doctrine"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "A rule is silently shortened into weaker guidance.",
        "failing_assertion_or_artifact": "Reviewer identifies missing or weakened rule by file/line."
      },
      "status": "planned"
    },
    {
      "proof_id": "B2-P1",
      "task_slug": "consumer-reference-update",
      "anchor_ids": ["BB2"],
      "claim": "Testing-doctrine consumers route to the broad router or focused owner matching their claim.",
      "material_variants": ["code-review", "verification-before-completion", "webapp-testing", "mobileapp-testing", "testing-best-practices"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "static-check",
      "exact_proof": [
        "rg -n \"testing-strategy|touched-test-gate|proof-strength|layer-selection|corpus-audit\" skills/code-review skills/verification-before-completion skills/webapp-testing skills/mobileapp-testing skills/testing-best-practices"
      ],
      "expected_evidence": ["specific concerns point to focused references; broad concerns may point to testing-strategy.md"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "A consumer names exact-string or touched-test gates but links only the broad router when a focused owner exists.",
        "failing_assertion_or_artifact": "The rg inventory shows stale broad-only routing for a specific concern."
      },
      "status": "planned"
    },
    {
      "proof_id": "B3-P1",
      "task_slug": "bounded-wording-compaction",
      "anchor_ids": ["BB3"],
      "claim": "Compaction is bounded to redundant testing-doctrine route text and preserves trigger clarity.",
      "material_variants": ["testing-best-practices SKILL", "testing-strategy router", "consumer route sentences"],
      "proof_classification": "doc-only",
      "owner_layer": "doc-only",
      "exact_proof": [
        "closeout table columns: file | before owner claim | after owner claim | preserved meaning | counterfactual trigger check",
        "closeout table must include exactly the predeclared compaction candidate surfaces and no opportunistic additions"
      ],
      "expected_evidence": ["one closeout disposition row for each compacted surface"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "A trim removes when-to-load guidance or an enforcement trigger.",
        "failing_assertion_or_artifact": "Closeout table cannot state the preserved owner claim."
      },
      "status": "planned"
    },
    {
      "proof_id": "B3-P2",
      "task_slug": "bounded-wording-compaction",
      "anchor_ids": ["BB3"],
      "claim": "The resulting skill/reference paths remain parsable and locally linked.",
      "material_variants": ["all changed SKILL.md and reference files"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "static-check",
      "exact_proof": ["just quality"],
      "expected_evidence": ["quality passes"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "A moved or compacted reference link breaks validation.",
        "failing_assertion_or_artifact": "validate_harness reports a broken reference."
      },
      "status": "planned"
    },
    {
      "proof_id": "B4-P1",
      "task_slug": "backlog-closeout-state",
      "anchor_ids": ["BB4"],
      "claim": "Absorbed backlog items are removed from active workflow state.",
      "material_variants": ["delivery-map", "two backlog detail files"],
      "proof_classification": "automated-suite-provable",
      "owner_layer": "static-check",
      "exact_proof": [
        "rg -n \"harness-hardening__testing-strategy__owner-map|harness-hardening__wording-compaction__bounded-trims\" docs-ai/current-work"
      ],
      "expected_evidence": ["no active backlog references or backlog detail files remain"],
      "counterfactual_regression_probe": {
        "weaker_implementation": "Backlog items stay active after their work is absorbed.",
        "failing_assertion_or_artifact": "rg prints active delivery-map/backlog detail references."
      },
      "status": "planned"
    }
  ]
}
```

## Execution State

### Decisions And Blockers

| Type | Item | Action | Owner |
|---|---|---|---|
| decision | Split shape | Four focused references plus lean router. | agent |
| decision | Wording compaction scope | Only testing-doctrine route text made redundant by split. | agent |
| blocker | none | none | none |

### Technical Debt And Deferred Follow-Up

- none expected

## Acceptance Anchors

- `BB1`: Testing doctrine owner map is explicit and focused.
- `BB2`: Consumer references point to the correct broad or focused owner.
- `BB3`: Wording compaction reduces redundant route text without weakening
  triggers or rules.
- `BB4`: Absorbed backlog items are removed from active workflow state.

## Completion Bar

Wave B is complete only when:
- planning-critic approves this scope or all material findings are addressed,
- implementation passes `just quality`,
- final isolated review approves the changed slice,
- closeout includes bounded compaction dispositions,
- backlog state no longer lists absorbed active items.
