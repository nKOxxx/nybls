1. Insufficient evidence for the exact command. [00:21-00:55] Speaker says "open your laptop and type this... this will help you install QuadCode" and "All you need is Node.js" [00:55], but the command is on a slide and never spoken. Inference/own knowledge (not from transcript): `npm install -g @anthropic-ai/claude-code`, which fits the Node.js remark but is unconfirmed here.

2. Only partly determinable. Transcript [02:50-03:50] lists setup commands: "run terminal setup" (gives shift-enter for newlines, no backslashes) [02:52]; "/theme" for light/dark/daltonize [03:01]; "/install GitHub app" to @-mention Claude on issues/PRs [03:07]; customize allowed tools so you aren't prompted each time [03:21]; macOS dictation (system settings > accessibility) to speak prompts [03:36]. No command for notifications is mentioned in the transcript; insufficient evidence for which one turns on notifications (the slide may show it). Inference only: likely the terminal-setup/config-type command, unconfirmed.

3. Keybindings [18:53-20:34]:
- Shift+Tab: switch to auto-accept edits mode; bash still needs approval; edits auto-accepted, can ask Claude to undo [18:54-19:04].
- # (pound sign): tell Claude something to remember; it's added to CLAUDE.md, and you can pick which memory file [19:17-19:28; 17:44].
- ! (exclamation mark): bash mode, runs the command locally and puts command and output into context [19:30-19:48].
- @: mention files and folders [19:51].
- Escape: stop Claude at any time safely, without corrupting the session [19:53-20:01].
- Escape twice: jump back in history [20:17].
- claude --resume (or --continue): resume a previous session [20:21-20:24] (spoken "resume"/"dash dash continue").
- Ctrl+R: show the full output, same as what Claude sees in its context window [20:28-20:34].

4. Transcript [21:11-21:41] says: `claude -p` with a prompt, optional allowed tools (including specific bash commands), and an output format (JSON or streaming JSON); example of piping `git status` in and using `jq` to select the result [21:50-21:55]. The exact command, prompt text and flag value are on the slide and not spoken; insufficient evidence for exact text. Inference (own knowledge, unconfirmed): something like `git status | claude -p "..." --output-format json | jq ...` ; `--output-format` is the real flag name, and values json / stream-json.

5. Transcript [04:44-04:49]: onboarding for technical hires "used to take about two or three weeks. It's now about two or three days."

6. Transcript [09:52-10:30] covers the concepts: bash tool example (made-up "Burly CLI", tell Claude to use it and use --help to learn it; can be put in CLAUDE.md) and MCP tools (add one, tell Claude how to use it). The exact register command (e.g. `claude mcp add ...`) and the example prompts are on slides and not spoken; insufficient evidence for the exact text. Own knowledge, unconfirmed: the register command is `claude mcp add <name> ...`. Also [16:45] mentions an .mcp.json checked into the repo to share MCP servers.

7. Transcript [25:43-26:25]: two reasons. (1) Anthropic staff use a broad range of IDEs (VS Code, Zed, Xcode, Vim, Emacs), so it was hard to build something for everyone; terminal is "the common denominator." (2) The model is improving fast; he thinks "there's a good chance that by the end of the year people aren't using IDEs anymore," so they avoid over-investing in UI/layers on top.

8. Transcript [14:15-14:21] only says slash commands live in `.claude/commands` (spoken "dot quad slash commands"), either in your home directory or checked into the project; the invocation syntax (e.g. user-level vs project-level prefix, nested subdirectory naming) is not stated aloud, so presumably on the slide. Insufficient evidence for the exact invocation. Own knowledge (unconfirmed by transcript, may differ by version): project commands are invoked as /name, user-home commands appear as /name (shown labelled "user"), and nested subdirectories use a namespace like /subdir:name.
