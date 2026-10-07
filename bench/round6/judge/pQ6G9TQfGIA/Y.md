# Answers

1. **Insufficient evidence for the exact command.** At [00:39]-[00:48] the speaker says "open your laptop and type this, and this will help you install [Claude Code]" and [00:55] "All you need is Node.js." The command was shown on a slide/screen that no frame captures (am00_93s.png is a close-up of the speaker, no text). Seen: Node.js is the prerequisite. Not seen: the command text. I will not supply it from memory.

2. **Notifications command: insufficient evidence.** The transcript [02:45]-[03:30] lists the setup steps but never names a notifications command, and no frame shows the setup slide. What the transcript says the other setup items cover (heard, not seen): "terminal setup" gives shift+enter for newlines (no backslashes) [02:52]-[02:56]; "/theme" sets light, dark or daltonized themes [03:01]; "/install GitHub app" enables @-mentioning Claude on GitHub issues/PRs [03:07]-[03:18]; customizing allowed tools so you aren't prompted each time [03:21]-[03:30]; plus a macOS dictation tip (system settings > accessibility > dictation; press the dictation key twice) [03:32]-[03:48]. A notifications command may be on the slide but I can't confirm it.

3. **Keybindings (from transcript [18:53]-[20:34], heard).** The slide itself (am06_1209s.png, "Interlude: Keybindings", 8 numbered items) is too small/blurry to read, so the mapping to slide items is inferred; the list below is what the speaker said:
   - Shift+Tab: switch into auto-accept-edits mode (bash still needs approval; edits auto-accepted; can ask Claude to undo) [18:53]
   - # (pound sign) then text: have Claude remember something; written into CLAUDE.md [19:17]
   - ! (exclamation mark): bash mode; runs the command locally and puts command and output into context [19:30]
   - @: mention files and folders [19:51]
   - Esc: stop Claude at any time, safe, won't corrupt the session [19:53]
   - Esc twice: jump back in history [20:17]
   - `claude --resume` or `--continue`: resume a past session [20:20] (a CLI flag rather than a key)
   - Ctrl+R: show full output, same as what Claude sees in context [20:28]
   That is 8 items, matching the 8 slots in the frame, but I could not read the slide text to confirm exact wording or order.

4. **Exact piped command: insufficient evidence.** No frame shows the SDK slide. Transcript [20:43]-[21:41]: `claude -p` is the CLI SDK; you pass a prompt, allowed tools (can include specific bash commands) and an output format (JSON or streaming JSON); "think of it as like a Unix utility". [21:48]-[21:55] mentions piping `git status` in and using `jq` to select the result. The prompt text and exact flag spelling were not stated aloud, so I can't reproduce the command.

5. **Onboarding went from about two or three weeks to about two or three days** for technical hires at Anthropic ([04:43]-[04:49], spoken by the speaker). Seen: nothing on a frame (am01_279s.png is a different slide, "Use Claude Code to answer questions about your codebase", whose small list items are unreadable).

6. **Exact MCP registration command: insufficient evidence.** Transcript [09:44]-[10:43]: two kinds of tools, bash and MCP. For a bash CLI the speaker gives a made-up "Burly CLI" ("this isn't a real thing"), "use the CLI to do something", and telling Claude to use `--help` to learn it, optionally saving it in CLAUDE.md [09:52]-[10:13]. For MCP: "add an MCP tool, tell it how to use it" [10:25]. The slide with the literal `claude mcp add ...` example and the two example prompts is not in any frame, and the speaker did not read them aloud. Seen in am05_1023s.png ("Share with your team" table): only the generic `claude mcp` and `.mcp.json` entries in the MCP servers row, not an add example. am03_651s.png ("Common workflows") shows prompts, but none for MCP/bash tool registration.

7. **Two reasons, stated by the speaker at [25:36]-[26:25] (heard):** (a) Anthropic staff use a wide range of IDEs (VS Code, Zed, Xcode, Vim, Emacs), so it was hard to build one thing for everyone; the terminal is the common denominator. (b) Models are improving fast, so there is a good chance people won't use IDEs by end of year; they wanted to avoid over-investing in UI layers that may soon not be useful. (Inferred nothing beyond this; the "by end of year" claim is the speaker's prediction.) The last frame (am08_1582s.png) shows the Q+A label and the speaker, consistent with this being in the Q&A.

8. **Where they live:** the transcript says slash commands are in ".claude/commands, and this can be in your home directory, or it can be checked into your project" [14:15]-[14:21]. The "Share with your team" slide (am05_1023s.png) shows, in the Slash commands row, `~/.claude/commands/` under Global (just me) and `.claude/commands/` under Project (shared) (read at low resolution; the paths are legible but not crisp). Inference: home-directory commands are user-global and project commands are shared via checkout.
   **How to invoke each (e.g. `/name`, `/project:name`, `/user:name`, or a namespaced form for nested subdirectories): insufficient evidence.** The speaker never states the invocation syntax and no frame shows it. Nested-subdirectory commands: nothing in the pack; the only nested-directory mention is for CLAUDE.md files [13:32], not slash commands.
