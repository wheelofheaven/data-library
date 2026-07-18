#!/usr/bin/env python3
"""Local (Voxtral + mlx-whisper) audiobook backend — the audiobook engine.

The Library books (TBWTT/ETMTTP) are voiced by ElevenLabs (generate_audio.py),
which returns word timings from its `with-timestamps` endpoint. The Timeline
audiobook is voiced LOCALLY: Voxtral-4B-TTS (MLX) synthesizes each paragraph and
mlx-whisper force-aligns the audio to recover word timings — so we produce the
exact same `c{n}.timing.json` + opus contract the web player and build_timeline.py
consume, with no API and no cost.

Deviation from the design note: the note named WhisperX; on Apple Silicon
mlx-whisper is the native fit (MLX ecosystem, no torch). It transcribes rather
than force-aligns, but on clean TTS audio recognition is near-perfect and we map
recognized words back to the known transcript by count.

Output mirrors generate_audio.py exactly:
    assets.wheelofheaven.world/audio/{lang}/{slug}/c{n}.mp3
    assets.wheelofheaven.world/audio/{lang}/{slug}/c{n}.opus
    assets.wheelofheaven.world/audio/{lang}/{slug}/c{n}.timing.json
then update_book_manifest (from generate_audio.py) writes the manifest.

Setup:
    data-library/.venv-tts/bin/python  (mlx-audio, mlx-whisper, soundfile)
    brew install ffmpeg

Usage (from data-library/):
    .venv-tts/bin/python scripts/generate_audio_local.py --slug wheel-of-heaven-timeline --chapter 1 --lang en
    .venv-tts/bin/python scripts/generate_audio_local.py --slug wheel-of-heaven-timeline --chapter 1 --limit 3   # quick validation
    .venv-tts/bin/python scripts/generate_audio_local.py --slug wheel-of-heaven-timeline --list-voices
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf

LIB = Path(__file__).resolve().parent.parent            # data-library/
ASSETS_AUDIO = LIB.parent / "assets.wheelofheaven.world" / "audio"
WORK = LIB / "audio" / "_work_local"                    # separate from ElevenLabs _work

VOXTRAL_MODEL = "mlx-community/Voxtral-4B-TTS-2603-mlx-4bit"
WHISPER_MODEL = "mlx-community/whisper-large-v3-turbo"    # fast; word_timestamps ok
SR = 24000                                               # Voxtral output rate

# Audiobook-first casting: the neutral site voice narrates; scripture is set
# apart. Voxtral voice names — audition with --list-voices, override in
# {book}/voices.local.json.
DEFAULT_VOICES = {
    "Narrator": "neutral_male",
    "Scripture": "neutral_male",   # TODO: distinct preset once voices auditioned
}
# Pause grammar (ms), mirroring generate_audio.py's defaults.
PAUSES = {
    "between_paragraphs": 600,
    "between_speakers": 900,
    "before_title": 1800,
    "after_title": 1200,
}


# ===== ffmpeg helpers (duplicated from generate_audio.py to keep this backend
#       importable from the lightweight MLX venv) =====

def ffprobe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nokey=1:noprint_wrappers=1", str(path)],
        capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def ffmpeg_silence_wav(out_path: Path, seconds: float) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi",
         "-i", f"anullsrc=r={SR}:cl=mono", "-t", f"{seconds:.3f}",
         "-c:a", "pcm_s16le", str(out_path)], check=True)


def ffmpeg_concat_to_mp3(parts: list[Path], out_path: Path) -> None:
    """Concatenate WAV parts, re-encoding to a single mp3."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    listfile = out_path.with_suffix(".concat.txt")
    listfile.write_text("".join(f"file '{p.resolve()}'\n" for p in parts))
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(listfile), "-c:a", "libmp3lame", "-q:a", "2",
         "-ar", str(SR), "-ac", "1", str(out_path)], check=True)
    listfile.unlink(missing_ok=True)


def transcode_opus(mp3_path: Path, opus_path: Path) -> None:
    """libopus voip 40k mono — matches transcode_audio.py."""
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp3_path),
         "-c:a", "libopus", "-b:a", "40k", "-application", "voip",
         "-ac", "1", str(opus_path)], check=True)


# ===== model loading (lazy singletons) =====

_tts = {"model": None}
_whisper_loaded = {"done": False}


def get_tts():
    if _tts["model"] is None:
        from mlx_audio.tts.utils import load
        t0 = time.time()
        print(f"loading Voxtral {VOXTRAL_MODEL} …", flush=True)
        _tts["model"] = load(VOXTRAL_MODEL)
        print(f"  ready in {time.time()-t0:.1f}s", flush=True)
    return _tts["model"]


