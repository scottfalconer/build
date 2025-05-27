"""Simple Fibonacci utilities."""

from functools import lru_cache
import argparse


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Fibonacci calculator")
    parser.add_argument("n", type=int, help="Index of Fibonacci number to compute")
    parser.add_argument(
        "--list", action="store_true", help="List numbers up to n instead of just printing the n-th value"
    )
    args = parser.parse_args(argv)

    if args.list:
        seq = [fib(i) for i in range(args.n + 1)]
        print(" ".join(str(num) for num in seq))
    else:
        print(fib(args.n))


if __name__ == "__main__":
    main()
