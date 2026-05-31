# Audio Generation Config

Config + workspace for the ElevenLabs audiobook generation pipeline.

## What's here

| File / Dir | Purpose |
|---|---|
| `voices.yaml` | Per-(speaker, language) ElevenLabs voice IDs + voice settings + pause durations + model choice |
| `_work/` (gitignored) | Per-paragraph audio cache, regenerable. Concatenated into per-chapter MP3s during the pipeline run |

## What's NOT here

The final per-chapter audio files live in
[`assets.wheelofheaven.world/audio/`](https://github.com/wheelofheaven/assets.wheelofheaven.world/tree/main/audio),
served at `https://assets.wheelofheaven.world/audio/{lang}/{slug}/c{N}.mp3`.

The TTS-normalized source text lives at
[`data-library/{slug}/tts/chapter-N.{lang}.json`](../).

The pronunciation lexicons live at [`data-library/lexicon/{lang}.yaml`](../lexicon/).

## Pipeline overview

```
data-library/{slug}/tts/chapter-N.{lang}.json    (text)
                +
data-library/lexicon/{lang}.yaml                  (pronunciation hints)
                +
data-library/audio/voices.yaml                    (speaker → voice mapping)
                +
data-library/scripts/generate_audio.py            (the script)
                ↓
ElevenLabs API
                ↓
data-library/audio/_work/{slug}/{lang}/c{N}/p{n}.mp3    (per-paragraph cache)
                ↓
assets.wheelofheaven.world/audio/{lang}/{slug}/c{N}.mp3 + c{N}.timing.json
```

## Quick reference

See [docs.wheelofheaven.world Audiobook Pipeline](https://docs.wheelofheaven.world/contributing/dev/audiobook-pipeline/)
for the full workflow including voice casting, cost estimation,
running the script, troubleshooting, and player integration.
