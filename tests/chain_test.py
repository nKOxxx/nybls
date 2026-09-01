"""End-to-end chain test: scenes -> contact sheet with timestamps -> full frame."""
import json, subprocess, sys, time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from scenedetect import AdaptiveDetector, detect

ROOT = Path(__file__).parent
VIDEO = ROOT / "sample" / "test1.mp4"
OUT = ROOT / "sample" / "out"
OUT.mkdir(exist_ok=True)

t0 = time.time()
scenes = detect(str(VIDEO), AdaptiveDetector())
t1 = time.time()
scene_list = [
    {"n": i, "start_s": round(s.get_seconds(), 2), "end_s": round(e.get_seconds(), 2)}
    for i, (s, e) in enumerate(scenes)
]
(OUT / "scenes.json").write_text(json.dumps(scene_list, indent=1))
print(f"scenes: {len(scene_list)} detected in {t1-t0:.0f}s")

# --- contact sheet: 6 scene-midpoint thumbs from the first 12 scenes, 3x2, ts overlay
picks = scene_list[:12:2][:6] if len(scene_list) >= 6 else scene_list[:6]
tiles = []
for sc in picks:
    mid = (sc["start_s"] + sc["end_s"]) / 2
    f = OUT / f"thumb_{sc['n']}.png"
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-ss", str(mid), "-i", str(VIDEO),
         "-frames:v", "1", "-vf", "scale=480:-2", str(f)],
        check=True,
    )
    tiles.append((f, mid))

tw, th = Image.open(tiles[0][0]).size
sheet = Image.new("RGB", (tw * 3 + 8, th * 2 + 4), "black")
try:
    font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 22)
except OSError:
    font = ImageFont.load_default()
for i, (f, ts) in enumerate(tiles):
    im = Image.open(f)
    d = ImageDraw.Draw(im)
    label = f"{int(ts//60):02d}:{int(ts%60):02d}"
    d.rectangle([4, th - 34, 96, th - 4], fill=(0, 0, 0))
    d.text((10, th - 32), label, fill=(255, 200, 60), font=font)
    sheet.paste(im, ((i % 3) * (tw + 4), (i // 3) * (th + 2)))
sheet.save(OUT / "sheet_test.png")
print(f"sheet: {sheet.size[0]}x{sheet.size[1]} px, 6 tiles")

# --- one full-res frame mid-video
subprocess.run(
    ["ffmpeg", "-y", "-loglevel", "error", "-ss", "570", "-i", str(VIDEO),
     "-frames:v", "1", "-vf", "scale=1568:-2", str(OUT / "frame_0930.png")],
    check=True,
)
print("full frame at 09:30 written")
