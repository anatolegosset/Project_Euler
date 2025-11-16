from src.project_euler.lib import generate_primes_under
from collections import Counter


def main(max_n=50_000_000):
    primes = generate_primes_under(max_n, under_root=True)
    counter = Counter()
    for p1 in primes:
        quart = p1**4
        if quart >= max_n:
            break
        for p2 in primes:
            cube = p2**3
            if quart + cube >= max_n:
                break
            for p3 in primes:
                a = quart + cube + p3 * p3
                if a > max_n:
                    break
                counter[a] += 1

    return len(counter.keys())
