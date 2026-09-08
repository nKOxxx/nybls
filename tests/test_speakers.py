"""Shot clustering behind `nybls speakers`.

A recorded call in speaker view cuts to whoever is talking, so a shot change is
a turn boundary and the probes that find it cost no vision tokens. These tests
cover the clustering itself, which is pure and needs no ffmpeg.
"""
from nybls_core import media


def _h(bits: str) -> str:
    """A 64-bit hash from a 64-character bit string."""
    return f"{int(bits, 2):016x}"


A = _h("1010" * 16)
B = _h("0101" * 16)                      # maximally far from A
A_NUDGED = _h("1010" * 15 + "1011" * 1)  # A with a few bits moved, same shot


def test_two_distinct_shots_stay_apart():
    assign, order = media.cluster_hashes([A, B, A, B, A])
    assert assign == [0, 1, 0, 1, 0]
    assert order == [0, 1]


def test_small_movement_does_not_start_a_new_shot():
    """Someone shifting in their chair must not read as a scene change."""
    assert media.hamming(A, A_NUDGED) <= media.SHOT_MERGE
    assign, _ = media.cluster_hashes([A, A_NUDGED, A])
    assert len(set(assign)) == 1


def test_clusters_are_ranked_by_how_much_screen_time_they_hold():
    """Cluster 0 is always the most-seen shot, so callers can read a talk ratio
    off the top rows without sorting."""
    assign, order = media.cluster_hashes([B, A, A, A, B])
    assert assign.count(0) == 3 and assign[1] == 0
    assert order == [0, 1]


def test_single_static_shot_yields_one_cluster():
    """A screen share or a static camera has no turn signal at all, and the
    command reports that rather than inventing a dominant speaker."""
    assign, order = media.cluster_hashes([A] * 40)
    assert order == [0] and set(assign) == {0}


def test_empty_input_is_not_an_error():
    assert media.cluster_hashes([]) == ([], [])
