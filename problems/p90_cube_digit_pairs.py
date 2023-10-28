from pe_lib import gen_subsets


def _is_valid(dice_config1, dice_config2):
    flag_1 = (0 in dice_config1 and 1 in dice_config2) or (1 in dice_config1 and 0 in dice_config2)
    flag_4 = (0 in dice_config1 and 4 in dice_config2) or (4 in dice_config1 and 0 in dice_config2)
    flag_9 = ((0 in dice_config1 and (9 in dice_config2 or 6 in dice_config2)) or (
            (9 in dice_config1 or 6 in dice_config1) and 0 in dice_config2))
    flag_16 = (1 in dice_config1 and (9 in dice_config2 or 6 in dice_config2)) or (
                (9 in dice_config1 or 6 in dice_config1) and 1 in dice_config2)
    flag_25 = (2 in dice_config1 and 5 in dice_config2) or (5 in dice_config1 and 2 in dice_config2)
    flag_36 = (3 in dice_config1 and (9 in dice_config2 or 6 in dice_config2)) or (
            (9 in dice_config1 or 6 in dice_config1) and 3 in dice_config2)
    flag_49_64 = (4 in dice_config1 and (9 in dice_config2 or 6 in dice_config2)) or (
            (9 in dice_config1 or 6 in dice_config1) and 4 in dice_config2)
    flag_81 = (8 in dice_config1 and 1 in dice_config2) or (1 in dice_config1 and 8 in dice_config2)
    return flag_1 and flag_4 and flag_9 and flag_16 and flag_25 and flag_36 and flag_49_64 and flag_81


def main():
    possible_sets = gen_subsets(range(10), 6)
    n = len(possible_sets)
    nb_possible = 0
    for i in range(n):
        for j in range(i, n):
            if _is_valid(possible_sets[i], possible_sets[j]):
                print(possible_sets[i], possible_sets[j])
                nb_possible += 1
    return nb_possible

