import math
from collections import Counter
from string import ascii_uppercase
from typing import Callable
from collections.abc import Iterator

uppercase_letter_value = {}
for _char in ascii_uppercase:
    uppercase_letter_value[_char] = ascii_uppercase.index(_char) + 1


def word_value(word):
    result = 0
    for char in word:
        result += uppercase_letter_value[char]
    return result


def is_palindrome(number):
    num_str = str(number)
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[-i - 1]:
            return False
    return True


def max_product(num_str, length=13):
    if len(num_str) < length:
        return 0

    product = 1
    for i in range(length):
        product *= int(num_str[i])

    current_max = product

    for i in range(len(num_str) - length):
        product = product // int(num_str[i]) * int(num_str[i + 13])
        current_max = max(product, current_max)

    return current_max


def lprod(int_list, start=1):
    result = start
    for a in int_list:
        result *= a
    return result


def is_pyth(a, b, c):
    return a * a + b * b == c * c


def mini_prod(l, i, length):
    product = 1
    for j in range(i, i + length):
        product *= int(l[j])
    return product


def simple_max_product_list(num_list, length=4):
    if len(num_list) < length:
        return 0

    acc = 0

    for i in range(len(num_list) - length):
        acc = max(acc, mini_prod(num_list, i, length))

    return acc


def generate_primes_under(
    n: int,
    under_root: bool = False,
    min_prime: int = 0,
) -> list[int]:
    """
    Returns an increasing list of first primes, such that all primes are <= n if
    under_root = False, or <= ceil(sqrt(n)) if under_root = True, and all primes are
    >= min_prime.
    """
    if under_root:
        max_n = math.ceil(math.sqrt(n))
    else:
        max_n = n
    root = math.ceil(math.sqrt(max_n))
    is_prime = [True] * (max_n + 1)
    primes = []
    for i in range(2, root):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    for j in range(root, max_n + 1):
        if is_prime[j] and j >= min_prime:
            primes.append(j)

    return primes


def prime_decomp_under(n):
    root = int(math.sqrt(n)) + 1
    primes = generate_primes_under(n)
    decomps = [(1, Counter())]
    large_prime_decomps = []
    for prime in primes:
        if prime > n // 2:
            large_prime_decomps.append((prime, Counter({prime: 1})))
            continue
        if prime > root:
            for a, decomp in decomps:
                product = prime * a
                if product > n:
                    break
                large_prime_decomps.append((product, Counter({prime: 1}) + decomp))
        else:
            exponent = 1
            factor = prime
            new_decomps = []
            while True:
                if factor > n:
                    break
                for a, decomp in decomps:
                    product = factor * a
                    if product > n:
                        break
                    new_decomps.append((product, Counter({prime: exponent}) + decomp))

                exponent += 1
                factor *= prime
            decomps = sorted(decomps + new_decomps)
    decomps = sorted(decomps + large_prime_decomps)
    return sorted(decomps, key=(lambda x: x[0]))


def smallest_prime_factors(n: int) -> list[int]:
    """
    Returns a list of integer result such that result[k] is the smallest prime factor of
    k for all k <= n.
    """
    result = list(range(n + 1))
    for i in range(2, int(math.sqrt(n)) + 1):
        if result[i] == i:
            for j in range(i * i, n + 1, i):
                if result[j] == j:
                    result[j] = i
    return result


