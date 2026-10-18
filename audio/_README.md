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

### Rebuild after paragraph-boundary repairs

Refresh the affected language's TTS sidecar before generating narration:

```sh
python3 scripts/dump_tts_text.py --slug BOOK --chapter N --lang LANG
python3 scripts/generate_audio.py --slug BOOK --chapter N --lang LANG --dry-run
python3 scripts/generate_audio.py --slug BOOK --chapter N --lang LANG
```

Continuation-only changes reuse the existing narration clips and remove the
inserted pauses. Text moved between reference units invalidates only those
units' narration caches. Do not renumber the references.

The renderer decodes the final, treated clips to uniform PCM and measures their
sample counts before assembly. Measuring untreated MP3 files and then assembling
treated files can accumulate timing drift. PCM concatenation also avoids decoder
state leaking between compressed clips. Intermediate `.concat.wav` files and
their metadata stay in the ignored `_work/` cache.

After a chapter changes, regenerate its Opus encoding, ambient track, and
cinematic timeline; then refresh the book manifest after all media are final.
`generate_audio.update_book_manifest()` updates content hashes even when every
narration clip was reused. Keep voice and ambient durations within encoding
tolerance of the timing sidecar, and check that continuation records start at
the preceding spoken record's end.

The ambient renderer also loops decoded PCM beds. Looping MP3 packets can move
scene boundaries through repeated encoder padding.
Word highlights are bounded by their decoded paragraph clips. Oversized MP3
masters remain local; manifests use Opus when an MP3 exceeds the host's 25 MiB
per-file limit.

Regression checks (requires PyYAML, requests, and FFmpeg):

```sh
python3 -m unittest discover -s scripts -p 'test_*timing.py' -v
python3 -m unittest discover -s scripts -p 'test_audio_manifest_refresh.py' -v
```

See [docs.wheelofheaven.world Audiobook Pipeline](https://docs.wheelofheaven.world/contributing/dev/audiobook-pipeline/)
for the full workflow including voice casting, cost estimation,
running the script, troubleshooting, and player integration.
