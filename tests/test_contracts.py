"""A contract that accepts a malformed extraction is worse than no contract."""
from nybls_core import contracts as ct


def _teach(**over):
    item = {"name": "A", "plain": "a plain sentence", "at": 10}
    item.update(over)
    return {"shape": "teach", "concepts": [item]}


def test_valid_extraction_passes():
    assert ct.validate(_teach(), "teach") == []


def test_missing_required_field_is_caught():
    bad = {"shape": "teach", "concepts": [{"name": "A", "at": 10}]}
    assert any("plain" in e for e in ct.validate(bad, "teach"))


def test_missing_citation_is_caught():
    bad = {"shape": "teach", "concepts": [{"name": "A", "plain": "x"}]}
    assert any("'at'" in e for e in ct.validate(bad, "teach"))


def test_dangling_prerequisite_is_caught():
    """A prerequisite pointing at nothing makes the graph decorative."""
    errs = ct.validate(_teach(prerequisites=["Nonexistent"]), "teach")
    assert any("not a concept here" in e for e in errs)


def test_resolved_prerequisite_passes():
    obj = {"shape": "teach", "concepts": [
        {"name": "A", "plain": "x", "at": 1},
        {"name": "B", "plain": "y", "at": 2, "prerequisites": ["A"]},
    ]}
    assert ct.validate(obj, "teach") == []


def test_unexpected_field_is_caught():
    assert any("unexpected" in e for e in ct.validate(_teach(vibes="high"), "teach"))


def test_wrong_type_is_caught():
    assert any("expected number" in e for e in ct.validate(_teach(at="ten"), "teach"))


def test_dangling_contradiction_is_caught():
    bad = {"shape": "brief", "claims": [
        {"claim": "X is true", "at": 1, "contradicts": "something never claimed"}]}
    assert any("not a claim here" in e for e in ct.validate(bad, "brief"))


def test_every_shape_renders():
    for shape in ct.SHAPES:
        out = ct.render(shape, "any purpose")
        assert "required" in out and ct.SHAPES[shape]["root"] in out
