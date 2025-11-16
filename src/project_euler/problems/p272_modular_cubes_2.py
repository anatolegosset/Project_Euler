import math
from collections.abc import Iterable

from project_euler.lib import (
    generate_primes_under,
    fast_prime_decomp_under,
)


def gen_subsets(primes: list[int], k: int, max_prod: int) -> Iterable[list[int]]:
    stack = []

    def _rec(choose_from: int, left_to_choose: int, max_prod_left: int):
        if left_to_choose == 0:
            yield stack
        else:
            for i, prime in enumerate(primes[choose_from:]):
                if prime**left_to_choose > max_prod_left:
                    break
                stack.append(prime)
                yield from _rec(
                    choose_from + i + 1,
                    left_to_choose - 1,
                    max_prod_left // prime,
                )
                stack.pop()

    yield from _rec(0, k, max_prod)


def main(n: int):
    # The first four "primes" p for which there is 3 solutions to x ** 3 % p == 1
    first_four_relevant_primes = [7, 9, 13, 19]
    max_relevant = n // math.prod(first_four_relevant_primes)
    primes = generate_primes_under(max_relevant, under_root=False)
    primes = [prime for prime in primes if prime % 3 == 1]
    primes.insert(1, 9)
    all_relevant_primes = set(primes)
    decomps = fast_prime_decomp_under(math.prod(primes[:5]))
    total = 0
    for subset in gen_subsets(primes, 5, n):
        subtotal = 0
        print(subset)
        for k in range(1, (n // math.prod(subset)) + 1):
            if all(
                (p not in all_relevant_primes or p in subset)
                and (p != 3 or decomps[k][p] < 2 or 9 in subset)
                for p in decomps[k]
            ):
                subtotal += k
        total += subtotal * math.prod(subset)
    print(total)


if __name__ == "__main__":
    main(10**11)
    # 3723246992826625523
