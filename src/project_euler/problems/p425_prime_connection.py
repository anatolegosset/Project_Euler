from collections import deque

from project_euler.lib import generate_primes_under, nb_digits


def find_connected(k: int, primes: set[int]) -> list[int]:
    nb_digit = nb_digits(k)
    output = []
    power_10 = 10 ** (nb_digit - 1)
    first_digit, rem = divmod(k, power_10)
    if rem in primes and rem // (power_10 // 10) > 0:
        output.append(rem)
    for i in range(power_10, first_digit * power_10, power_10):
        if i + rem in primes:
            output.append(i + rem)
    while power_10 > 1:
        digit = k % power_10
        power_10 //= 10
        digit //= power_10
        base = k - digit * power_10
        for i in range(0, digit * power_10, power_10):
            if base + i in primes:
                output.append(base + i)
    return output


def main(n: int):
    primes = generate_primes_under(n, under_root=False)
    primes_set = set(primes)
    graph = {p: [] for p in primes}
    for p in primes:
        for other_p in find_connected(p, primes_set):
            graph[p].append(other_p)
            graph[other_p].append(p)
    min_max = {prime: n for prime in primes}
    min_max[2] = 2
    queue = deque([2])
    while queue:
        current = queue.popleft()
        for potential_next in graph[current]:
            if min_max[potential_next] > max(min_max[current], potential_next):
                queue.append(potential_next)
                min_max[potential_next] = max(min_max[current], potential_next)
    print(sum(p for p, min_max in min_max.items() if p < min_max))


if __name__ == "__main__":
    main(10_000_000)
