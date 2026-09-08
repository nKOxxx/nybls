"""`nybls --version` errored instead of printing a version through 0.7.1.

It is the first thing anyone types after installing, and the failure mode is
silent to us: a required subcommand makes argparse reject the bare flag, so
the release still passes every test that invokes a subcommand.
"""
import subprocess
import sys


def test_version_flag_exits_clean():
    r = subprocess.run(
        [sys.executable, "-m", "nybls_core.cli", "--version"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.startswith("nybls "), r.stdout


def test_version_is_not_hardcoded():
    """The version must come from package metadata, so it cannot drift from
    pyproject.toml the way a literal in the source would."""
    from nybls_core import cli
    src = __import__("inspect").getsource(cli._version)
    assert "_pkg_version" in src


def test_plugin_manifests_match_package_version():
    """The Claude Code plugin manifests carried 0.7.1 while PyPI served 0.8.0.
    Nothing exercised them, so nothing noticed. Three files, one version."""
    import json, re
    from pathlib import Path
    root = Path(__file__).parent.parent
    ver = re.search(r'^version = "([^"]+)"', (root / "pyproject.toml").read_text(), re.M).group(1)
    plugin = json.loads((root / ".claude-plugin/plugin.json").read_text())
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    assert plugin["version"] == ver
    assert all(p["version"] == ver for p in market["plugins"])


def test_plugin_description_carries_the_package_line_plus_prerequisites():
    """Two audiences, so two descriptions, but they must not drift apart.

    pyproject's description is the PyPI summary, read by someone who already
    has pip. plugin.json's is what the Claude Code Discover tab shows, read by
    someone about to install who may not have ffmpeg or the CLI at all. There
    is no prerequisites field in plugin.json, so the description is the only
    place a prerequisite can be stated before install rather than after.
    """
    import json, re
    from pathlib import Path
    root = Path(__file__).parent.parent
    desc = re.search(r'^description = "(.+)"$', (root / "pyproject.toml").read_text(), re.M).group(1)
    plugin = json.loads((root / ".claude-plugin/plugin.json").read_text())["description"]
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text())["plugins"]
    assert plugin.startswith(desc), "plugin description must lead with the package line"
    for text in (plugin, *[m["description"] for m in market]):
        assert "ffmpeg" in text and "pip install nybls" in text, "state the prerequisites"
    for text in (desc, plugin, *[m["description"] for m in market]):
        assert "—" not in text and "–" not in text, "no dashes in shipped copy"
