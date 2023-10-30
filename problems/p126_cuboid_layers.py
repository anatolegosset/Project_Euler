def _direct_formula(a, b, c, i):
    return 2 * a * b + 4 * i * (a + b) + 4 * i * (i - 1) + c * (2 * (a + b) + 4 * i)


def main(max_n=20000):
    nb_cuboids = [0] * (max_n + 1)
    a = 1
    while _direct_formula(a, 1, 1, 0) <= max_n:
        for b in range(1, a + 1):
            if _direct_formula(a, b, 1, 0) > max_n:
                break
            for c in range(1, b + 1):
                if _direct_formula(a, b, c, 0) > max_n:
                    break
                i = 0
                while _direct_formula(a, b, c, i) <= max_n:
                    nb_cuboids[_direct_formula(a, b, c, i)] += 1
                    i += 1
        a += 1

    print(max(nb_cuboids))
    for i, a in enumerate(nb_cuboids):
        if a == 1000:
            return i
    return None
