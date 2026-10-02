# Verdict, vxP2PTA1GEk, "I Code HTML & CSS Without Saying a Word" (28:17)

Scored against ground_truth.md as written. Arms W, X, Y, Z. Scale: 2 correct, 1 partial, 0 wrong/abstained, -1 fabricated.

| Q | Label | W | X | Y | Z | Rationale |
|---|---|---|---|---|---|---|
| 1 Address bar URL | P | 0 abstained | 2 correct | 2 correct | 0 abstained | GT `127.0.0.1:5500/index.html`. X and Y give it exactly, with honest resolution caveats on the port digits. W and Z say insufficient evidence; both mention the Live Server URL as an explicitly disclaimed generic guess, not an answer, so abstained, not partial. |
| 2 `lang` attribute | P | 0 abstained | 2 correct | 2 correct | 0 abstained | GT `ru`. X and Y read `lang="ru"` in the editor (Y: DevTools match inferred, labelled). W and Z abstain; Z notes `ru` as plausible from the Russian channel name but refuses to assert it. |
| 3 `max-width` hiding `.header__nav` | P | 0 abstained | 2 correct | 2 correct | 0 abstained | GT `1240px`. X and Y both read 1240px; Y names 1200 as an unexcluded alternative but commits to 1240, which is correct with a caveat. |
| 4 DevTools `.header__nav-btn span` width and background-color | T | 0 abstained | 2 correct | 2 correct | 0 abstained | GT `width: 200px`, `background-color: blue` from the DevTools panel. X and Y both give exactly that, both note the editor file differs (100%, hex/var), both caveat the first width digit. Y self-labels "partial" but its stated values are complete and correct, so 2. |
| 5 Second `@media` block | T | 0 abstained | 2 correct | 2 correct | 0 abstained | GT `1080px`, first selector `.about__inner`. X and Y both give both parts with matching padding/gap detail. |

## Totals

| Arm | Total /10 | Outcomes |
|---|---|---|
| W | 0 | 5 abstained, 0 wrong, 0 fabricated |
| X | 10 | 5 correct |
| Y | 10 | 5 correct |
| Z | 0 | 5 abstained, 0 wrong, 0 fabricated |

## Extra claims (noted, not scored)

- X: editor rule reads `background-color: #3772FF`. GT has `#37..FF` (middle digits unreadable at grid resolution); consistent, not verifiable from GT.
- Y: editor rule reads `background-color: var(...)`. GT says the editor value is a hex colour `#37..FF`. Disagrees with GT and with X; not asked, so not scored, but it is a likely misread by Y.
- Y: DevTools source link `style.css:75`. GT says `style.css?_...:933`. Disagrees with GT; not asked, not scored.
- Y: Q4 rule shows `position: relative;` at 20:08; GT says that line is added from ~1145 s, consistent.
- Y: native video resolution 360x640. Not in GT, unverifiable here.
- Z: channel name "Код на костылях" and its translation. Not in GT, unverifiable here.
- X: inference (labelled) that the server is VS Code Live Server; GT agrees in its answer note.
- W and Z both correctly state the transcript is music tags only, matching GT's transcript verdict.

## Ground truth concerns

- None affecting scores. Both frame-reading arms agree with GT on all five answers.
- Minor: Y's `style.css:75` and `var(...)` readings conflict with GT's `:933` and `#37..FF`. GT is explicit and sourced from the DevTools/editor at specific frames, so GT is presumed right; if a frame check ever showed otherwise it would not change any score since neither item was asked.
- The appended errata section concerns other videos (QtqYNyBv9r8, Wlu4MsBnjuk) and does not apply here.
