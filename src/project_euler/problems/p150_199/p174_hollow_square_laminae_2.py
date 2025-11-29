from collections import Counter
from math import sqrt, ceil


def main(n: int):
    counter = Counter()
    for i in range(3, n // 4 + 1):
        square = i * i
        if square < n:
            for j in range(i - 2, 0, -2):
                counter[square - j * j] += 1
        else:
            min_size = ceil(sqrt(square - n))
            for j in range(i - 2, min_size - 1, -2):
                counter[square - j * j] += 1
    other_counter = Counter(counter.values())
    print(other_counter[15])
    print(sum(other_counter[i] for i in range(1, 11)))


if __name__ == "__main__":
    main(10**6)
