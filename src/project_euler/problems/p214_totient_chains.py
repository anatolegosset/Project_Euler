from project_euler.lib import (
    compute_totient_under,
    generate_primes_under,
    fast_is_prime,
)


def find_totient_chain_length(k: int, totients: list[int]):
    """
    For an integer k > 0 with k < len(totients), and if totients is a list of integers
    such that totients[i] is the totient of i for all 1 <= i < len(totients), returns
    the length of the iterated totient chain until 1.
    """
    length = 0
    while k != 1:
        length += 1
        k = totients[k]
    length += 1
    return length


def main(n: int, chain_length: int):
    totients = compute_totient_under(n)
    primes = generate_primes_under(n + 50000, under_root=True)
    total = 0
    for i in range(2, n):
        if (
            fast_is_prime(i, primes)
            and find_totient_chain_length(i, totients) == chain_length
        ):
            total += i
    return total


if __name__ == "__main__":
    print(main(40_000_000, 25))
