def _check_rule1(to_check):
    sums = [0]
    for i, a in enumerate(to_check):
        for previous_sum in sums[: 2 ** (i + 1)]:
            sums.append(previous_sum + a)
    return len(set(sums)) == len(sums)


def _check_rule2(to_check):
    for i in range(len(to_check)):
        if sum(to_check[:i + 2]) <= sum(to_check[-i - 1:]) and (len(to_check[:i + 2]) != len(to_check[-i - 1:])):
            return False
    return True


def main():
    with open("./Data/0105_sets.txt") as f:
        sets = [sorted([int(char) for char in line.split(',')]) for line in f.read().splitlines()]

    total = 0
    for tentative_set in sets:
        if _check_rule1(tentative_set) and _check_rule2(tentative_set):
            total += sum(tentative_set)
    return total