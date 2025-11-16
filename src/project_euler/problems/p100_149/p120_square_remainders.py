def main():
    # print(2 * ((a - 1) // 2), 2 * ((a - 1) // 2) * a)
    total = 0
    for a in range(3, 1001):
        total += 2 * ((a - 1) // 2) * a

    return total
