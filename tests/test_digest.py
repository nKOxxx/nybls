"""The digest pass must stay free, never raise per-frame, and read old stores.

Failure history that shaped these tests: the Grok corpus was indexed with
hand-run scripts because the tool stopped at the archive; the scripts hardcoded
a 30-second interval that silently mislabeled timestamps when a second capture
used 20s frames; and a corrupt JPEG killed a whole OCR batch. Each test below
pins the property that prevents one of those.
"""
import shutil
from pathlib import Path

import pytest

from nybls_core import digest as dg


def test_ts_label_formats_both_scales():
    assert dg.ts_label(754.0) == "12:34"
    assert dg.ts_label(3661.0) == "1:01:01"
    assert dg.ts_label(0.0) == "00:00"


def test_list_frames_accepts_both_generations(tmp_path):
    """Older stores named frames f_00001.jpg, the extractor writes frame_00001.jpg.
    A digest must read either, in numeric order, and ignore bystanders."""
    (tmp_path / "f_00002.jpg").write_bytes(b"x")
    (tmp_path / "frame_00001.jpg").write_bytes(b"y")
    (tmp_path / "frame_00003.png").write_bytes(b"z")   # wrong suffix: skip
    (tmp_path / "notes.txt").write_bytes(b"w")
    assert [n for n, _ in dg.list_frames(tmp_path)] == [1, 2]


def test_scene_events_flag_changes_not_flicker(tmp_path):
    """A screen change is a BIG relative jump AND big in absolute bytes; a caption
    flicker is neither. Two guards on purpose: 2% of a huge slide is real bytes
    but not a change, and +90% of a thumbnail is real relative but not a change."""
    f1 = tmp_path / "frame_00001.jpg"; f1.write_bytes(b"a" * 100_000)
    f2 = tmp_path / "frame_00002.jpg"; f2.write_bytes(b"a" * 102_000)   # +2%: no
    f3 = tmp_path / "frame_00003.jpg"; f3.write_bytes(b"b" * 300_000)   # +194%: yes
    f4 = tmp_path / "frame_00004.jpg"; f4.write_bytes(b"b" * 305_000)   # +1.7%: no
    frames = dg.list_frames(tmp_path)
    events = dg.scene_events(frames, every=30.0)
    assert [(n, a, b) for n, _, a, b in events] == [(3, 99, 292)]


def test_ocr_one_never_raises_on_missing_file():
    """One corrupt/missing JPEG must not cost the index: the worker degrades to
    an empty-text record, which ocr_frames logs as a chars-0 row. The grayscale
    primary pass reads the file BEFORE tesseract runs, so the missing-file
    exception must be caught on that path too."""
    assert dg._ocr_one((1, "/nonexistent/frame.jpg", "tesseract")) == (1, "", "-")


def test_gray_png_returns_mode_l_bytes(tmp_path):
    """The sparse pass feeds tesseract grayscale PNG bytes over stdin. Pin the
    conversion itself: output is PNG bytes that decode to an 'L' (grayscale)
    image of unchanged size."""
    from PIL import Image
    import io
    src = tmp_path / "frame_00001.jpg"
    Image.new("RGB", (64, 32), (200, 30, 30)).save(src, "JPEG")
    raw = dg._gray_png(str(src))
    assert raw[:8] == b"\x89PNG\r\n\x1a\n"
    img = Image.open(io.BytesIO(raw))
    assert img.mode == "L" and img.size == (64, 32)


def test_rescue_gate_rejects_wordless_noise():
    """psm 6 invents plausible-looking junk out of stage texture. A rescue that
    yields no real word (4+ letters) is discarded, keeping the index honest."""
    assert dg._has_word("; er oe = eS ee EB 2mee @") is False
    assert dg._has_word("Introducing @ Grok Bot Galaxy") is True


def test_pick_engine_honors_explicit_tesseract(monkeypatch):
    monkeypatch.setattr(dg.shutil, "which", lambda name: "/usr/bin/tesseract")
    engine, _ = dg.pick_engine("tesseract")
    assert engine == "tesseract"


