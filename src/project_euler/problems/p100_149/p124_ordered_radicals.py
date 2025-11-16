from src.project_euler.lib import prime_decomp_under, lprod


def main(max_n=100_000):
    decomps = prime_decomp_under(max_n)
    radicals = sorted(
        [(lprod(decomps[i][1].keys()), decomps[i][0]) for i in range(max_n)]
    )
    return radicals[9999][1]
