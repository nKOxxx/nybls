"""Phone-share receiver: private HTTP endpoint + background worker.

Binds to the Tailscale address when connected (private to your own devices),
otherwise localhost only. Never exposed to the public internet.
"""
import hmac
import json
import re
import secrets
import subprocess
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from .store import scrub, utc_now

INBOX = Path.home() / ".nybls" / "inbox"
UPLOADS = Path.home() / ".nybls" / "uploads"
TOKEN_FILE = Path.home() / ".nybls" / "secrets" / "receiver_token"
MAX_UPLOAD = 500 * 1024 * 1024  # 500 MB
SAFE_NAME = re.compile(r"[^A-Za-z0-9._-]")
MEDIA_SUFFIXES = {".mp4", ".mov", ".m4v", ".webm", ".mkv", ".jpg", ".jpeg", ".png", ".webp"}
PORT = 8422


def token() -> str:
    if not TOKEN_FILE.exists():
        TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)
        TOKEN_FILE.write_text(secrets.token_urlsafe(32))
        TOKEN_FILE.chmod(0o600)
    return TOKEN_FILE.read_text().strip()


def bind_host() -> tuple[str, str]:
    """Tailscale IP if connected, else localhost. Never 0.0.0.0."""
    for tsbin in ("/usr/local/bin/tailscale", "/Applications/Tailscale.app/Contents/MacOS/Tailscale"):
        if not Path(tsbin).exists():
            continue
        try:
            r = subprocess.run([tsbin, "ip", "-4"], capture_output=True, text=True, timeout=5)
            ip = (r.stdout or "").strip().splitlines()
            if r.returncode == 0 and ip and ip[0].startswith("100."):
                return ip[0], "tailscale (reachable from your phone)"
        except Exception:  # noqa: BLE001 — tailscale absent/stopped is expected
            pass
    return "127.0.0.1", "localhost only — Tailscale is not connected, so the phone cannot reach this yet"


# ── queue ────────────────────────────────────────────────────────────────────

def notify(title: str, message: str) -> None:
    """Non-blocking macOS notification — arg array, never a shell string."""
    try:
        subprocess.run(
            ["osascript", "-e", "on run {t, m}\ndisplay notification m with title t\nend run",
             title, message],
            capture_output=True, timeout=10,
        )
    except Exception:  # noqa: BLE001 — a failed notification must never break intake
        pass


def enqueue(source: str, kind: str) -> dict:
    INBOX.mkdir(parents=True, exist_ok=True)
    item = {
        "id": uuid.uuid4().hex[:12],
        "source": source,
        "kind": kind,
        "received_utc": utc_now(),
        "status": "pending",  # nothing is downloaded until you approve
        "media_id": None,
        "note": None,
    }
    (INBOX / f"{item['id']}.json").write_text(json.dumps(item, indent=1))
    notify("nybls — approval needed", f"{source[:90]}\nRun: nybls approve {item['id']}")
    return item


def set_status(item_id: str, status: str) -> dict:
    p = INBOX / f"{re.sub(r'[^a-f0-9]', '', item_id)}.json"
    if not p.exists():
        raise FileNotFoundError(f"no inbox item {item_id}")
    item = json.loads(p.read_text())
    item["status"] = status
    p.write_text(json.dumps(item, indent=1))
    return item


def _save(item: dict) -> None:
    (INBOX / f"{item['id']}.json").write_text(json.dumps(item, indent=1))


