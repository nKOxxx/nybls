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
    monkeypatch.setattr(tr, "MODEL_DIR", tmp_path)
    monkeypatch.setattr(tr.subprocess, "run", _fake_curl(b"not a model"))
    with pytest.raises(RuntimeError, match="SHA-256"):
        tr.model_path("tiny")
    assert list(tmp_path.iterdir()) == []


def test_good_checksum_is_kept(tmp_path, monkeypatch):
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
