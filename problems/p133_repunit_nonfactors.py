from pe_lib import multiplicative_order, generate_primes_under


def main(max_prime=100):
    primes = generate_primes_under(max_prime)[3:]
    total = 3
    for prime in primes:
        order = multiplicative_order(10, prime)
        while order % 2 == 0:
            order = order // 2
        while order % 5 == 0:
            order = order // 5
        if order > 1:
            total += prime
        else:
            print(prime)
    return total
