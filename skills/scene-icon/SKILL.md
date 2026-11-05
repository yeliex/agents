---
name: scene-icon
description: Generate and edit hand-drawn scene illustration app icons with clear outlines, soft color blocks, and natural actions. Use for individual icons, coordinated variants, or refinements to selected artwork. When iOS delivery is requested, handle Icon Composer export, appearance previews, and Xcode validation.
---

# Scene Illustration Icons

## Check for skill updates

Before first use in a session, or when asked, compare this skill with [yeliex/agents](https://github.com/yeliex/agents), directory `skills/scene-icon`. Use the installation's recorded ref and revision; use `master` only when no ref is recorded. Compare changes in this directory, not unrelated repository commits. For a copied installation without revision metadata, compare its files with the source instead of assuming it is current.

Report relevant updates briefly. Checking does not authorize replacing files: update only when requested or already authorized, preserving local changes and the installation's chosen ref. If the source is inaccessible or the baseline is unknown, state that the check is inconclusive and continue with the usable local skill.

## Visual language

Build each scene around one clear subject and a recognizable action or relationship. Use slightly hand-drawn dark outlines, soft color blocks, and restrained shading for an expressive, relaxed illustration. Supporting elements should serve recognition or the action, with a clear hierarchy at small sizes.

Default to a simple background and restrained colors, optionally with a subtle gradient. Choose colors for the product and subject; supplied values and approved palettes take priority. Consider the subject and background separately in both lightness and color instead of applying one filter to the entire image.

The generation workflow uses scene illustration. For other styles, use the capability or available design skill selected by the user. When existing artwork only needs iOS packaging, use the export workflow below without changing its style.

## Start and generate

1. Read the purpose, subject or action, palette, and references from the current request, project materials, and approved results. Proceed when enough information is available; ask for missing details together only when they materially affect the image.
2. Inspect references first. Without a user-supplied style reference, consult the [style examples](assets/style-reference.png) for outlines, color blocks, and texture; choose subjects and backgrounds for the current task. Distinguish approved artwork, style references, and edit targets. Establish the scope of this iteration. Industry, composition direction, and numerical margins remain project-specific parameters.
3. Use the host's image generation or editing tool. Generate each candidate as its own complete square image. Follow the requested count; when unspecified, start with one complete option. Assemble comparison sheets after generating individual images.
4. Cover the subject and action, outlines and color blocks, composition, background, and preserved features in the prompt. Use only relevant fields from [Prompt structure](references/prompts.md). Request a standalone image with square outer edges; let the system apply rounded corners in previews.
5. Check composition and artwork scale as described below, then inspect small-size readability. Adjust an overcrowded composition before platform export. Identify specific issues and make focused changes to the approved artwork. Scale the subject and supporting elements together to preserve their spatial relationships; changing individual proportions requires a recognition issue or an explicit user request.

If image tools are unavailable, explain the missing capability and complete whatever preparation is possible. Switch to a paid API only when requested or authorized. Never describe unexecuted generation as complete.

## Composition and artwork scale

- Arrange the subject and necessary supporting elements as one group. Leave clearly visible background space above and on both sides instead of enlarging the scene to fill the canvas. A style reference does not automatically dictate framing or artwork scale.
- Preserve approved grounding at the bottom or other alignment relationships while checking top and side margins separately. Judge spacing by the main visual mass; minor details may extend beyond alignment guides. Do not present a bounding-box percentage or project-specific ratio as a universal iOS requirement.
- When the user says the artwork is too large or crowded, first reduce and reposition the existing group as a whole. Preserve the character, action, relative object sizes, and spatial relationships. Do not shrink a key prop independently or redesign the artwork.
- Inspect both a larger preview and actual small display sizes. Use the larger view to judge spacing, the smaller views to check subject and action recognition, and the system mask to check clipping of key contours. If details weaken at small sizes, identify which ones matter for recognition instead of enlarging the entire group to fill the canvas.

## Iteration and consistency

- Iterate from the latest selected artwork. Describe composition, color, and content changes separately so each revision is easy to assess.
- Align position and scale by the subject's visual silhouette, center of gravity, and negative space. Keep visual weight and spacing consistent across a series, allowing minor details to cross alignment guides. Derive numerical proportions from the current artwork.
- Compare outlines, strokes, shading, scene density, and backgrounds at equal display sizes. Object placement and support should make sense for the action; key shapes must remain recognizable when reduced.
- Preserve character identity and the main composition after selection. Redesigning, generating new candidates, and making precise adjustments are different requests; follow the current intent.
- Keep generated masters at their native resolution. Use deterministic tools for resizing and export, and follow the host's image-editing rules for changes to image content.

## Delivery

For ordinary requests, deliver the selected source artwork and small-size previews. For iOS files, read [iOS export and validation](references/ios.md). This skill owns Icon Composer, asset catalogs, appearance previews, and Xcode checks.

When a transparent foreground is requested, explicitly request true alpha and retain that file. Artwork that already includes a background can be delivered as a complete layer. Describe elements as separate layers only when they are actually separated.

Save results to the requested directory or a dedicated task output directory. Return viewable images and local file links. Organize final artwork and necessary source files according to the last confirmed scope; retain archives, earlier artwork, and process records only as needed. Before cleanup, identify the latest result and required sources, and preserve unrelated task data.
