"""Prime number utilities."""

import argparse


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_up_to(n: int):
    """Generate all prime numbers up to n inclusive."""
    return [i for i in range(2, n + 1) if is_prime(i)]


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Prime number utilities")
    parser.add_argument("n", type=int, help="Generate primes up to n")
    args = parser.parse_args(argv)
    print(" ".join(str(p) for p in primes_up_to(args.n)))


if __name__ == "__main__":
    main()
