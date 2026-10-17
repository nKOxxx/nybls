"""Real pipeline on a generated video: probe, sheet, frames, zoom, ledger.

The rest of the suite never calls ffmpeg. This one does, so the core path
(ingest, scene map, contact sheet, frame extraction, spend ledger) is exercised
for real. Skipped when ffmpeg is absent. The generated video has a tone but no
speech, so the transcript step is told there are no captions and is not asked to
download a model: NYBLS_NO_DOWNLOAD is set and `probe` must degrade, not fail.
"""
import os
import re
import shutil
import subprocess
import sys

import pytest

pytestmark = pytest.mark.skipif(
    not (shutil.which("ffmpeg") and shutil.which("ffprobe")), reason="ffmpeg not installed")


@pytest.fixture(scope="module")
def env(tmp_path_factory):
    home = tmp_path_factory.mktemp("home")
    video = home / "demo.mp4"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "testsrc=duration=12:size=640x360:rate=10",
         "-f", "lavfi", "-i", "sine=frequency=440:duration=12", "-shortest",
         "-pix_fmt", "yuv420p", str(video)], check=True)
    e = {**os.environ, "HOME": str(home), "NYBLS_NO_DOWNLOAD": "1"}
    return video, e


def nybls(env, *args):
    return subprocess.run([sys.executable, "-m", "nybls_core.cli", *args],
                          capture_output=True, text=True, env=env, timeout=120)


def test_probe_sheet_frames_zoom_ledger(env):
    video, e = env
    r = nybls(e, "probe", str(video))
    assert r.returncode == 0, r.stderr
    m = re.search(r"^id:\s*(\S+)", r.stdout, re.M)
    assert m, r.stdout
    vid = m.group(1)
    assert "640x360" in r.stdout  # dimensions are reported

    r = nybls(e, "sheet", vid)
    assert r.returncode == 0, r.stderr
    assert ".png" in r.stdout

    r = nybls(e, "frames", vid, "--at", "3", "--looking-for", "3s to 3s: the counter reads about 3")
    assert r.returncode == 0, r.stderr

    r = nybls(e, "zoom", vid, "--at", "3", "--box", "0,0,0.5,0.5", "--looking-for", "top left corner")
    assert r.returncode == 0, r.stderr

    r = nybls(e, "ledger", vid)
    assert r.returncode == 0, r.stderr
    assert "image" in r.stdout.lower()


def test_unknown_id_fails_cleanly(env):
    _, e = env
    r = nybls(e, "sheet", "doesnotexist")
    assert r.returncode != 0
    assert "Traceback" not in r.stderr
