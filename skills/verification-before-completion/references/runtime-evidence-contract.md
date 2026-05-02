# Runtime Evidence Contract

Owner for shared runtime-evidence report shape, screenshot verdict vocabulary,
and visual reject floor across browser and mobile proof.

Does not own:
- browser proof mechanics: `../../webapp-testing/SKILL.md`
- mobile/device proof mechanics: `../../mobileapp-testing/SKILL.md`
- end-user composition scorecards, thresholds, or anti-pattern taxonomy: the
  project design-fidelity governance reference
- project runtime recipes, ports, services, secrets, or product acceptance
  criteria: the active project overlay

## Role Contract

Runtime evidence validates the handed-off live claim. It must:
- use the supplied runtime target or recipe
- exercise real behavior, not only inspect source or static output
- inspect the artifacts it cites
- check that the supplied recipe fits the Runtime Claim Map from
  `runtime-proof-escalation.md`
- return one behavioral verdict: `pass | reject | blocked`
- name the claim boundary covered by the verdict
- name block impact for `reject`, `blocked`, or incomplete proof

It must not approve planning, code quality, architecture, or release readiness.
Those verdicts stay with their owning review gates.

## Verdict Vocabulary

Behavioral verdict:
- `pass`
- `reject`
- `blocked`

Design-fidelity verdict:
- `pass`
- `reject`
- `underspecified`
- `not-applicable`

Finding severity:
- `blocking`
- `advisory`

## Guard Authority

Runtime evidence is a completion blocker for the runtime-visible claim it was
asked to validate.

- `pass`: the observed runtime behavior supports the named claim boundary.
- `reject`: the observed runtime behavior contradicts the claim or hits the
  automatic visual reject floor.
- `blocked`: the harness cannot honestly complete the live validation because
  a required runtime, data state, credential, device, recipe, or claim-map
  field is missing.

If the claim map is missing, inconsistent, or broader than the supplied
runtime recipe or artifacts, return `blocked` with a message such as
`claim too broad for supplied runtime recipe`. Runtime evidence may suggest a
narrowed claim, but must not choose new entrypoints, expand branches, debug,
plan, review code quality, or approve readiness.

`adjacent-only` proof cannot pass readiness, end-to-end, or user-flow claims.
`simulated-boundary` proof must name the unproved boundary and supports only a
narrowed claim.

`reject`, `blocked`, or incomplete runtime evidence blocks or narrows the
affected claim even when automated tests or review agents pass.

## Shared Report Fields

Runtime evidence reports must include:
- claim boundary covered
- runtime recipe or command path used
- entrypoint fidelity:
  `exact | faithful-wrapper | simulated-boundary | adjacent-only | not-needed`
- whether observability was enabled
- flow, request, screen, state, or branch exercised
- material variants considered and exact variants covered
- candidate discovery status when data-dependent
- artifacts, logs, screenshots, or trace pointers reviewed
- selected trace/correlation IDs when telemetry matters, or explicit
  `none observed` / `not used`
- behavioral verdict
- block impact for `reject` or `blocked`
- proof class
- pass/fail and residual risk

Completion claim fields belong to
`../../code-review/references/review-governance.md`.

Do not include long raw logs, full console dumps, screenshots that were not
reviewed, or unrelated diagnostics in the evidence of record.

## Surface Posture

### End-User Surfaces

Use project-supplied design anchors, `DESIGN.md`, or end-user design
governance when the claim materially concerns UI quality, hierarchy, density,
shell composition, polish, or cohesion.

Requirements:
- consume the supplied scorecard, anchors, or design contract
- apply supplied reject thresholds when present
- name anti-pattern matches using supplied taxonomy when present
- do not invent project-specific standards

### Internal Or Admin Surfaces

Do not apply end-user scorecard or archetype scoring by default.

Use:
- behavioral verdict
- visible-defect `blocking` findings
- layout/usability `advisory` findings
- `design-fidelity verdict: not-applicable`

Exception:
- if the parent provides explicit design anchors or a surface-specific design
  contract, issue a design-fidelity verdict against that supplied contract.

## Automatic Visual Reject Floor

These are always `blocking` and force `reject` when observed:
- visible overlap
- clipping of important content or controls
- unreadable primary labels
- broken responsive layout
- broken grouping that makes intended structure unclear
- missing or broken media on a visual surface
- any screen where a reasonable reviewer must mentally reconstruct the
  intended UI

This floor still applies when anchors are weak, absent, or incomplete.

## Missing-Anchor Posture

For end-user UI quality or hierarchy claims:
- if required design anchors or archetype posture are missing, use
  `design-fidelity verdict: underspecified`
- do not improvise an end-user score from taste alone
- still issue `reject` if the automatic visual reject floor is hit
- keep behavioral verdict separate from the underspecified design-fidelity
  verdict

If no project design contract is supplied for an end-user UI quality claim, the
runtime worker may still report obvious `blocking` defects and `advisory`
issues, but must not call the design quality fully proven.

## Visual Verdict Fields

Every delegated runtime UI verdict must name:
- runtime recipe used
- flow or screen/state reviewed
- reviewed screenshot paths
- viewport or device posture for each reviewed screenshot
- behavioral verdict

When end-user design-fidelity applies, also include:
- design-fidelity verdict
- per-dimension scores from the project-owned scorecard
- total score and threshold result
- anti-pattern matches
- `blocking` defects
- `advisory` notes

When end-user design-fidelity is underspecified, include:
- `design-fidelity verdict: underspecified`
- missing owner inputs
- any `blocking` defects still observed
- any `advisory` notes still worth reporting

When internal/admin default posture applies, include:
- `design-fidelity verdict: not-applicable`
- `blocking` defects
- `advisory` notes

## Review Notes

- `behavioral verdict: pass` does not soften `design-fidelity verdict: reject`.
- `design-fidelity verdict: underspecified` is not permission to approve weak
  end-user UI claims.
- use `blocking` for visible defects, not as a synonym for dislike.
- screenshots are evidence only after the reviewer opens or inspects them.
