def plus_reverse(n: int) -> int:
    initial = n
    output = 0
    while n > 0:
        n, r = divmod(n, 10)
        output = output * 10 + r
    return output + initial


def check_reversible(n: int) -> bool:
    if n % 10 == 0:
        return False
    total = plus_reverse(n)
    while total > 0:
        if total % 2 == 0:
            return False
        total //= 10
    return True


def main(n: int):
    return sum(check_reversible(i) for i in range(n))


if __name__ == "__main__":
    print(main(1_000_000_000))
