import math


def main(max_d=12_000):
    count = 0
    for d in range(max_d + 1):
        min_n = math.ceil((d + 1) / 3)
        max_n = (d - 1) // 2
        for n in range(min_n, max_n + 1):
            if math.gcd(d, n) == 1:
                count += 1
    return count
