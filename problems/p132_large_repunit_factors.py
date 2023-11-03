from pe_lib import generate_primes_under


def _repunit_modulus(repunit, n):
    if n % 2 == 0 or n % 5 == 0:
        return 1
    remainders = []
    remainder = 1
    flag = True
    while flag:
        remainders.append(remainder)
        remainder = (remainder * 10) % n
        if remainder == 1:
            flag = False
    q, r = repunit // len(remainders), repunit % len(remainders)
    return (sum(remainders) * q + sum(remainders[:r])) % n


def main(max_primes=200_000, repunit_size=1_000_000_000):
    primes = generate_primes_under(max_primes)
    total = 0
    nb_primes = 0
    for prime in primes:
        if _repunit_modulus(repunit_size, prime) == 0:
            print(prime)
            total += prime
            nb_primes += 1
            if nb_primes == 40:
                return total
    print(nb_primes)
    return -1
