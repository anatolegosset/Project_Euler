from queue import PriorityQueue


def main():
    with open("./Data/0081_matrix.txt") as f:
        matrix = f.read().splitlines()

    matrix = [[int(number) for number in line.split(",")] for line in matrix]
    size = len(matrix)

    def neighbours(x, y):
        result = []
        if x == -1 and y == - 1:
            result = [(i, 0) for i in range(size)]
        if x > 0:
            result.append((x - 1, y))
        if x < size - 1:
            result.append((x + 1, y))
        if y < size - 1:
            result.append((x, y + 1))
        return result

    distances = [[-1] * size for _ in range(size)]

    def distance(x, y):
        if x == -1 and y == -1:
            return 0
        else:
            return distances[x][y]

