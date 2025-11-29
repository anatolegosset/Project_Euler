from project_euler.lib import (
    fast_prime_decomp_under,
    cartesian_product,
    crt_solve_multi,
)


def main(n: int):
    decomps = fast_prime_decomp_under(n)
    print("done decomp")
    total = 0
    for k, decomp in enumerate(decomps[2:], start=2):
        if len(decomp) == 1:
            total += 1
            continue
        single_prime_factors = [p ** decomp[p] for p in sorted(decomp.keys())]
        max_solution = 1
        for combination in cartesian_product(
            [[0, 1] for _ in range(len(single_prime_factors))],
        ):
            solution = crt_solve_multi(zip(combination, single_prime_factors))
            max_solution = max(max_solution, solution)
        total += max_solution
    print(total)


if __name__ == "__main__":
    main(10_000_000)
