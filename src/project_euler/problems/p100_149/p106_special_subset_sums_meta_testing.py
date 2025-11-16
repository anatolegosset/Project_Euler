from src.project_euler.lib import gen_subsets


def main(n=12):
    subsets = gen_subsets(range(n))
    filtered_subsets = {i: [] for i in range(2, n // 2 + 1)}
    for subset in subsets:
        if 1 < len(subset) <= n // 2:
            filtered_subsets[len(subset)].append(subset)

    total = 0

    for i in filtered_subsets:
        for a, subset1 in enumerate(filtered_subsets[i]):
            set_subset1 = set(subset1)
            for subset2 in filtered_subsets[i][a + 1 :]:
                if set_subset1.intersection(set(subset2)):
                    continue
                flag = True
                sign = subset2[0] - subset1[0]
                for j, k in zip(subset1, subset2):
                    if (k - j) * sign < 0:
                        flag = False
                if flag:
                    continue
                total += 1
                print(subset1, subset2)
    return total
