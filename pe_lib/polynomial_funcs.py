import math


def quadratic_auto_solver(quadratic, value=0):
    """
    :param quadratic: a quadratic function (with integer coefficients
    :param value: solves quadratic(x) == value
    :return: a list of roots
    """

    c = quadratic(0) - value
    a = (quadratic(1) + quadratic(-1)) // 2 - quadratic(0)
    b = (quadratic(1) - quadratic(-1)) // 2
    disc_sq = b * b - 4 * a * c
    if disc_sq < 0:
        return []
    elif disc_sq == 0:
        return [-1 * b / (2 * a)]
    else:
        return [(-1 * b - math.sqrt(disc_sq)) / (2 * a), (-1 * b + math.sqrt(disc_sq)) / (2 * a)]

