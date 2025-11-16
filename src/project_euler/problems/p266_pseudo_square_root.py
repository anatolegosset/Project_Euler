from bisect import bisect_left
from math import log

from project_euler.lib import generate_primes_under


def compute_subset_weights(weights: list[float]):
    result = []
    for i in range(2 ** len(weights)):
        w_sum = 0
        for weight in weights:
            i, rem = divmod(i, 2)
            if rem:
                w_sum += weight
        result.append(w_sum)
    return result


def find_psr(primes: list[int], modulus: int = 10**16):
    all_weights = [log(prime) for prime in primes]
    total_weight = sum(all_weights)
    limit = total_weight / 2
    half_length = len(primes) // 2
    first_half = all_weights[:half_length]
    second_half = all_weights[half_length:]
    first_weights = compute_subset_weights(first_half)
    second_weights = compute_subset_weights(second_half)
    second_weights = sorted(enumerate(second_weights), key=lambda x: x[1])
    max_sum = 0
    max_pair = (0, 0)
    for i, weight in enumerate(first_weights):
        k = bisect_left(second_weights, limit - weight, key=lambda x: x[1])
        j, other_weight = second_weights[k - 1]
        if max_sum < weight + other_weight:
            max_sum = weight + other_weight
            max_pair = (i, j)
    bitmask = max_pair[0] + max_pair[1] * (2**half_length)
    result = 1
    for prime in primes:
        bitmask, rem = divmod(bitmask, 2)
        if rem:
            result = (result * prime) % modulus
    return result


def main():
    primes = generate_primes_under(190, under_root=False)
    # primes = [2, 3, 11, 47]
    print(find_psr(primes))


if __name__ == "__main__":
    main()
