"""Whisper never fails loudly. Fed silence it returns a stock politeness; fed a
language its model cannot handle it loops. Both are reported as success, so both
have to be caught here or they reach the user as fact."""
from nybls_core import transcribe as tr

WORDS = ("pipeline latency cluster deploy schema rollback index cache queue worker "
         "shard replica backup restore migrate throttle retry timeout socket buffer "
         "kernel packet router tunnel session token cursor commit branch rebase").split()

def _segs(lines, step=3.0):
    return [(i * step, t) for i, t in enumerate(lines)]


def test_stock_politeness_on_silence_is_caught():
    for filler in ["Thank you.", "We'll see you next time.", "We'll be right back.",
                   "¡Suscríbete al canal!", "Thanks for watching"]:
        assert tr.looks_degenerate(_segs([filler])), f"missed: {filler}"


def test_looping_output_is_caught():
    segs = _segs(["the same line over and over"] * 40)
    r = tr.looks_degenerate(segs)
    assert r and "looped" in r


def test_consecutive_repetition_is_caught():
    """Varied overall, but a long identical run still means the model stalled."""
    segs = _segs([f"line number {i}" for i in range(30)] + ["stuck here"] * 14)
    assert tr.looks_degenerate(segs)


def test_a_real_transcript_passes():
    # Real speech keeps introducing new words. A fixture that repeats one
    # sentence template has the vocabulary of a hallucination, and the guard
    # correctly says so, which is why this fixture uses a real word bank.
    segs = _segs([f"{WORDS[i % len(WORDS)]} {WORDS[(i * 7) % len(WORDS)]} happens around step number {i}" for i in range(60)])
    assert tr.looks_degenerate(segs) is None


def test_short_but_genuine_transcript_passes():
    """A brief clip with real speech must not be flagged just for being short."""
    segs = _segs(["so the first thing to understand about the compressor stage",
                  "is that it raises pressure before the air reaches the burner"])
    assert tr.looks_degenerate(segs) is None


def test_the_word_you_alone_is_caught():
    """Whisper's most common silence artefact is the bare word 'you'."""
    assert tr.looks_degenerate(_segs(["You"]))


def test_silent_video_guidance_is_inverted():
    """A silent video is the case where frames carry everything, so pointing the
    agent at the transcript is the wrong instruction. This was a real failure:
    a degenerate-transcript report was read as 'low-value video' and four reels
    full of architecture diagrams went unexamined."""
    import inspect
    from nybls_core import cli
    src = inspect.getsource(cli.cmd_probe)
    # Pin the property, not the line (TESTING.md rule 3): the unreliable-transcript
    # branch exists and comes before the default advice.
    assert '"UNRELIABLE" in tsource' in src
    # the misleading default must not be what a silent video receives
    i_guard = src.index('"UNRELIABLE" in tsource')
    i_default = src.index("Read the transcript first")
    assert i_default > i_guard, "silent-video branch must precede the default advice"


