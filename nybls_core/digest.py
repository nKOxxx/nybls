"""Digest: the free, post-archive layer — OCR index, contact sheet, scene timeline.

`probe` answers "what was said", at zero images. But a lecture stream carries half
its content on screen: slides, dashboards, leaderboards, chat. Reading all of it
through model vision is the expensive way when the machine can read text itself.
The digest pass runs after (or instead of) any model viewing:

  1. uniform frame pass (ffmpeg, one JPEG every `--every` seconds)
  2. OCR every frame with whatever is installed — Apple Vision via `ocrmac`
     (already an optional extra) or the tesseract binary
  3. write `digest/ocr-index.jsonl` (one record per frame that yielded text),
     `digest/contact_sheet.html` (human-browsable, OCR snippets under tiles),
     `digest/scenes.txt` (JPEG-size-delta screen-change timeline)

Everything here is local and costs zero vision tokens; `ledger` is untouched.
The Gemini corpus that motivated this: 1,686 frames, 1,313 with text, indexed in
about seven minutes on a laptop — enough to answer "which frame shows the
sponsor page" with grep, before any model looks at anything.
"""
import json
import re
import shutil
import subprocess
from multiprocessing import Pool
from pathlib import Path

NAME_RE = re.compile(r"^(?:f|frame)_(\d+)\.jpg$")
MAX_TEXT = 1200          # per-frame OCR budget, chars; a frame is a signpost, not a page
MIN_TEXT = 3             # shorter than this is JPEG noise, not text
SCENE_THRESHOLD = 0.35   # relative JPEG-size jump that counts as a screen change
SCENE_MIN_BYTES = 12000  # ...and big enough not to be a caption flicker


def ts_label(seconds: float) -> str:
    """1234.0 -> '20:34', 3661.0 -> '1:01:01'. Frames are numbered from 1."""
    s = int(seconds)
    h, m, sec = s // 3600, (s % 3600) // 60, s % 60
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m:02d}:{sec:02d}"


def list_frames(frames_dir: Path) -> list[tuple[int, Path]]:
    """All digest frames in NUMERIC order. Sorting paths as strings breaks the
    moment a directory mixes naming generations (`f_` sorts before `frame_`),
    which is exactly what a store digested before and after a rename looks like.
    Accepts both generations so older stores stay digestable."""
    out = []
    for p in frames_dir.iterdir():
        m = NAME_RE.match(p.name)
        if m:
            out.append((int(m.group(1)), p))
    return sorted(out, key=lambda t: t[0])


def pick_engine(prefer: str = "auto") -> tuple[str, str | None]:
    """OCR backend choice. Apple Vision first (no install beyond the extra,
    handles handwriting and Arabic), tesseract as the portable fallback.
    Returns (engine, install_hint) — engine empty when nothing is available."""
    if prefer != "tesseract":
        try:
            import ocrmac  # type: ignore[import-not-found]  # noqa: F401
            return "ocrmac", None
        except ImportError:
            if prefer == "ocrmac":
                return "", 'pipx install "nybls[macos]" for Apple Vision OCR'
    if shutil.which("tesseract"):
        return "tesseract", None
    return "", 'brew install tesseract (or: pipx install "nybls[macos]")'


def _ocr_one(task: tuple[int, str, str]) -> tuple[int, str] | None:
    """Worker: OCR one frame, return (frame_no, text) or None. Never raises —
    one corrupt JPEG must not cost the whole index."""
    n, path, engine = task
    try:
        if engine == "ocrmac":
            from ocrmac import ocr
            parts = [t for t, conf, _ in ocr.OCR().recognize(path)
                     if conf >= 0.3 and t.strip()]
            text = " ".join(parts)
        else:
            text = subprocess.run(
                ["tesseract", path, "stdout", "--psm", "3"],
                capture_output=True, text=True, timeout=120,
            ).stdout
    except Exception:
        return None
    text = " ".join(text.split())
    if len(text) < MIN_TEXT:
        return None
    return n, text[:MAX_TEXT]


