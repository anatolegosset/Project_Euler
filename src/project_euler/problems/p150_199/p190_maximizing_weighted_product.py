import math


def compute_product(values: list[float]):
    return math.prod(x**j for j, x in enumerate(values, start=1))


def generate(n: int, nb_rounds: int):
    max_reached = 1
    values = [1] * n
    epsilon = 3 / 16
    flag = False
    for k in range(nb_rounds):
        if not flag:
            epsilon *= 9 / 10
        max_score = max_reached
        max_index = -1
        flag = False
        for i in range(n):
            new_values = values.copy()
            new_values[i] += epsilon
            factor = n / sum(new_values)
            new_values = [x * factor for x in new_values]
            score = compute_product(new_values)
            if score > max_score:
                max_score = score
                max_index = i
        if max_score > max_reached:
            values[max_index] += epsilon
            factor = n / sum(values)
            values = [x * factor for x in values]
            max_reached = max_score
            flag = True
            print(k, "plus", epsilon, max_reached, values)

        for i in range(n):
            new_values = values.copy()
            new_values[i] -= epsilon
            if new_values[i] < 0:
                continue
            factor = n / sum(new_values)
            new_values = [x * factor for x in new_values]
            score = compute_product(new_values)
            if score > max_score:
                max_score = score
                max_index = i
        if max_score > max_reached:
            values[max_index] -= epsilon
            factor = n / sum(values)
            values = [x * factor for x in values]
            max_reached = max_score
            flag = True
            print(k, "minus", epsilon, max_reached, values)
    return math.floor(compute_product(values))


if __name__ == "__main__":
    generate(10, 1000)
    print(sum(generate(i, 1000) for i in range(2, 16)))
