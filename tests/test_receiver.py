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


def test_upload_over_the_cap_is_refused_without_writing(srv, monkeypatch, tmp_path):
    port, tok = srv
    monkeypatch.setattr(r, "MAX_UPLOAD", 10)
    code, _ = call(port, "POST", "/upload", tok, b"x" * 11, {"X-Filename": "a.mp4"})
    assert code == 413
    assert not (tmp_path / "up").exists() or list((tmp_path / "up").iterdir()) == []


def test_truncated_upload_is_not_queued(srv, tmp_path):
    import socket
    port, tok = srv
    s = socket.create_connection(("127.0.0.1", port))
    s.sendall((f"POST /upload HTTP/1.1\r\nHost: x\r\nAuthorization: Bearer {tok}\r\n"
               "X-Filename: a.mp4\r\nContent-Length: 1000\r\n\r\n").encode() + b"only a little")
    s.shutdown(socket.SHUT_WR)
    assert b"400" in s.recv(200).split(b"\r\n")[0]
    s.close()
    assert r.items() == []
    assert not (tmp_path / "up").exists() or list((tmp_path / "up").iterdir()) == []


def test_empty_upload_is_refused(srv):
    port, tok = srv
    assert call(port, "POST", "/upload", tok, b"", {"X-Filename": "a.mp4"})[0] == 400


def test_pending_queue_is_capped(srv, monkeypatch):
    port, tok = srv
    monkeypatch.setattr(r, "MAX_PENDING_ITEMS", 2)
    body = json.dumps({"url": "https://example.com/v"}).encode()
    assert call(port, "POST", "/watch", tok, body)[0] == 202
    assert call(port, "POST", "/watch", tok, body)[0] == 202
    assert call(port, "POST", "/watch", tok, body)[0] == 429


def test_upload_dir_quota(srv, monkeypatch, tmp_path):
    port, tok = srv
    monkeypatch.setattr(r, "MAX_UPLOAD_DIR_BYTES", 5)
    assert call(port, "POST", "/upload", tok, b"abcdef", {"X-Filename": "a.mp4"})[0] == 507


def test_stalled_client_is_dropped_by_the_socket_timeout():
    assert r.Handler.timeout == r.SOCKET_TIMEOUT_S


def test_token_file_is_private_from_creation(tmp_path, monkeypatch):
    monkeypatch.setattr(r, "TOKEN_FILE", tmp_path / "secrets" / "tok")
    r.token()
    assert oct((tmp_path / "secrets" / "tok").stat().st_mode & 0o777) == "0o600"
    assert oct((tmp_path / "secrets").stat().st_mode & 0o777) == "0o700"