def ocr_frames(frames: list[tuple[int, Path]], engine: str,
               every: float = 30.0, workers: int = 6) -> list[dict]:
    """OCR all frames, ordered records for frames that yielded text."""
    tasks = [(n, str(p), engine) for n, p in frames]
    records = []
    with Pool(min(workers, len(tasks) or 1)) as pool:
        for rec in pool.imap_unordered(_ocr_one, tasks, chunksize=8):
            if rec:
                records.append(rec)
    return [
        {"frame": n, "ts": ts_label((n - 1) * every), "chars": len(t), "text": t}
        for n, t in sorted(records)
    ]


def scene_events(frames: list[tuple[int, Path]], every: float,
                 threshold: float = SCENE_THRESHOLD,
                 min_abs: int = SCENE_MIN_BYTES) -> list[tuple[int, str, int, int]]:
    """Screen-change timeline from JPEG size deltas. Extraction is nearly free and
    size is a crude but honest proxy: a slide change moves the byte count far more
    than a talking head does. Returns (frame_no, timestamp, kb_before, kb_after)."""
    events = []
    for (_, pa), (nb, pb) in zip(frames, frames[1:]):
        sa, sb = pa.stat().st_size, pb.stat().st_size
        delta = abs(sb - sa)
        if delta > min_abs and delta / max(sa, 1) > threshold:
            events.append((nb, ts_label((nb - 1) * every), sa // 1024, sb // 1024))
    return events


def contact_sheet_html(items: list[dict], label: str) -> str:
    """Standalone, offline HTML grid. OCR snippets render under each tile so the
    page is find-in-page searchable — for a human, grep on the JSONL."""
    cells = []
    for it in items:
        snippet = (
            (it.get("snippet") or "")
            .replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        cells.append(
            f'<a class="c" href="../{it["path"]}" target="_blank">'
            f'<img loading="lazy" src="../{it["path"]}">'
            f'<span>{it["ts"]} &middot; {it["kb"]}KB</span></a>'
            + (f'<div class="o">{snippet[:140]}</div>' if snippet else "")
        )
    return (
        "<!doctype html><html><head><meta charset=\"utf-8\">\n"
        f"<title>{label} — visual index</title><style>\n"
        "body{background:#111;color:#ddd;font-family:-apple-system,sans-serif;margin:20px}\n"
        "h1{font-size:18px}.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}\n"
        ".c{display:block;position:relative}.c img{width:100%;border-radius:6px;display:block}\n"
        ".c span{position:absolute;bottom:6px;left:6px;background:rgba(0,0,0,.75);padding:2px 6px;"
        "border-radius:4px;font-size:11px}\n"
        ".o{font-size:10px;color:#9a9a9a;margin:-4px 0 6px;height:2.4em;overflow:hidden}\n"
        "</style></head><body>\n"
        f"<h1>{label} — {len(items)} frames. Click any to enlarge; grey text under each tile is its OCR.</h1>\n"
        f"<div class=\"g\">{''.join(cells)}</div></body></html>"
    )


def update_manifest(video_id: str, patch: dict) -> dict:
    """Merge keys into manifest.json without touching created_utc (write_manifest
    would stamp a fresh one, which would lie about when the video was probed)."""
    from .store import workspace
    p = workspace(video_id) / "manifest.json"
    data = json.loads(p.read_text()) if p.exists() else {}
    data.update(patch)
    p.write_text(json.dumps(data, indent=1))
    return data


def extract_frames(video: Path, ws: Path, every: float = 30.0,
                   width: int = 1280, force: bool = False) -> tuple[Path, int, bool]:
    """Uniform JPEG pass. Reuses an existing frames30/ unless --force. A second
    digest run after a partial one must not re-encode an hour of video."""
    d = ws / "frames30"
    if force and d.exists():
        shutil.rmtree(d)
    d.mkdir(exist_ok=True)
    frames = list_frames(d)
    if frames:
        return d, len(frames), False
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(video),
         "-vf", f"fps=1/{every},scale='min({width},iw)':-2", "-q:v", "3",
         str(d / "frame_%05d.jpg")],
        check=True, timeout=3600,
    )
    frames = list_frames(d)
    return d, len(frames), True
