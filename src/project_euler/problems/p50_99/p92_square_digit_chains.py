def _square_digit_step(n):
    return sum([int(char) ** 2 for char in str(n)])


def main(max_n=10_000_000):
    end_of_chain = [0] * (max_n + 1)
    end_of_chain[1] = 1
    end_of_chain[89] = 2
    total = 1
    for n in range(1, max_n + 1):
        temp_n = n
        current_path = []
        while end_of_chain[temp_n] == 0:
            current_path.append(temp_n)
            temp_n = _square_digit_step(temp_n)
        end = end_of_chain[temp_n]
        if end == 2:
            total += len(current_path)
        while current_path:
            current = current_path.pop()
            end_of_chain[current] = end
    print(end_of_chain)
    return total
