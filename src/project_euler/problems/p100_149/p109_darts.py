def main():
    singles = [(1, i) for i in range(1, 21)]
    singles.append((1, 25))
    doubles = [(2, i * 2) for i in range(1, 21)]
    doubles.append((2, 50))
    trebles = [(3, i * 3) for i in range(1, 21)]
    all_shots = sorted(singles + doubles + trebles)
    totals = [0] * 100
    subsets = [[]]
    for i, shot2 in enumerate(all_shots):
        subsets.append([shot2])
        for shot1 in all_shots[i:]:
            subsets.append([shot1, shot2])

    print(subsets)

    for a, value3 in doubles:
        for subset in subsets:
            total = value3
            for _, value in subset:
                total += value
            if total < 100:
                totals[total] += 1
                if total == 6:
                    print(a, value3, subset)
    print(totals[6])
    return sum(totals)
