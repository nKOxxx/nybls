"""TESTING.md claims each rule is enforced by a specific file. Check that.

A standards document is the easiest thing in a repository to let rot. It states
what you intend, nothing executes it, and it stays true-sounding long after it
has stopped being true. That is the same failure it was written about: a claim
nobody was willing to be wrong about.

So the document's own enforcement claims are checked here. If a rule cites a
mechanism, the mechanism must exist.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOC = (ROOT / "TESTING.md").read_text()


def test_every_file_the_document_cites_exists():
    """A rule pointing at a file that is gone is worse than no rule."""
    cited = set(re.findall(r"`((?:scripts|tests|\.github)/[\w./-]+)`", DOC))
    assert cited, "the document should cite its enforcement points"
    missing = sorted(p for p in cited if not (ROOT / p).exists())
    assert not missing, f"TESTING.md cites files that do not exist: {missing}"


def test_the_install_check_is_wired_into_ci_and_the_release():
    """Rules 1 and 4 both rest on this. If either wiring is removed, the
    document is lying and the class of bug is back."""
    install_wf = (ROOT / ".github/workflows/install.yml").read_text()
    publish_wf = (ROOT / ".github/workflows/publish.yml").read_text()
    assert "check_documented_install.py" in install_wf, "not wired into CI"
    assert "check_documented_install.py" in publish_wf, "not gating the release"
    assert "ubuntu-latest" in install_wf and "macos-latest" in install_wf, \
        "Rule 2 requires machines that do not already have it working"


def test_no_swallowed_failures_in_any_workflow():
    """Rule 4. `pytest ... || true` meant a failing test could not stop a
    release, and nobody noticed because the tests were passing."""
    for wf in (ROOT / ".github/workflows").glob("*.yml"):
        assert "|| true" not in wf.read_text(), f"{wf.name} swallows a failure"


def test_the_document_admits_what_is_not_covered():
    """Rule 6 applies to the document itself. An honest standards doc that
    claims full coverage is just a more confident lie."""
    assert "What this still does not cover" in DOC
    body = DOC.split("What this still does not cover", 1)[1]
    assert len(body.split()) > 80, "the gaps section must be substantive"
