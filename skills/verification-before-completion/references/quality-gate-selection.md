# Quality Gate Selection

Owner for reusable quality-tier semantics and local completion-gate selection.

Migration guardrails follow
project overlay migration guardrails.

## Tier Contract

| Tier | Purpose | Default use |
| --- | --- | --- |
| `quality-fast` | cheapest shared baseline | local iteration + GitHub CI |
| `quality` | standard completion gate | default before saying work is done |
| `quality-full` | expanded-confidence local follow-up | when user, reviewer, wave, or feature-owner doctrine requires extra local proof |

Rule: CI baseline is `quality-fast`. Completion proof is still local
`quality` unless another owner doc raises bar.

Rule: self-contained local performance budgets that are optional
expanded-confidence follow-up may live in `quality-full`. Runtime-bound browser
or app-carrier follow-up should stay explicit runtime proof, not a shared
quality-tier dependency, unless a durable owner doc explicitly chooses the
heavier gate. Once a durable owner adopts a budget or proof as required for the
claim or owned path, failure is blocking.

Rule: root `tests` is a separate rollup and is not part of the quality tier
contract.

Rule: some stacks may omit `quality-full` when there is no honest extra local
proof to expose. If a stack does expose `quality-full`, it must represent a real
follow-up tier rather than a renamed `quality` or `quality-fast`.

## Local Gates

Use `just` wrappers:

- fast gate: `just quality-fast`
- standard gate: `just quality`
- expanded-confidence gate: `just quality-full`
- alias: `just qfull`

Tier meaning:

- stack `quality` should compose on top of `quality-fast` and add only the
  smaller default-completion delta that still belongs in the normal gate
- stack `quality-full` is where slower policy, security, persistence, or local
  expanded-confidence follow-up belongs when that extra proof really earns a
  separate, self-contained tier

Rule: a stack may omit `quality-full` when the only remaining extra proof is
runtime-bound browser/app verification that should stay explicit.

When a feature adopts local performance budgets through `quality-full`, run that
gate on purpose for changes on the owned performance path and for any baseline
recalibration. When the proof is runtime-bound and explicit instead, run the
owner command directly instead of relying on memory of ad hoc scripts.

CI workflow names, hosted branch-protection checks, and stack-specific command
bodies belong to the active project overlay or repo-local workflow docs.