def items(limit: int = 20) -> list[dict]:
    INBOX.mkdir(parents=True, exist_ok=True)
    files = sorted(INBOX.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return [json.loads(p.read_text()) for p in files[:limit]]


# ── worker ───────────────────────────────────────────────────────────────────

def _process(item: dict) -> None:
    item["status"] = "processing"
    _save(item)
    r = subprocess.run(
        [sys.executable, "-m", "nybls_core.cli", "probe", item["source"]],
        capture_output=True, text=True, timeout=3600,
        cwd=str(Path(__file__).resolve().parent.parent),
    )
    if r.returncode == 0:
        m = re.search(r"^id:\s*(\S+)", r.stdout, re.M)
        item["media_id"] = m.group(1) if m else None
        title = re.search(r"^title:\s*(.+)$", r.stdout, re.M)
        poster = re.search(r"^posted by:\s*(.+)$", r.stdout, re.M)
        item["note"] = (title.group(1) if title else "") or (poster.group(1) if poster else "")
        item["status"] = "ready"
    else:
        item["status"] = "error"
        item["note"] = scrub((r.stderr or "unknown error").strip()[-300:])
    item["finished_utc"] = utc_now()
    _save(item)


def worker_loop(stop: threading.Event) -> None:
    while not stop.is_set():
        # only items YOU approved are ever fetched — "pending" is never touched
        approved = [i for i in items(200) if i["status"] == "approved"]
        for item in sorted(approved, key=lambda i: i["received_utc"]):
            try:
                _process(item)
            except Exception as e:  # noqa: BLE001 — one bad item must not kill the worker
                item["status"] = "error"
                item["note"] = scrub(str(e))[:300]
                _save(item)
        stop.wait(3)


# ── http ─────────────────────────────────────────────────────────────────────

class Handler(BaseHTTPRequestHandler):
    server_version = "nybls"

    def _auth_ok(self) -> bool:
        got = (self.headers.get("Authorization") or "").removeprefix("Bearer ").strip()
        return bool(got) and hmac.compare_digest(got, token())

    def _reply(self, code: int, payload: dict) -> None:
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):  # quieter, and never logs the token
        sys.stderr.write(f"[{utc_now()}] {self.address_string()} {fmt % args}\n")

    def do_GET(self):  # noqa: N802
        if not self._auth_ok():
            return self._reply(401, {"error": "unauthorized"})
        if self.path.startswith("/status"):
            return self._reply(200, {"items": [
                {k: v for k, v in i.items() if k in ("id", "status", "note", "media_id", "received_utc")}
                for i in items(10)
            ]})
        self._reply(404, {"error": "not found"})

    def do_POST(self):  # noqa: N802
        if not self._auth_ok():
            return self._reply(401, {"error": "unauthorized"})
        length = int(self.headers.get("Content-Length") or 0)
        if length > MAX_UPLOAD:
            return self._reply(413, {"error": "file too large (max 500 MB)"})

        if self.path.startswith("/watch"):
            try:
                data = json.loads(self.rfile.read(length) or b"{}")
                url = str(data.get("url", "")).strip()
            except Exception:  # noqa: BLE001
                return self._reply(400, {"error": "expected JSON body with a url field"})
            if urlparse(url).scheme != "https":
                return self._reply(400, {"error": "only https links are accepted"})
            item = enqueue(url, "url")
            return self._reply(202, {"received": item["id"], "status": "awaiting approval on the Mac"})

        if self.path.startswith("/upload"):
            raw_name = (self.headers.get("X-Filename") or "video.mp4").strip()
            name = SAFE_NAME.sub("_", Path(raw_name).name)[:120]
            if Path(name).suffix.lower() not in MEDIA_SUFFIXES:
                return self._reply(400, {"error": f"unsupported file type: {Path(name).suffix or 'none'}"})
            UPLOADS.mkdir(parents=True, exist_ok=True)
            dest = UPLOADS / f"{int(time.time())}_{name}"
            remaining, chunk = length, 1 << 20
            with dest.open("wb") as fh:
                while remaining > 0:
                    buf = self.rfile.read(min(chunk, remaining))
                    if not buf:
                        break
                    fh.write(buf)
                    remaining -= len(buf)
            item = enqueue(str(dest), "file")
            return self._reply(202, {"received": item["id"], "status": "awaiting approval on the Mac"})

        self._reply(404, {"error": "not found"})


def serve(window_min: int = 30) -> int:
    """Open the intake window. Not a daemon: runs only while you keep it open."""
    host, mode = bind_host()
    token()  # ensure it exists; never printed
    stop = threading.Event()
    threading.Thread(target=worker_loop, args=(stop,), daemon=True).start()
    try:
        httpd = ThreadingHTTPServer((host, PORT), Handler)
    except OSError:
        # Tailscale address configured but interface down (Tailscale not connected)
        host, mode = "127.0.0.1", "localhost only — connect Tailscale to reach this from the phone"
        httpd = ThreadingHTTPServer((host, PORT), Handler)

    until = f"for {window_min} min" if window_min else "until you press Ctrl-C"
    print(f"intake window OPEN on http://{host}:{PORT} {until}  [{mode}]")
    print("shares arrive as PENDING — nothing is downloaded until you run `nybls approve <id>`")
    print("token: cat ~/.nybls/secrets/receiver_token")
    if window_min:
        threading.Timer(window_min * 60, httpd.shutdown).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        stop.set()
        httpd.server_close()
    print("\nintake window CLOSED — nothing is listening now.")
    pend = [i for i in items(50) if i["status"] == "pending"]
    if pend:
        print(f"{len(pend)} item(s) still awaiting approval: nybls inbox")
    return 0
