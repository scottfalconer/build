import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.gcd import gcd


def test_gcd_basic():
    assert gcd(6, 9) == 3
    assert gcd(10, 5) == 5
    assert gcd(13, 7) == 1


def test_gcd_negative():
    assert gcd(-4, 6) == 2
    assert gcd(5, -15) == 5
