# n ** 2 = 1_2_3_4_5_6_7_8_9_0
# m = n // 10
# m ** 2 = 1_2_3_4_5_6_7_8_9 => ends with 3 or 7


def check(n: int):
    square = n * n
    for i in range(9, 0, -1):
        if square % 10 != i:
            return False
        square = square // 100
    return True


def main():
    print(141_421_357**2)
    last_three = [
        43,
        53,
        83,
        167,
        197,
        207,
        293,
        303,
        333,
        417,
        447,
        457,
        543,
        553,
        583,
        667,
        697,
        707,
        793,
        803,
        833,
        917,
        947,
        957,
    ]
    for i in range(100_000_000, 141_421_357, 1000):
        for end in last_three:
            if check(i + end):
                print(10 * (i + end))
                print((10 * (i + end)) ** 2)


if __name__ == "__main__":
    main()
