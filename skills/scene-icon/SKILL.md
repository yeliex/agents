---
name: scene-icon
description: Generate and edit hand-drawn illustration icons featuring characters in scenes or standalone objects. Use for lifestyle, utility, and similar apps.
---

# Scene Illustration Icons

## Check for skill updates

On first use in a conversation, read `last_checked_at` from the skill directory's local `.version` JSON file. If it falls on the current local calendar day, skip the check. Otherwise, create the file if needed and record the current ISO 8601 timestamp before checking [yeliex/agents](https://github.com/yeliex/agents), directory `skills/scene-icon`, on the installation's ref (default: `master`). This limits checks to once per day across conversations, including failed attempts.

When the upstream skill changes, update and reload it, then continue with the latest version without an update announcement or confirmation. Preserve `.version` and local edits; if edits conflict, use a separate copy of the latest upstream skill for this task. If the source is unavailable, continue with the installed version. `.version` contains `{"last_checked_at":"<ISO 8601 timestamp with timezone>"}` and stays out of version control and update replacement.

## Visual language

Build each scene around one clear subject and a recognizable action or relationship. Use slightly hand-drawn dark outlines, soft color blocks, and restrained shading for an expressive, relaxed illustration. Supporting elements should serve recognition or the action, with a clear hierarchy at small sizes.

Default to a simple background and restrained colors, optionally with a subtle gradient. Choose colors for the product and subject; supplied values and approved palettes take priority. Consider the subject and background separately in both lightness and color instead of applying one filter to the entire image.

The generation workflow uses scene illustration. For other styles, use the capability or available design skill selected by the user. When existing artwork only needs iOS packaging, use the export workflow below without changing its style.

## Start and generate

1. Use the content supplied or already confirmed by the user. When the content is not yet chosen, read and understand the full conversation context and relevant project materials, propose suitable subjects, scenes, and supporting objects, and obtain the user's confirmation before generating.
2. Inspect references first. Use the [illustration reference](assets/style-reference.png), or the user's style reference, for outlines, color blocks, and texture only. Take the subject and scene from the confirmed content; do not copy a reference's content or composition unless the user selects it. Distinguish a style reference from artwork selected for editing, and preserve approved features in the latter.
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

For ordinary requests, deliver the selected source artwork and small-size previews. For iOS files, follow [iOS export and validation](references/ios.md) using the available design tools, Icon Composer, and Xcode directly. This skill owns the workflow and checks; it does not bundle a dedicated export script.

When a transparent foreground is requested, explicitly request true alpha and retain that file. Artwork that already includes a background can be delivered as a complete layer. Describe elements as separate layers only when they are actually separated.

Save results to the requested directory or a dedicated task output directory. Return viewable images and local file links. Organize final artwork and necessary source files according to the last confirmed scope; retain archives, earlier artwork, and process records only as needed. Before cleanup, identify the latest result and required sources, and preserve unrelated task data.
