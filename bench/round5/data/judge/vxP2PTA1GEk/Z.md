# Answers — "I Code HTML & CSS Without Saying a Word… Like a Real Frontend Monk" (Код на костылях, 28:17)


## 1. Exact URL in the browser address bar
**Answer: insufficient evidence.**
Basis: metadata does not show the address bar. Inference only (not an answer): a silent HTML/CSS coding video typically uses a local dev server such as Live Server (`127.0.0.1:5500/index.html`) or opens the file directly, but the specific host, port and path cannot be determined from the title/channel/duration.

## 2. Value of the `lang` attribute on `<html>`
**Answer: insufficient evidence.**
Basis: not visible in metadata. Inference only: the channel name is Russian ("Код на костылях" = "Code on crutches"), so `lang="ru"` is plausible, but VS Code's default `!` Emmet boilerplate emits `lang="en"`, and the author could have used either. I cannot determine which.

## 3. `max-width` of the `@media` rule that hides `.header__nav`
**Answer: insufficient evidence.**
Basis: no stylesheet content is available in metadata. Common breakpoints (768px, 992px, 1024px) are guesses, not evidence.

## 4. DevTools-edited `.header__nav-btn span` rule — `width` and `background-color`
**Answer: insufficient evidence.**
Basis: requires seeing the DevTools Styles panel; nothing in metadata determines it.

## 5. Second `@media` block near the end — `max-width` and first selector
**Answer: insufficient evidence.**
Basis: requires the final frames of the video; nothing in metadata determines it.

## Summary
All five questions are visual questions about on-screen code and browser state. The only evidence permitted (title, channel, duration) does not determine any of them; the BEM-style class names in the questions (`.header__nav`, `.header__nav-btn`) are consistent with a Russian-language frontend tutorial, but that is confirmation of context, not an answer.
