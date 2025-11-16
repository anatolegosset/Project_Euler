from src.project_euler.lib import nb_digits, generate_primes_under


def _min_multiple(prime1, prime2):
    k = nb_digits(prime1)
    factor = 10**k
    remainder = factor % prime2
    inverse = pow(remainder, -1, prime2)
    a = -prime1 * inverse % prime2
    return a * factor + prime1


def main(max_prime=1_000_000):
    primes = generate_primes_under(max_prime * 2)
    total = 0
    for i, prime1 in enumerate(primes[2:-1]):
        if prime1 > max_prime:
            break
        prime2 = primes[i + 3]
        multiple = _min_multiple(prime1, prime2)
        total += multiple
    return total
