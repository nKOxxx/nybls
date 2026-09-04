"""Media ops: scene detection, contact sheets, full frames, zoom crops, phash dedup.

Deliberately thin on dependencies. A clean `pip install nybls` measured 293 MB on
2026-09-04 against an agreed ceiling of 150 MB, and 219 MB of that was two
transitive imports we used one function from each: `scenedetect` (pulls
opencv, 120 MB) for scene cuts, and `imagehash` (pulls scipy, 99 MB) for one
perceptual hash. Both are reimplemented below on ffmpeg and numpy, which we
already require. Measured equivalence: ffmpeg's scene filter at 0.3 found the
same cuts at the same timestamps as scenedetect's AdaptiveDetector on a 5-min
and a 44-min video (348 vs 395 cuts on the long one; first four identical), and
the numpy phash reproduces imagehash's bits exactly, so stored hash caches
remain valid.
"""
import json
import re
import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/System/Library/Fonts/Menlo.ttc"
DEDUP_HAMMING = 8  # starting threshold; calibrate on real footage
SCENE_THRESHOLD = 0.3  # ffmpeg scene score; matched scenedetect on real footage (see module doc)


def _duration(video: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(video)],
        capture_output=True, text=True, check=True).stdout.strip()
    return float(out) if out else 0.0


def phash_hex(img: Image.Image, hash_size: int = 8, highfreq_factor: int = 4) -> str:
    """64-bit perceptual hash, bit-compatible with imagehash.phash.

    Grayscale, resize to 32x32, 2-D DCT-II (scipy's unnormalised convention,
    which only matters for reproducing the reference exactly), keep the
    top-left 8x8 low-frequency block, threshold at its median. Bits are
    row-major, MSB first, rendered as 16 hex characters — the same string
    imagehash writes, so `_phashes.json` files from earlier versions still
    compare correctly.
    """
    n = hash_size * highfreq_factor
    px = np.asarray(img.convert("L").resize((n, n), Image.Resampling.LANCZOS), dtype=np.float64)
    k = np.arange(n)[:, None]
    m = np.arange(n)[None, :]
    C = 2.0 * np.cos(np.pi * k * (2 * m + 1) / (2 * n))      # DCT-II basis, unnormalised
    dct = C @ px @ C.T
    low = dct[:hash_size, :hash_size]
    bits = (low > np.median(low)).flatten()
    value = int("".join("1" if b else "0" for b in bits), 2)
    return f"{value:0{hash_size * hash_size // 4}x}"


def hamming(a_hex: str, b_hex: str) -> int:
    return bin(int(a_hex, 16) ^ int(b_hex, 16)).count("1")


