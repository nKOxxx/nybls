#!/usr/bin/env python3
"""Run the install this project actually documents, on a machine that does not have it.

The bug this exists to prevent: for eight releases the README's first command was
`pip install nybls`, which PEP 668 refuses on Homebrew Python and most current
Linux. Every test passed throughout, because the tests read the command as a
string and never executed it. One of them asserted the broken command was
present, so a correct README would have failed CI.

The fix is not a better assertion. It is to stop treating the documented command
as text. This script extracts the commands from INSTALL.md for the platform it is
running on, runs them, and then proves the result works by watching a video that
ffmpeg generates locally. If the docs drift, this breaks. That is the point.
"""
from __future__ import annotations

import argparse
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INSTALL_DOC = ROOT / "INSTALL.md"

# Which row of the platform table applies to the machine running this.
PLATFORM_ROW = {
    "Darwin": "macOS (Homebrew)",
    "Linux": "Debian, Ubuntu",
}


def run(cmd: str, *, check: bool = True) -> subprocess.CompletedProcess:
    print(f"$ {cmd}", flush=True)
    r = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if r.stdout.strip():
        print(r.stdout.rstrip(), flush=True)
    if r.returncode and check:
        print(r.stderr.rstrip(), file=sys.stderr, flush=True)
        raise SystemExit(f"FAILED: {cmd}")
    return r


def system_deps_command() -> str:
    """Pull this platform's row out of the table in INSTALL.md."""
    want = PLATFORM_ROW.get(platform.system())
    if want is None:
        raise SystemExit(f"no documented row for {platform.system()}")
    for line in INSTALL_DOC.read_text().splitlines():
        if line.startswith("|") and want in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            cmd = re.sub(r"^`|`$", "", cells[1].strip())
            if "`" in cmd:                      # rows that chain two commands
                cmd = " && ".join(re.findall(r"`([^`]+)`", cells[1]))
            return cmd
    raise SystemExit(f"no row matching {want!r} in INSTALL.md")


def package_command() -> str:
    """The pipx line from Step 2, taken verbatim from the doc."""
    m = re.search(r"## Step 2: nybls.*?```bash\n(.*?)```", INSTALL_DOC.read_text(), re.S)
    if not m:
        raise SystemExit("could not find the Step 2 install block in INSTALL.md")
    return m.group(1).strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", choices=("published", "local"), default="published",
                    help="published: install exactly what the docs say, from PyPI. "
                         "local: install the wheel in ./dist, to gate a release before it ships.")
    args = ap.parse_args()

    print("== system dependencies, as documented for this platform ==")
    run(system_deps_command())

    print("\n== the package, as documented ==")
    pkg = package_command()
    if args.source == "local":
        wheels = sorted((ROOT / "dist").glob("*.whl"))
        if not wheels:
            raise SystemExit("no wheel in dist/; run `python -m build` first")
        pkg = re.sub(r'"?nybls\[download\]"?', f'"{wheels[-1]}[download]"', pkg)
    run(pkg + " --force" if pkg.startswith("pipx") else pkg)

    print("\n== is the command on PATH, where the docs promise it ==")
    if not shutil.which("nybls"):
        raise SystemExit("nybls is not on PATH after the documented install")
    run("nybls --version")
    run("nybls doctor")

    # Prove it actually works, on a video ffmpeg makes locally so the check needs
    # no network and cannot be broken by a platform blocking downloads.
    print("\n== watch something, end to end ==")
    with tempfile.TemporaryDirectory() as d:
        clip = Path(d) / "clip.mp4"
        run(f'ffmpeg -hide_banner -loglevel error -f lavfi -i testsrc=duration=20:size=640x360:rate=10 '
            f'-f lavfi -i sine=frequency=440:duration=20 -shortest -pix_fmt yuv420p "{clip}"')
        probe = run(f'nybls probe "{clip}"')
        vid = re.search(r"^id: (\S+)", probe.stdout, re.M)
        if not vid:
            raise SystemExit("probe did not report an id")
        run(f"nybls sheet {vid.group(1)}")
        run(f"nybls ledger {vid.group(1)}")

    print("\nOK: the documented install works on a clean machine.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
