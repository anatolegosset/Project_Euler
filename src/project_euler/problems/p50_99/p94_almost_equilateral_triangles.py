from src.project_euler.lib import check_gonal


def _is_area_int(a, to_add):
    height_sq = a * a - ((a + to_add) // 2) ** 2
    return check_gonal(height_sq, 4)


def main(max_perimeter=1_000_000_000):
    max_a = max_perimeter // 3 + 2
    total = 0
    for a in range(3, max_a + 1, 2):
        if _is_area_int(a, -1) and 3 * a - 1 <= max_perimeter:
            total += 3 * a - 1
        if _is_area_int(a, 1) and 3 * a + 1 <= max_perimeter:
            total += 3 * a + 1
    print(3 * a + 1)
    return total
