def sum_distribution(nb_dices: int, nb_sides: int):
    distrib = [1]
    for i in range(nb_dices):
        new_distrib = [0] * (nb_sides * (i + 1) + 1)
        for j in range(1, nb_sides + 1):
            for k, x in enumerate(distrib):
                new_distrib[j + k] += x / nb_sides
        distrib = new_distrib
    return distrib


def main():
    pyramidal = sum_distribution(nb_dices=9, nb_sides=4)
    cubic = sum_distribution(nb_dices=6, nb_sides=6)
    total = 0
    print(pyramidal)
    print(cubic)
    print(sum(pyramidal))
    print(sum(cubic))
    for i, p_i in enumerate(pyramidal):
        for j, p_j in enumerate(cubic):
            if i > j:
                total += p_j * p_i
    print(total)


if __name__ == "__main__":
    main()
