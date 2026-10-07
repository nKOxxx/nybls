# Answers

Transcript read first: it carries talk-heavy content (Q5, Q7 and most of Q2/Q6 context), but all commands/slides are on screen only, so 8 stills + 1 zoom were spent.

1. `npm install -g @anthropic-ai/claude-code` (requires Node.js, spoken [00:55]). Slide "Follow along:" in frame f_44000_1568.png [00:44]. Speaker only says "type this" [00:39-00:46], so the command is from the frame.

2. `/config` = "Turn on notifications" (slide "Optimize your setup", f_180000_1568.png [03:00]). Others on the slide: `/allowed-tools` customize tool permissions; `/terminal-setup` enable shift+enter for newlines; `/install-github-app` tag @claude on your issues & PRs; `/theme` enable light/dark mode; plus "Turn on MacOS dictation" (not a slash command). Transcript [02:52-03:48] corroborates all except /config.

3. Keybindings slide (f_1155000_1568.png [19:15], explained in transcript [18:53-20:34]):
 1. Shift+tab: auto-accept edits (bash still needs approval)
 2. #: create a memory (goes into CLAUDE.md)
 3. !: enter bash mode (command and output go into context)
 4. @: add a file/folder to context
 5. Esc: cancel (safe, doesn't corrupt session)
 6. Double-Esc: jump back in history; `--resume` to resume (he also says `--continue`)
 7. ctrl+r: verbose output (full output as Claude sees it)
 8. /vibe: on the slide, never explained in the transcript; function not determinable from my evidence.

4. Slide "Claude Code SDK" [21:58] (f_1318000, zoom z_1318000_27_38_20.png): `git status | claude -p "What are my changes?" --output-format=json | jq '.result'` (multi-line with backslashes; output shown as "Your changes are:..."). Text is blurry; the `=` in `--output-format=json` and the exact prompt capitalization are read from a low-res zoom (moderate confidence). The earlier slide [21:40] (f_1300000) shows a different non-piped example: `claude -p "what did i do this week?" --allowedTools Bash(git log:*) --output-format json`. Speaker: "think of it as like a Unix utility" [21:38].

5. Onboarding for technical hires went from about two or three weeks to about two or three days [04:44-04:49] (transcript, speaker's claim).

6. Slide "Plug in your team's tools" (f_602000_1568.png [10:02]):
 - Register MCP server: `claude mcp add barley_server -- node myserver`
 - Bash CLI prompt: "Use the barley CLI to check for error logs in the last training run. Use -h to check how to use it."
 - MCP prompt: "Use the barley MCP server to check for error logs in the last training run"
 (Speaker calls the tool "Burly CLI", made up; slide spells barley. Tip to dump it into CLAUDE.md [10:09].)

7. Two reasons [25:43-26:25]: (a) Anthropic people use many IDEs (VS Code, Zed, Xcode, Vim, Emacs), hard to build for everyone, so terminal is the common denominator; (b) models improve fast, possibly IDEs obsolete by year end, so they avoid over-investing in UI layers.

8. Slide "Give Claude more context" (f_857000_1568.png [14:17]):
 - Home dir `~/.claude/commands/foo.md`: type `/user:foo`
 - Project `project-root/.claude/commands/foo.md`: type `/project:foo`
 - Nested `project-root/a/commands/foo.md`: type `/project:a:foo`
 (Slide also: `@a` for the directory, `@a/foo.py` for a file; a/CLAUDE.md pulled in on demand.)

## Evidence strip
- [00:42] f_42000: speaker only (no slide yet)
- [00:44] f_44000: "Follow along: npm install -g @anthropic-ai/claude-code"
- [03:00] f_180000: Optimize your setup slide
- [10:02] f_602000: Plug in your team's tools slide
- [14:17] f_857000: Give Claude more context slide (slash command paths)
- [19:15] f_1155000: Keybindings slide
- [21:40] f_1300000: SDK slide with claude -p example
- [21:58] f_1318000: SDK slide, pipe in/pipe out
- [21:58] z_1318000_27_38_20: zoom on piped command
Transcript sections cited inline.
