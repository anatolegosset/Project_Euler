import random
from collections import Counter


def compute_segments(sub_perm: list[int], n: int):
    in_place = [False] * n
    for x in sub_perm:
        in_place[x] = True
    previous = False
    nb_segments = 0
    for current in in_place:
        if current and not previous:
            nb_segments += 1
        previous = current
    return nb_segments


def compute_max(permutation: list[int]):
    current_max = 0
    for i in range(1, len(permutation) + 1):
        potential = compute_segments(permutation[:i], len(permutation))
        current_max = max(current_max, potential)
    return current_max


def main(n: int, nb_iter: int):
    counter = Counter()
    permutation = list(range(n))
    for i in range(nb_iter):
        random.shuffle(permutation)
        counter[compute_max(permutation)] += 1
    print(counter)
    avg = sum(
        count * max_nb_segment for count, max_nb_segment in counter.items()
    ) / sum(counter.values())
    print(avg)


if __name__ == "__main__":
    main(10, 10000000)
