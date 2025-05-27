"""Simple factorial utilities."""

import argparse


def factorial(n: int) -> int:
    """Return the factorial of n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Factorial calculator")
    parser.add_argument("n", type=int, help="Compute n factorial")
    args = parser.parse_args(argv)
    print(factorial(args.n))


if __name__ == "__main__":
    main()
