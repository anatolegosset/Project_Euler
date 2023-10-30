from pe_lib import fast_is_prime, generate_primes_under, gen_subsets, generate_cartesian_product


def main(nb_digits=10):
    upper_bound = 2 * 10 ** nb_digits
    lower_bound = 10 ** (nb_digits - 1)
    primes = generate_primes_under(upper_bound, under_root=True)
    max_number_sum = []
    subsets = []
    cartesian_product = []
    total = 0
    for digit in range(10):
        for nb_repeated in range(nb_digits, 0, -1):
            non_repeated = nb_digits - nb_repeated
            m, n, s, = -1, 0, 0
            if non_repeated >= len(subsets):
                subsets.append([set(temp_subset) for temp_subset in gen_subsets(range(nb_digits), non_repeated)])
                cartesian_product.append(generate_cartesian_product(range(10), non_repeated))

            for subset in subsets[non_repeated]:
                for product in cartesian_product[non_repeated]:
                    if digit == 2 and nb_repeated == 3 and product == [9] and subset == {3}:
                        print(1)
                    k = 0
                    number = 0
                    for i in range(nb_digits):
                        if i in subset:
                            number = 10 * number + product[k]
                            k += 1
                        else:
                            number = 10 * number + digit
                    if fast_is_prime(number, primes) and number >= lower_bound:
                        m = nb_repeated
                        n += 1
                        s += number
            if n > 0:
                max_number_sum.append((digit, m, n, s))
                total += s
                break
    print(max_number_sum)
    return total




