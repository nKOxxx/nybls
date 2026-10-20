import hashlib
import subprocess

import pytest

from nybls_core import transcribe as tr


def test_every_model_has_a_pinned_sha256():
    for fname, _, _ in tr.MODELS.values():
        assert len(tr.SHA256[fname]) == 64


def _fake_curl(payload):
    def run(cmd, **kw):
        out = cmd[cmd.index("-o") + 1]
        open(out, "wb").write(payload)
        return subprocess.CompletedProcess(cmd, 0)
    return run


def test_bad_checksum_is_discarded(tmp_path, monkeypatch):
    monkeypatch.setenv("NYBLS_ASSUME_YES", "1")
    monkeypatch.setattr(tr, "MODEL_DIR", tmp_path)
    monkeypatch.setattr(tr.subprocess, "run", _fake_curl(b"not a model"))
    with pytest.raises(RuntimeError, match="SHA-256"):
        tr.model_path("tiny")
    assert list(tmp_path.iterdir()) == []


def test_good_checksum_is_kept(tmp_path, monkeypatch):
    monkeypatch.setenv("NYBLS_ASSUME_YES", "1")
    payload = b"pretend model"
    monkeypatch.setattr(tr, "MODEL_DIR", tmp_path)
    monkeypatch.setitem(tr.SHA256, "ggml-tiny.en.bin", hashlib.sha256(payload).hexdigest())
    monkeypatch.setattr(tr.subprocess, "run", _fake_curl(payload))
    assert tr.model_path("tiny").read_bytes() == payload


def test_no_download_env_refuses_without_touching_the_network(tmp_path, monkeypatch):
    monkeypatch.setattr(tr, "MODEL_DIR", tmp_path)
    monkeypatch.setenv("NYBLS_NO_DOWNLOAD", "1")
    monkeypatch.setattr(tr.subprocess, "run", lambda *a, **k: pytest.fail("network"))
    with pytest.raises(FileNotFoundError, match="NYBLS_NO_DOWNLOAD"):
        tr.model_path("tiny")


def test_non_interactive_download_needs_explicit_opt_in(tmp_path, monkeypatch):
    monkeypatch.setattr(tr, "MODEL_DIR", tmp_path)
    monkeypatch.delenv("NYBLS_ASSUME_YES", raising=False)
    monkeypatch.delenv("NYBLS_NO_DOWNLOAD", raising=False)
    monkeypatch.setattr(tr.sys.stdin, "isatty", lambda: False)
    monkeypatch.setattr(tr.subprocess, "run", lambda *a, **k: pytest.fail("network"))
    with pytest.raises(FileNotFoundError, match="NYBLS_ASSUME_YES"):
        tr.model_path("tiny")


def test_existing_model_is_hashed_and_a_wrong_one_refused(tmp_path, monkeypatch):
    monkeypatch.setattr(tr, "MODEL_DIR", tmp_path)
    (tmp_path / "ggml-tiny.en.bin").write_bytes(b"tampered")
    with pytest.raises(RuntimeError, match="pinned SHA-256"):
        tr.model_path("tiny")


def test_existing_good_model_is_verified_once_then_trusted_by_sidecar(tmp_path, monkeypatch):
    payload = b"pretend model"
    monkeypatch.setattr(tr, "MODEL_DIR", tmp_path)
    monkeypatch.setitem(tr.SHA256, "ggml-tiny.en.bin", hashlib.sha256(payload).hexdigest())
    (tmp_path / "ggml-tiny.en.bin").write_bytes(payload)
    assert tr.model_path("tiny").exists()
    calls = []
    real = tr._sha256
    monkeypatch.setattr(tr, "_sha256", lambda p: (calls.append(p), real(p))[1])
    tr.model_path("tiny")
    assert calls == []  # the sidecar answered
    (tmp_path / "ggml-tiny.en.bin").write_bytes(b"swapped!!!!!!")  # size/mtime change
    with pytest.raises(RuntimeError):
        tr.model_path("tiny")
