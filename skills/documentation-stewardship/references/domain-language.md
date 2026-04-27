# Domain Language

Owner for shared terminology discipline in durable harness docs.

Goal: the same concept uses the same term everywhere unless an owner explicitly
documents an alias.

## Rules

- One domain concept has one canonical term.
- The doc that owns the concept owns its term.
- Secondary docs reuse the owner term instead of inventing synonyms.
- If a term needs an adapter/provider alias, name the alias and point back to
  the canonical owner.
- Do not rename a term casually during wording compaction.
- When splitting docs, keep the original canonical term with the moved rule.
- When a term changes, update direct consumers in the same change or create a
  backlog item.

## Canonical Pattern

Use this shape when a doc introduces reusable vocabulary:

```md
## Vocabulary

| Term | Meaning | Owner |
|---|---|---|
| `<term>` | `<one meaning>` | `<owner doc>` |
```

Keep this table short. It is for terms that affect routing, proof, review,
state, ownership, or workflow behavior, not ordinary prose.

## Common Harness Terms

Use these existing owners rather than redefining terms:

| Domain | Canonical owner |
|---|---|
| skill structure, `SKILL.md`, frontmatter `description`, references, assets, scripts | `../../harness-governance/references/skill-architecture.md` |
| durable rule ownership and doc placement | `policy-single-source-of-truth.md`, `durable-doc-placement.md` |
| wave lifecycle, delivery map, backlog item | `../../initiatives-workflow/references/initiatives-workflow.md` |
| execution packet, task card, proof row | `../../initiatives-workflow/references/wave-packet-contract.md` |
| role names and subagent boundaries | `../../subagent-orchestration/references/coding-agent-topology.md` |
| review verdicts and approval state | `../../code-review/references/review-governance.md` |
| runtime proof classes and runtime evidence vocabulary | `../../verification-before-completion/references/runtime-proof-escalation.md`, `../../verification-before-completion/references/runtime-evidence-contract.md` |
| persistent-test doctrine | `../../testing-best-practices/references/testing-strategy.md` |

## Audit Heuristics

When auditing language consistency:

1. Pick one domain and its owner doc.
2. List canonical terms and obvious aliases.
3. Search secondary docs for aliases.
4. Classify each alias:
   - `rename-now`: same concept, different word
   - `document-alias`: adapter/provider term users will see externally
   - `leave`: different concept or ordinary prose
5. Patch only `rename-now` cases in the same domain slice.

Do not run repo-wide wording churn without a term owner and alias list.
