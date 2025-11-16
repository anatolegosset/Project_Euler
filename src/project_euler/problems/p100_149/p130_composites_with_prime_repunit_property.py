from src.project_euler.lib import generate_primes_under, fast_is_prime
import math


def _divisible_repunit(n):
    remainders = []
    remainder = 1
    flag = True
    while flag:
        remainders.append(remainder)
        remainder = (remainder * 10) % n
        if remainder == 1:
            flag = False
    remainder_sum = 0
    flag = True
    exponent = 0
    while flag:
        for remainder in remainders:
            remainder_sum = (remainder_sum + remainder) % n
            exponent += 1
            if remainder_sum == 0:
                flag = False
    return exponent


def main(max_n=15_000):
    primes = generate_primes_under(max_n, under_root=True)
    composites = []
    for n in range(2, max_n):
        if (
            not fast_is_prime(n, primes, True)
            and math.gcd(n, 10) == 1
            and (n - 1) % _divisible_repunit(n) == 0
        ):
            composites.append(n)
    print(composites, len(composites))
    if len(composites) > 24:
        return sum(composites[:25])
