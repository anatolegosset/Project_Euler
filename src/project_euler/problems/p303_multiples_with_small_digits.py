# def small_digits():
#     current = 1
#     digit_list = [1]
#     while True:
#         yield current
#         i = 0
#         power = 1
#         while i < len(digit_list) and digit_list[i] == 2:
#             digit_list[i] = 0
#             i += 1
#             current -= 2 * power
#             power *= 10
#         if i == len(digit_list):
#             digit_list.append(1)
#         else:
#             digit_list[i] += 1
#         current += power
#
#
# def main(n: int):
#     total = 0
#     not_done_yet = set(range(1, n + 1))
#     for small in small_digits():
#         to_remove = []
#         for i in not_done_yet:
#             if i > small:
#                 continue
#             if small % i == 0:
#                 print(i, small, total)
#                 total += small // i
#                 to_remove.append(i)
#         for i in to_remove:
#             not_done_yet.remove(i)
#         if not not_done_yet:
#             break
#     return total


def find_solution(k: int):
    available_moduli = {}
    power = 1
    while True:
        new_available = {}
        for already_available, solution in available_moduli.items():
            new_mod = (already_available + 2 * power) % k
            if (
                existing := new_available.get(new_mod)
            ) is None or existing > 2 * power + solution:
                new_available[new_mod] = 2 * power + solution
            new_mod = (already_available + power) % k
            if (
                existing := new_available.get(new_mod)
            ) is None or existing > power + solution:
                new_available[new_mod] = power + solution
        if (existing := new_available.get(power % k)) is None or existing > power:
            new_available[power % k] = power
        if (
            existing := new_available.get((2 * power) % k)
        ) is None or existing > 2 * power:
            new_available[(2 * power) % k] = 2 * power
        new_available.update(available_moduli)
        available_moduli = new_available
        power *= 10
        if 0 in available_moduli:
            return available_moduli[0]


def main(n: int):
    total = 0
    for i in range(1, n + 1):
        total += find_solution(i) // i
    return total


"""
1998 111222222222222 113629093811
2997 112222221222222 169295871700
5994 112222221222222 206740723626
3996 121222222222212 225463149589
6993 122211222222222 255799041036
8991 122212222222221 273275263290
7992 221222222222112 286867991821
"""

if __name__ == "__main__":
    # print(find_solution(7992))
    print(main(10000))
