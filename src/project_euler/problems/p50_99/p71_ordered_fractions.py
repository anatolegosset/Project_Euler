

def main(max_d=1_000_000):
    best_num, best_den = 0, 1
    for d in range(max_d + 1):
        n = (3 * d + 6) // 7 - 1
        if best_num * d < best_den * n:
            print(n, d)
            best_num = n
            best_den = d
    return best_num, best_den
