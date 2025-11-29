from project_euler.lib import generate_primes_under, bezout_solve


def find_multiplier(prime: int):
    multiple = prime if prime > 10 else prime * 7
    digit = multiple % 10
    rem = (multiple // 10) % prime
    for k in range(prime):
        if (k * digit) % prime == rem:
            return prime - k
    raise ValueError("????????")


def find_multiplier_2(prime: int):
    digit = prime % 10
    rem = (prime // 10) % prime
    x, y = bezout_solve(digit, prime)
    return prime - (x * rem) % prime


def main(n: int):
    primes = generate_primes_under(n, under_root=False)
    total = 6
    for prime in primes[4:]:
        if prime == 2 or prime == 5:
            continue
        total += find_multiplier_2(prime)
    print(total)


def wait():
    for k in range(100):
        print(((k * 113) // 10) % 113)


if __name__ == "__main__":
    wait()
    # main(10_000_000)
