import pytest

from nybls_core import ingest


@pytest.mark.parametrize("url", [
    "https://127.0.0.1/x", "https://localhost/x", "https://10.0.0.5/x",
    "https://192.168.1.1/x", "https://169.254.169.254/latest/meta-data", "https://[::1]/x",
])
def test_non_public_hosts_are_refused(url):
    with pytest.raises(ValueError, match="non-public"):
        ingest.check_public_url(url)


def test_opt_out_allows_private(monkeypatch):
    monkeypatch.setenv("NYBLS_ALLOW_PRIVATE", "1")
    ingest.check_public_url("https://192.168.1.1/x")


def test_ytdlp_calls_end_options_before_the_source():
    import inspect
    src = inspect.getsource(ingest.ingest)
    assert src.count('"--", source') == 3


@pytest.mark.parametrize("url", [
    "https://100.100.100.200/x", "https://100.64.0.1/x", "https://[::ffff:100.100.100.200]/x",
    "https://[::ffff:127.0.0.1]/x",
])
def test_cgnat_and_mapped_addresses_are_refused(url):
    with pytest.raises(ValueError, match="non-public"):
        ingest.check_public_url(url)


def test_allow_private_zero_does_not_disable_the_guard(monkeypatch):
    monkeypatch.setenv("NYBLS_ALLOW_PRIVATE", "0")
    with pytest.raises(ValueError):
        ingest.check_public_url("https://127.0.0.1/x")


def test_ingest_rejects_non_https_before_any_subprocess(monkeypatch):
    monkeypatch.setattr(ingest, "_run", lambda *a, **k: pytest.fail("ran yt-dlp"))
    with pytest.raises(ValueError, match="https"):
        ingest.ingest("http://example.com/v")
