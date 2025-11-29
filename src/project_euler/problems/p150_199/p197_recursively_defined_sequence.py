import math

POWER = 10 ** (-9)


def f(x: float) -> float:
    return POWER * math.floor(2 ** (30.403243784 - x**2))


def main():
    x = -1
    for k in range(10**4):
        print(x)
        x = f(x)
    print(1.029461839 + 0.681175878)


# 1.029461839
# 0.681175878
# 1.029461839
# 0.681175878


if __name__ == "__main__":
    main()