def fast_prime_decomp_under(n: int):
    """
    For any integer n >= 1, returns a list of dicts output such that for all i such
    that 0 <= i <= n, output[i] is a dict that maps prime divisors of i to their
    exponent in the prime decomposition of i.
    """
    output = [Counter(), Counter()]
    spf = smallest_prime_factors(n)
    for k in range(2, n + 1):
        p = spf[k]
        divisors = output[k // p].copy()
        divisors[p] += 1
        output.append(divisors)
    return output


def compute_multiplicative_under(
    n: int,
    on_radical: Callable[[int, int], int],
) -> list[int]:
    """
    For any multiplicative function f, and given an integer n and a function on_radical
    that is such that on_radical(p, exp) = f(p ** exp) for all prime number p and
    exp > 0, computes f(k) for all 1 <= k <= n and returns the output as a list result
    such that result[k] = f(k).
    """
    spf = smallest_prime_factors(n)
    result = [0, 1]
    for i in range(2, n + 1):
        p = spf[i]
        exp = 0
        while i % p == 0:
            i = i // p
            exp += 1
        if i == 1:
            result.append(on_radical(p, exp))
        else:
            result.append(result[i] * result[p**exp])
    return result


def compute_totient_under(n: int):
    """
    Returns a list output such that output[k] == totient(k) for 1 <= k <= n.
    """
    result = [0, 1]
    spf = smallest_prime_factors(n)
    for i in range(2, n + 1):
        p = spf[i]
        quotient = i // p
        tot = result[quotient]
        if quotient % p > 0:
            result.append((p - 1) * tot)
        else:
            result.append(p * tot)
    return result


def generate_divisors_under(n, include_self=True, include_1=True, to_sort=True):
    result = [[] for _ in range(n + 1)]
    min_i = 1
    min_j = 1
    if not include_1:
        min_i += 1
    if not include_self:
        min_j += 1

    for i in range(min_i, n + 1):
        product = i * min_j
        while product <= n:
            result[product].append(i)
            product += i

    if to_sort:
        return [sorted(divisors) for divisors in result]
    return result


def generate_sod_under(n, include_self=True, include_1=True):
    result = [0 for _ in range(n + 1)]
    min_i = 1
    min_j = 1
    if not include_1:
        min_i += 1
    if not include_self:
        min_j += 1

    for i in range(min_i, n + 1):
        j = min_j
        while j * i <= n:
            result[i * j] += i
            j += 1

    return result


def prime_decomposition(n, primes=None):
    root = math.ceil(math.sqrt(n))

    if primes is None:
        print("Warning: slow factorization due to prime generation.")
        primes = generate_primes_under(n, under_root=True)

    if root > 2 * primes[-1]:
        print("Warning: n could be too big to factorize with primes given")

    if n == 0:
        raise ValueError("Cannot do prime decomposition of 0.")

    result = []
    temp_n = n
    for prime in primes:
        if prime > root:
            break
        alpha = 0
        while temp_n % prime == 0:
            alpha += 1
            temp_n = temp_n // prime
        if alpha > 0:
            result.append((prime, alpha))
        if temp_n == 1:
            break
    if temp_n > 1:
        result.append((temp_n, 1))
    return result


def compute_totient(n: int, primes=None):
    """
    Computes the totient function for n.

    :param n: the number to compute the totient for.
    :param primes: an ordered list of the first primes. Must have all primes that are
        <= sqrt(n)
    :return: the totient of n
    """
    root = math.ceil(math.sqrt(n))

    if primes is None:
        print("Warning: slow factorization due to prime generation.")
        primes = generate_primes_under(n, under_root=True)

    if root > 2 * primes[-1]:
        raise ValueError("n too big to factorize with primes given")

    if n == 0:
        raise ValueError("Cannot compute phi(0).")

    result = 1
    temp_n = n
    for prime in primes:
        if prime > root:
            break
        if temp_n % prime == 0:
            temp_n = temp_n // prime
            result *= prime - 1
        while temp_n % prime == 0:
            result *= prime
            temp_n = temp_n // prime
        if temp_n == 1:
            break
    if temp_n > 1:
        result *= temp_n - 1
    return result


def collatz_step(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def is_pandigital(n, k=None):
    digits = []
    temp_n = n
    while temp_n > 0:
        digits.append(temp_n % 10)
        temp_n = temp_n // 10
    if k is None:
        target = len(digits) + 1
    else:
        target = k + 1
    return sorted(digits) == list(range(1, target))


def check_if_pandigital_product(m, n):
    digits = []
    temp_m = m
    while temp_m > 0:
        digits.append(temp_m % 10)
        temp_m = temp_m // 10

    temp_n = n
    while temp_n > 0:
        digits.append(temp_n % 10)
        temp_n = temp_n // 10

    product = n * m
    while product > 0:
        digits.append(product % 10)
        product = product // 10

    return sorted(digits) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


_first_factorials = {i: factorial(i) for i in range(10)}


def factorial_digit_sum(n):
    return sum([_first_factorials[i] for i in non_unique_digits(n, to_sort=False)])


def generate_cycles(n):
    exponent = len(str(n)) - 1
    factor = 10**exponent
    current_number = n
    result = [current_number]
    for i in range(exponent):
        digit = current_number % 10
        current_number = current_number // 10 + digit * factor
        result.append(current_number)

    return result


def convert_to_fake_base(n, base=2):
    temp_n = n
    result = []

    while temp_n > 0:
        result.append(temp_n % base)
        temp_n = temp_n // base

    true_result = 0
    for i, a in enumerate(result):
        true_result += a * 10**i

    return true_result


def remove_first_digit(n):
    exponent = int(math.floor(math.log10(n)))
    return n % 10**exponent


# def nb_distinct_prime_factors(n):
#     temp_n = n
#     distinct = set()
#
#     for prime in under_million_primes:
#         while temp_n % prime == 0:
#             distinct.add(prime)
#             temp_n = temp_n // prime
#         if temp_n == 1:
#             break
#     return len(distinct)


def int_from_digit_list(digit_list, base=10, reverse=False):
    if not reverse:
        result = 0
        for digit in digit_list:
            result *= base
            result += digit
    else:
        factor = 1
        result = 0
        for digit in digit_list:
            result += factor * digit
            factor *= 10
    return result


def is_int_in_order(n):
    listed_int = list(str(n))
    return listed_int == sorted(listed_int)


def int_permutations(n):
    number_of_digits = len(str(n))
    result = set()
    current_path = []
    possible = Counter([int(i) for i in str(n)])

    def rec_permute():
        if len(current_path) == number_of_digits:
            result.add(int_from_digit_list(current_path))
        else:
            for i in possible.keys():
                if possible[i] > 0:
                    current_path.append(i)
                    possible[i] -= 1
                    rec_permute()
                    possible[i] += 1
                    current_path.pop()

    rec_permute()
    return sorted(list(result))


def one_mask(n, digit):
    """
    :param n: number to extract one mask from
    :param digit: digit of mask
    :return: integer mask such that n - mask is n with all digit digits replaced by zeroes
    """
    mask_list = []
    str_digit = str(digit)

    for d in str(n):
        if d == str_digit:
            mask_list.append("1")
        else:
            mask_list.append("0")
    return int("".join(mask_list))


def unique_digits(number, base=10):
    result = set()
    temp_number = number
    while temp_number > 0:
        result.add(temp_number % base)
        temp_number = temp_number // base
    return sorted(list(result))


def non_unique_digits(number, base=10, to_sort=True):
    result = []
    temp_number = number
    while temp_number > 0:
        result.append(temp_number % base)
        temp_number = temp_number // base
    if to_sort:
        return sorted(result)
    return result


def is_int_permutation_of(a, b):
    return non_unique_digits(a) == non_unique_digits(b)


def reverse(n):
    digit_list = non_unique_digits(n, to_sort=False)
    return int_from_digit_list(digit_list)


def nb_digits(n, base=10):
    if n == 0:
        return 1
    return int(math.floor(math.log(n, base))) + 1


def sum_of_digits(n, base=10):
    current_number = n
    current_sum = 0
    while current_number > 0:
        current_sum += current_number % base
        current_number = current_number // base
    return current_sum


def iterated_sum_of_digits(n, base=10):
    current_sum = n
    while current_sum >= base:
        current_sum = sum_of_digits(current_sum, base)
    return current_sum


def ascii_list_to_str(ascii_list):
    result = [chr(i) for i in ascii_list]
    return "".join(result)


def str_to_ascii_list(text_str):
    return [ord(i) for i in text_str]


def decode_xor(text: list, key: str):
    """
    :param text: a list of ascii values representing the text
    :param key: a string of ascii characters
    :return: a list of ascii values
    """
    result = []
    period = len(key)
    key_list = [ord(char) for char in key]

    for i, char in enumerate(text):
        result.append(char ^ key_list[i % period])

    return result


def fast_is_prime(n, primes, ignore_low_primes=False):
    if n == 1:
        return False
    root = int(math.ceil(math.sqrt(n)))
    if not ignore_low_primes and root > primes[-1]:
        raise ValueError("Warning: not enough primes in list for fast_is_prime.")
    for prime in primes:
        if prime > root:
            return True
        if n % prime == 0 and n != prime:
            return False
    return True


def concat_ints(int_list):
    return int("".join([str(i) for i in int_list]))


def generate_permutation(list_to_permute, constraints=None):
    """
    :param list_to_permute: the list of elements to generate a permutation of.
    :param constraints: a list of functions. They must be of the form f: current_path, element -> can_add_element,
                                                        returning True if element can be in the permutation at this spot
    :return: a list of all possible permutations
    """

    if constraints is None:

        def constraint_func(*args):
            return True
    else:

        def constraint_func(previous_path, elem):
            for constraint in constraints:
                if not constraint(previous_path, elem):
                    return False
            return True

    result = []
    max_depth = len(list_to_permute)
    possible = Counter(list_to_permute)
    current_path = []

    def rec_permute():
        if len(current_path) == max_depth:
            result.append(list(current_path))
        else:
            for element in possible:
                if possible[element] > 0 and constraint_func(current_path, element):
                    possible[element] -= 1
                    current_path.append(element)
                    rec_permute()
                    current_path.pop()
                    possible[element] += 1

    rec_permute()
    return result


def is_magic_n_gon(n_gon):
    n = len(n_gon) // 2
    line_sum = n_gon[0] + n_gon[1] + n_gon[3]
    for i in range(n):
        if n_gon[2 * i] + n_gon[2 * i + 1] + n_gon[(2 * i + 3) % (2 * n)] != line_sum:
            return False
    return True


def _n_choose_k(set_to_choose_from, k, previous_subsets=None):
    if min(set_to_choose_from) < 0:
        raise ValueError(
            "_n_choose_k function in various_funcs cannot choose from negative integers.",
        )
    choices = set(set_to_choose_from)
    n = len(choices)
    if k < 0 or k > n:
        if previous_subsets is None:
            return []
        return previous_subsets
    if previous_subsets is None:
        result = []
    else:
        result = previous_subsets
    current_set = []

    def _rec_choose(previous):
        if len(current_set) == k:
            result.append(list(current_set))
            return
        for a in set_to_choose_from:
            if a > previous:
                current_set.append(a)
                _rec_choose(a)
                current_set.pop()

    _rec_choose(-1)
    return result


def gen_subsets(set_to_sub, k=None):
    if len(set_to_sub) == 0 and k == 0:
        return [[]]
    if k is None:
        result = []
        for k in range(len(set_to_sub) + 1):
            _n_choose_k(set_to_sub, k, result)
        return result
    return _n_choose_k(set_to_sub, k)


def generate_cartesian_product(set_to_perm, k):
    result = []
    current_path = []

    def _rec_product():
        if len(current_path) == k:
            result.append(list(current_path))
        else:
            for a in set_to_perm:
                current_path.append(a)
                _rec_product()
                current_path.pop()

    _rec_product()
    return result


def multiplicative_order(k: int, n: int):
    """
    :param k: int
    :param n: int
    :return: the least positive integer alpha such that k ** alpha == 1 mod n
    """
    if math.gcd(k, n) != 1:
        raise ValueError(
            f"{k} and {n} are not coprime and so cannot compute order of k in Z/nZ.",
        )
    order_10 = 1
    remainder = 10
    while remainder != 1:
        remainder = (remainder * 10) % n
        order_10 += 1
    return order_10


def bezout_solve(a: int, b: int) -> tuple[int, int]:
    """
    Returns a tuple of two integers (m, n) such that m * a + n * b == gcd(a, b).
    """
    old_r = a
    old_s = 1
    old_t = 0
    new_r = b
    new_s = 0
    new_t = 1
    while new_r != 0:
        quotient, remainder = divmod(old_r, new_r)
        old_r, new_r = new_r, remainder
        old_s, new_s = new_s, old_s - quotient * new_s
        old_t, new_t = new_t, old_t - quotient * new_t
    return old_s, old_t


def crt_solve(rem_1: int, mod_1: int, rem_2: int, mod_2: int) -> int:
    """
    Assuming that mod_1 is coprime to mod_2, returns the unique integer x such that:
    - x % mod_1 == rem_1 % mod_1
    - x % mod_2 == rem_2 % mod_2
    - 0 <= x < mod_1 * mod_2
    """
    c_1, c_2 = bezout_solve(mod_1, mod_2)
    return (rem_1 * c_2 * mod_2 + rem_2 * c_1 * mod_1) % (mod_1 * mod_2)


def crt_solve_multi(constraints: Iterator[tuple[int, int]]) -> int:
    """
    If constraints is a list[tuple[int, int]] such that the x[1] are pairwise coprime
    for all x in constraints, returns the only integer matching all constraints.

    Works even if len(constraints) == 1
    """
    current_sol, current_mod = next(constraints)
    current_sol = current_sol % current_mod
    for rem, modulus in constraints:
        current_sol = crt_solve(current_sol, current_mod, rem, modulus)
        current_mod = current_mod * modulus
    return current_sol


def cartesian_product(components: list[list]) -> Iterator[list]:
    status = [[0, len(component), component] for component in components]
    while status[0][0] < status[0][1]:
        output = []
        for current, max_current, component in status:
            output.append(component[current])
        yield output
        try:
            i = -1
            while status[i][0] == status[i][1] - 1:
                status[i][0] = 0
                i -= 1
            status[i][0] += 1
        except IndexError:
            return
