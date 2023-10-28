import numpy as np


def _matrix(triangle):
    return np.array([[triangle[2 * i] for i in range(3)],
                     [triangle[2 * i + 1] for i in range(3)],
                     [1, 1, 1]])


def main():
    with open("./Data/0102_triangles.txt") as f:
        triangles = [[int(number) for number in line.split(",")] for line in f.read().splitlines()]
    total = 0
    for triangle in triangles:
        solution = np.linalg.solve(_matrix(triangle), [0, 0, 1])
        if max(solution) <= 1 and min(solution) >= 0:
            total += 1
    return total
