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

## Shared Report Fields

Runtime evidence reports should include:
- runtime recipe or command path used
- whether observability was enabled
- flow, request, screen, state, or branch exercised
- material variants considered and exact variants covered
- candidate discovery status when data-dependent
- artifacts, logs, screenshots, or trace pointers reviewed
- selected trace/correlation IDs when telemetry matters, or explicit
  `none observed` / `not used`
- behavioral verdict
- proof class
- pass/fail and residual risk

Completion claim fields belong to
`../../code-review/references/review-governance.md`.

## Surface Posture

### End-User Surfaces

Use end-user design governance when the claim materially concerns UI quality,
hierarchy, density, shell composition, polish, or cohesion.

Requirements:
- consume the scorecard from the project design-fidelity governance reference
- apply that reference's reject thresholds
- name anti-pattern matches using that reference's taxonomy
- do not restate the scorecard locally

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
