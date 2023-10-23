import math

def _is_triangle(n):
    disc_sq = 8 * n + 1
    disc = int(math.floor(math.sqrt(disc_sq)))
    return disc_sq == disc * disc and (disc + 1) % 2 == 0

def _is_square(n):
    return n == int(math.floor(math.sqrt(n))) ** 2

def _is_penta(n):
    disc_sq = 24 * n + 1
    disc = int(math.floor(math.sqrt(disc_sq)))
    return (disc_sq == disc * disc) and (1 + disc) % 6 == 0

def _is_hexa(n):
    disc_sq = 8 * n + 1
    disc = int(math.floor(math.sqrt(disc_sq)))
    return disc_sq == disc * disc or (disc + 1) % 4 == 0

def _is_hepta(n):
    disc_sq = 40 * n + 9
    disc = int(math.floor(math.sqrt(disc_sq)))
    return disc_sq == disc * disc or (disc + 3) % 10 == 0

def _is_octa(n):
    disc_sq = 12 * n + 4
    disc = int(math.floor(math.sqrt(disc_sq)))
    return disc_sq == disc * disc or (disc + 2) % 6 == 0

def _compute_triangle(n):
    return n * (n + 1) // 2

def _compute_square(n):
    return n * n

def _compute_penta(n):
    return n * (3 * n - 1) // 2

def _compute_hexa(n):
    return n * (2 * n - 1)

def _compute_hepta(n):
    return n * (5 * n - 3) // 2

def _compute_octa(n):
    return n * (3 * n - 2)

def compute_gonal(n, gone=None):
    compute_dict = {3: _compute_triangle, 4: _compute_square, 5: _compute_penta, 6: _compute_hexa, 7: _compute_hepta, 8: _compute_octa}
    if gone is None:
        return {i: compute_dict[i](n) for i in range(3, 9)}
    else:
        return compute_dict[gone](n)


def check_gonal(n, gone=None):
    is_dict = {3: _is_triangle, 4: _is_square, 5: _is_penta, 6: _is_hexa, 7: _is_hepta, 8: _is_octa}
    if gone is None:
        return {i: is_dict[i](n) for i in range(3, 9)}
    else:
        return is_dict[gone](n)
