import math

from project_euler.lib import generate_primes_under, fast_is_prime


def generate_heuristic(primes: list[int]):
    output: dict[int, list[int]] = {}
    offsets = [1, 3, 7, 9, 13, 27]
    for prime in primes:
        output[prime] = []
        for i in range(prime):
            flag = True
            square = i * i
            for offset in offsets:
                if (to_check := (square + offset)) % prime == 0 and to_check != prime:
                    flag = False
                    break
            if flag:
                output[prime].append(i)
    del output[2]
    del output[5]
    return output


def find_possible_solutions(max_prime: int, max_int: int):
    primes = generate_primes_under(max_prime)
    heuristic = generate_heuristic(primes)
    output = []
    modulus = math.prod(primes)
    for i in range(0, min(modulus, max_int), 10):
        if all(i % prime in possible for prime, possible in heuristic.items()):
            output.append(i)
    print(output[:10])
    return modulus, output


def main(n: int, prime_split: int = 18):
    primes = generate_primes_under(n + 20, under_root=False, min_prime=prime_split)
    print("done primes")
    modulus, possible = find_possible_solutions(prime_split, n)
    print("done possible")
    total = 0
    # for i in range(0, n, 10):
    #     if i % 3 == 0 or not (i % 7 == 3 or i % 7 == 4):
    #         continue
    #     to_check = i * i
    #     if (
    #         fast_is_prime(to_check + 1, primes)
    #         and fast_is_prime(to_check + 3, primes)
    #         and fast_is_prime(to_check + 7, primes)
    #         and fast_is_prime(to_check + 9, primes)
    #         and fast_is_prime(to_check + 13, primes)
    #         and fast_is_prime(to_check + 27, primes)
    #     ):
    #         print(i)
    #         total += i
    for i in range(0, n, modulus):
        for j in possible:
            if i + j > n:
                break
            to_check = (i + j) * (i + j)
            if (
                fast_is_prime(to_check + 1, primes)
                and fast_is_prime(to_check + 3, primes)
                and fast_is_prime(to_check + 7, primes)
                and fast_is_prime(to_check + 9, primes)
                and fast_is_prime(to_check + 13, primes)
                and fast_is_prime(to_check + 27, primes)
            ):
                print(i + j)
                total += i + j
    return total


def re_check():
    primes = generate_primes_under(150_000_000)
    print("done primes")
    for i in [
        10,
        315410,
        927070,
        2525870,
        8146100,
        16755190,
        39313460,
        97387280,
        119571820,
        121288430,
        130116970,
        139985660,
        144774340,
    ]:
        to_check = i * i
        if not (
            fast_is_prime(to_check + 1, primes)
            and fast_is_prime(to_check + 3, primes)
            and fast_is_prime(to_check + 7, primes)
            and fast_is_prime(to_check + 9, primes)
            and fast_is_prime(to_check + 13, primes)
            and fast_is_prime(to_check + 27, primes)
        ):
            print(i)


if __name__ == "__main__":
    print(
        sum(
            [
                10,
                315410,
                927070,
                2525870,
                8146100,
                16755190,
                39313460,
                97387280,
                119571820,
                121288430,
                130116970,
                139985660,
                144774340,
            ],
        ),
    )
    # re_check()
    # print(main
    # (150_000_000, prime_split=10000))
