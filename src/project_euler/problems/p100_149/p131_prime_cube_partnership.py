from src.project_euler.lib import generate_primes_under, fast_is_prime


def main(max_prime=1_000_000):
    primes = generate_primes_under(max_prime, under_root=True)
    nb_primes = 0
    i = 1
    while True:
        potential_prime = 3 * i * (i + 1) + 1
        if potential_prime > max_prime:
            break
        if fast_is_prime(3 * i * (i + 1) + 1, primes, ignore_low_primes=True):
            nb_primes += 1
        i += 1
    return nb_primes
