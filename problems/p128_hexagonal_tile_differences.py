from pe_lib import compute_gonal, quadratic_auto_solver


def _vertical_quadratic(ring_nb):
    if ring_nb == -1:
        return 1
    else:
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
    else:
        return _vertical_quadratic(ring_nb) + (ring_nb + 1) * side + left


def _nb_prime_differences(n):
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


def main():
    for i in range(2, 50):
        a, b, c = _find_coordinates(i)
        print(i, (a, b, c), _value_from_coordinates(a, b, c))
    print(_find_coordinates(19))
    print(_nb_prime_differences(7))