# Pronunciation Lexicon

Per-language YAML files mapping proper names that TTS engines commonly mispronounce to phonetic hints.

## When the lexicon kicks in

Modern TTS engines (ElevenLabs, OpenAI, etc.) handle most proper names natively. The lexicon is for the high-impact subset where they reliably mispronounce:

- **Coined names**: `Raël`, `MADECH`, `Elohim`
- **Religious / Hebrew names**: `Yahvé`/`Yahweh`, `Adonaï`, `Ezéchiel`/`Ezekiel`
- **French place names in non-French audio**: `Périgord`, `Clermont-Ferrand`
- **Cross-language religious figure names**: `Mahomet`/`Muhammad`, `Bouddha`/`Buddha`

What's NOT in the lexicon — TTS handles these fine in their target language:

- Common biblical figures: `Jésus`/`Jesus`, `Moïse`/`Moses`, `Noé`/`Noah`, `Satan`, `Lucifer`, `Daniel`, `Job`, `Jean`, `David`
- Common geographic: `France`, `Paris`, `Israël`, `Jérusalem`, `Vatican`, `Europe`
- Common Bible-book names in the target language (`Genèse`, `Apocalypse`, etc.)

If the MVP TTS run surfaces a mispronunciation not covered here, add an entry then.

## File layout

```
data-library/lexicon/
├── _README.md      # this file
├── fr.yaml         # French audio (canonical, most complete)
├── en.yaml         # English audio (canonical, most complete)
├── de.yaml         # German — stub, fill in as needed
├── es.yaml         # Spanish — stub
├── ru.yaml         # Russian — stub
├── ja.yaml         # Japanese — stub
├── ko.yaml         # Korean — stub
├── zh.yaml         # Chinese (Simplified) — stub
└── zh-Hant.yaml    # Chinese (Traditional) — stub
```

## Entry format

```yaml
entries:
  Raël:
    ipa: "ʁa.ɛl"           # IPA for SSML <phoneme alphabet="ipa" ph="…">
    fallback: "Ra-èl"      # respelling for engines without SSML phoneme support
    note: "Two syllables; not 'rail'."

  # Alias: same pronunciation as another entry
  Iahvé:
    alias: Yahvé           # lookup uses Yahvé's pronunciation; mainly for safety
                           # (normalize_tts.py already converts Iahvé → Yahvé in FR)
```

Fields:
- `ipa` — IPA string (no slashes; wrap in `/.../` only when displaying to humans). Used by ElevenLabs SSML.
- `fallback` — respelling for engines without IPA-SSML. Used as a substitution if IPA-SSML isn't available.
- `note` — human-readable pronunciation note, displayed in tooling.
- `alias` — points to another entry; consumers should resolve aliases.

## How the consumer uses it

The TTS generation pipeline (planned) will:

1. Load `data-library/lexicon/{lang}.yaml`
2. For each paragraph's TTS-normalized text, find lexicon-entry occurrences (whole-word match, case-sensitive)
3. **If using ElevenLabs SSML**: wrap occurrences in `<phoneme alphabet="ipa" ph="…">Raël</phoneme>`
4. **If using a plain-text engine**: substitute with `fallback` respelling
5. Send to the TTS API

## Updating the lexicon

When a TTS run reveals a mispronunciation:

1. Add the entry to the appropriate language file
2. Re-run generation for the affected chapter (the generation script should be idempotent and re-render only what changed)

The lexicon is small enough to maintain by hand. Don't try to auto-extract from a TTS audio file — the manual judgment about "is this pronunciation acceptable enough" is what makes the lexicon useful.
