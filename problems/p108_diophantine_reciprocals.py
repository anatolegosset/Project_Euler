def main():
    n = 4
    while True:
        nb_sols = 0
        for i in range(n + 1, 2 * n + 1):
            if (n * i) % abs(i - n) == 0:
                nb_sols += 1
        print(n, nb_sols)
        if nb_sols > 1000:
            return n
        else:
            n += 1
