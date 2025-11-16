from src.project_euler.lib import continued_frac_root_expansion


def main(max_n=10000):
    count = 0

    for i in range(max_n + 1):
        temp = continued_frac_root_expansion(i)
        if temp is not None:
            print(temp)
            if temp[3] % 2 == 1:
                count += 1

    return count
