from src.project_euler.lib import multiplicative_order
import math


def _divisible_repunit(n):
    remainders = []
    remainder = 1
    flag = True
    while flag:
        remainders.append(remainder)
        remainder = (remainder * 10) % n
        if remainder == 1:
            flag = False
    remainder_sum = 0
    flag = True
    exponent = 0
    while flag:
        for remainder in remainders:
            remainder_sum = (remainder_sum + remainder) % n
            exponent += 1
            if remainder_sum == 0:
                flag = False
    return exponent


def main(min_a=1_000_000):
    n = min_a
    while True:
        if math.gcd(n, 10) == 1:
            order_10 = multiplicative_order(10, n)
            if math.lcm(n, order_10) > min_a:
                exponent = _divisible_repunit(n)
                if exponent > min_a:
                    break
        n += 1
    return n
