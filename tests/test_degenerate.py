"""Whisper never fails loudly. Fed silence it returns a stock politeness; fed a
language its model cannot handle it loops. Both are reported as success, so both
have to be caught here or they reach the user as fact."""
from nybls_core import transcribe as tr


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
    segs = _segs([f"this is genuinely varied sentence number {i} with content" for i in range(60)])
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
