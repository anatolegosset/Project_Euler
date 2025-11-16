from math import sqrt


def main(n: int):
    relevant_squares = [i * i for i in range(1, n)]
    squares_set = set(relevant_squares)
    for i, s1 in enumerate(relevant_squares):
        for j, s3 in enumerate(relevant_squares[:i]):
            for k, s2 in enumerate(relevant_squares[(i % 2) : j : 2]):
                if (
                    (s1 + s2 - s3) in squares_set
                    and (s3 - s2) in squares_set
                    and (s1 - s3) in squares_set
                ):
                    x = (s1 + s2) / 2
                    y = (s1 - s2) / 2
                    z = (2 * s3 - s1 - s2) / 2
                    print(x, y, z)
                    break


def check(x, y, z):
    print(x > y > z)
    print(x + y)
    print(x - y)
    print(x + z)
    print(x - z)
    print(y + z)
    print(y - z)
    print(x + y + z)


def is_square(k: int):
    return int(sqrt(k)) ** 2 == k


if __name__ == "__main__":
    # main(1000)
    check(434657, 420968, 150568)
    print(is_square(855625))
    print(is_square(13689))
