---
name: scene-icon
description: Generate and edit hand-drawn illustration icons featuring characters in scenes or standalone objects. Suited to apps with clear usage scenarios, such as lifestyle and utility apps.
---

# Scene Illustration Icons

## Check for skill updates

On first use in a conversation, read `last_checked_at` from the skill directory's local `.version` JSON file. If it falls on the current local calendar day, skip the check. Otherwise, create the file if needed and record the current ISO 8601 timestamp before checking [yeliex/agents](https://github.com/yeliex/agents), directory `skills/scene-icon`, on the installation's ref (default: `master`). This limits checks to once per day across conversations, including failed attempts.

When the upstream skill changes, silently update and reload it, then continue with the latest version. Preserve `.version` and local edits; if edits conflict, use a separate copy of the latest upstream skill for this task. If the source is unavailable, continue with the installed version. `.version` contains `{"last_checked_at":"<ISO 8601 timestamp with timezone>"}`. Keep it local, git-ignored, and preserved across updates.

## Visual language

Build each scene around one clear subject and a recognizable action or relationship. Use clear, continuous dark outlines with slight hand-drawn variation, clean soft color blocks, and restrained shading for an expressive, relaxed illustration. Keep texture subtle and localized so it preserves edge clarity and separation between shapes. Supporting elements should serve recognition or the action, with a clear hierarchy at small sizes.

Default to a simple background and restrained colors, optionally with a subtle gradient. Choose colors for the product and subject; supplied values and approved palettes take priority. Choose lightness and color separately for the subject and background.

## Start and generate

1. Use the content supplied or already confirmed by the user. When the content is not yet chosen, read and understand the full conversation context and relevant project materials, propose suitable subjects, scenes, and supporting objects, and obtain the user's confirmation before generating.
2. Inspect references first. Use the [illustration reference](assets/style-reference.png), or the user's style reference, to guide outlines, color blocks, and texture. Use the confirmed content for the subject and scene. For edits, work from the selected artwork and preserve its approved features and composition.
3. Use the host's image generation or editing tool. Generate each candidate as its own complete square image. Follow the requested count; when unspecified, start with one complete option. When a comparison is requested, assemble it from the individual images.
4. Cover the subject and action, outlines and color blocks, composition, background, and preserved features in the prompt. Describe the request naturally, using the relevant points in [Prompt guidance](references/prompts.md). Request a standalone image with square outer edges; let the target platform apply its mask.
5. After each generation or revision, assess the result in its intended use using the [composition and artwork scale checks](#composition-and-artwork-scale). Check position, margins, and recognition at the target display sizes, and resolve issues before delivery or platform export.

## Composition and artwork scale

- Set the content's position, scale, and negative space for its intended use throughout design and revision. For iOS icons, assess the composition within the system mask and at the sizes where the app icon will appear.
- Judge spacing by the main visual mass. Preserve approved grounding and alignment, with room around key contours; minor details may extend beyond alignment guides. Derive proportions from the artwork and its intended use.
- If the content is too large, too small, or off-center for the intended use, scale and reposition the subject and supporting elements as a group. Preserve character identity, action, relative object sizes, and spatial relationships.
- Make the subject and key action readable at small display sizes. Simplify nonessential details or improve separation when needed. Check using the tool's display scaling or temporary renders.

## Iteration and consistency

- Iterate from the latest selected artwork. Describe composition, color, and content changes separately so each revision is easy to assess.
- Keep visual weight, spacing, and grounding consistent across a series, judged by the main visual mass.
- Compare outlines, strokes, shading, scene density, and backgrounds at equal display sizes. Object placement and support should make sense for the action; key shapes must remain recognizable when reduced.
- For revisions, preserve the selected character identity and main composition except for the requested changes.
- Keep generated masters at their native resolution. Use deterministic tools for resizing and format export.

## Delivery

By default, deliver the selected final icon file. Add platform resources or review previews when requested. For iOS resources, follow [iOS export and validation](references/ios.md) using the available design tools, Icon Composer, and Xcode directly.

For transparent foregrounds, request and retain a true alpha channel. Deliver flattened artwork as a single image; retain editable background and foreground files when supplied separately.

Save the final icon and required source files to the requested directory or a dedicated task output directory. Return viewable images and local file links.
