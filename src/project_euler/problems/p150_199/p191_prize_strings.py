from collections import Counter


def main(nb_days: int):
    counter = Counter()
    counter[(0, 0)] = 1
    for k in range(nb_days):
        new_counter = Counter()
        new_counter[(0, 0)] = (
            counter[(0, 0)] + counter[(0, 1)] + counter[(0, 2)]
        )  # add present to those with 0 late
        new_counter[(1, 0)] = sum(
            counter.values(),
        )  # either add present to those with one late, or add late to those with zero (6 cases)
        # those 4 add absent
        new_counter[(0, 1)] = counter[(0, 0)]
        new_counter[(1, 1)] = counter[(1, 0)]
        new_counter[(0, 2)] = counter[(0, 1)]
        new_counter[(1, 2)] = counter[(1, 1)]
        # the two remaining absent lead to non-prize, idem for the three remaining late
        counter = new_counter
    print(sum(counter.values()))


if __name__ == "__main__":
    main(30)
