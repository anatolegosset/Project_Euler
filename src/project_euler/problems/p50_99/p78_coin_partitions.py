import math


def main(max_n=500000):
    values = [1]

    def p(temp_n):
        if temp_n < 0:
            return 0
        else:
            return values[temp_n]

    for n in range(1, max_n + 1):
        min_k = math.floor(-1 * (math.sqrt(24 * n + 1) - 1) / 6)
        max_k = math.ceil((math.sqrt(24 * n + 1) + 1) / 6)
        value = 0
        for k in range(min_k, max_k + 1):
            if k != 0:
                if k % 2 == 0:
                    value -= p(n - k * (3 * k - 1) // 2)
                else:
                    value += p(n - k * (3 * k - 1) // 2)
        values.append(value)
        if value % 1000000 == 0:
            print(n, value)
            break

    return values[-1]
