import math

from src.project_euler.lib import check_gonal


def main(max_b=100_000_000):
    for b in range(4, max_b, 4):
        if check_gonal((b + 1) ** 2 + (b // 2) ** 2, 4):
            print(b, int(math.sqrt((b + 1) ** 2 + (b // 2) ** 2)))
        if check_gonal((b - 1) ** 2 + (b // 2) ** 2, 4):
            print(b, int(math.sqrt((b - 1) ** 2 + (b // 2) ** 2)))
