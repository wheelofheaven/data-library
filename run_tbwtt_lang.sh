#!/usr/bin/env bash
# Full per-language TBWTT audio pipeline (local only — does NOT deploy).
# Usage: run_tbwtt_lang.sh <lang>
set -euo pipefail
cd "$(dirname "$0")"
set -a; . ./.env; set +a
LANG_CODE="$1"
SLUG="the-book-which-tells-the-truth"
PY=./.venv/bin/python

echo "########## [$LANG_CODE] 1/4 voice generation (ElevenLabs TTS) ##########"
$PY scripts/generate_audio.py --slug "$SLUG" --lang "$LANG_CODE"

echo "########## [$LANG_CODE] 2/4 transcode MP3 -> Opus ##########"
$PY scripts/transcode_audio.py --slug "$SLUG" --lang "$LANG_CODE"

echo "########## [$LANG_CODE] 3/4 ambient beds (cached SFX, ~free) ##########"
$PY scripts/generate_ambient.py --slug "$SLUG" --lang "$LANG_CODE"

echo "########## [$LANG_CODE] 4/4 refresh manifest (cached re-run, \$0) ##########"
$PY scripts/generate_audio.py --slug "$SLUG" --lang "$LANG_CODE"

echo "########## [$LANG_CODE] DONE ##########"
