"""Ingest: any yt-dlp-supported URL, or a local media file.

Additional sources (e.g. platforms needing session cookies) live in separate
adapters that write into the same store and reuse this engine.
"""
import json
import shutil
import subprocess
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image

from .store import local_file_id, safe_id, workspace

SUB_LANGS = "en"                      # exact langs, never globs (rate-limit lesson)
VIDEO_SUFFIXES = {".mp4", ".webm", ".mkv", ".mov", ".m4v"}
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}
MEDIA_SUFFIXES = VIDEO_SUFFIXES | IMAGE_SUFFIXES


def _run(cmd: list[str], timeout: int = 900) -> subprocess.CompletedProcess:
    # arg-array only, never shell=True: titles and filenames are hostile input
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def is_image(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_SUFFIXES


def ingest(source: str, max_height: int = 720) -> tuple[str, Path]:
    """Return (id, media_path). Downloads URL sources into the store."""
    if source.startswith(("http://", "https://")):
        if urlparse(source).scheme != "https":
            raise ValueError("only https URLs accepted")

        probe = _run(["yt-dlp", "--no-playlist", "--dump-json", "--no-download", source], 120)
        if probe.returncode != 0:
            raise RuntimeError(f"yt-dlp probe failed: {probe.stderr.strip()[-400:]}")
        meta = json.loads(probe.stdout)
        media_id = safe_id(str(meta["id"]))
        ws = workspace(media_id)
        video = ws / "video.mp4"

        if not video.exists():
            dl = _run([
                "yt-dlp", "--no-playlist",
                "-f", f"bv*[height<={max_height}]+ba/b[height<={max_height}]",
                "--merge-output-format", "mp4",
                "-o", str(ws / "video.%(ext)s"),
                "--write-info-json", source,
            ])
            if dl.returncode != 0 or not video.exists():
                raise RuntimeError(f"download failed: {dl.stderr.strip()[-400:]}")

        # Captions are a bonus (whisper is the fallback), so a rate limit or a
        # missing language must never fail the run: best-effort, ignore result.
        if not any(ws.glob("*.vtt")):
            _run(["yt-dlp", "--no-playlist", "--skip-download",
                  "--write-auto-subs", "--write-subs", "--sub-langs", SUB_LANGS,
                  "--sub-format", "vtt", "-o", str(ws / "video.%(ext)s"), source], 300)
        return media_id, video

    path = Path(source).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"not a file: {source}")
    media_id = local_file_id(path)
    ws = workspace(media_id)
    dest = (ws / ("media" if is_image(path) else "video")).with_suffix(path.suffix.lower())
    if not dest.exists():
        shutil.copy2(path, dest)
    return media_id, dest


def media_info(path: Path) -> dict:
    if is_image(path):
        with Image.open(path) as im:
            w, h = im.size
        return {"kind": "image", "duration_s": 0.0, "width": w, "height": h}
    r = _run([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height:format=duration",
        "-of", "json", str(path),
    ], 60)
    d = json.loads(r.stdout)
    stream = (d.get("streams") or [{}])[0]
    return {
        "kind": "video",
        "duration_s": round(float(d["format"]["duration"]), 2),
        "width": stream.get("width"),
        "height": stream.get("height"),
    }
