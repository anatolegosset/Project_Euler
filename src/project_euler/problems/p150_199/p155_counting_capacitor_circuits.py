from fractions import Fraction


def main(n: int):
    all_values = {Fraction(60)}
    previous = {1: all_values.copy()}
    for i in range(2, n + 1):
        print(i)
        new_values = set()
        for k in range(1, i // 2 + 1):
            for value_1 in previous[k]:
                for value_2 in previous[i - k]:
                    parallel = value_1 + value_2
                    if parallel not in all_values:
                        all_values.add(parallel)
                        new_values.add(value_1 + value_2)
                    series = Fraction(1) / (
                        Fraction(1) / value_1 + Fraction(1) / value_2
                    )
                    if series not in all_values:
                        all_values.add(series)
                        new_values.add(series)
        previous[i] = new_values
    print(previous)
    print(len(all_values))


if __name__ == "__main__":
    main(18)
