# Scene images — audioplay cinematic backgrounds

Language-neutral background stills for the **cinematic view** of the audiobook
player and the YouTube video export. One image per scene id, reused across all
9 site languages (captions are an overlay — never bake text into the art).

## Files

| File | Role |
|------|------|
| `scenes.yaml` | Image-generation manifest: style bible + per-scene prompts. The Codex/OpenAI handoff. |
| `<scene>.jpg` | Generated still for a scene id (e.g. `elohim-vessel.jpg`). Source of truth. |

The `<scene>` ids match the `scene:` values in `../cues/c*.yaml`. The default
backdrop is `default.jpg` (shown wherever no specific scene is cued).

## Spec

- **Aspect:** 16:9. Generate at **2560×1440** (zoom headroom for the Ken-Burns
  pan); the pipeline outputs 1080p.
- **No text/watermark** in the image. Leave negative space in the lower third
  for the subtitle overlay.
- **Style consistency:** every prompt inherits `style.prefix`/`style.suffix`
  from `scenes.yaml` so the slideshow reads as one film.

## Workflow

1. **Author scenes (Phase 1a).** Expand `../cues/c*.yaml` into a real shot
   list (distinct named beats), and add a matching entry to `scenes.yaml` for
   each new scene id. Today the cues use a single placeholder (`elohim-vessel`).
2. **Generate (Codex + OpenAI).** For each `pending` scene, compose
   `prefix + prompt + suffix`, generate at `gen_size`, write `<id>.jpg`, set
   `status: generated`, record the `seed`.
3. **Review.** Human accepts (`status: accepted`) or requests a redo
   (`status: redo` + prompt tweak).
4. **Sync to CDN** alongside the audio assets:
   `assets.wheelofheaven.world/images/cinematic/<book>/<scene>.jpg`.

The timeline builder references scene ids only — it does not need the images to
exist. The whole pipeline runs end-to-end with `default` placeholders before any
art is produced.
