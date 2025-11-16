def main():
    with open("./Data/0081_matrix.txt") as f:
        matrix = f.read().splitlines()

    matrix = [[int(number) for number in line.split(",")] for line in matrix]
    # matrix = [
    #     [131, 673, 234, 103, 18],
    #     [201, 96, 342, 965, 150],
    #     [630, 803, 746, 422, 111],
    #     [537, 699, 497, 121, 956],
    #     [805, 732, 524, 37, 331],
    # ]
    size = len(matrix)

    def neighbours(i, j):
        result = []
        if x > 0:
            result.append((x - 1, y))
        if y > 0:
            result.append((x, y - 1))
        if x < size - 1:
            result.append((x + 1, y))
        if y < size - 1:
            result.append((x, y + 1))
        return result

    path_sums = [[-1] * size for _ in range(size)]

    path_sums[-1][-1] = matrix[-1][-1]

    modified = {(size - 1, size - 1)}

    next_modified = set()

    while modified:
        for x, y in modified:
            for a, b in neighbours(x, y):
                if (
                    path_sums[a][b] == -1
                    or path_sums[a][b] > path_sums[x][y] + matrix[a][b]
                ):
                    path_sums[a][b] = path_sums[x][y] + matrix[a][b]
                    next_modified.add((a, b))
        modified = next_modified
        next_modified = set()
    return path_sums[0][0]
