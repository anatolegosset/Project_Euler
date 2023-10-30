def main(max_k=200):
    depths = [-1] * max_k
    depths[0] = 0
    depths[1] = 1
    current_path = [1, 2]

    def _rec_find_sums(max_depth):
        if len(current_path) == max_depth:
            if current_path[-1] <= max_k and depths[current_path[-1] - 1] == -1:
                depths[current_path[-1] - 1] = max_depth - 1
            return None

        for i, a in enumerate(current_path):
            for b in current_path[i:]:
                if current_path[-1] < a + b <= max_k:
                    current_path.append(a + b)
                    _rec_find_sums(max_depth)
                    current_path.pop()
        return None

    # current_max_depth = 3
    # while min(depths) == -1:
    #     _rec_find_sums(current_max_depth)
    #     print(current_max_depth)
    #     print(depths)
    #     current_max_depth += 1
    # print(depths[14])
    test = [0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 5, 4, 5, 5, 6, 5, 6, 6, 6, 5, 6, 6, 6, 6, 7, 6, 7, 5, 6, 6,
    7, 6, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 8, 6, 7, 7, 7, 7, 8, 7, 8, 7, 8, 8, 8, 7, 8, 8, 8, 6, 7, 7, 8, 7, 8, 8, 9,
    7, 8, 8, 8, 8, 8, 8, 9, 7, 8, 8, 8, 8, 8, 8, 9, 8, 9, 8, 9, 8, 9, 9, 9, 7, 8, 8, 8, 8, 9, 8, 9, 8, 9, 9, 9, 8,
    9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 10, 7, 8, 8, 9, 8, 9, 9, 9, 8, 9, 9, 10, 9, 10, 10, 10,
    8, 9, 9, 9, 9, 9, 9, 10, 9, 9, 9, 10, 9, 10, 10, 10, 8, 9, 9, 9, 9, 9, 9, 10, 9, 10, 9, 10, 9, 10, 10, 10, 9,
    10, 10, 10, 9, 10, 10, 10, 9, 10, 10, 10, 10, 10, 10, -1, 8, 9, 9, 9, 9, 10, 9, 10, 9]
    return sum(test) + 1 + 11
