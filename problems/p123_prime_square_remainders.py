from pe_lib import generate_primes_under


def main(min_remainder=10_000_000_000):
    primes = generate_primes_under(1_000_000)
    n = 1
    while True:
        prime = primes[n - 1]
        remainder = 2 * prime * n % (prime * prime)
        if remainder > min_remainder:
            return n
        n += 2
