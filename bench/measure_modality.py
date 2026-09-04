"""Where does a video's information actually live: in the speech, or in the pixels?

The claim under test is the project's revised thesis: the value of looking is
inverse to what the transcript carries. Speech and pixels are substitutes. A
podcast can be read; a silent screen recording cannot be read at all.

That is a comparative claim, so it needs a number that is comparable across
videos. We use the VISUAL EXCLUSIVITY RATIO: of the content words legible on
screen, what fraction never appear in the transcript?

    exclusivity = |ocr_words \\ transcript_words| / |ocr_words|

A ratio near 1.0 means essentially nothing on screen is recoverable by reading.
A low ratio means the narration restates what is shown, and a transcript first
tool loses little.

Also reported, because it is the failure mode that motivated the guard: whether
the transcript is degenerate, measured as unique lines over total lines. Whisper
does not fail loudly on audio it cannot handle; it loops or emits stock
politeness and reports success.

Usage: python bench/measure_modality.py <media_id> [--frames 40]
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nybls_core.store import read_manifest, workspace  # noqa: E402

STOP = {"the","and","for","you","your","this","that","with","from","are","was","not",
        "but","have","has","had","can","will","all","its","it's","they","them","their",
        "our","out","get","got","one","two","new","now","how","why","what","when","who"}


def words(text: str) -> set[str]:
    out = set()
    for w in re.sub(r"[^a-z0-9]+", " ", text.lower()).split():
        if len(w) >= 3 and w not in STOP:
            out.add(w)
    return out


def video_path(ws: Path) -> Path:
    v = [p for p in list(ws.glob("video.*")) + list(ws.glob("media*"))
         if p.suffix.lower() in {".mp4", ".webm", ".mkv", ".mov", ".m4v"}]
    if not v:
        raise SystemExit(f"no video in {ws}")
    return v[0]


def run(media_id: str, n_frames: int) -> dict:
    from ocrmac import ocrmac
    ws = workspace(media_id)
    man = read_manifest(media_id)
    dur = float(man["duration_s"])
    vid = video_path(ws)
    tmp = ws / "_modality"
    tmp.mkdir(exist_ok=True)

    ocr_words: set[str] = set()
    frames_with_text = 0
    for i in range(n_frames):
        ts = dur * (i + 0.5) / n_frames
        f = tmp / f"m_{i:03d}.png"
        try:
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{ts:.3f}",
                            "-i", str(vid), "-frames:v", "1", "-vf", "scale=1280:-2", str(f)],
                           check=True, timeout=90)
        except subprocess.CalledProcessError:
            continue
        try:
            res = ocrmac.OCR(str(f), language_preference=["en-US"]).recognize()
            txt = " ".join(str(x[0]) for x in res)
        except Exception:
            txt = ""
        w = words(txt)
        if w:
            frames_with_text += 1
        ocr_words |= w
        f.unlink(missing_ok=True)
    for leftover in tmp.glob("*.png"):
        leftover.unlink(missing_ok=True)
    tmp.rmdir()

    tpath = ws / "transcript.txt"
    traw = tpath.read_text() if tpath.exists() else ""
    lines = [l.strip() for l in traw.splitlines() if l.strip()]
    twords = words(traw)
    only_visual = ocr_words - twords

    return {
        "media_id": media_id,
        "title": man.get("title", "")[:60],
        "duration_s": round(dur, 1),
        "frames_sampled": n_frames,
        "frames_with_on_screen_text": frames_with_text,
        "transcript_lines": len(lines),
        "transcript_unique_lines": len(set(lines)),
        "transcript_degeneracy": round(len(set(lines)) / len(lines), 3) if lines else None,
        "transcript_unique_words": len(twords),
        "ocr_unique_words": len(ocr_words),
        "ocr_words_absent_from_transcript": len(only_visual),
        "visual_exclusivity": round(len(only_visual) / len(ocr_words), 4) if ocr_words else None,
        "sample_visual_only_words": sorted(only_visual)[:25],
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("media_id")
    ap.add_argument("--frames", type=int, default=40)
    a = ap.parse_args()
    res = run(a.media_id, a.frames)
    out = Path(__file__).parent / "round3" / f"modality_{a.media_id}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, indent=1))
    slim = {k: v for k, v in res.items() if k != "sample_visual_only_words"}
    print(json.dumps(slim, indent=1))
