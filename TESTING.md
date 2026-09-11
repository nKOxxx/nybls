# How this project tests

Every rule below exists because it was broken here, in this repository, and
shipped. Each one names the incident that produced it and the file that enforces
it. A rule with no enforcement is not a rule, it is a wish, so if you add one,
add the check with it.

## The distinction the whole document rests on

A **claim** is something the tool asserts about the world. Does it beat a uniform
control? Is the answer grounded? Claims are what benchmarks measure, and this
project measures them hard: four rounds, 12 videos, 112 audited questions, the
latest round written and scored by separate agents with the arms hidden from the
judge.

A **premise** is something you assume in order to test the claims at all. That
the install command runs. That the binary is on PATH. That the file you are
parsing is the file that ships.

Premises do not feel like claims. They feel like the floor. That is why 58 tests,
a blind-judged benchmark round and an adversarial review pass all missed the fact
that the first command in the README had not worked for eight releases.

**A test can only fail if you were willing to be wrong about the thing it
checks.** Nobody was willing to be wrong about the floor.

## Rule 1: execute documented commands, never assert their text

For eight releases the README opened with `pip install nybls`, which PEP 668
refuses on Homebrew Python and most current Linux. Every check passed, because
every check read the command as a string.

Worse, the test written to protect that instruction asserted the broken command
was *present*, so a correct README would have failed CI. It confidently confirmed
its own mistake.

**Enforced by:** `scripts/check_documented_install.py` parses the platform table
out of `INSTALL.md` and runs those exact commands. `.github/workflows/install.yml`
runs it on every push and weekly against PyPI. If the docs drift, it breaks.

## Rule 2: test where it is not already working

`pipx install "nybls[download]"` left the tool unable to download anything. pipx
isolates nybls, so the extra's `yt-dlp` lands in that environment's bin directory
rather than on PATH, and `shutil.which` could not see it. nybls reported a
required dependency missing that it was itself shipping.

It passed on the author's Mac for one reason: Homebrew had put a second `yt-dlp`
on PATH years earlier. The machine was lying, and it had been lying the whole time.

Two clean CI runners found it in about ninety seconds.

**Enforced by:** the same workflow, on `ubuntu-latest` and `macos-latest`, which
have never seen this project. Verification runs against the built artifact in a
throwaway environment, never against the source tree.

## Rule 3: pin the property, not the current value

A test that asserts today's string will happily protect tomorrow's bug. When the
plugin description was wrong, the test asserting its contents was the thing
keeping it wrong.

Write the check against the property that must hold. Not `assert x == "pipx
install nybls"` but `assert the documented command executes`. Not `assert
"--break-system-packages" not in doc` (which fails a doc that forbids the flag)
but `assert it does not appear in a runnable block`.

**Enforced by:** `tests/test_footprint.py`, which greps fenced code blocks rather
than raw substrings, and `tests/test_cli_surface.py`, which requires the install
command to be one that works rather than one that matches.

## Rule 4: a release gate must be able to stop a release

`pytest` in the publish workflow ended in `|| true`. A failing test could not have
stopped a release, and nobody noticed because the tests were passing.

**Enforced by:** `.github/workflows/publish.yml` runs the full suite and the
clean-environment install before `gh-action-pypi-publish`, with no swallowed exit
codes. A build a stranger cannot install does not ship.

## Rule 5: verify against the artifact, never the working copy

The source tree is the most contaminated environment you own. Editable installs
go stale (`nybls --version` reported 0.7.1 for three releases), caches lie
(pipx served a stale index twice), and your PATH holds things a user's does not.

Check the wheel, the fresh clone, the live index. The git history purge was
verified by cloning the remote and grepping every blob that had ever existed, not
by looking at the local repo.

**Enforced by:** habit, and by Rules 1 and 2 making the artifact path the default.
This is the weakest rule here, because it is the one still carried by discipline.

## Rule 6: say what is untested, in the artifact, not in your head

`speakers` was measured properly on exactly one call. Gallery view has never been
tested. Attribution collapses during a screen share. Screen time is a proxy for
talk time, not a measurement of it.

All four sentences are in the README, next to the feature, because a limit known
only to the author is not a limit, it is a trap.

**Enforced by:** `tests/test_footprint.py::test_every_command_is_documented_somewhere`,
which fails if a command exists that no document mentions. It cannot check that a
limit is stated honestly, only that the feature is not silent.

## What this still does not cover

Stated plainly, because Rule 6 applies to this document too.

- **Linux and Windows install paths beyond Ubuntu.** The `INSTALL.md` table lists
  dnf, pacman, winget and Chocolatey. Only the Debian and macOS rows are executed
  by CI. The rest are written from documentation and have never been run.
- **The Claude Code plugin install.** Verified once, by hand, on one machine. No
  automated check exists, because it needs an interactive client.
- **Non-English video.** The ASR guard is validated on space-separated scripts and
  deliberately skips CJK. No test covers Arabic, German or anything else.
- **The benchmark reference itself.** Round 4 built ground truth from a dense
  uniform grid by an agent with no access to the tool, which is a large
  improvement over earlier rounds, but the reference is still machine-made.
