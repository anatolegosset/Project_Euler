from pe_lib import check_gonal, continued_frac_root_step, root_convergents_step, sum_of_digits
import math


def main(max_n=100):
    factor = 10 ** 99
    total = 0
    for n in range(max_n + 1):
        if not check_gonal(n, 4):
            m = 0
            d = 1
            a = int(math.floor(math.sqrt(n)))
            a0 = a
            m, d, a = continued_frac_root_step(n, m, d, a)
            old_num, old_den = a0, 1
            num, den = a * a0 + 1, a
            while old_den * den < 100 * factor:
                m, d, a, num, den, old_num, old_den = root_convergents_step(n, m, d, a, num, den, old_num, old_den)
            print(num, den, (factor * num) // den)
            total += sum_of_digits((factor * num // den))
    return total

