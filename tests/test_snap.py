"""Scene drift: a label reads "24:12", so the model asks for second 1452 — but
the tile was rendered at 1452.4. Measured across three videos, 21 of 24
one-second offsets landed in a visibly different shot."""
import json
from nybls_core import media


def _ws(tmp_path, tiles):
    (tmp_path / "tiles.json").write_text(json.dumps(tiles))
    return tmp_path


def test_snaps_to_the_tile_actually_rendered(tmp_path):
    ws = _ws(tmp_path, [255.035, 528.7])
    ts, snapped = media.snap_to_tile(ws, 256)
    assert snapped and ts == 255.035


def test_does_not_snap_beyond_tolerance(tmp_path):
    """A request into unsampled territory must be served as asked."""
    ws = _ws(tmp_path, [255.035])
    ts, snapped = media.snap_to_tile(ws, 900)
    assert not snapped and ts == 900


def test_no_tiles_means_no_snapping(tmp_path):
    """Before any sheet exists there is nothing to snap to — old behaviour."""
    ts, snapped = media.snap_to_tile(tmp_path, 256)
    assert not snapped and ts == 256


def test_exact_hit_is_not_reported_as_snapped(tmp_path):
    ws = _ws(tmp_path, [255.035])
    ts, snapped = media.snap_to_tile(ws, 255.035)
    assert not snapped and ts == 255.035


def test_picks_the_nearest_of_several(tmp_path):
    ws = _ws(tmp_path, [100.0, 103.0, 260.0])
    ts, _ = media.snap_to_tile(ws, 102.2)
    assert ts == 103.0


def test_tiles_accumulate_without_duplicates(tmp_path):
    (tmp_path / "frames").mkdir()
    media.remember_tiles(tmp_path, [10.5, 20.25])
    media.remember_tiles(tmp_path, [20.25, 30.0])
    assert json.loads((tmp_path / "tiles.json").read_text()) == [10.5, 20.25, 30.0]
