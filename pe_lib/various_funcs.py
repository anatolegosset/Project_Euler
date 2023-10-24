import math
from collections import Counter
from string import ascii_uppercase

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


def generate_primes_under(n, under_root=False):
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
        if is_prime[j]:
            primes.append(j)

    return primes


def prime_decomposition(n, primes=None):
    root = math.ceil(math.sqrt(n))

    if primes is None:
        print("Warning: slow factorization due to prime generation.")
        primes = generate_primes_under(n, under_root=True)

    if root > 2 * primes[-1]:
        raise ValueError("n too big to factorize with primes given")

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


def totient(n, primes=None):
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
            result *= (prime - 1)
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
    else:
        return 3 * n + 1


def is_pandigital(n):
    digits = []
    temp_n = n
    while temp_n > 0:
        digits.append(temp_n % 10)
        temp_n = temp_n // 10
    return sorted(digits) == list(range(1, len(digits) + 1))


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


def generate_cycles(n):
    exponent = (len(str(n)) - 1)
    factor = 10 ** exponent
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
        true_result += a * 10 ** i

    return true_result


def remove_first_digit(n):
    exponent = int(math.floor(math.log10(n)))
    return n % 10 ** exponent


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
    else:
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


def fast_is_prime(n, primes):
    root = int(math.ceil(math.sqrt(n)))
    if root > primes[-1]:
        raise ValueError("Warning: not enough primes in list for fast_is_prime.")
    for prime in primes:
        if prime > root:
            return True
        elif n % prime == 0:
            return False


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
