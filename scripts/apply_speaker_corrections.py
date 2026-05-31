#!/usr/bin/env python3
"""Apply declarative speaker re-attributions to chapter JSON files in place.

Edit the CORRECTIONS dict below: {(book_slug, chapter_n, paragraph_n): new_speaker}.
The script is idempotent — paragraphs already matching the target speaker are
skipped. Validates that the paragraph exists and currently has a different
speaker (so a wrong key is loud).
"""

import json
import sys
from pathlib import Path

LIB = Path(__file__).resolve().parent.parent  # data-library/

# (book_slug, chapter_n, paragraph_n) -> new_speaker
CORRECTIONS = {
    # === ETTMTTP ch2: 49 paragraphs ===
    # Narrator → Yahweh: misattributed Yahweh speech blocks
    # The "second message" speech (p22-p43)
    ('extraterrestrials-took-me-to-their-planet', 2, 22): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 23): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 24): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 25): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 26): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 27): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 28): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 29): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 30): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 31): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 32): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 33): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 34): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 35): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 36): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 37): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 38): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 39): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 40): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 41): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 42): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 43): 'Yahweh',
    # The eternals + biological robots discourse (p50-p60)
    ('extraterrestrials-took-me-to-their-planet', 2, 50): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 51): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 52): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 53): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 54): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 55): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 56): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 57): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 58): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 59): 'Yahweh',
    ('extraterrestrials-took-me-to-their-planet', 2, 60): 'Yahweh',
    # Yahweh's closing line (p129)
    ('extraterrestrials-took-me-to-their-planet', 2, 129): 'Yahweh',

    # Yahweh → Narrator: scene description mislabeled as Yahweh
    # Arrival sequence in the ship
    ('extraterrestrials-took-me-to-their-planet', 2, 12): 'Narrator',
    ('extraterrestrials-took-me-to-their-planet', 2, 14): 'Narrator',
    ('extraterrestrials-took-me-to-their-planet', 2, 15): 'Narrator',
    ('extraterrestrials-took-me-to-their-planet', 2, 16): 'Narrator',
    ('extraterrestrials-took-me-to-their-planet', 2, 17): 'Narrator',
    ('extraterrestrials-took-me-to-their-planet', 2, 20): 'Narrator',
    # Dinner scene + transitions
    ('extraterrestrials-took-me-to-their-planet', 2, 65): 'Narrator',
    ('extraterrestrials-took-me-to-their-planet', 2, 67): 'Narrator',
    ('extraterrestrials-took-me-to-their-planet', 2, 68): 'Narrator',
    # Robot machine demo transitions
    ('extraterrestrials-took-me-to-their-planet', 2, 79): 'Narrator',
    ('extraterrestrials-took-me-to-their-planet', 2, 81): 'Narrator',
    ('extraterrestrials-took-me-to-their-planet', 2, 86): 'Narrator',
    # Closing of night-with-companions scene
    ('extraterrestrials-took-me-to-their-planet', 2, 94): 'Narrator',
    # Next-morning setup
    ('extraterrestrials-took-me-to-their-planet', 2, 95): 'Narrator',
    ('extraterrestrials-took-me-to-their-planet', 2, 97): 'Narrator',
}


def main():
    by_book_chap = {}
    for (book, chap, pn), new_spkr in CORRECTIONS.items():
        by_book_chap.setdefault((book, chap), []).append((pn, new_spkr))

    for (book, chap), items in by_book_chap.items():
        path = LIB / book / f'chapter-{chap}.json'
        ch = json.loads(path.read_text())
        changes = 0
        skipped = 0
        for pn, new_spkr in items:
            try:
                p = next(x for x in ch['paragraphs'] if x['n'] == pn)
            except StopIteration:
                print(f'ERROR {book} ch{chap} p{pn}: not found', file=sys.stderr)
                sys.exit(1)
            current = p.get('speaker', '')
            if current == new_spkr:
                skipped += 1
                continue
            print(f'  {book} ch{chap} p{pn}: {current!r} → {new_spkr!r}')
            p['speaker'] = new_spkr
            changes += 1
        if changes:
            path.write_text(json.dumps(ch, ensure_ascii=False, indent=2) + '\n')
            print(f'wrote {path} ({changes} changes, {skipped} already-applied)')
        else:
            print(f'  no changes for {book} ch{chap} ({skipped} already-applied)')


if __name__ == '__main__':
    main()
