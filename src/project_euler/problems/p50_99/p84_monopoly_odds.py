import numpy as np

np.set_printoptions(threshold=50000, linewidth=2000, precision=3)


def main(nb_sides=4):
    indices = {'GO': 0, 'CC1': 2, 'R1': 5, 'CH1': 7, 'JAIL': 10, 'C1': 11, 'U1': 12, 'R2': 15, 'CC2': 17, 'CH2': 22,
               'E3': 24, 'R3': 25, 'U2': 28, 'G2J': 30, 'CC3': 33, 'CH3': 36, 'H2': 39}
    size = 40

    three_doubles_chance = 1 / (nb_sides ** 3)
    three_doubles = np.add(np.identity(size), -1 * three_doubles_chance * np.identity(size))
    for i in range(size):
        three_doubles[i][indices['JAIL']] += three_doubles_chance

    go_to_jail = np.identity(size)
    go_to_jail[indices['G2J']][indices['G2J']] = 0
    go_to_jail[indices['G2J']][indices['JAIL']] = 1

    community_chest = np.identity(size)
    for cc in ['CC1', 'CC2', 'CC3']:
        community_chest[indices[cc]][indices[cc]] -= 1 / 8
        community_chest[indices[cc]][indices['GO']] += 1 / 16
        community_chest[indices[cc]][indices['JAIL']] += 1 / 16

    chance_card = np.identity(size)
    for ch in ['CH1', 'CH2', 'CH3']:
        chance_card[indices[ch]][indices[ch]] -= 5 / 8
        chance_card[indices[ch]][indices['GO']] += 1 / 16
        chance_card[indices[ch]][indices['JAIL']] += 1 / 16
        chance_card[indices[ch]][indices['C1']] += 1 / 16
        chance_card[indices[ch]][indices['E3']] += 1 / 16
        chance_card[indices[ch]][indices['H2']] += 1 / 16
        chance_card[indices[ch]][indices['R1']] += 1 / 16
        chance_card[indices[ch]][indices[ch] - 3] += 1 / 16
    chance_card[indices['CH1']][indices['R2']] += 1 / 8
    chance_card[indices['CH2']][indices['R3']] += 1 / 8
    chance_card[indices['CH3']][indices['R1']] += 1 / 8
    chance_card[indices['CH1']][indices['U1']] += 1 / 16
    chance_card[indices['CH2']][indices['U2']] += 1 / 16
    chance_card[indices['CH3']][indices['U1']] += 1 / 16

    jail = np.matmul(three_doubles, go_to_jail)
    cards = np.matmul(chance_card, community_chest)
    post_roll = np.matmul(jail, cards)

    roll = np.zeros((size, size))
    for i in range(size):
        for j in range(2, 2 * nb_sides + 1):
            roll[i][(i + j) % 40] = (nb_sides - abs(j - nb_sides - 1)) / (nb_sides * nb_sides)

    full_transition = np.matmul(roll, post_roll)

    iterated = full_transition
    for i in range(100):
        iterated = np.matmul(iterated, full_transition)
    print(iterated)

    to_sort = [(i, iterated[0][i]) for i in range(size)]
    to_sort.sort(key=lambda x: x[1], reverse=True)
    print(to_sort)
