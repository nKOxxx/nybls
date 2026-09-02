"""A corpus: many videos from one source, read as one body of work.

The hard part is not merging. It is telling two things apart that look identical
in the data:

  - a **contradiction** — two sources asserting incompatible things, which the
    reader must adjudicate; and
  - an **evolution** — one author changing their mind over time, which is not a
    contradiction at all but the most interesting thing a corpus can show you.

Both look like "claim A conflicts with claim B" until you know who said each and
when. So every claim carries two clocks (after ATOM, arXiv:2510.22590):
`at`, the moment inside its video, and `observed`, the date that video was
published. Same author + different dates = evolution. Different authors, or the
same date = contradiction, surfaced and never silently resolved.

The tool does the mechanical half: assembling the timeline, verifying each
citation against its own video's transcript, and flagging candidate pairs. Deciding
whether two claims genuinely conflict is a judgement, and stays with the reader.
"""
from __future__ import annotations

import json
from pathlib import Path

from .store import read_manifest, utc_now, workspace

CORPORA = Path.home() / ".nybls" / "corpora"


def _dir() -> Path:
    CORPORA.mkdir(parents=True, exist_ok=True)
    return CORPORA


def describe(media_id: str) -> dict:
    """Pull the facts a corpus needs from a video's own manifest."""
    m = read_manifest(media_id)
    ig = m.get("instagram") or {}
    return {
        "id": media_id,
        "title": m.get("title") or "",
        "author": ig.get("owner") or "",
        "observed": (ig.get("posted") or "")[:10],
        "duration_s": m.get("duration_s", 0),
        "transcript": bool(m.get("transcript")),
    }


def register(name: str, ids: list[str]) -> dict:
    path = _dir() / f"{name}.json"
    existing = json.loads(path.read_text()) if path.exists() else {"name": name, "videos": []}
    known = {v["id"] for v in existing["videos"]}
    added, failed = [], []
    for i in ids:
        if i in known:
            continue
        try:
            existing["videos"].append(describe(i))
            added.append(i)
        except FileNotFoundError:
            failed.append(i)
    # undated entries sort last rather than pretending to be oldest
    existing["videos"].sort(key=lambda v: v["observed"] or "9999-99-99")
    existing["updated_utc"] = utc_now()
    path.write_text(json.dumps(existing, indent=1))
    return {"corpus": existing, "added": added, "failed": failed}


def load(name: str) -> dict:
    path = _dir() / f"{name}.json"
    if not path.exists():
        raise FileNotFoundError(f"no corpus '{name}' — create it with `nybls corpus {name} --add <ids>`")
    return json.loads(path.read_text())


def list_all() -> list[str]:
    return sorted(p.stem for p in _dir().glob("*.json"))


def undated(corpus: dict) -> list[str]:
    """Videos with no publication date cannot be placed on the timeline, and an
    evolution claim about them would be unfounded."""
    return [v["id"] for v in corpus["videos"] if not v["observed"]]


def verify_corpus(corpus: dict, items: list[dict], label: str) -> list:
    """Verify each claim against the transcript of the video it names.

    A corpus makes citation drift easy: a claim can name video A while quoting
    video B, and nothing about the merged file would look wrong.
    """
    from . import verify as vf

    cache: dict[str, list] = {}
    verdicts = []
    for it in items:
        vid = it.get("video")
        if not vid:
            continue
        if vid not in cache:
            tpath = workspace(vid) / "transcript.txt"
            cache[vid] = vf.load_transcript(tpath) if tpath.exists() else []
        text = " ".join(str(it.get(k, "")) for k in (label, "rationale", "plain", "quote", "evidence"))
        v = vf.verify_claim(cache[vid], text.strip(), float(it.get("at", 0)))
        verdicts.append((vid, v))
    return verdicts


def evolution(corpus: dict, items: list[dict], subject_key: str) -> list[dict]:
    """Group claims by subject and order them by publication date.

    A subject touched by more than one video, on more than one date, by the same
    author, is a position that moved. That is the question a corpus exists to
    answer: what did they think, when, and what changed.
    """
    dates = {v["id"]: v["observed"] for v in corpus["videos"]}
    authors = {v["id"]: v["author"] for v in corpus["videos"]}

    groups: dict[str, list[dict]] = {}
    for it in items:
        subj = (it.get(subject_key) or "").strip()
        vid = it.get("video")
        if not subj or not vid:
            continue
        groups.setdefault(subj.lower(), []).append({
            "subject": subj,
            "video": vid,
            "observed": dates.get(vid, ""),
            "author": authors.get(vid, ""),
            "at": it.get("at"),
            "claim": it.get("decision") or it.get("claim") or it.get("name") or "",
            "rationale": it.get("rationale") or "",
            "supersedes": it.get("supersedes"),
        })

    out = []
    for subj, entries in groups.items():
        entries.sort(key=lambda e: e["observed"] or "9999-99-99")
        span = {e["observed"] for e in entries if e["observed"]}
        if len(entries) < 2:
            continue
        same_author = len({e["author"] for e in entries if e["author"]}) <= 1
        if len(span) > 1 and same_author:
            kind = "evolution"          # one voice, moving over time
        elif len(span) > 1:
            kind = "disagreement-over-time"
        else:
            kind = "same-date conflict"
        out.append({"subject": entries[0]["subject"], "kind": kind, "entries": entries})
    return sorted(out, key=lambda g: -len(g["entries"]))
