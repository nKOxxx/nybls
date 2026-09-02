"""The verifier is the component that makes every other claim checkable,
so it is the one that most needs its own checks."""
import pytest
from nybls_core import verify as vf

SEGS = [
    (0.0, "welcome to the lesson"),
    (36.0, "first of all you fight for the center this is the small center"),
    (242.0, "it does not mean wow how cool you play chess it means what opponent wants"),
    (266.0, "and it is checks captures threats and active moves"),
    (376.0, "it is going to save you from 90% of the blunders you make"),
    (2833.0, "only care about three things kings activity pieces activity and passers"),
]


def test_supported_claim_verifies():
    v = vf.verify_claim(SEGS, "WOW means what opponent wants", 242)
    assert v.status == "verified" and v.coverage >= 0.55


def test_fabricated_claim_is_caught():
    """The control that matters: a plausible-sounding wrong claim must fail."""
    v = vf.verify_claim(SEGS, "the wow principle ranks candidate moves by quality", 242)
    assert v.status == "unsupported"
    assert "rank" in v.missing or "candidate" in v.missing


def test_stemming_prevents_false_negative():
    """ASR says 'ask'/'save'; a written claim says 'asking'/'saves'. Same fact."""
    v = vf.verify_claim(SEGS, "asking saves you from blunders", 376)
    assert v.status in ("verified", "weak")
    assert "save" in v.found


def test_numerals_normalise():
    v = vf.verify_claim(SEGS, "90 percent of blunders", 376)
    assert "percent" in v.found


def test_right_words_wrong_timestamp_fails():
    """Citation integrity means the timestamp must be right, not just the words."""
    v = vf.verify_claim(SEGS, "checks captures threats and active moves", 36)
    assert v.status != "verified"


def test_timestamp_past_end_is_out_of_range():
    assert vf.verify_claim(SEGS, "anything at all", 99999).status == "out-of-range"


def test_window_is_asymmetric_forward():
    """A term is often named before it is explained, so the window leans forward."""
    assert vf.WINDOW_AFTER > vf.WINDOW_BEFORE


@pytest.mark.parametrize("line,expect", [("[04:02] hello there", 242.0), ("[00:36] x", 36.0)])
def test_transcript_parsing(tmp_path, line, expect):
    p = tmp_path / "t.txt"
    p.write_text(line)
    assert vf.load_transcript(p)[0][0] == expect
