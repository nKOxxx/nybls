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


def test_install_docs_use_pipx_not_bare_pip():
    """`pip install nybls` is refused under PEP 668 on Homebrew Python and most
    current Linux distributions, so it fails on a normal modern Mac. Both docs
    must lead with pipx, and must never suggest overriding the guard with
    --break-system-packages on someone else's machine."""
    from pathlib import Path
    root = Path(__file__).parent.parent
    for name in ("README.md", "INSTALL.md"):
        doc = (root / name).read_text()
        assert "pipx install" in doc, f"{name} must lead with pipx"
        assert "PEP 668" in doc, f"{name} must say why"
        # The flag may be named in prose in order to forbid it. What must never
        # happen is it appearing in a command someone can copy and run.
        import re
        blocks = re.findall(r"```[a-z]*\n(.*?)```", doc, re.S)
        assert not any("--break-system-packages" in b for b in blocks), \
            f"{name} must not put --break-system-packages in a runnable block"


def test_every_command_is_documented_somewhere():
    """`speakers` shipped in 0.9.0 and was documented only in the README, so the
    skill an agent follows did not know it existed. Every command the CLI exposes
    must appear in at least one document a reader or an agent will actually see."""
    import re
    from pathlib import Path
    root = Path(__file__).parent.parent
    src = (root / "nybls_core/cli.py").read_text()
    commands = set(re.findall(r'sub\.add_parser\("([a-z-]+)"', src))
    docs = "\n".join((root / n).read_text() for n in
                     ("README.md", "docs/PROTOCOL.md", "skills/watch/SKILL.md", "INSTALL.md"))
    # serve/inbox/approve/reject are the phone-sharing path, documented in SECURITY
    docs += (root / "docs/SECURITY.md").read_text()
    missing = sorted(c for c in commands if c not in docs)
    assert not missing, f"undocumented commands: {missing}"


def test_the_skill_gives_an_install_command_that_works():
    """The skill's preflight fires exactly when the CLI is missing, so the one
    thing it must get right is the install line. It shipped `pip install nybls`,
    which is refused under PEP 668 on Homebrew Python and most current Linux."""
    import re
    from pathlib import Path
    skill = (Path(__file__).parent.parent / "skills/watch/SKILL.md").read_text()
    blocks = re.findall(r"```[a-z]*\n(.*?)```", skill, re.S)
    installs = [b for b in blocks if "install" in b and "nybls" in b]
    assert installs, "the skill must show an install command"
    for b in installs:
        assert "pipx install" in b, f"skill install block must use pipx:\n{b}"
        assert not re.search(r"^\s*pip install nybls", b, re.M), f"bare pip install:\n{b}"
