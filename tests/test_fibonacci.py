import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.fibonacci import fib


def test_first_few_values():
    assert [fib(i) for i in range(6)] == [0, 1, 1, 2, 3, 5]


def test_negative_input():
    try:
        fib(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative input"
