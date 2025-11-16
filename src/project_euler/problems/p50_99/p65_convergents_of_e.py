from src.project_euler.lib import convergents_from_expansion, sum_of_digits


def main(expansion_size=100):
    e_expansion = []

    for i in range(expansion_size):
        if i % 3 == 1:
            e_expansion.append(2 * (1 + i // 3))
        else:
            e_expansion.append(1)

    print(e_expansion)
    convergents = convergents_from_expansion(2, e_expansion)
    return sum_of_digits(convergents[-2][0])
