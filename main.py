from various_funcs import nb_digits, check_gonal
import math

if __name__ == "__main__":
    def continous_frac(irrational):
        return int(math.floor(irrational)), 1 / (irrational - int(math.floor(irrational)))

    max_n = 13
    count = 0

    for i in range(max_n + 1):
        if not check_gonal(i, 4):
            frac_part = math.sqrt(i)
            a0 = int(math.floor(frac_part))
            frac_part = 1 / (frac_part - a0)
            expansion = []
            if i == 7:
                print(1)
            while True:
                a, b = continous_frac(frac_part)
                expansion.append(a)
                frac_part = b
                if len(expansion) % 2 == 0 and expansion[:len(expansion) // 2] == expansion[len(expansion) // 2:]:
                    if (len(expansion) // 2) % 2 == 1:
                        count += 1
                    break
            print(i, len(expansion) // 2)


