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
    assert 'if "UNRELIABLE" in tsource:' in src
    # the misleading default must not be what a silent video receives
    i_guard = src.index('if "UNRELIABLE" in tsource:')
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
