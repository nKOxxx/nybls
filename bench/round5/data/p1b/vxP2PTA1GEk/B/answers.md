# Answers — vxP2PTA1GEk

Note: the video is silent (transcript is only "(upbeat music)") and the stored source is 360x640, so all answers come from frames; small text is at the limit of legibility. Confidence is stated per answer. Status: PARTIAL (Q1 port/path and Q5 digits not fully resolved at this resolution).

1. **Address bar URL.** Host is `127.0.0.1` (legible in zooms at [01:00], [23:50]). The remainder reads as `:5500/index.html` on the contact sheets throughout (e.g. [00:25]–[28:00]), i.e. `http://127.0.0.1:5500/index.html`, but the port and path digits/letters could not be resolved sharply at 360px source resolution — LOW confidence on port and path, HIGH on host.

2. **`lang` attribute on `<html>`:** `lang="ru"` — read in the editor's index.html at [04:00] (`<html lang="ru">`). HIGH confidence.

3. **First `@media` max-width (hiding `.header__nav`):** `1240px` — `@media (max-width: 1240px) { .header__nav { display: none; } }` in the editor at [23:50]; the same breakpoint is echoed in the DevTools Styles panel header at [19:35]. HIGH confidence.

4. **DevTools-edited `.header__nav-btn span` rule:** `width: 200px;` and `background-color: blue;` (the rule also shows `height: 4px; position: relative;` and is labelled `*style.css`, i.e. edited in DevTools, at [19:35] and [20:25]). HIGH confidence.

5. **Second `@media` block:** best reading is `@media (max-width: 1000px)` ([26:21], [27:00], [28:00]); the four-digit value is clearly four digits starting with 1 and ending in 0, and reads as 1000 rather than 1080/1200, but MEDIUM confidence on the middle digits at this resolution. The first selector inside it is `.about__inner` (with `padding: 60px 0; gap: 12px;`). HIGH confidence on the selector.

## Evidence strip
- [00:25–04:35] sheet_000: browser (127.0.0.1 URL, DevTools Elements/Styles) over VS Code; style.css with first @media visible; index.html opened ~03:45
- [05:25–09:35] sheet_001: editor adding .header__nav-btn / span rules; @media 1240px block visible
- [10:25–14:35] sheet_002: editing .header__nav-btn rule in editor
- [15:25–19:35] sheet_003: .header__nav-btn span rule in editor; DevTools Styles editing begins ~17:55–19:35
- [20:25–24:35] sheet_004: DevTools rule shown; responsive view toggled; page renders hero section at 24:35
- [25:16–28:00] sheet_005: second @media block added below the first; .about__inner rule written
- [01:00] zoom address bar: "127.0.0.1" legible, rest blurred
- [04:00] zoom editor: `<html lang="ru">`
- [02:55] zoom editor right pane: missed the line (empty area)
- [19:35] zoom DevTools Styles: @media (max-width: 1240px) .header__nav-btn span { width: 200px; height: 4px; background-color: blue; position: relative; } *style.css
- [20:25] zoom DevTools Styles: same rule, same values
- [28:00] zoom editor: @media (max-width: 1000px) { .about__inner { padding: 60px 0; gap: 12px; } }
- [23:50] zoom address bar: "127.0.0.1" only, rest blurred
- [23:50] zoom editor: @media (max-width: 1240px) { .header__nav { display: none; } }
- [28:00] zoom (tight) second @media digits: four digits, reads 1000px
- [26:21] zoom editor: @media (max-width: 1000px) { .about__inner { ... } } being typed
- [15:00] zoom address bar: unreadable
- [27:00] zoom address bar: unreadable
- [27:00] zoom (tight) second @media digits: unreadable at this crop

## Ledger
watched 28 min · examined 19 images (~28,288 visual tokens, ≈$0.06 at sonnet-5 input rate) of ~42,418 total frames · budget 19/114 units
