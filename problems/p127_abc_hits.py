from pe_lib import lprod, prime_decomp_under
from math import gcd


def main(max_c=120_000):
    decomps = prime_decomp_under(max_c)
    rads = [lprod(decomp[1].keys()) for decomp in decomps]
    print(rads)
    total, nb_hits = 0, 0
    for b in range(2, max_c):
        if rads[b - 1] * rads[b] < b + 1:
            total += (b + 1)
            nb_hits += 1
    for c in range(7, max_c):
        print(c)
        rad_c = rads[c - 1]
        if c // rad_c < 7:
            continue
        step = 1
        if c % 2 == 0:
            step += 1
        for a in range(2 + step - 1, c // 2, step):
            rad_a = rads[a - 1]
            b = c - a
            if gcd(a, c) == 1 and rad_a * rad_c * rads[b - 1] < c:
                total += c
                nb_hits += 1
    print(nb_hits)
    return total
