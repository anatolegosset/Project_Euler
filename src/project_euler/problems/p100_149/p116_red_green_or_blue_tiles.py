def main(row_length=50):
    def non_rec_comb(row_length1, color_block_size):
        possible_combs = [0] * (row_length1 + 1)
        possible_combs[0] = 1

        def _rec_combs(remaining_length):
            if remaining_length < 0:
                return 0
            if possible_combs[remaining_length] > 0:
                return possible_combs[remaining_length]
            else:
                result = _rec_combs(remaining_length - 1) + _rec_combs(remaining_length - color_block_size)
                possible_combs[remaining_length] = result
                return result
        return _rec_combs(row_length1)

    total = 0
    for color_length in range(2, 5):
        total += non_rec_comb(row_length, color_length) - 1
    return total
