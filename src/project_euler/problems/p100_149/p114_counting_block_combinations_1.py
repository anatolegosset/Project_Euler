def main(min_red_size=50):
    def non_rec_comb(row_length, min_red_size_1=min_red_size):
        possible_combs = [0] * (row_length + 1)
        possible_combs[0] = 1

        def _rec_combs(remaining_length):
            if remaining_length == -1:
                return 1
            if possible_combs[remaining_length] > 0:
                return possible_combs[remaining_length]
            else:
                result = _rec_combs(remaining_length - 1)
                for i in range(min_red_size_1, remaining_length + 1):
                    result += _rec_combs(remaining_length - i - 1)
                possible_combs[remaining_length] = result
                return result
        return _rec_combs(row_length)

    n = 2 * min_red_size
    while True:
        if non_rec_comb(n) > 1_000_000:
            return n
        n += 1
