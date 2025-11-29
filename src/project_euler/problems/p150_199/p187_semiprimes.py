from bisect import bisect

from project_euler.lib import generate_primes_under


def main(n: int):
    primes = generate_primes_under(n, under_root=False)
    print("done primes")
    count = 0
    for i, prime in enumerate(primes):
        max_other_prime = n // prime
        if max_other_prime <= prime:
            break
        other_prime_index = bisect(primes, max_other_prime)
        count += other_prime_index - i
    print(count)


if __name__ == "__main__":
    main(10**8)
