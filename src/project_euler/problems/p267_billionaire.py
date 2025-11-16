from math import log, ceil


def compute_nb_heads_needed(precision: int, nb_flips: int):
    for i in range(1, precision):
        k = (9 * log(10) - nb_flips * log(1 - i / precision)) / log(
            (1 + 2 * i / precision) / (1 - i / precision),
        )
        k = ceil(k)
        if k < 433:
            print(i / precision, k)


def compute_probability(k: int, n: int, precision: int):
    """
    Computes the probability to have at least k heads with n fair coin flips with
    k decimal digits of precision
    """
    binomial = 1
    total = 1
    for i in range(1, k):
        binomial *= n - i + 1
        binomial //= i
        total += binomial
    total *= 10 ** (precision + 1)
    probability = total // (2**n)
    probability = 10 ** (precision + 1) - probability
    return probability


if __name__ == "__main__":
    print(compute_probability(432, 1000, 13))