def test_pick_engine_reports_install_hint(monkeypatch):
    monkeypatch.setattr(dg.shutil, "which", lambda name: None)
    monkeypatch.setitem(__import__("sys").modules, "ocrmac", None)  # force ImportError path
    engine, hint = dg.pick_engine("tesseract")
    assert engine == "" and "tesseract" in hint


@pytest.mark.skipif(not shutil.which("tesseract"), reason="tesseract not installed")
def test_ocr_one_reads_rendered_text(tmp_path):
    """Clean rendered text must survive the whole worker path, size-cap included."""
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGB", (900, 140), "white")
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 36)
    except OSError:
        font = ImageFont.load_default()
    d.text((20, 40), "DIGEST PIPELINE CHECK 12345", fill="black", font=font)
    p = tmp_path / "frame_00001.jpg"
    img.save(p, "JPEG")
    rec = dg._ocr_one((1, str(p), "tesseract"))
    assert rec and "DIGEST" in rec[1]


def test_contact_sheet_escapes_ocr_text():
    """OCR text is video content, i.e. hostile input; the sheet is opened in a
    browser, so a frame containing markup must not become markup."""
    html = dg.contact_sheet_html(
        [{"path": "frames30/frame_00001.jpg", "ts": "0:00", "kb": 12,
          "snippet": "<script>alert(1)</script> SPONSOR"}], "test")
    assert "<script>" not in html
    assert "&lt;script&gt;" in html
    assert "SPONSOR" in html


def test_contact_sheet_escapes_label():
    """The title comes from downloaded metadata, i.e. hostile input too: it goes
    into <title>/<h1>, so it must be escaped exactly like OCR snippets."""
    html = dg.contact_sheet_html(
        [{"path": "frames30/frame_00001.jpg", "ts": "0:00", "kb": 12,
          "snippet": "harmless"}],
        '<script>alert("title")</script>')
    assert '<script>alert("title")</script>' not in html
    assert "&lt;script&gt;" in html
    assert "visual index" in html  # the page itself stays well-formed


def test_frames_meta_roundtrip_and_legacy(tmp_path):
    """extract_frames records its interval/width as .meta.json; a missing file
    reads as legacy (None) so old archives still digest."""
    d = tmp_path / "frames30"
    d.mkdir()
    assert dg.read_frames_meta(d) is None  # legacy frames: no metadata
    (d / ".meta.json").write_text('{"every_s": 30, "width": 1280}')
    meta = dg.read_frames_meta(d)
    assert meta == {"every_s": 30, "width": 1280}


def test_extract_frames_refuses_interval_mismatch_without_video(tmp_path):
    """The reviewer's high-severity case: frames30/ made at 30s must never be
    relabeled as 10s frames. With the video gone (transcribe-then-delete
    archive) that mismatch is a hard error, not a silently wrong index."""
    d = tmp_path / "frames30"
    d.mkdir()
    (d / "frame_00001.jpg").write_bytes(b"not a real jpeg")
    (d / ".meta.json").write_text('{"every_s": 30, "width": 1280}')
    with pytest.raises(ValueError, match="30s intervals"):
        dg.extract_frames(None, tmp_path, every=10.0)


def test_extract_frames_reuses_matching_interval(tmp_path):
    """The flip side: an identical --every rerun must still reuse (no re-encode
    of an hour of video), which is the whole reason frames30/ persists."""
    d = tmp_path / "frames30"
    d.mkdir()
    (d / "frame_00001.jpg").write_bytes(b"not a real jpeg")
    (d / ".meta.json").write_text('{"every_s": 30, "width": 1280}')
    d_, n, extracted = dg.extract_frames(None, tmp_path, every=30.0)
    assert extracted is False and n == 1 and d_ == d


