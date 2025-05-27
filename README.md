# Build Anything Project

This repository showcases a simple example project. It contains Python scripts for computing Fibonacci numbers, factorials, prime numbers, and the greatest common divisor (GCD).

## Usage

Run the scripts with Python. Most scripts take a single integer argument `n`,
while `gcd.py` expects two integers.

```bash
python3 src/fibonacci.py 5        # prints the 5th Fibonacci number
python3 src/fibonacci.py 5 --list # prints 0 1 1 2 3 5
python3 src/factorial.py 5        # prints 120
python3 src/prime.py 10           # prints 2 3 5 7
python3 src/gcd.py 20 30          # prints 10
```

## Testing

Run the tests using `pytest`:

```bash
pytest
```
