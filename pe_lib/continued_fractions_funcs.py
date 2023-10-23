import math
from .gonal_funcs import check_gonal


def continous_frac_step(irrational):
    return int(math.floor(irrational)), 1 / (irrational - int(math.floor(irrational)))


def continuous_frac_expansion(i):
    # doesn't work
    if not check_gonal(i, 4):
        frac_part = math.sqrt(i)
        a0 = int(math.floor(frac_part))
        frac_part = 1 / (frac_part - a0)
        expansion = []
        flag = False
        while True:
            a, b = continous_frac_step(frac_part)
            expansion.append(a)
            frac_part = b
            if a == 2 * a0:
                if flag:
                    return i, a0, expansion, len(expansion) // 2
                else:
                    flag = True
    else:
        return None


def continued_frac_root_step(n, m, d, a):
    new_m = d * a - m
    new_d = (n - new_m * new_m) // d
    new_a = (int(math.floor(math.sqrt(n))) + new_m) // new_d
    return new_m, new_d, new_a


def continued_frac_root_expansion(n):
    if not check_gonal(n, 4):
        expansion = []
        m = 0
        d = 1
        a = int(math.floor(math.sqrt(n)))
        a0 = a
        flag = False
        while True:
            m, d, a = continued_frac_root_step(n, m, d, a)
            expansion.append(a)
            if a == 2 * a0:
                if flag:
                    return n, a0, expansion, len(expansion) // 2
                else:
                    flag = True
    else:
        return None


def continued_convergent_step(num, den, old_num, old_den, a):
    return num * a + old_num, den * a + old_den


def convergents_from_expansion(a0, expansion):
    result = [(a0, 1), (a0 * expansion[0] + 1, expansion[0])]
    for a in expansion[1:]:
        num, den = result[-1]
        old_num, old_den = result[-2]
        result.append(continued_convergent_step(num, den, old_num, old_den, a))
    return result
