from pe_lib import generate_primes_under, generate_permutation, fast_is_prime, concat_ints


def _check_last(current_path, element):
    if len(current_path) == 8:
        return element % 2 == 1 or element == 2
    else:
        return True


primes = generate_primes_under(10 ** 9, under_root=True)


def _rec_count_valid_concats(perm, nb_treated, previous_prime):
    if nb_treated == len(perm):
        return 1
    nb_valid = 0
    to_concat = []
    for i, digit in enumerate(perm[nb_treated:]):
        to_concat.append(digit)
        potential_prime = concat_ints(to_concat)
        if fast_is_prime(potential_prime, primes) and potential_prime > previous_prime:
            nb_valid += _rec_count_valid_concats(perm, nb_treated + i + 1, potential_prime)
    return nb_valid


def main():
    permutations = generate_permutation(range(1, 10), constraints=[_check_last])
    total = 0
    for perm in permutations:
        a = _rec_count_valid_concats(perm, 0, 0)
        if a > 0:
            print(perm)
            total += a
    return total

    # print(_rec_count_valid_concats([2, 5, 4, 7, 8, 9, 6, 3, 1], 0, 0))
