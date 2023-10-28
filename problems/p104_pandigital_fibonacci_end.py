from pe_lib import is_pandigital
import math


def main():
    phi = (1 + math.sqrt(5)) / 2
    log_phi = math.log10(phi)
    log_s5 = math.log10(math.sqrt(5))
    current = 1
    previous = 0
    k = 1
    modulus = 10 ** 9
    while True:
        k += 1
        old = previous
        previous = current
        current = (old + previous) % modulus
        if is_pandigital(current, 9):
            print(k)
            exponent = (k * log_phi - log_s5) % 1.0
            print(int(10 ** (exponent + 8)))
            if is_pandigital(int(10 ** (exponent + 8)), 9):
                break
    return k

