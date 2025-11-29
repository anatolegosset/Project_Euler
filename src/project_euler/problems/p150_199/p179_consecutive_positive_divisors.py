import math

from project_euler.lib.various_funcs import fast_prime_decomp_under


def main(n: int):
    decomp = fast_prime_decomp_under(n)
    print("done decomp")
    previous = 0
    total = 0
    for counter in decomp[2:]:
        nb_divisors = math.prod(exp + 1 for exp in counter.values())
        if nb_divisors == previous:
            total += 1
        previous = nb_divisors
    return total


if __name__ == "__main__":
    print(main(10_000_000))
