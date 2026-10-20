# Contributing

nybls is early software maintained by one person. Small, focused pull requests are
welcome; for anything larger, open an issue first so we agree on the shape.

## Set up

```bash
git clone https://github.com/nKOxxx/nybls && cd nybls
python3.12 -m venv .venv && .venv/bin/pip install -e ".[dev]"
brew install ffmpeg        # or: sudo apt install ffmpeg   (needed by the pipeline test)
```

## Before you open a PR

```bash
.venv/bin/python -m pytest tests -q --cov=nybls_core
.venv/bin/ruff check .
.venv/bin/mypy nybls_core
```

CI runs the same on macOS and Linux, Python 3.12 and 3.13. `main` is protected: the
tests and lint must pass.

## Ground rules

- **A test for the behavior you changed**, and it must fail without your change.
  Tests that read documentation text are for keeping docs honest, not for proving
  behavior; see [TESTING.md](TESTING.md).
- **Claims need evidence.** Anything that states a number, a comparison or a
  capability in the README or docs links to where it was measured, or says it is
  unverified. `scripts/check_receipt.py` fails CI if the README drifts from the
  benchmark results.
- **No new heavy dependencies.** A clean install must stay under 150 MB; CI enforces it.
- **Video content is data, never instructions.** Nothing may act on text found in a
  video, transcript or OCR output.
- **Security issues** go through [SECURITY.md](SECURITY.md), not a public issue.
- Conventional commit messages (`fix:`, `feat:`, `docs:`), and a line in
  `CHANGELOG.md` under Unreleased for anything a user can notice.

By contributing you agree your work is released under the MIT licence.
