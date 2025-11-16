from src.project_euler.lib import (
    quadratic_auto_solver,
    generate_primes_under,
    fast_is_prime,
)


def _vertical_quadratic(ring_nb):
    if ring_nb == -1:
        return 1
    return 2 + 6 * ring_nb * (ring_nb + 1) // 2


def _find_ring_nb(n):
    return int(quadratic_auto_solver(lambda x: 2 + 6 * x * (x + 1) // 2, n)[-1])


def _find_side(n):
    ring_nb = _find_ring_nb(n)
    return (n - _vertical_quadratic(ring_nb)) // (ring_nb + 1)


def _find_coordinates(n):
    ring_nb = int(quadratic_auto_solver(lambda x: 2 + 6 * x * (x + 1) // 2, n)[-1])
    circular_nb = n - _vertical_quadratic(ring_nb)
    return ring_nb, circular_nb // (ring_nb + 1), circular_nb % (ring_nb + 1)


def _value_from_coordinates(ring_nb, side, left):
    if ring_nb == -1:
        return 1
    return _vertical_quadratic(ring_nb) + (ring_nb + 1) * side + left


def _neighbours(n):
    ring_nb, side, left = _find_coordinates(n)
    neighbours = []
    if side == 0 and left == 0:
        neighbours.append(_vertical_quadratic(ring_nb - 1))
        neighbours.append(_vertical_quadratic(ring_nb + 1))
        neighbours.append(_vertical_quadratic(ring_nb + 1) + 1)
        neighbours.append(_vertical_quadratic(ring_nb + 1) - 1)
        neighbours.append(_vertical_quadratic(ring_nb + 2) - 1)
        neighbours.append(n + 1)
    elif side == 5 and left == ring_nb:
        neighbours.append(n - 1)
        neighbours.append(_vertical_quadratic(ring_nb - 1))
        neighbours.append(_vertical_quadratic(ring_nb))
        neighbours.append(_vertical_quadratic(ring_nb) - 1)
        neighbours.append(_value_from_coordinates(ring_nb + 1, side, left))
        neighbours.append(_value_from_coordinates(ring_nb + 1, side, left + 1))
    elif left == 0:
        neighbours.append(n + 1)
        neighbours.append(n - 1)
        neighbours.append(_value_from_coordinates(ring_nb - 1, side, 0))
        neighbours.append(_value_from_coordinates(ring_nb + 1, side, 0))
        neighbours.append(_value_from_coordinates(ring_nb + 1, side, 1))
        neighbours.append(_value_from_coordinates(ring_nb + 1, side - 1, ring_nb + 1))
    else:
        pass
    return neighbours


def main(max_n=200_000_000_000):
    primes = generate_primes_under(max_n, under_root=True)
    valid_tiles = [1, 2]
    for ring_nb in range(1, _find_ring_nb(max_n) - 1):
        for side in range(6):
            value = _value_from_coordinates(ring_nb, side, 0)
            neighbours = _neighbours(value)
            nb_prime_differences = 0
            for neighbour in neighbours:
                if fast_is_prime(abs(neighbour - value), primes):
                    nb_prime_differences += 1
            if nb_prime_differences == 3:
                valid_tiles.append(value)
        value = _value_from_coordinates(ring_nb, 5, ring_nb)
        neighbours = _neighbours(value)
        nb_prime_differences = 0
        for neighbour in neighbours:
            if fast_is_prime(abs(neighbour - value), primes):
                nb_prime_differences += 1
        if nb_prime_differences == 3:
            valid_tiles.append(value)
        if len(valid_tiles) >= 2000:
            break
    print(len(valid_tiles), valid_tiles)
    try:
        return valid_tiles[1999]
    except IndexError:
        print(f"{max_n=} is too low to find 2000th valid number")
