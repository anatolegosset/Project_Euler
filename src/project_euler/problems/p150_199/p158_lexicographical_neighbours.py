from math import comb


def count(k: int):
    return comb(26, k) * (2**k - k - 1)


def main():
    print(max(count(k) for k in range(1, 27)))


if __name__ == "__main__":
    main()
