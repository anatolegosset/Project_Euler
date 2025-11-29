from math import sqrt

from project_euler.lib import generate_divisors_under, iterated_sum_of_digits


def main(n: int):
    all_divisors = generate_divisors_under(n - 1, include_1=False)
    total = 0
    previous_values = [0, 0]
    for i in range(2, n):
        divisors = all_divisors[i]
        if len(divisors) == 1:
            drs = iterated_sum_of_digits(i)
            previous_values.append(drs)
            total += drs
            continue
        root = sqrt(i)
        max_drs = 0
        for divisor in divisors:
            if divisor > root + 1:
                break
            max_drs = max(
                max_drs,
                previous_values[divisor] + previous_values[i // divisor],
            )
        max_drs = max(max_drs, iterated_sum_of_digits(i))
        total += max_drs
        previous_values.append(max_drs)
    print(total)
    # 11504186


if __name__ == "__main__":
    main(10**6)
