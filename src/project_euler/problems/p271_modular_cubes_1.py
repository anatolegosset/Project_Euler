import math

from project_euler.lib import (
    generate_primes_under,
    cartesian_product,
    crt_solve_multi,
    crt_solve,
)


def main():
    primes = generate_primes_under(43, under_root=False)
    prime_sols: dict[int, list[int]] = {}
    for prime in primes:
        prime_sols[prime] = [1]
        for i in range(2, prime):
            if (i * i * i % prime) == 1:
                prime_sols[prime].append(i)
    only_one_is_sol = [prime for prime, sols in prime_sols.items() if len(sols) == 1]
    with_sols = [(prime, sols) for prime, sols in prime_sols.items() if len(sols) > 1]
    print(with_sols)
    primes_with_sols = [prime for prime, _ in with_sols]
    modulus_with_sols = math.prod(primes_with_sols)
    modulus_without_sols = math.prod(only_one_is_sol)
    total = 0
    count = 0
    for remainders in cartesian_product([sols for _, sols in with_sols]):
        solution = crt_solve_multi(zip(remainders, primes_with_sols))
        solution = crt_solve(solution, modulus_with_sols, 1, modulus_without_sols)
        if solution > 1:
            total += solution
            count += 1
    print(total, count)


if __name__ == "__main__":
    # find_sols(43)
    main()
