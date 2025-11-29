from project_euler.lib import convert_to_fake_base


def main(n: int):
    x = convert_to_fake_base(n, 2)
    print(x)
    nb_with_one = 1
    nb_with_split = 0
    nb_zeroes = 0
    while n:
        n, rem = divmod(n, 2)
        if rem == 0:
            nb_zeroes += 1
        else:
            nb_with_one, nb_with_split = (
                nb_with_one + nb_with_split,
                nb_zeroes * (nb_with_split + nb_with_one) + nb_with_split,
            )
            nb_zeroes = 0
    print(nb_with_split + nb_with_one)


if __name__ == "__main__":
    main(10**25)
