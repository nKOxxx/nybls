"""The benchmark headline must follow from the stored results, and the README must quote it."""
import importlib.util
from pathlib import Path


def test_benchmark_receipt_holds():
    path = Path(__file__).parent.parent / "scripts" / "check_receipt.py"
    spec = importlib.util.spec_from_file_location("check_receipt", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.check() == []
