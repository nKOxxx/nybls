"""Workspace store: ~/.nybls/store/<id>/ with manifest.json as the contract."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 1
ID_RE = re.compile(r"^[A-Za-z0-9_-]{4,64}$")


def store_root() -> Path:
    root = Path.home() / ".nybls" / "store"
    root.mkdir(parents=True, exist_ok=True)
    return root


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def safe_id(video_id: str) -> str:
    if not ID_RE.match(video_id):
        raise ValueError(f"invalid video id: {video_id!r}")
    return video_id


def local_file_id(path: Path) -> str:
    h = hashlib.sha1(f"{path.resolve()}:{path.stat().st_size}".encode()).hexdigest()[:12]
    return f"local_{h}"


def workspace(video_id: str) -> Path:
    ws = store_root() / safe_id(video_id)
    ws.mkdir(parents=True, exist_ok=True)
    (ws / "frames").mkdir(exist_ok=True)
    return ws


def scrub(text: str) -> str:
    """Remove the home directory from any user-facing string (privacy guard)."""
    return text.replace(str(Path.home()), "~")


def write_manifest(video_id: str, data: dict) -> Path:
    ws = workspace(video_id)
    data = {"schema_version": SCHEMA_VERSION, "id": video_id, "created_utc": utc_now(), **data}
    p = ws / "manifest.json"
    p.write_text(json.dumps(data, indent=1))
    return p


def read_manifest(video_id: str) -> dict:
    p = workspace(video_id) / "manifest.json"
    if not p.exists():
        raise FileNotFoundError(f"no manifest for {video_id} — run `nybls probe` first")
    return json.loads(p.read_text())
