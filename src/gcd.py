"""Greatest common divisor utilities."""

import argparse


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b."""
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Greatest common divisor calculator")
    parser.add_argument("a", type=int, help="First integer")
    parser.add_argument("b", type=int, help="Second integer")
    args = parser.parse_args(argv)
    print(gcd(args.a, args.b))


if __name__ == "__main__":
    main()
