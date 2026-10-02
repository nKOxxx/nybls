# Ground truth — jtl4KKRIheo (iFixit, iPhone 11 screen replacement)

Grid frames are sampled at 5 s, 15 s, 25 s ... 395 s (g_00005s.png ... g_00395s.png). Video ends ~6:37.

## Q1 — Tools needed
- Label: **S**
- Answer: iOpener; iFixit opening picks; suction handle or iSclack; spudger; tweezers; and screwdriver bits: P2 pentalobe, Y000 tri-point, Phillips.
- Evidence: transcript [00:13]–[00:26] ("you'll need an eye opener a set of ifixit opening picks a suction handle or ice clack a spudger tweezers and the following screwdriver bits a p tube pentalobe bit a y triple zero bit and a phillips"). The ASR garbles "iOpener"/"iSclack"/"P2"; the on-screen list in g_00015s.png and g_00025s.png gives the clean spellings: iOpener, iFixit Opening Picks, Suction Handle, iSclack, Spudger, Tweezers, P2 Pentalobe, Tri-point Y000. Note the on-screen list omits Phillips, which is only spoken (and confirmed at [03:32]).
- Partial: missing one or two items (e.g. Phillips, or iOpener), or wrong bit sizes (P2 / Y000) counts as partial.

## Q2 — Battery before starting
- Label: **S**
- Answer: Discharge the battery to below 25%. A charged lithium-ion battery can catch fire and/or explode if accidentally damaged during the repair.
- Evidence: transcript [00:39]–[00:46] ("discharge your battery to below 25 ... a charged lithium-ion battery can catch fire and or explode if you accidentally damage it"). Visual corroboration: g_00045s.png shows Control Center with the battery at 24%.
- Partial: "discharge the battery" without the 25% figure, or threshold without the fire/explosion reason.

## Q3 — iOpener heating times
- Label: **S**
- Answer: Bottom edge: about one minute. Top front of the display (to soften the sensor adhesive): about one to two minutes.
- Evidence: transcript [00:56]–[01:01] ("place a heated eye opener on the bottom edge of the phone and leave it there for about a minute"); [03:46]–[03:51] ("heat up the top front of the display for about one to two minutes so that we can soften the adhesive holding down the sensors"). g_00055s.png shows the iOpener being brought to the phone.
- Partial: only one of the two durations.

## Q4 — Bracket screw counts and bit
- Label: **S**
- Answer: Battery connector bracket: 3 screws. Logic board cover bracket: 5 screws. Both use the Y000 (tri-point) bit.
- Evidence: transcript [02:42]–[02:45] ("you'll need your y triple zero bit to remove the three screws securing the battery connector in place"); [03:02]–[03:05] ("grab your y triple zero again and remove the five screws from the logic board cover bracket"). Visual: g_00185s.png shows the five screws circled on the logic board cover; g_00175s.png shows the small battery-connector bracket being lifted with tweezers.
- Partial: correct counts with wrong/unspecified bit, or one count wrong.

## Q5 — Cracked screen, suction cup won't stick
- Label: **B**
- Answer: Spoken: cover the display with a piece of clear packing tape so the suction cup can grip. On screen (the ifixit.com guide pages shown): tape over the cracks with overlapping strips of packing tape (Step 2, "Tape over any cracks") and wear safety glasses; if broken glass still prevents the suction cup from sticking, fold a strong piece of tape (such as duct tape) into a handle and lift the display with that; alternatively use very sticky tape instead of the suction cup, or, if all else fails, superglue the suction cup to the broken screen. The video also says to follow the opening procedure on the ifixit.com guide if you only have a single suction handle rather than an iSclack.
- Evidence: transcript [01:02]–[01:17] ("if you have a cracked display suction cups might have a hard time attaching to the glass if you're having trouble getting them to stick cover the display with a piece of clear packing tape ... if you only have an ifixit suction handle follow the opening procedure on the guide at ifixit.com"). Frames: g_00065s.png (guide Step 2 "Tape over any cracks": overlapping strips of packing tape, safety glasses warning, duct-tape handle tip); g_00075s.png (guide text: clear packing tape, very sticky tape instead of suction cup, superglue the suction cup; Step 7 "Lift the display slightly").
- Key terms: packing tape; duct tape / tape handle; sticky tape; superglue; safety glasses; Step 2 "Tape over any cracks"; Step 7 "Lift the display slightly".
- Partial: packing tape alone (transcript only) is partial; full credit needs at least two of the on-screen-only workarounds (duct-tape handle, sticky tape, superglue).

## Q6 — Pick route and the clipped edge
- Label: **S**
- Answer: After the iSclack makes a small gap at the bottom, insert the pick at the bottom edge and slide it around the lower-left corner and up the left edge; insert again at the bottom and slide up the right side; the top edge is held by both adhesive and clips, so gently pull the right side of the display down slightly toward the Lightning port, insert the pick in the top-right corner and, while pulling down, slide it across the top edge. Then swing the display up from the left side like the back cover of a book (it is still attached by ribbon cables).
- Evidence: transcript [01:39]–[01:48] (insert pick in gap, lower left corner, up left edge); [01:59]–[02:06] (bottom edge again, up the right side); [02:06]–[02:20] ("the top edge of the display is held on with both adhesive and clips so gently pull the right side of the display down slightly towards the lightning port and insert your pick in the top right corner while gently pulling down slide the pick across the top edge"); [02:25]–[02:34] (swing up from the left side). Frames: g_00105s.png (pick inserted at the gap by the iSclack), g_00115s.png (pick on left edge), g_00125s.png (pick on right edge), g_00135s.png (pick at top edge), g_00145s.png/g_00155s.png (display swung open).
- Partial: correct sequence without the top-edge clips detail, or clips detail without the pull-toward-Lightning-port step.

## Q7 — Front sensor assembly screws and reinstall order
- Label: **S**
- Answer: Four screws: three Phillips and one Y000. Reinstall order on the new display: press the proximity sensor and flood illuminator into their slots; slide the ambient light sensor back into place with tweezers and place its bracket straight onto it; press the microphone back into place with a finger; press the flex cable below the microphone onto the display (spudger OK); flip the speaker assembly over and reinstall the four screws.
- Evidence: transcript [03:27]–[03:34] ("remove the front assembly begin by removing four screws three being phillips and one y triple zero"); [04:36]–[05:06] (reinstall sequence: proximity sensor and flood illuminator → ambient light sensor and bracket → microphone → flex cable → flip speaker assembly over and reinstall the four screws). Frames: g_00205s.png (screws being removed around the earpiece speaker), g_00215s.png (speaker assembly before flipping), g_00225s.png (speaker flipped down), g_00245s.png/g_00255s.png (tweezers on the ambient light sensor bracket), g_00285s.png (pressing components into the display).
- Partial: correct screw count/types but reinstall order missing or out of sequence, or vice versa.

## Q8 — Battery capacity and voltage
- Label: **V**
- Answer: 3110 mAh, 3.83 V (11.91 Wh). The label also reads APN 616-00644.
- Evidence: battery label readable in g_00165s.png ("3110mAh", "3.83V ⎓ 11.91Wh", "APN: 616-00644"), g_00185s.png, g_00195s.png and most clearly g_00355s.png. The transcript never states any battery figure (search: "3110", "mAh", "3.83", "11.91", "616-00644" — none present).
- Key terms: 3110 mAh; 3.83 V; 11.91 Wh; APN 616-00644; "Rechargeable Li-ion Battery".
- Partial: one of the two values (capacity or voltage) correct; "insufficient evidence" is acceptable from a transcript-only arm.
