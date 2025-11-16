from src.project_euler.lib import check_gonal
import math


def main(min_t=121):
    t = min_t
    while True:
        delta = 4 + 8 * t * (t - 1)
        if check_gonal(delta, 4):
            if (2 + int(math.sqrt(delta))) % 4 == 0:
                b = (2 + int(math.sqrt(delta))) // 4
                print(b, t)
                break
        t += 1

    return t
