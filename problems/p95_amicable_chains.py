from pe_lib import generate_sod_under


def main(max_n=1_000_000):
    sum_of_digits = generate_sod_under(max_n, include_self=False)
    chain_lengths = [0] * (max_n + 1)
    chain_lengths[0] = - 1
    chain_lengths[1] = - 1
    current_path = []
    max_chain_length = 0
    min_value = 0
    for i in range(2, max_n + 1):
        current_pos = i
        while current_pos <= max_n and chain_lengths[current_pos] == 0:
            chain_lengths[current_pos] = -2
            current_path.append(current_pos)
            current_pos = sum_of_digits[current_pos]

        if current_pos >= max_n or chain_lengths[current_pos] == -1:
            while current_path:
                a = current_path.pop()
                chain_lengths[a] = -1
        elif chain_lengths[current_pos] == -2:
            current_pos_index = current_path.index(current_pos)
            chain_length = len(current_path) - current_pos_index
            flag = max_chain_length < chain_length
            if flag:
                max_chain_length = chain_length
                min_value = current_pos
                print(chain_length, current_path[current_pos_index:])
            for a in current_path[current_pos_index:]:
                chain_lengths[a] = chain_length
                if flag:
                    min_value = min(min_value, a)
            for a in current_path[:current_pos_index]:
                chain_lengths[a] = -1

    return min_value
