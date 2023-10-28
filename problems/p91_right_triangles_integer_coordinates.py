def main(max_coords=50):
    nb_right_triangles = 0
    sols = []
    for x1 in range(max_coords + 1):
        for y1 in range(max_coords + 1):
            if x1 + y1 == 0:
                continue
            for x2 in range(max_coords + 1):
                for y2 in range(max_coords + 1):
                    if x2 + y2 == 0 or (x1 == x2 and y1 == y2):
                        continue
                    if (x1 * x2 + y1 * y2) * (x1 * (x2 - x1) + y1 * (y2 - y1)) * (x2 * (x2 - x1) + y2 * (y2 - y1)) == 0:
                        sols.append((x1, y1, x2, y2))
                        nb_right_triangles += 1

    print(sols)
    return nb_right_triangles // 2


