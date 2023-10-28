import math


def main():
    with open('./Data/0099_base_exp.txt') as f:
        pairs = [pair.split(',') for pair in f.read().splitlines()]
    current_max = 0
    best_id = 0
    for i, pair in enumerate(pairs):
        a = int(pair[1]) * math.log(int(pair[0]))
        if a > current_max:
            current_max = a
            best_id = i + 1

    return best_id