def list_voices() -> None:
    model = get_tts()
    for attr in ("voices", "available_voices", "speakers", "VOICES"):
        v = getattr(model, attr, None)
        if v:
            print(f"{attr}: {list(v) if not isinstance(v, (list, tuple)) else v}")
            return
    print("No voice registry exposed on the model; POC used 'neutral_male'.")


# ===== synth + align (cached per paragraph) =====

def cache_key(text: str, voice: str) -> str:
    return hashlib.sha256(f"{VOXTRAL_MODEL}|{voice}|{text}".encode()).hexdigest()[:16]


def synth_paragraph(text: str, voice: str, wav_path: Path) -> None:
    """Voxtral synth → 24 kHz mono WAV. Cached by caller."""
    model = get_tts()
    pieces = []
    for result in model.generate(text=text, voice=voice, verbose=False):
        pieces.append(np.asarray(result.audio, dtype=np.float32).reshape(-1))
    audio = np.concatenate(pieces) if pieces else np.zeros(1, dtype=np.float32)
    wav_path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(wav_path, audio, SR)


def align_words(wav_path: Path, known_text: str) -> list[dict]:
    """mlx-whisper word timestamps → [{w,start,end}] relative to wav start.

    The DISPLAYED tokens are ALWAYS the known transcript (whisper is an ASR pass
    and can misrecognize, especially on short segments — e.g. it heard the title
    "A Shape That Recurs" as "The knee, shape that recurs"). Timings come from
    whisper:
      - counts match  → 1:1 relabel, exact per-word timing (the common case;
                        long paragraphs recognize cleanly and match).
      - counts differ → known tokens distributed across the recognized span,
                        proportional to token length. Display stays correct;
                        timings are approximate but monotonic.
    """
    import mlx_whisper
    if not _whisper_loaded["done"]:
        print(f"aligning with {WHISPER_MODEL} …", flush=True)
        _whisper_loaded["done"] = True
    r = mlx_whisper.transcribe(
        str(wav_path), path_or_hf_repo=WHISPER_MODEL,
        word_timestamps=True, language="en", verbose=False,
        condition_on_previous_text=False)
    recognized = []
    for seg in r.get("segments", []):
        for w in seg.get("words", []):
            if (w.get("word") or "").strip():
                recognized.append((round(float(w["start"]), 3),
                                   round(float(w["end"]), 3)))
    known = known_text.split()
    if not known or not recognized:
        return []
    if len(known) == len(recognized):
        return [{"w": kw, "start": s, "end": e}
                for kw, (s, e) in zip(known, recognized)]
    # count mismatch → proportional distribution over the recognized time span
    t0, t1 = recognized[0][0], recognized[-1][1]
    span = max(t1 - t0, 0.01)
    lens = [len(k) + 1 for k in known]
    total = sum(lens)
    out, acc = [], 0
    for k, l in zip(known, lens):
        s = t0 + span * acc / total
        acc += l
        e = t0 + span * acc / total
        out.append({"w": k, "start": round(s, 3), "end": round(e, 3)})
    return out


# ===== chapter assembly =====

def load_voices(slug: str) -> tuple[dict, dict]:
    cfg_path = LIB / slug / "voices.local.json"
    voices = dict(DEFAULT_VOICES)
    pauses = dict(PAUSES)
    if cfg_path.exists():
        cfg = json.loads(cfg_path.read_text())
        voices.update(cfg.get("voices", {}))
        pauses.update(cfg.get("pauses", {}))
    return voices, pauses


