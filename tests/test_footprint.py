"""The install size ceiling is 150 MB. A clean `pip install nybls` measured 293 MB
on 2026-09-04, and 219 MB of it was opencv and scipy, dragged in by two libraries
we used one function from each. Those functions now live on ffmpeg and numpy.
This file makes the regression loud: if either heavy library is imported by the
core package again, the budget is blown silently and nobody notices until a user
complains about a 300 MB download for a 36 KB tool.
"""
import subprocess
import sys

import numpy as np
from PIL import Image

from nybls_core import media


def test_core_never_imports_the_heavy_libraries():
    code = ("import sys, nybls_core.media, nybls_core.cli, nybls_core.verify, "
            "nybls_core.corpus, nybls_core.transcribe; "
            "print(sorted(m for m in sys.modules if m.split('.')[0] in "
            "('cv2','scipy','scenedetect','imagehash','pywt')))")
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == "[]", f"heavy modules loaded: {r.stdout}"


def test_declared_dependencies_are_only_numpy_and_pillow():
    import tomllib
    from pathlib import Path
    deps = tomllib.loads((Path(__file__).parent.parent / "pyproject.toml").read_text())["project"]["dependencies"]
    names = sorted(d.split(">")[0].split("=")[0].strip().lower() for d in deps)
    assert names == ["numpy", "pillow"], names


def _img(seed: int) -> Image.Image:
    rng = np.random.default_rng(seed)
    return Image.fromarray(rng.integers(0, 255, (64, 96, 3), dtype=np.uint8))


def test_phash_is_16_hex_and_deterministic():
    h = media.phash_hex(_img(1))
    assert len(h) == 16 and int(h, 16) >= 0
    assert media.phash_hex(_img(1)) == h


def test_hamming_zero_for_self_and_large_for_unrelated():
    a, b = media.phash_hex(_img(1)), media.phash_hex(_img(2))
    assert media.hamming(a, a) == 0
    assert media.hamming(a, b) > media.DEDUP_HAMMING


def test_phash_matches_reference_library_if_available():
    """Bit-compatibility keeps every stored `_phashes.json` valid across the
    dependency change. Verified on 217 real frames at the time of the change;
    this re-checks whenever the reference library happens to be installed."""
    try:
        import imagehash
    except ImportError:
        import pytest
        pytest.skip("imagehash not installed (it is only a bench extra now)")
    for seed in range(5):
        img = _img(seed)
        assert str(imagehash.phash(img)) == media.phash_hex(img)


def test_download_extra_exists_and_base_install_stays_lean():
    """`yt-dlp` is a Python package, so URL downloads need no system package
    manager. It stays an extra rather than a dependency because it adds ~25 MB
    and local files work without it, which keeps the advertised base install
    honest."""
    import tomllib
    from pathlib import Path
    proj = tomllib.loads((Path(__file__).parent.parent / "pyproject.toml").read_text())["project"]
    extras = proj["optional-dependencies"]
    assert "download" in extras and any("yt-dlp" in d for d in extras["download"])
    assert not any("yt-dlp" in d for d in proj["dependencies"]), "must not be a base dependency"


def test_install_doc_covers_more_than_homebrew():
    """The install page is meant to be followed by an agent on someone else's
    machine. Homebrew-only instructions would make it guess on Linux."""
    from pathlib import Path
    doc = (Path(__file__).parent.parent / "INSTALL.md").read_text()
    for token in ("brew install ffmpeg", "apt", "dnf", "winget", "nybls doctor"):
        assert token in doc, token
    assert "sudo" in doc, "must tell the agent to ask before sudo"
