from collections import Counter
from math import sqrt


def smallest_prime_factors(n: int):
    result = list(range(n + 1))
    for i in range(2, int(sqrt(n)) + 1):
        if result[i] == i:
            for j in range(i * i, n + 1, i):
                if result[j] == j:
                    result[j] = i
    return result


def factor(k, spf):
    result = Counter()
    while k > 1:
        p = spf[k]
        result[p] += 1
        k //= p
    return result


def find_square_divisors(factors: Counter, root: int):
    divisors = [1]
    for p, exp in factors.items():
        divisors = [
            new_div
            for x in divisors
            for i in range(2 * exp + 1)
            if (new_div := x * (p**i)) < root
        ]
    return divisors


def main(n: int):
    root = int(sqrt(n))
    spf = smallest_prime_factors(root + 1)
    relevant_squares = [i * i for i in range(1, root + 1)]
    squares_set = set(relevant_squares)
    relevant_squares = [(i + 1, square) for i, square in enumerate(relevant_squares)]
    total = 0
    print("starting")
    for j, square in relevant_squares:
        factors = factor(j, spf)
        divisors = find_square_divisors(factors, j)
        for divisor in divisors:
            quotient = square // divisor
            to_check = divisor + j * quotient
            if to_check in squares_set:
                total += to_check
                squares_set.remove(to_check)
            to_check = j + divisor * quotient
            if to_check in squares_set:
                total += to_check
                squares_set.remove(to_check)
    return total


if __name__ == "__main__":
    print(main(100_000))
