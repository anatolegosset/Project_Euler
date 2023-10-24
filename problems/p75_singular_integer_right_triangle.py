from collections import Counter
import math

# a, b, c, = m * m - n * n, 2 * m * n, m * m + n * n
# print(a, b, c, a + b + c)


def main(max_p=1_500_000):
    primitive_pythagorean = Counter()

    for p in range(6, max_p // 2 + 2):
        min_m = math.floor(math.sqrt(p / 2))
        max_m = math.ceil((math.sqrt(4 * p + 1) - 1) / 2)
        for m in range(min_m, max_m + 1):
            n = p // m - m
            if p % m == 0 and math.gcd(m, n) == 1 and (m % 2 == 0 or n % 2 == 0) and n < m and m > 1 and n > 0:
                a, b, c, = m * m - n * n, 2 * m * n, m * m + n * n
                if a + b + c == 2 * p:
                    primitive_pythagorean[2 * p] += 1

    unique_count = 0
    all_pythagorean = Counter()
    for p in primitive_pythagorean:
        for multiple in range(p, max_p + 1, p):
            all_pythagorean[multiple] += 1
            if all_pythagorean[multiple] == 1:
                unique_count += 1
            elif all_pythagorean[multiple] == 2:
                unique_count -= 1

    return unique_count

