def main(nb_rounds: int):
    expected_value = 0
    for k in range(1, nb_rounds + 1):
        expected_value += k * ((1 - 1 / 2**k) ** 32 - (1 - 1 / 2 ** (k - 1)) ** 32)
    print(expected_value)


if __name__ == "__main__":
    main(10000)
