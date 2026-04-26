# User Apps Atomic Design Convention

Owner for end-user UI composition in web and mobile applications.

- This file defines atomic UI composition policy.
- Text-overflow ownership lives in
  `text-constraints.md`.

## Layers

| Layer | Owns |
| --- | --- |
| Atoms | smallest reusable primitives: button, input, chip, icon, badge |
| Molecules | compact combinations with one intent: search header, compare row, login field row |
| Organisms / Patterns | larger reusable sections: error panel, auth action block, list section |
| Screens / Routes | composition-only layer that arranges patterns and binds feature state |

## Composition Rules

- screens and routes should mostly compose existing atoms, molecules, and
  patterns,
- duplicated reusable structure must not stay as route-local primitive markup,
- if structure appears in 2+ places, or clearly spans surfaces, promote it,
- keep business logic out of visual atoms and molecules when possible,
- avoid parallel component families for same semantic role.

## Show, Do Not Narrate

Prefer affordance over explanation.

- express state, hierarchy, emphasis, selection, grouping, and primary action
  through layout, spacing, color, iconography, motion, and control shape first,
- use labels, helper text, and descriptions as support, not primary
  disambiguation,
- treat explanatory prompts, upgrade nudges, helper paragraphs, and "what this
  means" labels as last resort,
- if surface needs multiple lines of explanation for core interaction, treat it
  as design smell and rework UI semantics,
- when explanatory copy remains, it must be minimal and justified by domain
  ambiguity, trust/risk, or recovery needs the interface cannot carry alone.

## Text Constraint Rule

Reusable components must not invent truncation, clamping, or overflow behavior.
Follow `text-constraints.md`.

## Design Gallery Rule

When a project has a design-gallery or component-inventory surface, update it in the same change when a reusable atom, molecule, or pattern changes materially. If one surface is intentionally deferred, planning artifacts must record exact follow-up scope.

## Allowed Inline Markup At Screen Level

Inline markup is acceptable only when all are true:

- layout-only scaffolding for that screen,
- not reused elsewhere,
- not a design-system semantic component.

If one fails, extract to proper atomic layer.

## Review Gate

UI work is not complete until review can answer:

- which atoms, molecules, and patterns were reused,
- which new reusable block was added and why existing inventory failed,
- which route-level blocks stayed inline and why they are intentionally local,
- which design gallery updates were made,
- which critical states or actions are understandable from affordance alone,
- where explanatory copy remains and why interface semantics could not carry it,
- which labels, prompts, or helper text were removed or avoided because
  structure carried meaning.

If review cannot answer these, change fails atomic-design gate.
