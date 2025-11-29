import math


def find_split(n: int):
    k_low, k_high = math.floor(n / math.e), math.ceil(n / math.e)
    k = (
        k_low
        if k_low * (math.log(n) - math.log(k_low))
        > k_high * (math.log(n) - math.log(k_high))
        else k_high
    )
    return k


def main(n: int):
    result = 0
    for i in range(5, n + 1):
        split = find_split(i)
        gcd = math.gcd(i, split)
        denom = split // gcd
        while denom % 2 == 0:
            denom = denom // 2
        while denom % 5 == 0:
            denom = denom // 5
        if denom > 1:
            result += i
        else:
            result -= i
    print(result)


if __name__ == "__main__":
    main(10000)
