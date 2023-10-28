def _check_row(i, j, grid):
    for k in range(9):
        if grid[i][j] == grid[i][k] and j != k:
            return False
    return True


def _check_col(i, j, grid):
    for k in range(9):
        if grid[i][j] == grid[k][j] and i != k:
            return False
    return True


def _check_square(i, j, grid):
    for k in range(9):
        if grid[k % 3 + 3 * (i // 3)][k // 3 + 3 * (j // 3)] == grid[i][j] and (i != k % 3 + 3 * (i // 3) or j != k // 3 + 3 * (j // 3)):
            return False
    return True


def _next(i, j):
    if i == 8 and j == 8:
        raise ValueError
    elif j == 8:
        return i + 1, 0
    else:
        return i, j + 1


def main():
    with open("./Data/p096_sudoku.txt") as f:
        lines = f.read().splitlines()

    print(lines)
    grids = []
    for i in range(50):
        grids.append([[int(char) for char in line] for line in lines[10 * i + 1: 10 * (i + 1)]])

    print(grids)
    total = 0

    for grid in grids:

        def _backtrack(a, b):
            try:
                next_a, next_b = _next(a, b)
            except ValueError:
                if _check_col(a, b, grid) and _check_square(a, b, grid) and _check_row(a, b, grid):
                    print(grid)
                    return 100 * grid[0][0] + 10 * grid[0][1] + grid[0][2]
                else:
                    return 0
            if grid[a][b] != 0:
                return _backtrack(next_a, next_b)
            else:
                result = 0
                for k in range(1, 10):
                    grid[a][b] = k
                    if grid[0][0] == 4 and grid[0][1] == 8 and grid[0][2] == 3 and grid[0][3] == 9:
                        print(1)
                    if _check_col(a, b, grid) and _check_square(a, b, grid) and _check_row(a, b, grid):
                        result += _backtrack(next_a, next_b)
                    if result > 0:
                        return result
                grid[a][b] = 0
                return result

        total += _backtrack(0, 0)
    return total
