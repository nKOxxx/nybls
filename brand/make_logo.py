"""Saccade mark — an ECG-style scan trace whose peaks are eyes.

Angular monitor trace (it is watching, continuously, and measuring) with the two
tall spikes terminating in cyberpunk slit-pupil eyes (it is looking, at the
moments that spike). Black ground, neon cyan → magenta along the trace.
Geometry auto-fits the canvas so the mark fills an iOS icon tile.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

S = 2048
FILL = 0.91
OUT = Path(__file__).parent
BG = (8, 8, 10, 255)
CYAN = (34, 231, 255)
MAGENTA = (255, 47, 160)
STROKE = 46

BASE = 620
EYE_W, EYE_H = 392, 132          # full width, half-height → 3:2 almond
EYE1 = (620, 215)                # eye centres
EYE2 = (1180, 140)
# the spike apex stops at the eye's lower point, so the eye caps the peak
P1 = (EYE1[0], EYE1[1] + EYE_H * 0.80)
P2 = (EYE2[0], EYE2[1] + EYE_H * 0.80)
# ECG trace: flat → blip → spike to eye 1 → dip → spike to eye 2 → dip → blip → flat
TRACE = [
    (60, BASE), (250, BASE), (320, BASE - 70), (390, BASE + 60), (450, BASE),
    (540, BASE), P1, (700, BASE), (770, BASE + 130), (840, BASE),
    (1010, BASE), P2, (1265, BASE), (1335, BASE + 150), (1405, BASE),
    (1520, BASE), (1580, BASE - 55), (1640, BASE + 45), (1700, BASE), (1860, BASE),
]


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def arc_pts(p0, p1, p2, steps=40):
    out = []
    for i in range(steps + 1):
        t, u = i / steps, 1 - i / steps
        out.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return out


def eye_polygon(cx, cy, w=EYE_W, h=EYE_H):
    """Almond: two arcs meeting at pointed corners; apex lands at cy ∓ h."""
    top = arc_pts((cx - w / 2, cy), (cx, cy - h * 2), (cx + w / 2, cy))
    bot = arc_pts((cx + w / 2, cy), (cx, cy + h * 2), (cx - w / 2, cy))
    return top + bot


def bbox_all():
    xs, ys = [], []
    for x, y in TRACE:
        xs += [x - STROKE / 2, x + STROKE / 2]
        ys += [y - STROKE / 2, y + STROKE / 2]
    for cx, cy in (EYE1, EYE2):
        xs += [cx - EYE_W / 2, cx + EYE_W / 2]
        ys += [cy - EYE_H, cy + EYE_H]
    return min(xs), min(ys), max(xs), max(ys)


def fit():
    x0, y0, x1, y1 = bbox_all()
    sc = (S * FILL) / max(x1 - x0, y1 - y0)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return (lambda p: ((p[0] - cx) * sc + S / 2, (p[1] - cy) * sc + S / 2)), sc


def draw_mark(layer: Image.Image, bold: float = 1.0, solid_pupil=BG) -> None:
    tf, sc = fit()
    d = ImageDraw.Draw(layer)
    n = len(TRACE) - 1
    w = max(2, round(STROKE * sc * bold))

    for i in range(n):
        a, b = tf(TRACE[i]), tf(TRACE[i + 1])
        col = lerp(CYAN, MAGENTA, i / n) + (255,)
        d.line([a, b], fill=col, width=w)
        d.ellipse([a[0] - w / 2, a[1] - w / 2, a[0] + w / 2, a[1] + w / 2], fill=col)  # miter joints

    for cx, cy, t in ((EYE1[0], EYE1[1], 0.30), (EYE2[0], EYE2[1], 0.85)):
        col = lerp(CYAN, MAGENTA, t)
        poly = [tf(p) for p in eye_polygon(cx, cy, EYE_W * bold, EYE_H * bold)]
        d.polygon(poly, fill=col + (255,))
        px, py = tf((cx, cy))
        pw, ph = EYE_W * sc * bold * 0.062, EYE_H * sc * bold * 0.70  # slit stays inside the eye
        d.ellipse([px - pw, py - ph, px + pw, py + ph], fill=solid_pupil)


def build() -> Image.Image:
    base = Image.new("RGBA", (S, S), BG)
    glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    draw_mark(glow, bold=1.18, solid_pupil=(0, 0, 0, 0))
    glow = glow.filter(ImageFilter.GaussianBlur(54))
    base = Image.alpha_composite(base, Image.blend(Image.new("RGBA", (S, S), (0, 0, 0, 0)), glow, 0.8))
    sharp = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    draw_mark(sharp)
    return Image.alpha_composite(base, sharp)


if __name__ == "__main__":
    img = build()
    for size in (1024, 180, 60):
        img.resize((size, size), Image.LANCZOS).convert("RGB").save(OUT / f"nybls_{size}.png")
    print("wrote", ", ".join(f"nybls_{s}.png" for s in (1024, 180, 60)))
