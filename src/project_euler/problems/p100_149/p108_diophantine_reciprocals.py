from src.project_euler.lib import prime_decomp_under


def _nb_divisors_of_square_from_prime_decomp(decomp: dict):
    product = 1
    for alpha in decomp.values():
        product *= 2 * alpha + 1
    return (product + 1) // 2


def main(max_n=1000000):
    decomps = prime_decomp_under(max_n)
    best_n = 0
    for n, decomp in decomps:
        if _nb_divisors_of_square_from_prime_decomp(decomp) > 1000:
            best_n = n
            print(decomp)
            break
    return best_n
