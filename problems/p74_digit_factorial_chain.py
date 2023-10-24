from pe_lib import factorial_digit_sum


def main(max_n=1_000_000):
    chain_lengths = [0] * (max_n + 1)
    initial_lengths = {145: 1, 169: 3, 363601: 3, 1454: 3, 871: 2, 45361: 2, 872: 2, 45362: 2}
    for i in initial_lengths:
        chain_lengths[i] = initial_lengths[i]

    count = 0

    for n in range(max_n + 1):
        if chain_lengths[n] == 0:
            current_path = [n]
            current_number = n
            while True:
                current_number = factorial_digit_sum(current_number)
                if current_number == current_path[-1]:
                    if current_number <= max_n:
                        chain_lengths[current_number] = 1
                    break
                if current_number <= max_n and chain_lengths[current_number] > 0:
                    break
                current_path.append(current_number)
            if current_number > max_n:
                depth = 1
            else:
                depth = chain_lengths[current_number] + 1
            while current_path:
                a = current_path.pop()
                if a <= max_n:
                    chain_lengths[a] = depth
                depth += 1

        if chain_lengths[n] == 60:
            count += 1

    return count