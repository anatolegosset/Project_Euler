from pe_lib.various_funcs import generate_divisors_under


def generate_partitions(n, max_parts=None, max_value=None):
    result = []
    current_partition = []
    if max_value is None:
        max_value = n
    if max_parts is None:
        max_value = n

    def _rec_partition(i, max_p=max_parts, max_v=max_value):
        if i == 0:
            result.append(list(current_partition))
            return None
        elif len(current_partition) == max_p:
            return None
        else:
            for j in range(1, min(i, max_v) + 1):
                current_partition.append(j)
                _rec_partition(i - j, max_p, min([i - j, j, max_v]))
                current_partition.pop()
            return None

    _rec_partition(n)

    return result


def generate_product_partitions(n, max_factors=None, max_value=None, divisors=None):
    if max_factors is None:
        max_factors = n
    if divisors is None:
        divisors = generate_divisors_under(n)
    if max_value is None:
        max_value = n

    result = []
    current_product = []

    def _rec_product_partitions(i, max_v=max_value):
        if i == 1:
            result.append(list(current_product))
        elif len(current_product) == max_factors:
            return None
        else:
            for j in divisors[i]:
                if j > max_v:
                    break
                current_product.append(j)
                _rec_product_partitions(i // j, max_v=j)
                current_product.pop()

    _rec_product_partitions(n, n - 1)

    return result
