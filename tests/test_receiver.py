import http.client
import json
import threading
from http.server import ThreadingHTTPServer

import pytest

from nybls_core import receiver as r


@pytest.fixture
def srv(tmp_path, monkeypatch):
    monkeypatch.setattr(r, "INBOX", tmp_path / "inbox")
    monkeypatch.setattr(r, "UPLOADS", tmp_path / "up")
    monkeypatch.setattr(r, "TOKEN_FILE", tmp_path / "tok")
    monkeypatch.setattr(r, "notify", lambda *a, **k: None)
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), r.Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    yield httpd.server_address[1], r.token()
    httpd.shutdown()
    httpd.server_close()


def call(port, method, path, token=None, body=b"", headers=None):
    c = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
    h = dict(headers or {})
    if token:
        h["Authorization"] = f"Bearer {token}"
    c.request(method, path, body=body, headers=h)
    resp = c.getresponse()
    return resp.status, json.loads(resp.read() or b"{}")


def test_no_token_and_wrong_token_are_refused(srv):
    port, _ = srv
    assert call(port, "GET", "/status")[0] == 401
    assert call(port, "GET", "/status", token="nope")[0] == 401
    assert call(port, "POST", "/watch", body=b"{}")[0] == 401


def test_watch_accepts_only_https_and_holds_it_pending(srv):
    port, tok = srv
    assert call(port, "POST", "/watch", tok, json.dumps({"url": "http://x.example/v"}).encode())[0] == 400
    assert call(port, "POST", "/watch", tok, json.dumps({"url": "file:///etc/passwd"}).encode())[0] == 400
    code, out = call(port, "POST", "/watch", tok, json.dumps({"url": "https://example.com/v"}).encode())
    assert code == 202
    assert [i["status"] for i in r.items()] == ["pending"]


def test_upload_filename_is_sanitized_and_type_checked(srv, tmp_path):
    port, tok = srv
    code, _ = call(port, "POST", "/upload", tok, b"x", {"X-Filename": "evil.sh"})
    assert code == 400
    code, _ = call(port, "POST", "/upload", tok, b"abc", {"X-Filename": "../../etc/pa ss.mp4"})
    assert code == 202
    saved = list((tmp_path / "up").iterdir())
    assert len(saved) == 1 and saved[0].parent == tmp_path / "up" and "/" not in saved[0].name


def test_oversized_and_malformed_lengths_are_refused(srv):
    port, tok = srv
    assert call(port, "POST", "/watch", tok, b"x", {"Content-Length": "-5"})[0] == 400
    assert call(port, "POST", "/watch", tok, b"x" * (r.MAX_JSON + 1))[0] == 413


def test_only_approved_items_are_ever_processed(srv, monkeypatch):
    port, tok = srv
    for u in ("https://example.com/a", "https://example.com/b"):
        call(port, "POST", "/watch", tok, json.dumps({"url": u}).encode())
    first = r.items()[0]["id"]
    r.set_status(first, "approved")
    seen = []
    stop = threading.Event()
    monkeypatch.setattr(r, "_process", lambda item: (seen.append(item["id"]), stop.set()))
    r.worker_loop(stop)
    assert seen == [first]
