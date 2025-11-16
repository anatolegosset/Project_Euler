from decimal import Decimal, getcontext
from math import pi, sqrt, cos

getcontext().prec = 100


def const_e(n):
    acc = Decimal(0)
    fac = Decimal(1)
    for i in range(n + 1):
        acc += Decimal(1) / fac
        fac *= Decimal(i + 1)
    return acc


def const_pi(n):
    return Decimal(
        "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066"[
            0:n
        ]
    )


def main():
    min_i = -1
    min_frac = 1
    cpi = const_pi(100)
    for i in range(1, 1001):
        if sqrt(i) == int(sqrt(i)):
            continue
        output = cos(pi * sqrt(i))
        rounded = round(output)
        if abs(output - rounded) < min_frac:
            min_i = i
            min_frac = abs(output - rounded)
    for i in range(-1000, 0):
        j = Decimal(i)
        if sqrt(-j) == int(sqrt(-j)):
            continue
        output = cpi * (-j).sqrt()
        output = (output.exp() + (-output).exp()) / Decimal(2)
        rounded = round(output)
        if abs(output - rounded) < min_frac:
            min_i = i
            min_frac = abs(output - rounded)
    return min_i
