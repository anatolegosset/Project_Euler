from pe_lib import generate_primes_under, is_int_permutation_of
import math


def main(max_n=10_000_000):
    primes = generate_primes_under(max_n)
    root = int(math.ceil(math.sqrt(max_n)))
    current_min = 10
    best_n = 0
    for i, prime1 in enumerate(primes):
        if prime1 > root:
            break
        for prime2 in primes[i:]:
            if prime1 * prime2 > max_n:
                break
            if is_int_permutation_of(prime1 * prime2, (prime1 - 1) * (prime2 - 1)):
                if (prime1 * prime2) / ((prime1 - 1) * (prime2 - 1)) < current_min:
                    current_min = (prime1 * prime2) / ((prime1 - 1) * (prime2 - 1))
                    best_n = prime1 * prime2
                    print(best_n, (prime1 - 1) * (prime2 - 1), current_min)

    return best_n


