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
