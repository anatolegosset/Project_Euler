from collections import Counter

from project_euler.lib import sum_of_digits


def main(nb_digits: int):
    current_count = Counter()
    for i in range(100):
        first_digit, second_digit = divmod(i, 10)
        if first_digit + second_digit <= 9:
            current_count[(first_digit, second_digit)] += 1
    for i in range(nb_digits - 2):
        offset = int(i == nb_digits - 3)
        new_count = Counter()
        for (first_digit, second_digit), count in current_count.items():
            for j in range(offset, 9 - first_digit - second_digit + 1):
                new_count[(j, first_digit)] += count
        current_count = new_count
    print(sum(current_count.values()))


def simple_check():
    print(len([i for i in range(100, 1000) if sum_of_digits(i) <= 9]))


if __name__ == "__main__":
    main(20)
    simple_check()
