def _is_bouncy(n):
    temp_n = n // 10
    previous_digit = n % 10
    flag_increase = True
    flag_decrease = True
    while temp_n > 0:
        flag_increase = flag_increase and (temp_n % 10 >= previous_digit)
        flag_decrease = flag_decrease and (temp_n % 10 <= previous_digit)
        previous_digit = temp_n % 10
        temp_n = temp_n // 10
        if not flag_decrease and not flag_increase:
            return True
    return False


def main():
    n = 100
    nb_bouncy = 0
    while True:
        if _is_bouncy(n):
            nb_bouncy += 1
        if (nb_bouncy * 100) % n == 0 and (nb_bouncy * 100) // n == 99:
            return n
        if n == 538 or n == 21780:
            print(n, nb_bouncy / n)
        n += 1
