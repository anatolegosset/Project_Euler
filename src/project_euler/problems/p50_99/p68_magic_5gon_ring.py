from src.project_euler.lib import generate_permutation, concat_ints


def main():
    possible_starts = [6]

    def start_with(previous_path, elem):
        return previous_path or elem in possible_starts

    def is_10_outer(previous_path, elem):
        return elem != 10 or len(previous_path) % 2 == 0

    def is_start_lower_than_outer(previous_path, elem):
        return (
            (not previous_path)
            or len(previous_path) % 2 == 1
            or elem > previous_path[0]
        )

    def is_magic_for_now(previous_path, elem):
        return (
            len(previous_path) % 2 == 0
            or len(previous_path) < 4
            or (elem + previous_path[-3] == previous_path[-4] + previous_path[-5])
        )

    permutations = generate_permutation(
        range(1, 11),
        constraints=[
            start_with,
            is_10_outer,
            is_start_lower_than_outer,
            is_magic_for_now,
        ],
    )

    current_max = 0
    print(len(permutations))
    for perm in permutations:
        to_concat = []
        for i in range(5):
            to_concat.append(perm[2 * i])
            to_concat.append(perm[2 * i + 1])
            to_concat.append(perm[(2 * i + 3) % (2 * 5)])
        value = concat_ints(to_concat)
        current_max = max(current_max, value)

    return current_max
