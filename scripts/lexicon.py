#!/usr/bin/env python3
"""Load + apply pronunciation lexicons.

Two operations:
- `load(lang)` — returns dict of entries with aliases resolved
- `apply_ssml(text, lang)` — wraps lexicon-entry occurrences in
  ElevenLabs <phoneme alphabet="ipa" ph="…"> tags
- `apply_fallback(text, lang)` — substitutes occurrences with fallback respellings

Standalone usage:
    python3 lexicon.py --lang fr --show         # dump lexicon
    python3 lexicon.py --lang fr --test         # apply to a few test sentences
    python3 lexicon.py --lang fr --coverage     # report which lexicon entries actually appear in the corpus
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print('Install PyYAML: pip install pyyaml', file=sys.stderr)
    sys.exit(1)

LIB = Path(__file__).resolve().parent.parent  # data-library/
LEXICON_DIR = LIB / 'lexicon'


def load(lang: str) -> dict[str, dict]:
    """Load lexicon for a language. Returns {name: {ipa, fallback, note}}.

    Aliases are resolved: `Iahvé: {alias: Yahvé}` becomes
    `Iahvé: <Yahvé's entry>`.
    """
    path = LEXICON_DIR / f'{lang}.yaml'
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    entries = data.get('entries') or {}
    # Resolve aliases
    resolved = {}
    for name, entry in entries.items():
        if entry is None:
            continue
        if 'alias' in entry:
            target = entry['alias']
            if target in entries and 'alias' not in (entries[target] or {}):
                resolved[name] = dict(entries[target])
                resolved[name]['_aliased_from'] = target
            # else: dangling alias, skip
        else:
            resolved[name] = entry
    return resolved


def _build_regex(entries: dict) -> re.Pattern:
    """Build a single regex that matches any lexicon entry as a whole word."""
    # Sort by length desc so longer matches win (e.g. "Religion Raëlienne" before "Raël")
    names = sorted(entries.keys(), key=len, reverse=True)
    if not names:
        return re.compile(r'(?!)')  # never-match
    # Word boundaries are tricky with non-ASCII; use lookarounds for safety
    pattern = '|'.join(re.escape(n) for n in names)
    return re.compile(r'(?<![\wÀ-ſ])(' + pattern + r')(?![\wÀ-ſ])')


def apply_ssml(text: str, lang: str) -> str:
    """Wrap each lexicon entry with <phoneme alphabet="ipa" ph="…"> SSML tag."""
    entries = load(lang)
    if not entries:
        return text
    pat = _build_regex(entries)

    def repl(m):
        name = m.group(1)
        entry = entries[name]
        ipa = entry.get('ipa')
        if not ipa:
            return name
        return f'<phoneme alphabet="ipa" ph="{ipa}">{name}</phoneme>'

    return pat.sub(repl, text)


def apply_fallback(text: str, lang: str) -> str:
    """Substitute each lexicon entry with its fallback respelling."""
    entries = load(lang)
    if not entries:
        return text
    pat = _build_regex(entries)

    def repl(m):
        name = m.group(1)
        entry = entries[name]
        return entry.get('fallback', name)

    return pat.sub(repl, text)


_AFFIX_LEAD = '«»"“”‘’\'(¿¡'
_AFFIX_TRAIL = '.,;:!?…)»"“”‘’\''


def _split_affix(tok: str) -> tuple[str, str, str]:
    """Split a token into (leading punct, core, trailing punct). Keeps internal
    hyphens (fallback respellings use them)."""
    i = 0
    while i < len(tok) and tok[i] in _AFFIX_LEAD:
        i += 1
    j = len(tok)
    while j > i and tok[j - 1] in _AFFIX_TRAIL:
        j -= 1
    return tok[:i], tok[i:j], tok[j:]


def relabel_to_display(words: list[dict], lang: str, original_text: str) -> list[dict]:
    """Inverse of apply_fallback for the timing word-stream.

    The audio is synthesized from fallback respellings (e.g. "YAH-way") so the
    voice pronounces names correctly, but the caption/timing stream must show
    the ORIGINAL spelling ("Yahweh"). We walk the lexicon matches in the
    original text in order and rewrite the matching fallback-token run in the
    word stream back to the original surface form, preserving timestamps and
    surrounding punctuation. Order-based matching disambiguates entries that
    share a fallback (e.g. fr Yahvé/Yahweh → "YAH-way")."""
    entries = load(lang)
    if not entries or not words:
        return words
    pat = _build_regex(entries)
    expected = []  # ordered (fallback_tokens, original_surface)
    for m in pat.finditer(original_text):
        fb = entries[m.group(1)].get('fallback')
        if fb:
            expected.append((tuple(fb.split()), m.group(1)))
    if not expected:
        return words

    out, i, e, n = [], 0, 0, len(words)
    while i < n:
        if e < len(expected):
            toks, surface = expected[e]
            L = len(toks)
            if i + L <= n and tuple(_split_affix(words[i + k]['w'])[1] for k in range(L)) == toks:
                lead = _split_affix(words[i]['w'])[0]
                trail = _split_affix(words[i + L - 1]['w'])[2]
                out.append({'w': lead + surface + trail,
                            'start': words[i]['start'], 'end': words[i + L - 1]['end']})
                i += L
                e += 1
                continue
        out.append(words[i])
        i += 1
    return out


def coverage_report(lang: str) -> dict:
    """Walk all TTS sidecars and count how often each lexicon entry appears.
    Returns {name: count}. Useful for knowing which lexicon entries are dead weight.
    """
    entries = load(lang)
    if not entries:
        return {}
    counts = {name: 0 for name in entries}
    pat = _build_regex(entries)

    for book_dir in LIB.iterdir():
        tts_dir = book_dir / 'tts'
        if not tts_dir.exists():
            continue
        for sidecar_path in tts_dir.glob(f'chapter-*.{lang}.json'):
            sidecar = json.loads(sidecar_path.read_text())
            for entry_data in sidecar.values():
                text = entry_data.get('text') or ''
                if not text:
                    continue
                for m in pat.finditer(text):
                    counts[m.group(1)] += 1
    return counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', default='fr', help='Language code (default: fr)')
    ap.add_argument('--show', action='store_true', help='Dump the loaded lexicon')
    ap.add_argument('--test', action='store_true', help='Run a few test sentences through SSML + fallback')
    ap.add_argument('--coverage', action='store_true', help='Report frequency of each lexicon entry in the corpus')
    args = ap.parse_args()

    if args.show:
        entries = load(args.lang)
        print(f'{args.lang}.yaml: {len(entries)} entries (aliases resolved)\n')
        for name, entry in sorted(entries.items()):
            origin = f' (← {entry["_aliased_from"]})' if '_aliased_from' in entry else ''
            ipa = entry.get('ipa', '—')
            fb = entry.get('fallback', '—')
            note = entry.get('note', '')
            print(f'  {name}{origin}')
            print(f'    ipa:      /{ipa}/')
            print(f'    fallback: {fb}')
            if note:
                print(f'    note:     {note}')
        return

    if args.coverage:
        counts = coverage_report(args.lang)
        if not counts:
            print(f'No lexicon entries loaded for {args.lang}.')
            return
        print(f'{args.lang}.yaml: lexicon entry frequency across all {args.lang} TTS sidecars\n')
        total = sum(counts.values())
        for name, n in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f'  {n:5d}  {name}')
        print(f'\n  Total: {total} occurrences across {sum(1 for v in counts.values() if v > 0)}/{len(counts)} entries')
        unused = [n for n, c in counts.items() if c == 0]
        if unused:
            print(f'\n  Unused entries (consider removing): {", ".join(unused)}')
        return

    if args.test:
        if args.lang == 'fr':
            samples = [
                "Raël rencontra Yahvé près de Clermont-Ferrand.",
                "Les Elohim parlent à travers Ezéchiel et Mahomet.",
                "Le MADECH est un mouvement raëlien.",
                "Bouddha et Mahomet sont des messagers, comme Raël.",
            ]
        elif args.lang == 'en':
            samples = [
                "Raël met Yahweh near Clermont-Ferrand.",
                "The Elohim spoke through Ezekiel and Muhammad.",
                "MADECH is a Raëlian movement.",
            ]
        else:
            samples = ["(no test samples for this language; use --show or --coverage)"]
        for s in samples:
            ssml = apply_ssml(s, args.lang)
            fb = apply_fallback(s, args.lang)
            print(f'SRC : {s}')
            print(f'SSML: {ssml}')
            print(f'FB  : {fb}')
            print()
        return

    ap.print_help()


if __name__ == '__main__':
    main()
