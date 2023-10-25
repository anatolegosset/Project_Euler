import math


def main(target=2_000_000):
    def nb_rectangles(n, m):
        return math.comb(n + 1, 2) * math.comb(m + 1, 2)

    root = math.sqrt(target)

    current_closest = 0
    best_i_j = (0, 0)
    for i in range(1, 2000):
        if math.comb(i + 1, 2) > root:
            break
        else:
            alpha = 4 * target / (i * (i + 1))
            j = math.floor((-1 + math.sqrt(4 * alpha + 1)) / 2)
            if abs(nb_rectangles(i, j) - target) < abs(current_closest - target):
                current_closest = nb_rectangles(i, j)
                best_i_j = i, j
            j = math.ceil((-1 + math.sqrt(4 * alpha + 1)) / 2)
            if abs(nb_rectangles(i, j) - target) < abs(current_closest - target):
                current_closest = nb_rectangles(i, j)
                best_i_j = i, j

    print(current_closest, best_i_j[0] * best_i_j[1])

    return best_i_j
