# Arm B (iterative, pinned fd11789), vxP2PTA1GEk, HTML and CSS session 28:17
Run 2026-09-07. Clean context, blind to ground truth. Ledger zeroed, frames archived first.
Declared no tool file modified. COST: 10 images, ~15,692 visual tokens (budget 10/114).
Verbatim answers follow; scoring is by the independent judge, not the experimenter.

1. 127.0.0.1:5500/index.html (host 127.0.0.1, port 5500, path /index.html). Seen:
   z_1041000_0_1_30 [17:21] shows the bold 127.0.0.1 followed by fainter :5500/index.html;
   the same string is visible in the address bar of every browser tile in sheet_000 [02:21
   to 25:55], sheet_001 and sheet_002. Caveat: the source video is 360x640 native, so the
   port and path digits are a low resolution read, consistent across about 18 tiles but not
   crisp in any one of them.

2. lang="ru". Seen: z_424000_0_53_50 [07:04], editor line <html lang="ru"> directly under
   the index.html > html > body breadcrumb. The same line is visible (unreadably small) in
   tiles at 11:46, 16:29, 21:12 in sheet_000. Not verified separately in the DevTools
   Elements panel; that is inferred to match, not seen.

3. max-width: 1240px. Seen: z_424000_50_70_50 [07:04] shows @media (max-width: 1240px) {
   .header__nav { display: none; } ... }; z_1611000_50_55_36 [26:51] shows the same block
   again. Also consistent in sheet tiles at 02:21, 24:18, 26:02 to 28:04. Caveat: digits at
   this resolution; "1240" is my best read across three independent images, "1200" is the
   alternative I cannot fully exclude.

4. width: 200px; background-color: blue (partial). Seen: z_1208000_44_41_30 [20:08],
   DevTools Styles panel, rule .header__nav-btn span { width: 2?0px; height: 4px;
   background-color: [blue swatch] blue; position: relative; } under a @media (max-width:
   12?0px) header, source style.css:75; z_1272000_48_38_52 [21:12] shows the same rule.
   Context: sheet_001 [18:45] shows a DevTools property autocomplete dropdown open
   confirming the edit is made in DevTools, and the editor's own version of the rule at
   [16:29]/[21:31] reads width: 100%; height: 4px; background-color: var(...), so the
   DevTools values differ from the file. Confidence: background-color: blue is solid (blue
   swatch plus a four letter word); the width is three characters before px, read as
   200px, but 240px cannot be excluded at 360p source resolution.

5. max-width: 1080px; first selector inside it: .about__inner. Seen: z_1611000_50_55_36
   [26:51], second block @media (max-width: 1080px) { .about__inner { padding: 40px 0;
   ... directly below the first @media; the editor breadcrumb in the same image reads
   @media (max-width: 1080px). Block first appears between the 26:02 and 26:26 tiles of
   sheet_002 and stays through 28:04. .about__inner is a clear read; 1080 is a consistent
   read across four images with the same low res caveat as Q3.

METHOD NOTE FROM THE ARM: transcript was 100% "(upbeat music)", zero speech, so the whole
budget went to frames. Sheet 0 located everything; rounds 2 and 3 were zooms. The
remaining ambiguity is not fixable by spending more: the stored video is 360x640, so every
zoom is an upscale of the same few pixels. Stopped at 10 images.

TOOL ANNOYANCE REPORTED, NOT FIXED: zoom --box at y=0.0 to 0.035 clipped the address bar
row (needs about 0.015 to 0.045); no error, just one wasted unit.
