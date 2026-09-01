"""Build the one-shot baseline evidence pack: N uniformly sampled frames.

This is the standard approach the field uses — sample at a fixed rate, hand
everything to the model at once. It is the control arm for the benchmark.
"""
import json
import subprocess
import sys
from pathlib import Path

from nybls_core.store import read_manifest, workspace


def main(media_id: str, n: int = 30, width: int = 1568) -> int:
    ws = workspace(media_id)
    m = read_manifest(media_id)
    dur = m["duration_s"]
    out = ws / "oneshot"
    out.mkdir(exist_ok=True)
    videos = [p for p in list(ws.glob("video.*")) + list(ws.glob("media*"))
              if p.suffix.lower() in {".mp4", ".webm", ".mkv", ".mov", ".m4v"}]
    stamps = [dur * (i + 0.5) / n for i in range(n)]
    for i, ts in enumerate(stamps):
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{ts:.3f}", "-i", str(videos[0]),
             "-frames:v", "1", "-vf", f"scale={width}:-2", str(out / f"u{i:02d}_{int(ts)}s.png")],
            check=True, timeout=120,
        )
    (out / "index.json").write_text(json.dumps(
        {"media_id": media_id, "n": n, "width": width,
         "timestamps_s": [round(t, 1) for t in stamps]}, indent=1))
    print(f"one-shot pack: {n} frames in {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 30))
