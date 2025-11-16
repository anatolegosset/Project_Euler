from src.project_euler.lib import generate_divisors_under


def main(max_n=1_000_000):
    divisors = generate_divisors_under(max_n)
    count = 0
    for n in range(max_n):
        if len(divisors[n]) < 10:
            continue
        solutions = []
        for divisor in divisors[n]:
            num = n // divisor + divisor
            if num % 4 == 0 and num // 4 < divisor:
                solutions.append((divisor - num // 4, divisor, divisor + num // 4))
        if len(solutions) == 10:
            count += 1
    return count
