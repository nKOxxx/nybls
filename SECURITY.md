# Security policy

nybls is a local-first command line tool. The threat model and what is and is not
protected are in [docs/SECURITY.md](docs/SECURITY.md).

## Reporting a vulnerability

Please report privately through GitHub:
**Security tab, then "Report a vulnerability"** on
[nKOxxx/nybls](https://github.com/nKOxxx/nybls/security/advisories/new).
Do not open a public issue for something exploitable.

Expect an acknowledgement within a few days. This is a small project maintained
by one person, so there is no bounty and no formal SLA, but credible reports are
fixed and credited.

## Supported versions

Only the latest release on PyPI receives fixes.

## In scope

The CLI, the phone-share receiver (`nybls serve`), the download path (yt-dlp
invocation, URL handling), model downloads, and the skill and plugin files.

## Out of scope

Prompt injection through the content of a video is a known, documented limit of
any tool that shows media to a model. Reports that a video can contain
instructions are not vulnerabilities; reports that the tool acts on them
without the agent's involvement would be.