def _vocab(n: int) -> list[str]:
    """n distinct content words. Synthetic, because the guard counts vocabulary
    size and rate, not whether the words are real English."""
    syl = ("ka ro mi tel sen dor vin lac pem nuz gri fal ost jen wub tam".split())
    out = []
    for i in range(n):
        out.append(syl[i % 16] + syl[(i // 16) % 16] + syl[(i // 256) % 16])
    return list(dict.fromkeys(out))[:n]


def test_catches_fluent_hallucination_that_never_repeats():
    """The line-ratio check only catches repetition. A model hallucinating from
    audio it cannot hear produces varied text at a normal rate, so it scores a
    perfect 1.000 there and was reported healthy. A real 24-minute video did
    exactly this: 183 words per minute, 7.5 distinct content words per minute.

    Built to that profile: plenty of words, almost no vocabulary, and no two
    lines alike, so every earlier check passes it.
    """
    import random
    rng = random.Random(0)          # seeded, so the fixture is reproducible
    pool = _vocab(10)
    segs = [(float(i * 3), " ".join(rng.choice(pool) for _ in range(9)))
            for i in range(500)]
    lines = [t for _, t in segs]
    assert len(set(lines)) / len(lines) > 0.25, "must survive the line-ratio check"
    wpm, distinct = tr.word_rates(segs, 1500)
    assert wpm > 100 and distinct < 9
    problem = tr.looks_degenerate(segs)
    assert problem is not None and "distinct content words" in problem


def test_catches_silence_captioned_as_room_tone():
    """A 63-minute silent screen recording came back as hundreds of lines of
    keyboard noise. Real speech never runs this quiet: 7 words per minute
    against 49 for the sparsest genuine narration measured."""
    tones = [f"(keyboard clicking {w})" for w in _vocab(60)]
    segs = [(float(i * 15), tones[i % 60]) for i in range(226)]
    assert len(set(t for _, t in segs)) / len(segs) > 0.25
    problem = tr.looks_degenerate(segs)
    assert problem is not None and "words per minute" in problem


def test_sparse_but_real_narration_is_not_flagged():
    """The guard must not punish genuinely quiet content. A console teardown
    with long silent working stretches runs 63 words per minute at 11.2 distinct
    content words per minute, and a stream billed as coding without commentary
    runs 49. Both are real speech and both must pass. This fixture is built to
    the teardown's measured profile, which sits closest to the threshold."""
    pool = _vocab(230)
    segs = []
    for i in range(100):
        new = pool[i * 2:i * 2 + 2]
        segs.append((float(i * 12), " ".join(new) + " so we lift it clear and set it aside now"))
    wpm, distinct = tr.word_rates(segs, 1200)
    assert 45 < wpm < 80 and 9 < distinct < 15, (wpm, distinct)
    assert tr.looks_degenerate(segs) is None


def test_vtt_entities_are_unescaped():
    """YouTube auto-captions use "&gt;&gt;" as a speaker marker and VTT carries
    HTML entities generally. Left raw, 288 of 1,666 segments in one real
    67-minute transcript read as "&gt;&gt;" rather than ">>", which is noise in
    every quote and in anything the verifier matches against."""
    import tempfile
    from pathlib import Path
    vtt = ("WEBVTT\n\n00:00:01.000 --> 00:00:03.000\n"
           "&gt;&gt; Rock &amp; roll, it&#39;s 5 &lt; 6\n")
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "x.vtt"
        p.write_text(vtt)
        segs = tr.condense_vtt(p)
    assert segs, "should parse one segment"
    text = segs[0][1]
    assert text.startswith(">>"), text
    assert "&" not in text.replace("&", "", 0) or "&gt;" not in text
    assert "Rock & roll" in text and "5 < 6" in text


def test_no_audio_track_is_not_a_crash():
    """A video with no audio stream made probe crash, because audio extraction
    ran unconditionally. Screen recordings often have no audio track, which is
    the content this tool is best at. It must report no speech and carry on."""
    from unittest import mock
    from pathlib import Path
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        ws = Path(d)
        with mock.patch.object(tr, "has_audio", return_value=False), \
             mock.patch.object(tr, "whisper", side_effect=AssertionError("must not transcribe")):
            path, source = tr.build_transcript("x", ws, ws / "video.mp4")
    assert path is None and "no audio track" in source


def test_probe_sends_a_no_audio_video_straight_to_the_frames():
    """The silent-video guidance must fire for a missing audio track, not only
    for an unreliable transcript."""
    import inspect
    from nybls_core import cli
    assert '"no audio track" in tsource' in inspect.getsource(cli.cmd_probe)


def _event_stream(rng, total, pool_n=4200):
    """A healthy long-event transcript: varied speech from a large vocabulary,
    the shape of a multi-hour build stream. Eight sampled content words per
    line from a 4,200-word pool keeps both rate gates comfortably above the
    measured healthy floors (30 wpm, 9 distinct/min over a ~5.5 h span), so
    the loop checks under test are what decide the verdict."""
    pool = _vocab(pool_n)
    out = []
    for i in range(total):
        out.append((float(i * 15), " ".join(rng.sample(pool, 8)) +
                    " so that is where we are"))
    return out


def test_intermission_holding_card_is_not_a_model_stall():
    """A 6-hour event stream re-aired its 'we'll be right back' holding card
    every 30 seconds for the whole intermission: 160 consecutive identical
    lines, 2% of the transcript, with 4h22m of real speech around it. The old
    unconditional run check called that a loop and told the user to discard a
    healthy transcript. An isolated run inside an otherwise varied transcript
    is show content, not a stall."""
    import random
    rng = random.Random(7)
    segs = _event_stream(rng, 500)
    segs += [(7500.0 + i * 30, "and we're gonna be right back with you in a bit")
             for i in range(160)]
    segs += [(12500.0 + ts0, t) for ts0, t in _event_stream(rng, 500)]
    # precondition: the run exists and the rest of the transcript is varied
    lines = [t.strip().lower() for _, t in segs]
    worst = run = 1
    for a, b in zip(lines, lines[1:]):
        run = run + 1 if a == b else 1
        worst = max(worst, run)
    assert worst == 160 and worst / len(lines) < 0.15
    assert len(set(lines)) / len(lines) > 0.25
    assert tr.looks_degenerate(segs) is None


def test_full_file_loop_is_still_caught():
    """The share gate must not blunt the original catch: a transcript that is
    mostly one repeated line is a stall, as before."""
    segs = _segs(["the same line over and over"] * 160 +
                 [f"line number {i}" for i in range(30)])
    lines = [t.strip().lower() for _, t in segs]
    assert 160 / len(lines) >= 0.15
    problem = tr.looks_degenerate(segs)
    assert problem is not None and "looped" in problem


def test_mid_speech_phrase_loop_is_caught():
    """The stall can happen inside one line: mid-speech audio the model cannot
    resolve comes back with the same phrase stamped over and over. Measured on
    a 6-hour stream: one line in 6,481, invisible to every gate - whole-line
    comparisons never match, ratio and vocabulary stay healthy."""
    import random
    rng = random.Random(11)
    segs = _event_stream(rng, 500)
    bad = ("i work on the work you know we're going to have a lot of people "
           "you know we're going to have a lot of people "
           "you know we're going to have a lot of people")
    segs[250] = (segs[250][0], bad)
    problem = tr.looks_degenerate(segs)
    assert problem is not None and "mid-speech hallucination" in problem, problem


def test_natural_emphasis_is_not_mid_speech_hallucination():
    """Real speakers repeat for emphasis, but never three times verbatim in a
    row. Two repeats, and repeats broken up by other words, must pass."""
    import random
    rng = random.Random(13)
    segs = _event_stream(rng, 100)
    segs.append((float(100 * 15),
                 "it works, it works, and after the fix today the pipeline "
                 "runs clean end to end without any manual steps"))
    assert tr.looks_degenerate(segs) is None
