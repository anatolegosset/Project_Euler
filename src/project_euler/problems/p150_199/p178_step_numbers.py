from collections import Counter


def main(n: int):
    current = {(i, i, i): 1 for i in range(10)}
    total = 0
    for _ in range(n - 1):
        new_counts = Counter()
        for (leading_digit, lowest, highest), count in current.items():
            if leading_digit != 0:
                new_counts[
                    (leading_digit - 1, min(leading_digit - 1, lowest), highest)
                ] += count
                if leading_digit != 1 and lowest == 0 and highest == 9:
                    total += count
            if leading_digit != 9:
                new_counts[
                    (leading_digit + 1, lowest, max(leading_digit + 1, highest))
                ] += count
                if lowest == 0 and max(leading_digit + 1, highest) == 9:
                    total += count
        current = new_counts
    print(total)


if __name__ == "__main__":
    main(40)
