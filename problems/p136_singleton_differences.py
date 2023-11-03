def main(max_n=50_000_000):
    has_solution = [0] * (max_n + 1)
    count = 0
    for divisor in range(2, max_n + 1):
        for i in range((-divisor - 1) % 4 + 1, 3 * divisor, 4):
            n = i * divisor
            if n > max_n:
                break
            if has_solution[n] == 0:
                count += 1
            elif has_solution[n] == 1:
                count -= 1
            has_solution[n] += 1
    return count
