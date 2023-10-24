

def main(max_n=100):
    nb_sums = [[0] * max_n for i in range(max_n + 1)]

    nb_sums[0] = [1] * max_n
    nb_sums[1] = [1] * max_n
    for i in range(max_n + 1):
        nb_sums[i][1] = 1

    for n in range(2, max_n + 1):
        for m in range(2, max_n):
            if m > n:
                nb_sums[n][m] = nb_sums[n][n]
            else:
                total = 0
                for i in range(1, m + 1):
                    total += nb_sums[n - i][i]
                nb_sums[n][m] = total

    return nb_sums[max_n][-1]
