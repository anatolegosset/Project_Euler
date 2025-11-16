import math
from src.project_euler.lib import generate_primes_under, prime_decomposition


def _corresponding_n(exponent_list, primes):
    result = 1
    for exponent, prime in zip(exponent_list, primes):
        result *= prime**exponent
    return result


def _nb_divisors(exponent_list):
    result = 1
    for exponent in exponent_list:
        result *= 2 * exponent + 1
    return result


def main(min_nb_sols=4_000_000):
    nb_divisors = (min_nb_sols - 1) * 2
    max_nb_primes = int(math.log(nb_divisors) / math.log(3)) + 1
    primes = generate_primes_under((max_nb_primes + 10) ** 2)[:max_nb_primes]
    initial_best_value = _corresponding_n([1] * max_nb_primes, primes)

    def _parcours(n, nb_divs, best_value, current_prime_index, max_exponent):
        if n >= best_value:
            return best_value
        prime = primes[current_prime_index]
        next_n = n
        exponent = 0
        best_n = best_value
        if prime == 2:
            print(1)
        while True:
            next_n *= prime
            exponent += 1
            if next_n >= best_n or exponent > max_exponent:
                break
            if nb_divs * (2 * exponent + 1) >= nb_divisors:
                best_n = next_n
                break
            best_n = min(
                best_n,
                _parcours(
                    next_n,
                    nb_divs * (2 * exponent + 1),
                    best_n,
                    current_prime_index + 1,
                    exponent,
                ),
            )
        return best_n

    print(prime_decomposition(9350130049860600, primes))
    return _parcours(1, 1, initial_best_value, 0, 1000)
