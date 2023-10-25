from pe_lib import generate_product_partitions, generate_divisors_under


def main(max_k=12000):
    divisors = generate_divisors_under(2 * max_k, include_self=True, include_1=False)

    smallest_n = set()

    for k in range(2, max_k + 1):
        flag = False
        for n in range(k + 1, 2 * k):
            product_partitions = generate_product_partitions(n, divisors=divisors, max_factors=k)
            for partition in product_partitions:
                if k + sum(partition) - len(partition) == n:
                    smallest_n.add(n)
                    print(k, n, partition)
                    flag = True
                    break
            if flag:
                break
        if not flag:
            print(k, 2 * k)
            smallest_n.add(2 * k)

    return sum(smallest_n)
