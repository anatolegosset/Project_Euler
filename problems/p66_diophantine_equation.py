from pe_lib import check_gonal, root_convergents_step, continued_frac_root_step
import math


def main(max_n=1000):
    current_max = 0
    best_n = 0

    for n in range(1, max_n + 1):
        if not check_gonal(n, 4):
            m = 0
            d = 1
            a = int(math.floor(math.sqrt(n)))
            a0 = a
            m, d, a = continued_frac_root_step(n, m, d, a)
            old_num, old_den = a0, 1
            num, den = a * a0 + 1, a
            if old_num * old_num == n * old_den * old_den + 1:
                print(n, old_num, old_den)
                if old_num > current_max:
                    current_max = old_num
                    best_n = n
            elif num * num == n * den * den + 1:
                print(n, num, den)
                if num > current_max:
                    current_max = old_num
                    best_n = n
            else:
                while True:
                    m, d, a, num, den, old_num, old_den = root_convergents_step(n, m, d, a, num, den, old_num, old_den)
                    if num * num == n * den * den + 1:
                        print(n, num, den)
                        break
                if num > current_max:
                    current_max = old_num
                    best_n = n

    return best_n, current_max
