"""Ingest: Instagram via gallery-dl, other URLs via yt-dlp, or a local file."""
import json
import re
import shutil
import subprocess
import time
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image

from .store import local_file_id, safe_id, utc_now, workspace

SUB_LANGS = "en,ar"  # exact langs, never globs (429 lesson, 2026-08-31)
VIDEO_SUFFIXES = {".mp4", ".webm", ".mkv", ".mov", ".m4v"}
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}
MEDIA_SUFFIXES = VIDEO_SUFFIXES | IMAGE_SUFFIXES

IG_HOSTS = {"instagram.com", "www.instagram.com"}
IG_PATH_RE = re.compile(r"/(?:reel|reels|p|tv)/([A-Za-z0-9_-]{5,24})")
IG_MIN_INTERVAL_S = 10.0  # ≤6 requests/min — burner-safety pacing


def _run(cmd: list[str], timeout: int = 900) -> subprocess.CompletedProcess:
    # arg-array only, never shell=True: titles/filenames are attacker-controlled
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def is_image(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_SUFFIXES


# ── Instagram ────────────────────────────────────────────────────────────────

def _ig_cookie_file() -> Path | None:
    sec = Path.home() / ".nybls" / "secrets"
    cands = sorted(sec.glob("ig_*.txt"), key=lambda p: p.stat().st_mtime, reverse=True)
    return cands[0] if cands else None


def _ig_pace() -> None:
    marker = Path.home() / ".nybls" / ".ig_last"
    marker.parent.mkdir(parents=True, exist_ok=True)
    if marker.exists():
        delta = time.time() - marker.stat().st_mtime
        if delta < IG_MIN_INTERVAL_S:
            time.sleep(IG_MIN_INTERVAL_S - delta)
    marker.touch()


def _ig_ingest(source: str) -> tuple[str, Path]:
    m = IG_PATH_RE.search(urlparse(source).path)
    if not m:
        raise ValueError("unrecognized Instagram URL — expected /reel/<code>/ or /p/<code>/")
    video_id = safe_id(f"ig_{m.group(1)}")
    ws = workspace(video_id)
    have = sorted(p for p in ws.glob("media*") if p.suffix.lower() in MEDIA_SUFFIXES)
    if have:
        return video_id, have[0]

    cookies = _ig_cookie_file()
    if cookies is None:
        raise RuntimeError(
            "no Instagram cookies. Log into a BURNER account in a browser, then run:  "
            "yt-dlp --cookies-from-browser <browser> --cookies ~/.nybls/secrets/ig.txt "
            "--skip-download --dump-json https://www.instagram.com/instagram/"
        )

    _ig_pace()
    tmp = ws / "_dl"
    tmp.mkdir(exist_ok=True)
    r = _run(["gallery-dl", "--cookies", str(cookies), "-D", str(tmp), "--write-metadata", source], 300)
    files = sorted(p for p in tmp.iterdir() if p.suffix.lower() in MEDIA_SUFFIXES)
    if not files:
        blob = r.stdout + r.stderr
        hint = ""
        if "JSONDecodeError" in blob or "unblock" in blob:
            hint = ("  →  Instagram redirected to a consent/checkpoint page. Open instagram.com in the "
                    "browser holding the burner session, clear the banner, re-export cookies, retry.")
        elif "401" in blob or "login" in blob.lower():
            hint = "  →  session expired; re-export cookies from the browser."
        raise RuntimeError(f"gallery-dl could not fetch this post: {r.stderr.strip()[-300:]}{hint}")

    primary: Path | None = None
    for i, f in enumerate(files):
        dest = ws / f"media{'' if len(files) == 1 else f'_{i:02d}'}{f.suffix.lower()}"
        shutil.move(str(f), dest)
        primary = primary or dest
        meta = f.with_suffix(f.suffix + ".json")
        if meta.exists() and not (ws / "ig_meta.json").exists():
            shutil.move(str(meta), ws / "ig_meta.json")
    shutil.rmtree(tmp, ignore_errors=True)
    assert primary is not None
    return video_id, primary


IG_USER_RE = re.compile(r"^/([A-Za-z0-9._]{1,30})/?$")


def profile_url(source: str) -> tuple[str, str]:
    """Accept a profile URL or bare username → (username, posts-listing URL)."""
    if source.startswith("https://"):
        u = urlparse(source)
        if u.hostname not in IG_HOSTS:
            raise ValueError("not an Instagram profile URL")
        m = IG_USER_RE.match(u.path)
        if not m:
            raise ValueError("that looks like a post URL, not a profile — use `nybls probe` for single posts")
        user = m.group(1)
    else:
        user = source.lstrip("@")
        if not re.fullmatch(r"[A-Za-z0-9._]{1,30}", user):
            raise ValueError(f"invalid username: {source!r}")
    return user, f"https://www.instagram.com/{user}/posts/"


def list_profile(source: str, limit: int = 12, refresh: bool = False) -> tuple[str, list[dict]]:
    """List recent posts WITHOUT downloading media. Returns (username, entries)."""
    user, url = profile_url(source)
    cache = Path.home() / ".nybls" / "profiles" / f"{user}.json"
    cache.parent.mkdir(parents=True, exist_ok=True)
    if cache.exists() and not refresh:
        cached = json.loads(cache.read_text())
        if len(cached["posts"]) >= limit:
            return user, cached["posts"][:limit]

    cookies = _ig_cookie_file()
    if cookies is None:
        raise RuntimeError("no Instagram cookies — see `nybls probe` help for the burner-cookie setup")
    _ig_pace()
    r = _run(["gallery-dl", "--cookies", str(cookies), "-j",
              "--range", f"1-{max(limit * 2, 4)}", url], 300)
    try:
        raw = json.loads(r.stdout or "[]")
    except json.JSONDecodeError:
        raise RuntimeError(f"could not read profile listing: {r.stderr.strip()[-300:]}") from None

    seen: dict[str, dict] = {}
    for entry in raw:
        meta = next((x for x in entry if isinstance(x, dict) and "post_shortcode" in x), None)
        if not meta:
            continue
        code = meta["post_shortcode"]
        if code in seen:
            continue
        seen[code] = {
            "n": len(seen) + 1,
            "shortcode": code,
            "url": meta.get("post_url") or f"https://www.instagram.com/p/{code}/",
            "type": meta.get("type", "post"),
            "date": str(meta.get("post_date") or meta.get("date") or "")[:16],
            "likes": meta.get("likes"),
            "media_count": meta.get("count", 1),
            "caption": (meta.get("description") or "").replace("\n", " ").strip(),
        }
    posts = list(seen.values())[:limit]
    if not posts:
        raise RuntimeError(
            f"no posts returned for @{user} — the account may be private, or Instagram "
            f"threw a checkpoint (open instagram.com in the burner's browser and clear it)."
        )
    cache.write_text(json.dumps({"user": user, "fetched_utc": utc_now(), "posts": posts}, indent=1))
    return user, posts


def ig_metadata(ws: Path) -> dict:
    p = ws / "ig_meta.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text())
    return {
        "caption": (d.get("description") or "").strip(),
        "owner": d.get("username") or d.get("fullname") or "",
        "posted": str(d.get("date") or ""),
        "likes": d.get("like_count"),
    }


# ── generic ingest ───────────────────────────────────────────────────────────

def ingest(source: str, max_height: int = 720) -> tuple[str, Path]:
    """Return (id, media_path). Downloads URL sources into the store."""
    if source.startswith(("http://", "https://")):
        u = urlparse(source)
        if u.scheme != "https":
            raise ValueError("only https URLs accepted")
        if u.hostname in IG_HOSTS:
            return _ig_ingest(source)

        probe = _run(["yt-dlp", "--no-playlist", "--dump-json", "--no-download", source], 120)
        if probe.returncode != 0:
            raise RuntimeError(f"yt-dlp probe failed: {probe.stderr.strip()[-400:]}")
        meta = json.loads(probe.stdout)
        video_id = safe_id(str(meta["id"]))
        ws = workspace(video_id)
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
        # Subtitles are a bonus (whisper is the fallback), so a 429 or a missing
        # language must never fail the run: fetch best-effort, ignore the result.
        if not any(ws.glob("*.vtt")):
            _run(["yt-dlp", "--no-playlist", "--skip-download",
                  "--write-auto-subs", "--write-subs", "--sub-langs", SUB_LANGS,
                  "--sub-format", "vtt", "-o", str(ws / "video.%(ext)s"), source], 300)
        return video_id, video

    path = Path(source).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"not a file: {source}")
    video_id = local_file_id(path)
    ws = workspace(video_id)
    dest = ws / ("media" if is_image(path) else "video")
    dest = dest.with_suffix(path.suffix.lower())
    if not dest.exists():
        shutil.copy2(path, dest)
    return video_id, dest


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
