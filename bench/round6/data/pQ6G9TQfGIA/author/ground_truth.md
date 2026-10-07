# Ground truth (video pQ6G9TQfGIA: Boris, Claude Code tips talk)

## Q1 — label V
Answer: `npm install -g @anthropic-ai/claude-code` (needs Node.js).
Evidence: grid/g_00056s.png (slide "Follow along: npm install -g @anthropic-ai/claude-code"). Transcript [00:39]-[00:57] only says "type this" and "All you need is Node.js"; the command is never spoken.
Key terms: npm install -g, @anthropic-ai/claude-code.
Partial: "npm install" of the claude-code package without exact scope/-g; Node.js only.

## Q2 — label V
Answer: `/config` = "Turn on notifications". Other setup items on the slide: /allowed-tools (customize tool permissions), /install-github-app (tag @claude on your issues & PRs), /terminal-setup (enable shift+enter to insert newlines), /theme (enable light/dark mode), and "Turn on MacOS dictation".
Evidence: grid/g_00168s.png, g_00182s.png. Transcript [02:52]-[03:50] covers terminal setup, theme, install GitHub app, allowed tools, dictation, but never mentions /config or notifications.
Key terms: /config, notifications.
Partial: lists the other commands but misses /config notifications.

## Q3 — label B
Answer (slide, 8 items): 1 Shift+tab to auto-accept edits; 2 # to create a memory; 3 ! to enter bash mode; 4 @ to add a file/folder to context; 5 Esc to cancel; 6 Double-esc to jump back in history, --resume to resume; 7 ctrl+r for verbose output; 8 /vibe (appears only on slide).
Speech: shift+tab = auto accept edits mode (bash still needs approval) [18:54]-[19:02]; # remembers into CLAUDE.md [19:17]-[19:28]; ! bash mode, output goes into context [19:30]-[19:48]; @ mention files/folders [19:51]; escape stops safely [19:53]-[20:14]; esc twice jumps back in history [20:17]; --resume or --continue [20:21]-[20:24]; ctrl+R shows full output [20:28]-[20:34]. "/vibe" is not spoken.
Evidence: grid/g_01134s.png, g_01162s.png.
Key terms (V part): /vibe, "Double-esc", "--resume".
Partial: most of items 1-7 without /vibe or without behaviours.

## Q4 — label B
Answer: `git status | claude -p "what are my changes?" --output-format=json | jq '.result'`, output shown as "Your changes are:...".
Speech: claude -p, pass a prompt/allowed tools/format (JSON or streaming JSON), "get status and pipe this in, and use jq to select the result" [21:11]-[21:57]. The exact prompt text and --output-format=json are only on the slide.
Evidence: grid/g_01302s.png, g_01330s.png.
Key terms: what are my changes?, --output-format=json, jq '.result'.
Partial: git status piped to claude -p then jq without the prompt text/flag.

## Q5 — label S
Answer: onboarding went from about two or three weeks to about two or three days for technical hires.
Evidence: transcript [04:44]-[04:49] "onboarding used to take about two or three weeks for technical hires. It's now about two or three days."
Partial: "weeks to days" without figures.

## Q6 — label V
Answer: `claude mcp add barley_server -- node myserver`. Bash-tool prompt: "Use the barley CLI to check for error logs in the last training run. Use -h to check how to use it." MCP prompt: "Use the barley MCP server to check for error logs in the last training run".
Evidence: grid/g_00588s.png (slide "Plug in your team's tools"). Transcript [09:52]-[10:30] says "Burly CLI", "dash dash help" and "add an MCP tool"; it never states the command, the server name, or the prompts, and the slide shows "-h" not --help.
Key terms: claude mcp add, barley_server, node myserver, barley CLI, error logs, last training run, -h.
Partial: gets the command but not prompts, or vice versa.

## Q7 — label S
Answer: (1) Anthropic engineers use a broad range of IDEs (VS Code, Zed, Xcode, Vim, Emacs), so the terminal is the common denominator; (2) models are improving so fast that people may not use IDEs by end of year, so they avoid over-investing in UI layers.
Evidence: transcript [25:40]-[26:25].
Partial: one of the two reasons.

## Q8 — label V
Answer: Slide "Give Claude more context / Pull in context on demand": `~/.claude/commands/foo.md` -> type `/user:foo`; `project-root/.claude/commands/foo.md` -> type `/project:foo`; nested `a/commands/foo.md` -> `/project:a:foo`. (Also `@a` for the directory, `@a/foo.py` for a file; a/CLAUDE.md is pulled in on demand.)
Evidence: grid/g_00868s.png (grid/g_00840s.png wide shot). Transcript [14:15]-[14:21] only says ".claude/commands ... in your home directory, or checked into your project ... for slash commands"; never gives the invocation syntax.
Key terms: /user:foo, /project:foo, /project:a:foo.
Partial: /user: and /project: prefixes without the nested form.
