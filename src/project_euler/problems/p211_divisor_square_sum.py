import math

from project_euler.lib import compute_multiplicative_under


def is_square(k: int):
    return round(math.sqrt(k)) ** 2 == k


def so2_on_radicals(prime: int, exp: int):
    return (prime ** (2 * exp + 2) - 1) // (prime**2 - 1)


def main(n: int):
    all_so2_values = compute_multiplicative_under(n, so2_on_radicals)
    total = 0
    for i, value in enumerate(all_so2_values):
        if is_square(value):
            print(i, value)
            total += i
    return total


if __name__ == "__main__":
    # explore()
    print(main(64_000_000))
