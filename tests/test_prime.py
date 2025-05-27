import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.prime import is_prime, primes_up_to


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(1)
    assert not is_prime(0)


def test_primes_up_to():
    assert primes_up_to(10) == [2, 3, 5, 7]
