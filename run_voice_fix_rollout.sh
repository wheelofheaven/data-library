#!/usr/bin/env bash
# One-off: roll out the voice fix (stability 0.75 + loudnorm + intro-norm)
# across all live audio. Per (book,lang):
#   1. generate_audio (regen Narrator/Raël paras, normalize all, intro)  [retry]
#   2. generate_ambient (re-tile beds to the new timing)
#   3. transcode_audio (mp3 -> opus)
#   4. generate_audio again (cached, $0) -> fold manifest w/ correct hashes
# Idempotent + per-paragraph cached, so re-runs resume cheaply.
set -uo pipefail
cd "$(dirname "$0")"
set -a; . ./.env; set +a
PY="$(pwd)/.venv/bin/python"
TBWTT=the-book-which-tells-the-truth
ETMTTP=extraterrestrials-took-me-to-their-planet

gen_retry() {  # $1=slug $2=lang
  for i in 1 2 3 4 5 6; do
    "$PY" scripts/generate_audio.py --slug "$1" --lang "$2" && return 0
    echo "  !! generate_audio $1/$2 failed, retry $i"; sleep 5
  done
  echo "  XX generate_audio $1/$2 gave up"; return 1
}

do_lang() {  # $1=slug $2=lang
  echo "############ $1 / $2 ############"
  gen_retry "$1" "$2" || return 1
  "$PY" scripts/generate_ambient.py --slug "$1" --lang "$2"   2>&1 | tail -3
  "$PY" scripts/transcode_audio.py  --slug "$1" --lang "$2"   2>&1 | tail -2
  gen_retry "$1" "$2" || return 1   # fold manifest (cached)
  echo "==== done $1/$2 ===="
}

for lang in en de es fr ja ko ru zh zh-Hant; do
  do_lang "$TBWTT" "$lang"
done
do_lang "$ETMTTP" en

echo "ALL_ROLLOUT_DONE"
