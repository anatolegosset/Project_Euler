from project_euler.lib import generate_primes_under


def main(n: int, x: int, y: int) -> list[int]:
    primes = generate_primes_under(n, under_root=True)
    potentials = []
    for bitmask in range(1, 2 ** len(primes) + 1):
        number = 1
        totient = 1
        for prime in primes:
            if bitmask % 2 == 1:
                number *= prime
                totient *= prime - 1
            bitmask = bitmask // 2
        if totient * y < (number - 1) * x:
            potentials.append((number, totient))
    return sorted(potentials, key=lambda x: x[0])


def temp():
    print(15499 / 94744)
    for i in range(2, 10):
        print(36495360 * i / (223092870 * i - 1), i)


if __name__ == "__main__":
    temp()
    # print(main(100, 4, 10))
    # print(main(2_000, 15499, 94744))
