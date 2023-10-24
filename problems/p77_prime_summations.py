from pe_lib import generate_primes_under
from bisect import bisect_right


def main(max_n=100):
    primes = generate_primes_under(max_n + 1)
    prime_rank = {prime: i for i, prime in enumerate(primes)}

    nb_sums = [[0] * (bisect_right(primes, i) + 1) for i in range(max_n + 1)]
    nb_sums[0] = [1]

    def f(temp_n, max_p):
        if prime_rank[max_p] >= len(nb_sums[temp_n]) - 1:
            return nb_sums[temp_n][-1]
        else:
            return nb_sums[temp_n][prime_rank[max_p] + 1]

    current_max = 0
    best_n = 2
    for n in range(1, max_n + 1):
        for i, p in enumerate(primes):
            if p > n:
                break
            else:
                total = 0
                for other_p in primes[:i + 1]:
                    total += f(n - other_p, other_p)
                nb_sums[n][prime_rank[p] + 1] = total
        if nb_sums[n][-1] > current_max:
            current_max = nb_sums[n][-1]
            print(n, current_max)
            best_n = n
        if nb_sums[n][-1] > 5000:
            break

    return nb_sums[best_n][-1]
