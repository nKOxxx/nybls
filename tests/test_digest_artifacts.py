
# --- write_digest_artifacts (extracted from cli.cmd_digest) -----------------
# Pins: all three stage artifacts land in digest/, the manifest is patched,
# and an all-empty OCR run (textless frames) still produces valid artifacts.

from nybls_core import digest as dg  # noqa: E402 (convention: tests import core modules)

def _fake_frame(tmp_path, name, kb=2):
    p = tmp_path / name
    p.write_bytes(b"x" * (kb * 1024))
    return p


def test_write_digest_artifacts_creates_all_three_files(tmp_path, monkeypatch):
    ws = tmp_path / "ws"; ws.mkdir()
    frames_dir = tmp_path / "frames30"; frames_dir.mkdir()
    f1 = _fake_frame(frames_dir, "frame_00001.jpg")
    f2 = _fake_frame(frames_dir, "frame_00002.jpg")
    records = [
        {"frame": 1, "text": "hello world", "chars": 11},
        {"frame": 2, "text": "", "chars": 0},
    ]
    monkeypatch.setattr(dg, "update_manifest", lambda vid, patch: {})
    stats = dg.write_digest_artifacts(ws, frames_dir, records, 30.0, "vid1", "T", "tesseract")

    assert (ws / "digest" / "ocr-index.jsonl").read_text().count("\n") == 2
    sheet = (ws / "digest" / "contact_sheet.html").read_text()
    assert "hello world" in sheet and "frames30/frame_00001.jpg" in sheet
    scenes_txt = (ws / "digest" / "scenes.txt").read_text()
    assert "vid1" in scenes_txt and "2 frames" in scenes_txt
    assert stats["hits"] == 1 and stats["n_frames"] == 2
    assert stats["idx"].exists() and stats["sheet"].exists() and stats["scenes_path"].exists()


def test_write_digest_artifacts_all_textless_still_valid(tmp_path, monkeypatch):
    """Textless pixels are logged as chars 0; pct math must not divide-by-zero and
    artifacts must still be written (the archive case)."""
    ws = tmp_path / "ws"; ws.mkdir()
    frames_dir = tmp_path / "frames30"; frames_dir.mkdir()
    _fake_frame(frames_dir, "frame_00001.jpg")
    records = [{"frame": 1, "text": "", "chars": 0}]
    captured = {}
    monkeypatch.setattr(dg, "update_manifest", lambda vid, patch: captured.update(patch))
    stats = dg.write_digest_artifacts(ws, frames_dir, records, 30.0, "vid2", "T", "tesseract")
    assert stats["hits"] == 0 and stats["n_frames"] == 1
    assert captured["digest"]["ocr_hits"] == 0 and captured["digest"]["engine"] == "tesseract"


def test_write_digest_artifacts_manifest_receives_engine_and_counts(tmp_path, monkeypatch):
    ws = tmp_path / "ws"; ws.mkdir()
    frames_dir = tmp_path / "frames30"; frames_dir.mkdir()
    _fake_frame(frames_dir, "frame_00001.jpg")
    records = [{"frame": 1, "text": "abc", "chars": 3}]
    captured = {}
    monkeypatch.setattr(dg, "update_manifest", lambda vid, patch: captured.update(patch))
    dg.write_digest_artifacts(ws, frames_dir, records, 15.0, "vid3", "T", "ocrmac")
    assert captured["digest"] == {"engine": "ocrmac", "every_s": 15.0, "frames": 1,
                                  "ocr_hits": 1, "scenes": 0}
