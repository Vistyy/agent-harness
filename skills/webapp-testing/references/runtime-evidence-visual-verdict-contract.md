# Runtime-Evidence Visual Verdict Contract

Owner for delegated `runtime_evidence` screenshot-verdict schema, severity
language, automatic visual reject floor, and report shape.

Does not own:
- end-user composition scorecard, reject thresholds, or anti-pattern taxonomy:
  the project design-fidelity governance reference
- proof-depth class selection:
  `../../testing-best-practices/references/testing-strategy.md`
- runtime-proof process selection:
  the project UI verification strategy, when present
- role routing surfaces:
  adapter configuration and runtime_evidence role definitions

## Purpose

Prevent delegated runtime UI verdict drift between:
- screenshot-only intuition,
- vague “looks good” approval,
- end-user scorecard duplication,
- and over-broad criticism on internal/operator surfaces.

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

## Surface Posture

### End-User Surfaces

Use end-user design governance when the request materially claims UI quality,
hierarchy, density, shell composition, polish, or cohesion.

Requirements:
- consume the eight-dimension scorecard from
  the project design-fidelity governance reference
- apply its fixed reject thresholds
- name anti-pattern matches using its taxonomy
- do not restate the scorecard locally as a new source of truth

### Internal Or Admin Surfaces

Do not apply end-user scorecard or archetype scoring by default.

Use:
- behavioral verdict,
- visible-defect `blocking` findings,
- layout/usability `advisory` findings,
- `design-fidelity verdict: not-applicable`

Exception:
- if the parent provides explicit design anchors or a surface-specific design
  contract for the internal/admin surface, runtime evidence may issue a
  design-fidelity verdict against that supplied contract instead of defaulting
  to `not-applicable`

## Automatic Visual Reject Floor

These are always `blocking` and force `reject` when observed, even if behavior
succeeds:
- visible overlap
- clipping of important content or controls
- unreadable primary labels
- broken responsive layout
- broken grouping that makes intended structure unclear
- missing or broken media on a visual surface
- any screen where a reasonable reviewer must mentally reconstruct the intended
  UI

This floor still applies when anchors are weak, absent, or incomplete.

## Missing-Anchor Posture

For end-user UI quality or hierarchy claims:
- if required design anchors or archetype posture are missing, use
  `design-fidelity verdict: underspecified`
- do not improvise an end-user score from taste alone
- still issue `reject` if the automatic visual reject floor is hit
- otherwise keep behavioral verdict separate from the underspecified
  design-fidelity verdict

## Required Report Shape

Every delegated runtime UI verdict must name:
- runtime recipe used
- flow or screen/state reviewed
- reviewed screenshot paths
- viewport for each reviewed screenshot
- behavioral verdict

When end-user design-fidelity applies, also include:
- design-fidelity verdict
- per-dimension scores for the scorecard owned by
  the project design-fidelity governance reference
- total score and threshold result
- anti-pattern matches
- `blocking` defects
- `advisory` notes

When end-user design-fidelity is underspecified, include:
- `design-fidelity verdict: underspecified`
- missing owner inputs:
  - missing anchors,
  - missing archetype or justified exception,
  - or other absent required context
- any `blocking` defects still observed
- any `advisory` notes still worth reporting

When internal/admin default posture applies, include:
- `design-fidelity verdict: not-applicable`
- `blocking` defects
- `advisory` notes

## Review Notes

- `behavioral verdict: pass` does not soften `design-fidelity verdict: reject`
- `design-fidelity verdict: underspecified` is not permission to approve weak
  end-user UI claims
- use `blocking` for visible defects, not as a synonym for dislike

## Related Owners

- runtime-legibility feature map:
  `../../verification-before-completion/references/runtime-proof-escalation.md`
- end-user design governance:
  the project design-fidelity governance reference
- UI proof process:
  the project UI verification strategy, when present
