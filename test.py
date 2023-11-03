def modified_generate_divisors_under(n, include_self=True, include_1=True, to_sort=True):
    result = [[] for _ in range(n + 1)]
    min_i = 1
    min_j = 1
    if not include_1:
        min_i += 1
    if not include_self:
        min_j += 1

    for i in range(min_i, n + 1):
        product = i * min_j
        bound = min(n, 3 * i * i)
        while product <= bound:
            result[product].append(i)
            product += i

    return result


def main(max_n=10_000):
    divisors = modified_generate_divisors_under(max_n, include_1=False, to_sort=False)
    print('done')
    count = 0
    for n in range(max_n):
        solutions = []
        for divisor in divisors[n]:
            num = n // divisor + divisor
            if num % 4 == 0 and num // 4 < divisor:
                solutions.append((divisor - num // 4, divisor, divisor + num // 4))
        if solutions:
            count += 1
        print(n, solutions)
    return count

print(main())
