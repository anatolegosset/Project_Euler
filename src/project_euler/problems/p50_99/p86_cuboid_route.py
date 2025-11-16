from src.project_euler.lib import check_gonal


def main(max_m=2000):
    total = 0
    for m in range(1, max_m + 1):
        square = m * m
        for k in range(2, 2 * m):
            if check_gonal(square + k * k, 4):
                nb_decomp = k - 1
                if k >= m + 1:
                    nb_decomp = 2 * m - nb_decomp
                total += (nb_decomp + 1) // 2
        if total > 1_000_000:
            print(m)
            break
    return total
