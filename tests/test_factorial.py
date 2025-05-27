import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.factorial import factorial


def test_factorial_basic():
    assert [factorial(i) for i in range(6)] == [1, 1, 2, 6, 24, 120]


def test_factorial_negative():
    try:
        factorial(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative input"
