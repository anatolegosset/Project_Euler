from collections import Counter


def main():
    initial = (1, 1, 1, 1)
    current_count = Counter()
    current_count[initial] += 1
    all_counts = [current_count]
    for i in range(14):
        new_count = Counter()
        for setup, count in current_count.items():
            for j, k in enumerate(setup):
                if k == 0:
                    continue
                new_setup = list(setup)
                new_setup[j] -= 1
                for m in range(j + 1, 4):
                    new_setup[m] += 1
                new_count[tuple(new_setup)] += k * count / sum(setup)
        all_counts.append(new_count)
        current_count = new_count
    print(all_counts)
    probabilities = []
    for step in all_counts:
        nb_with_just_one = 0
        nb_total = 0
        for setup, count in step.items():
            if sum(setup) == 1:
                nb_with_just_one += count
            nb_total += count
        probabilities.append((nb_with_just_one, nb_total))
    print(probabilities)
    print(sum(x / y for x, y in probabilities[:-1]))


if __name__ == "__main__":
    main()
