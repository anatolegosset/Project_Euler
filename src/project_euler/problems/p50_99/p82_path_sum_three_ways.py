def main():
    with open("./Data/0081_matrix.txt") as f:
        matrix = f.read().splitlines()

    matrix = [[int(number) for number in line.split(",")] for line in matrix]
    size = len(matrix)

    path_sums = [[-1] * size for _ in range(size)]

    for i in range(size):
        path_sums[i][-1] = matrix[i][-1]

    for j in range(size - 2, -1, -1):
        for i in range(0, size):
            path_sums[i][j] = matrix[i][j] + path_sums[i][j + 1]

        for i in range(0, size - 1):
            path_sums[i + 1][j] = min(
                path_sums[i + 1][j],
                path_sums[i][j] + matrix[i + 1][j],
            )
        for i in range(size - 1, 0, -1):
            path_sums[i - 1][j] = min(
                path_sums[i - 1][j],
                path_sums[i][j] + matrix[i - 1][j],
            )
    return min(path_sums[i][0] for i in range(size))