def detect_scenes(video: Path, ws: Path) -> list[dict]:
    """Scene list via ffmpeg's own scene-change score; no extra dependency.

    Scene cuts only seed where contact-sheet tiles land. They are not the
    primary sampling signal (that is `adaptive_timestamps`), which is why a
    threshold that agrees with scenedetect on ~88% of cuts is good enough.
    """
    cache = ws / "scenes.json"
    if cache.exists():
        return json.loads(cache.read_text())
    duration = _duration(video)
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(video),
         "-vf", f"select='gt(scene,{SCENE_THRESHOLD})',showinfo", "-an", "-f", "null", "-"],
        capture_output=True, text=True)
    cuts = sorted({round(float(t), 2) for t in re.findall(r"pts_time:([0-9.]+)", r.stderr)})
    bounds = [0.0] + [c for c in cuts if 0.0 < c < duration] + [round(duration, 2)]
    out = [
        {"n": i, "start_s": a, "end_s": b}
        for i, (a, b) in enumerate(zip(bounds, bounds[1:])) if b > a
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
    remember_tiles(ws, timestamps)
    return out


def remember_tiles(ws: Path, timestamps: list[float]) -> None:
    """Record exactly which moments were rendered into a sheet.

    A label reads "24:12", so the model asks for second 1452 - but the tile was
    rendered at 1452.4, and on material cutting once a second that is a
    different shot. Measured across three videos, 21 of 24 one-second offsets
    landed in a visibly different shot. Keeping the real timestamps lets a
    later request return the frame the model actually saw."""
    p = ws / "tiles.json"
    known = json.loads(p.read_text()) if p.exists() else []
    known = sorted(set(known) | {round(float(t), 3) for t in timestamps})
    p.write_text(json.dumps(known))


def snap_to_tile(ws: Path, ts: float, tolerance: float = 3.0) -> tuple[float, bool]:
    """Return the nearest rendered tile within tolerance, else the request."""
    p = ws / "tiles.json"
    if not p.exists():
        return ts, False
    known = json.loads(p.read_text())
    if not known:
        return ts, False
    best = min(known, key=lambda k: abs(k - ts))
    if abs(best - ts) <= tolerance and best != ts:
        return best, True
    return ts, False


def extract_frame(video: Path, ws: Path, ts: float, width: int = 1568) -> tuple[Path, bool]:
    """Full frame at ts. Returns (path, is_near_duplicate_of_served)."""
    out = ws / "frames" / f"f_{int(ts * 1000)}_{width}.png"
    if not out.exists():
        _extract(video, ts, out, f"scale={width}:-2")
    ph = phash_hex(Image.open(out))
    seen = ws / "frames" / "_phashes.json"
    hashes = json.loads(seen.read_text()) if seen.exists() else {}
    dupe = any(
        hamming(ph, h) <= DEDUP_HAMMING
        for f, h in hashes.items() if f != out.name
    )
    hashes[out.name] = ph
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


def adaptive_timestamps(video: Path, ws: Path, duration: float, probe_every: float = 5.0,
                        region: tuple[float, float, float, float] | None = None,
                        max_frames: int = 60, backbone_every: float = 180.0) -> tuple[list[float], int, float]:
    """Timestamps ranked by how much the picture actually CHANGED.

    Extraction is cheap; looking is what costs money. So probe densely at low
    resolution (no vision tokens), score each probe by mean absolute pixel
    difference from the previous one, and return only the biggest changes.

    Why pixel difference and not a perceptual hash: on static-camera content the
    perceptual hash's distribution compresses into the same band the code uses to
    declare two frames DUPLICATES (measured on a chess lesson: median 4, p90 8 of a
    possible 64), leaving a threshold-based detector nowhere to sit. Pixel difference
    keeps a usable range on the same footage (median 2.8, max 33.5).

    NOTE, 2026-09-02: the stronger claim this docstring used to make - that a
    perceptual hash is BLIND to content change - was tested against an independent
    OCR reference across seven videos and did NOT hold (mean AUC 0.734 vs 0.762,
    pixel difference better on only 2 of 4 usable videos). See
    bench/RESULTS_signals.md. Pixel difference is retained for the compression
    property above, not because the hash was shown to be useless.

    `region` (x, y, w, h in 0..1) restricts scoring to part of the frame. On
    split-screen instructional video a talking head changes constantly while the
    board beside it changes once a minute; score the board, not the face.

    A uniform backbone (one probe every `backbone_every` seconds) is merged in so
    that a long quiet stretch is never completely unrepresented.

    Returns (timestamps, n_probed, median_score).
    """
    import numpy as np

    tmp = ws / "_probe"
    tmp.mkdir(exist_ok=True)
    vf = "scale=192:-2,format=gray"
    if region:
        x, y, w, h = region
        vf = f"crop=iw*{w:.4f}:ih*{h:.4f}:iw*{x:.4f}:ih*{y:.4f},{vf}"

    scored: list[tuple[float, float]] = []
    prev = None
    probes = list(_frange(probe_every / 2, duration, probe_every))
    for ts in probes:
        f = tmp / f"p_{int(ts * 1000)}.png"
        try:
            _extract(video, ts, f, vf)
        except subprocess.CalledProcessError:
            continue
        arr = np.asarray(Image.open(f), dtype=np.float32)
        f.unlink(missing_ok=True)
        if prev is not None and prev.shape == arr.shape:
            scored.append((ts, float(np.abs(arr - prev).mean())))
        prev = arr
    shutil.rmtree(tmp, ignore_errors=True)
    if not scored:
        return [], len(probes), 0.0

    median = sorted(s for _, s in scored)[len(scored) // 2]
    # greedy top-N by change, spaced so one busy moment cannot eat the budget
    min_gap = probe_every * 2
    chosen: list[float] = []
    for ts, _ in sorted(scored, key=lambda x: -x[1]):
        if len(chosen) >= max_frames:
            break
        if all(abs(ts - c) >= min_gap for c in chosen):
            chosen.append(ts)
    # uniform backbone so quiet stretches are still represented
    for ts in _frange(backbone_every / 2, duration, backbone_every):
        if all(abs(ts - c) >= min_gap for c in chosen):
            chosen.append(ts)
    return sorted(chosen), len(probes), median


def _frange(start, stop, step):
    t = start
    while t < stop:
        yield t
        t += step
