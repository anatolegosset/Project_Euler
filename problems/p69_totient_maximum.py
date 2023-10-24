from pe_lib import totient, generate_primes_under


def main(max_n=1_000_000):
    primes = generate_primes_under(max_n + 1)
    current_max = 0
    best_n = 0
    for n in range(1, max_n + 1):
        a = n / totient(n, primes)
        if a > current_max:
            print(n, current_max)
            current_max = a
            best_n = n
    return best_n, current_max

