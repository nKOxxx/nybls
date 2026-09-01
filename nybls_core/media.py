"""Media ops: scene detection, contact sheets, full frames, zoom crops, phash dedup."""
import json
import subprocess
from pathlib import Path

import imagehash
from PIL import Image, ImageDraw, ImageFont
from scenedetect import AdaptiveDetector, detect

FONT_PATH = "/System/Library/Fonts/Menlo.ttc"
DEDUP_HAMMING = 8  # starting threshold; calibrate on real footage


def detect_scenes(video: Path, ws: Path) -> list[dict]:
    cache = ws / "scenes.json"
    if cache.exists():
        return json.loads(cache.read_text())
    scenes = detect(str(video), AdaptiveDetector())
    out = [
        {"n": i, "start_s": round(s.seconds, 2), "end_s": round(e.seconds, 2)}
        for i, (s, e) in enumerate(scenes)
    ]
    cache.write_text(json.dumps(out))
    return out


def _extract(video: Path, ts: float, out: Path, vf: str) -> None:
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{ts:.3f}", "-i", str(video),
         "-frames:v", "1", "-vf", vf, str(out)],
        check=True, timeout=120,
    )


def _font(size: int = 22):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except OSError:
        return ImageFont.load_default()


def _stamp(img: Image.Image, ts: float) -> Image.Image:
    d = ImageDraw.Draw(img)
    label = f"{int(ts // 60):02d}:{int(ts % 60):02d}"
    h = img.size[1]
    d.rectangle([4, h - 34, 96, h - 4], fill=(0, 0, 0))
    d.text((10, h - 32), label, fill=(255, 200, 60), font=_font())
    return img


def sheet_timestamps(scenes: list[dict], duration: float, start: float, end: float, n: int = 6) -> list[float]:
    """Pick n timestamps in [start,end]: scene midpoints if available, else uniform."""
    end = min(end, duration)
    mids = [
        (s["start_s"] + min(s["end_s"], end)) / 2
        for s in scenes
        if s["start_s"] < end and s["end_s"] > start
    ]
    if len(mids) >= n:
        step = len(mids) / n
        return [mids[int(i * step)] for i in range(n)]
    span = max(end - start, 1.0)
    return [start + span * (i + 0.5) / n for i in range(n)]


def make_sheet(video: Path, ws: Path, timestamps: list[float], idx: int, tile_w: int = 480) -> Path:
    tiles = []
    for ts in timestamps:
        tmp = ws / "frames" / f"_tile_{int(ts * 1000)}.png"
        _extract(video, ts, tmp, f"scale={tile_w}:-2")
        tiles.append((_stamp(Image.open(tmp).convert("RGB"), ts), tmp))
    tw, th = tiles[0][0].size
    cols, rows = 3, 2
    sheet = Image.new("RGB", (tw * cols + (cols - 1) * 4, th * rows + (rows - 1) * 4), "black")
    for i, (im, tmp) in enumerate(tiles):
        sheet.paste(im, ((i % cols) * (tw + 4), (i // cols) * (th + 4)))
        tmp.unlink(missing_ok=True)
    out = ws / "frames" / f"sheet_{idx:03d}.png"
    sheet.save(out)
    return out


def extract_frame(video: Path, ws: Path, ts: float, width: int = 1568) -> tuple[Path, bool]:
    """Full frame at ts. Returns (path, is_near_duplicate_of_served)."""
    out = ws / "frames" / f"f_{int(ts * 1000)}_{width}.png"
    if not out.exists():
        _extract(video, ts, out, f"scale={width}:-2")
    ph = imagehash.phash(Image.open(out))
    seen = ws / "frames" / "_phashes.json"
    hashes = json.loads(seen.read_text()) if seen.exists() else {}
    dupe = any(
        ph - imagehash.hex_to_hash(h) <= DEDUP_HAMMING
        for f, h in hashes.items() if f != out.name
    )
    hashes[out.name] = str(ph)
    seen.write_text(json.dumps(hashes))
    return out, dupe


def zoom_crop(video: Path, ws: Path, ts: float, box: tuple[float, float, float, float], width: int = 1200) -> Path:
    """box = (x, y, w, h) in 0..1 relative coordinates."""
    x, y, w, h = box
    if not all(0 <= v <= 1 for v in box) or w <= 0 or h <= 0 or x + w > 1.001 or y + h > 1.001:
        raise ValueError("box must be relative 0..1 coords: x,y,w,h with x+w<=1, y+h<=1")
    out = ws / "frames" / f"z_{int(ts * 1000)}_{int(x * 100)}_{int(y * 100)}_{int(w * 100)}.png"
    vf = f"crop=iw*{w:.3f}:ih*{h:.3f}:iw*{x:.3f}:ih*{y:.3f},scale={width}:-2"
    _extract(video, ts, out, vf)
    return out