def test_extract_frames_legacy_reused_without_video(tmp_path):
    """Legacy frames (no .meta.json) without the video: the only case where
    unknown provenance is tolerated -- nothing is destroyed, the CLI warns."""
    d = tmp_path / "frames30"
    d.mkdir()
    (d / "frame_00001.jpg").write_bytes(b"not a real jpeg")
    d_, n, extracted = dg.extract_frames(None, tmp_path, every=30.0)
    assert extracted is False and n == 1 and d_ == d
    assert not (d / ".meta.json").exists()  # reuse never fabricates provenance


def test_extract_frames_legacy_reextracted_when_video_present(tmp_path):
    """The reviewer's follow-up hole: legacy frames + video available must not
    be silently reused at an unverified --every. They are re-extracted, which
    both fixes the interval and backfills .meta.json provenance."""
    import json
    video = tmp_path / "video.mp4"
    video.write_bytes(b"")
    d = tmp_path / "frames30"
    d.mkdir()
    (d / "frame_00001.jpg").write_bytes(b"stale legacy frame")
    calls = []

    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        (d / "frame_00002.jpg").write_bytes(b"fresh")
        class R:
            returncode = 0
        return R()

    orig_run = dg.subprocess.run
    dg.subprocess.run = fake_run
    try:
        d_, n, extracted = dg.extract_frames(video, tmp_path, every=30.0)
    finally:
        dg.subprocess.run = orig_run
    assert extracted is True and len(calls) == 1
    assert n == 1  # stale legacy frame is gone; only the mock-created one remains
    assert json.loads((d / ".meta.json").read_text())["every_s"] == 30.0


def test_extract_frames_reextracts_on_mismatch_with_video(tmp_path):
    """With the video present, a different --every must re-extract (fresh meta
    written), because that is strictly better than refusing."""
    import json
    video = tmp_path / "video.mp4"
    video.write_bytes(b"")  # not ffmpeg-run here; extraction itself is mocked
    d = tmp_path / "frames30"
    d.mkdir()
    (d / "frame_00001.jpg").write_bytes(b"not a real jpeg")
    (d / ".meta.json").write_text('{"every_s": 30, "width": 1280}')
    calls = []

    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        (d / "frame_00002.jpg").write_bytes(b"junk")
        class R:
            returncode = 0
        return R()

    orig_run = dg.subprocess.run
    dg.subprocess.run = fake_run
    try:
        d_, n, extracted = dg.extract_frames(video, tmp_path, every=10.0)
    finally:
        dg.subprocess.run = orig_run
    assert extracted is True and len(calls) == 1
    assert any("fps=1/10.0" in a for a in calls[0])  # interval reached ffmpeg
    # re-extraction starts from a fresh frames30/: only mock-created frames remain
    assert n == 1
    assert json.loads((d / ".meta.json").read_text())["every_s"] == 10.0


def test_manifest_update_preserves_created_utc(tmp_path, monkeypatch):
    """write_manifest would stamp a fresh created_utc; the digest is a later pass
    and must not lie about when the video was probed."""
    import json
    from nybls_core import store
    ws = tmp_path
    (ws / "frames").mkdir()
    monkeypatch.setattr(store, "workspace", lambda vid: ws)
    manifest = ws / "manifest.json"
    manifest.write_text(json.dumps({"id": "test", "created_utc": "2026-09-01T00:00:00Z"}))
    data = dg.update_manifest("test", {"digest": {"frames": 9}})
    assert data["created_utc"] == "2026-09-01T00:00:00Z"
    assert data["digest"]["frames"] == 9


def test_digest_never_spends_ledger():
    """The whole point of the pass is that it is free. Pin the property the way
    TESTING.md rule 3 pins the silent-video guidance: on the source, not lines."""
    import inspect
    from nybls_core import cli
    src = inspect.getsource(cli.cmd_digest)
    assert "led.record" not in src, "digest must stay a zero-vision-token pass"
    assert "budget" not in src.replace("budgeted", ""), "no budget gate applies to a free pass"