def generate_chapter(slug: str, chap: int, lang: str, limit: int | None,
                     force: bool) -> dict:
    src = json.loads((LIB / slug / f"chapter-{chap}.json").read_text())
    paras = src["paragraphs"]
    if limit:
        paras = paras[:limit]
    voices, pauses = load_voices(slug)

    work = WORK / slug / lang / f"c{chap}"
    work.mkdir(parents=True, exist_ok=True)
    silence_dir = WORK / "silence"
    silence_dir.mkdir(parents=True, exist_ok=True)

    def silence(ms: int) -> Path:
        p = silence_dir / f"{ms}ms.wav"
        if not p.exists():
            ffmpeg_silence_wav(p, ms / 1000.0)
        return p

    pieces: list[Path] = []
    timings: list[dict] = []
    running_t = 0.0
    prev_speaker = None
    force_after_title = False
    new_count = cached_count = 0

    for p in paras:
        pn = p["n"]
        text = (p.get("text") or "").strip()
        if not text:
            continue
        speaker = p.get("speaker", "Narrator")
        kind = p.get("kind", "body")
        voice = voices.get(speaker, voices["Narrator"])

        key = cache_key(text, voice)
        wav = work / f"p{pn}.{key}.wav"
        align_cache = work / f"p{pn}.{key}.words.json"
        if force or not wav.exists():
            for stale in work.glob(f"p{pn}.*.wav"):
                stale.unlink()
            for stale in work.glob(f"p{pn}.*.words.json"):
                stale.unlink()
            print(f"  ch{chap} p{pn} [{speaker}] ({len(text)} chars) → Voxtral …",
                  flush=True)
            synth_paragraph(text, voice, wav)
            words = align_words(wav, text)
            align_cache.write_text(json.dumps(words, ensure_ascii=False))
            new_count += 1
        else:
            words = json.loads(align_cache.read_text()) if align_cache.exists() \
                else align_words(wav, text)
            cached_count += 1

        duration = ffprobe_duration(wav)

        # lead silence (kind grammar mirrors generate_audio.py)
        if pieces:
            if force_after_title:
                pause_ms = pauses["after_title"]
            elif kind == "title":
                pause_ms = pauses["before_title"]
            elif kind == "continuation":
                pause_ms = 0
            else:
                pause_ms = (pauses["between_speakers"]
                            if speaker != prev_speaker else pauses["between_paragraphs"])
            if pause_ms:
                s = silence(pause_ms)
                pieces.append(s)
                running_t += ffprobe_duration(s)
        force_after_title = (kind == "title")

        pieces.append(wav)
        entry = {"n": pn, "speaker": speaker,
                 "start": round(running_t, 3),
                 "end": round(running_t + duration, 3)}
        if kind != "body":
            entry["kind"] = kind
        if words:
            entry["words"] = [{"w": w["w"],
                               "start": round(w["start"] + running_t, 3),
                               "end": round(w["end"] + running_t, 3)} for w in words]
        timings.append(entry)
        running_t += duration
        prev_speaker = speaker

    # finalize: concat → mp3 → opus → timing.json
    book_dir = ASSETS_AUDIO / lang / slug
    mp3 = book_dir / f"c{chap}.mp3"
    opus = book_dir / f"c{chap}.opus"
    timing = book_dir / f"c{chap}.timing.json"
    ffmpeg_concat_to_mp3(pieces, mp3)
    transcode_opus(mp3, opus)
    timing.parent.mkdir(parents=True, exist_ok=True)
    timing.write_text(json.dumps({
        "book": slug, "lang": lang, "chapter": chap,
        "duration_seconds": round(running_t, 3),
        "paragraphs": timings,
    }, ensure_ascii=False, indent=2) + "\n")

    return {"paragraphs": len(timings), "duration_seconds": running_t,
            "new": new_count, "cached": cached_count,
            "mp3": str(mp3.relative_to(LIB.parent))}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default="wheel-of-heaven-timeline")
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--lang", default="en")
    ap.add_argument("--limit", type=int, default=None,
                    help="only first N paragraphs (quick validation)")
    ap.add_argument("--force", action="store_true", help="ignore per-paragraph cache")
    ap.add_argument("--list-voices", action="store_true")
    ap.add_argument("--no-manifest", action="store_true")
    args = ap.parse_args()

    if args.list_voices:
        list_voices()
        return 0
    if not args.chapter:
        ap.error("--chapter is required (or --list-voices)")

    t0 = time.time()
    stats = generate_chapter(args.slug, args.chapter, args.lang, args.limit, args.force)
    dur = stats["duration_seconds"]
    wall = time.time() - t0
    print(f"\nch{args.chapter}: {stats['paragraphs']} paras, {dur/60:.1f} min audio "
          f"({stats['new']} new, {stats['cached']} cached) — wall {wall:.0f}s "
          f"({wall/dur:.2f}x RT)\n  {stats['mp3']}", flush=True)

    if not args.no_manifest:
        # update_book_manifest lives in generate_audio.py (needs yaml/requests);
        # run it via whichever python has those deps.
        print("updating manifest …", flush=True)
        subprocess.run([sys.executable, "-c",
            "import sys;sys.path.insert(0,'scripts');"
            "from generate_audio import update_book_manifest;"
            f"update_book_manifest('{args.slug}','{args.lang}',{{}})"],
            cwd=str(LIB), check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
