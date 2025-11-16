from src.project_euler.lib import totient, generate_primes_under


def main(max_n=1_000_000):
    primes = generate_primes_under(max_n, under_root=True)
    total = 0
    for i in range(2, max_n + 1):
        total = total + totient(i, primes)

    return total
