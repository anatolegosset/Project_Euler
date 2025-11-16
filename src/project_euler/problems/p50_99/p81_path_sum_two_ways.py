

def main():
    with open("./Data/0081_matrix.txt") as f:
        matrix = f.read().splitlines()

    matrix = [[int(number) for number in line.split(",")] for line in matrix]
    size = len(matrix)

    distances = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            distances[i][j] = matrix[i][j]
            if i != 0 and j != 0:
                distances[i][j] += min(distances[i][j - 1], distances[i - 1][j])
            elif i != 0:
                distances[i][j] += distances[i - 1][j]
            elif j != 0:
                distances[i][j] += distances[i][j - 1]

    for i in range(size):
        print(distances[i])

    return distances[-1][-1]
