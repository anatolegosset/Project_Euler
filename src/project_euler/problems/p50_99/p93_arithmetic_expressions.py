from src.project_euler.lib import (
    generate_permutation,
    generate_cartesian_product,
    concat_ints,
)


def _mul(x, y):
    return x * y


def _add(x, y):
    return x + y


def _sub(x, y):
    return x - y


def _div(x, y):
    if y == 0:
        raise ValueError
    if x % y == 0:
        return x // y
    return x / y


def _compose_apply(function, permutation, variable_dict):
    try:
        innermost_value = function[2](
            variable_dict[permutation[2]], variable_dict[permutation[3]]
        )
    except ValueError:
        return set()

    if function[1] in [_sub, _div]:
        possible_values1 = []
        try:
            possible_values1.append(
                function[1](variable_dict[permutation[1]], innermost_value)
            )
        except ValueError:
            pass
        try:
            possible_values1.append(
                function[1](innermost_value, variable_dict[permutation[1]])
            )
        except ValueError:
            pass
    else:
        possible_values1 = [function[1](variable_dict[permutation[1]], innermost_value)]

    possible_results = []
    for possible_value in possible_values1:
        if function[0] in [_sub, _div]:
            try:
                possible_results.append(
                    function[0](variable_dict[permutation[0]], possible_value)
                )
            except ValueError:
                pass
            try:
                possible_results.append(
                    function[0](possible_value, variable_dict[permutation[0]])
                )
            except ValueError:
                pass
        else:
            possible_results.append(
                function[0](variable_dict[permutation[0]], possible_value)
            )

    return set(possible_results)


def main():
    operations = [_add, _sub, _mul, _div]
    functions = generate_cartesian_product(operations, 3)
    permutations = generate_permutation(range(4))

    current_max = 0
    best_abcd = ""
    for a in range(10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    variable_dict = {0: a, 1: b, 2: c, 3: d}
                    possible_values = set()
                    for function in functions:
                        if function[0] == _div:
                            print(1)
                        for permutation in permutations:
                            try:
                                possible_results = _compose_apply(
                                    function, permutation, variable_dict
                                )
                                for k in possible_results:
                                    if 0 < k == int(k):
                                        possible_values.add(k)
                            except ValueError:
                                pass
                    possible_values = sorted(list(possible_values))
                    nb_possible_values = 0
                    for i, value in enumerate(possible_values):
                        if value != i + 1:
                            break
                        nb_possible_values += 1

                    if nb_possible_values > current_max:
                        current_max = nb_possible_values
                        best_abcd = str(concat_ints([a, b, c, d]))
                        print(nb_possible_values, a, b, c, d)
    return best_abcd
