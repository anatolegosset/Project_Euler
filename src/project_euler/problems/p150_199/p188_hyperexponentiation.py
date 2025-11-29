from project_euler.lib import generate_primes_under, compute_totient


def tetration_mod(a: int, b: int, modulus: int, primes: list[int]):
    if b == 1:
        return a
    if modulus == 1:
        return 0
    exponent = tetration_mod(a, b - 1, compute_totient(modulus, primes), primes)
    return pow(a, exponent, modulus)


def main():
    primes = generate_primes_under(10**8, under_root=True)
    print(tetration_mod(1777, 1855, 10**8, primes))


if __name__ == "__main__":
    main()
