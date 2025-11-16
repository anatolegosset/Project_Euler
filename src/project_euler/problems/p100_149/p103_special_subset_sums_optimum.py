def _check_rule1(to_check):
    sums = [0]
    for i, a in enumerate(to_check):
        for previous_sum in sums[: 2 ** (i + 1)]:
            sums.append(previous_sum + a)
    return len(set(sums)) == len(sums)


def _check_rule2(to_check):
    for i in range(len(to_check)):
        if sum(to_check[: i + 2]) <= sum(to_check[-i - 1 :]) and (
            len(to_check[: i + 2]) != len(to_check[-i - 1 :])
        ):
            return False
    return True


def main(n=7):
    current_set = []

    def _rec(max_sum):
        a = len(current_set)
        if a == n - 1:
            if max_sum - sum(current_set) >= current_set[-2] + current_set[-1]:
                return None
            current_set.append(max_sum - sum(current_set))
            print(current_set)
            if _check_rule1(current_set) and _check_rule2(current_set):
                return current_set
            current_set.pop()
            return None
        max_value = 1 + (max_sum - sum(current_set) - ((n - a - 1) * (n - a)) // 2) // (
            n - a
        )
        if len(current_set) >= 2:
            max_value = min(max_value, current_set[-1] + current_set[-2] - n + a + 1)
        for i in range((current_set or [0])[-1] + 1, max_value):
            current_set.append(i)
            if _check_rule1(current_set) and _check_rule2(current_set):
                minimal = _rec(max_sum)
                if minimal is not None:
                    return minimal
                current_set.pop()
            else:
                current_set.pop()
        return None

    min_value = n * (n + 1) // 2
    while True:
        print(min_value)
        result = _rec(min_value)
        if result is not None:
            return result
        min_value += 1
