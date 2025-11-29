from math import sqrt, ceil


def main(n: int):
    count = 0
    for i in range(3, n // 4 + 1):
        square = i * i
        if square < n:
            count += (i - 1) // 2
        else:
            min_size = ceil(sqrt(square - n))
            count += (i - min_size) // 2
    print(count)


if __name__ == "__main__":
    main(10**6)
