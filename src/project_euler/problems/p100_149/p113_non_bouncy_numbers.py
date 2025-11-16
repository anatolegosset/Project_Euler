def main(max_digits=100):
    increasing = [[-1] * 10 for _ in range(max_digits + 1)]

    def _rec_increasing(min_first_digit, nb_digits):
        if increasing[nb_digits][min_first_digit] != -1:
            return increasing[nb_digits][min_first_digit]
        elif nb_digits == 0:
            increasing[0][min_first_digit] = int(min_first_digit != 0)
            return min_first_digit != 0
        else:
            result = 0
            for digit in range(min_first_digit, 10):
                result += _rec_increasing(digit, nb_digits - 1)
            increasing[nb_digits][min_first_digit] = result
            return result

    _rec_increasing(0, max_digits)
    nb_non_bouncy = increasing[-1][0]
    for i in range(1, max_digits + 1):
        nb_non_bouncy += increasing[i][0] - 9
    print(increasing)
    return nb_non_bouncy
