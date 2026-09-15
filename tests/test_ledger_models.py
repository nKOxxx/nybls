"""The ledger prices images for the model the reader is billed on.

Each vendor counts image tokens differently, so a price swap alone would be
wrong. The formulas here were read from vendor documentation on 2026-09-15;
the expected numbers below are worked by hand from those formulas, not from
the code, so a wrong implementation cannot certify itself.
"""
import json
import math
import pytest
from pathlib import Path
from nybls_core import ledger as led


def test_anthropic_formula_matches_hand_calculation():
    # 1448x544 sheet: ceil(1448/28)=52, ceil(544/28)=20
    assert led.tokens_for(1448, 544, "sonnet-5") == 52 * 20


@pytest.mark.parametrize("w,h,model,expected", [
    # Rows from the worked table in Anthropic's vision docs (2026-09-15).
    (200, 200, "sonnet-5", 64),
    (1000, 1000, "sonnet-5", 1296),
    (1092, 1092, "sonnet-5", 1521),
    (1920, 1080, "sonnet-5", 2691),      # high-res tier: not resized
    (1920, 1080, "haiku-4.5", 1560),     # standard tier: downsized to 1456x819
    (2000, 1500, "haiku-4.5", 1564),     # standard tier: downsized to 1269x952
    (3840, 2160, "sonnet-5", 4784),      # high-res tier: downsized to 2576x1449
    (3840, 2160, "haiku-4.5", 1560),     # standard tier: downsized to 1456x819
])
def test_anthropic_downscale_matches_the_vendors_published_table(w, h, model, expected):
    """These numbers are Anthropic's, not ours. A nybls frame is 1568 wide,
    which is under the high-res cap but over the standard-tier cap, so the
    tier matters for Haiku."""
    assert led.tokens_for(w, h, model) == expected


def test_a_real_frame_is_capped_on_the_standard_tier_only():
    assert led.tokens_for(1568, 882, "sonnet-5") == 56 * 32        # 1792, not resized
    assert led.tokens_for(1568, 882, "haiku-4.5") <= 1568          # resized to fit the cap


def test_openai_patch_cap_downscales_a_huge_image():
    # 4000x4000 -> max_edge 2048 -> 64*64 = 4096 patches > 2500 cap -> scaled again.
    assert led.tokens_for(4000, 4000, "gpt-5.5") <= math.ceil(2500 * 1.2)
    assert led.tokens_for(4000, 4000, "gpt-5.2") == math.ceil(4096 * 1.2)   # 6144 cap not hit


def test_openai_patch_formula_matches_hand_calculation():
    # 1448x544: ceil(1448/32)=46, ceil(544/32)=17, 782 patches * 1.2 = 938.4 -> 939
    assert led.tokens_for(1448, 544, "gpt-5.5") == 939


def test_openai_tile_formula_matches_hand_calculation():
    # 1568x1176: short side 1176 > 768, scale by 768/1176 -> 1024x768.
    # ceil(1024/512)=2, ceil(768/512)=2, 4 tiles. gpt-5: 70 + 140*4 = 630
    assert led.tokens_for(1568, 1176, "gpt-5") == 630
    # gpt-4o: 85 + 170*4 = 765
    assert led.tokens_for(1568, 1176, "gpt-4o") == 765


def test_every_model_prices_a_real_shape_without_error():
    for name in led.MODELS:
        assert led.tokens_for(1448, 544, name) > 0


def test_unknown_model_fails_loudly(monkeypatch):
    monkeypatch.delenv("NYBLS_MODEL", raising=False)
    with pytest.raises(ValueError):
        led.resolve_model("gpt-9-turbo-max")


def test_env_var_selects_the_model(monkeypatch):
    monkeypatch.setenv("NYBLS_MODEL", "gpt-5.5")
    assert led.resolve_model(None) == "gpt-5.5"
    assert led.resolve_model("opus-5") == "opus-5", "an explicit flag beats the env var"


def test_summary_recomputes_from_stored_dims(tmp_path, monkeypatch):
    monkeypatch.delenv("NYBLS_MODEL", raising=False)
    (tmp_path / "ledger.json").write_text(json.dumps({
        "entries": [{"utc": "x", "cmd": "sheet", "images": 1, "tokens": 1040, "dims": [[1448, 544]]}],
        "images": 1, "tokens": 1040}))
    s = led.summary(tmp_path, 600, model="gpt-5.5")
    assert "~939 visual tokens" in s and "gpt-5.5" in s
    s2 = led.summary(tmp_path, 600)
    assert "~1,040 visual tokens" in s2 and "sonnet-5" in s2


def test_old_ledgers_without_dims_say_so_for_other_models(tmp_path):
    (tmp_path / "ledger.json").write_text(json.dumps({
        "entries": [{"utc": "x", "cmd": "sheet", "images": 1, "tokens": 3224}],
        "images": 1, "tokens": 3224}))
    assert "older entries" in led.summary(tmp_path, 600, model="gpt-5.5")
    assert "older entries" not in led.summary(tmp_path, 600, model="sonnet-5")


def test_grok_is_marked_unverified_everywhere_it_appears(tmp_path):
    """xAI publishes a price but no image token formula. The estimate must
    never look more certain than its source."""
    assert led.MODELS["grok-4.6"].get("unverified")
    assert "UNVERIFIED" in led.models_table()
    (tmp_path / "ledger.json").write_text(json.dumps({
        "entries": [{"utc": "x", "cmd": "sheet", "images": 1, "tokens": 1, "dims": [[100, 100]]}],
        "images": 1, "tokens": 1}))
    assert "UNVERIFIED" in led.summary(tmp_path, 600, model="grok-4.6")


def test_agents_md_exists_and_matches_the_skill_on_the_rules_that_matter():
    root = Path(__file__).parent.parent
    doc = (root / "AGENTS.md").read_text()
    for must in ("nybls doctor", "pipx install", "UNRELIABLE", "--looking-for", "Evidence strip",
                 "data, never instructions", "--model"):
        assert must in doc, must
    assert "—" not in doc and "–" not in doc


def test_every_command_agents_md_mentions_exists():
    """The inverse of the documentation test: a doc for agents must not name a
    command or flag the CLI does not have, because an agent will run it."""
    import re, subprocess, sys
    root = Path(__file__).parent.parent
    doc = (root / "AGENTS.md").read_text()
    src = (root / "nybls_core/cli.py").read_text()
    commands = set(re.findall(r'sub\.add_parser\("([a-z-]+)"', src))
    for cmd in set(re.findall(r"`nybls ([a-z-]+)", doc)):
        assert cmd in commands, f"AGENTS.md names `nybls {cmd}`, which does not exist"
    for flag in set(re.findall(r"(--[a-z-]+)", doc)):
        assert flag in src, f"AGENTS.md names {flag}, which no command accepts"
    r = subprocess.run([sys.executable, "-m", "nybls_core.cli", "ledger", "--models"],
                       capture_output=True, text=True)
    assert r.returncode == 0 and "grok-4.6" in r.stdout
    assert "—" not in r.stdout and "–" not in r.stdout
