from project_euler.lib import gen_subsets

simple = """90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct"""

hard = """5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct"""


def process(input_data: str):
    data = [
        ([int(k) for k in x.split()[0]], int(x.split()[1].strip(";")))
        for x in input_data.splitlines()
    ]
    data.sort(key=lambda x: x[1])
    return data


def main():
    data = process(hard)
    length = len(data[0][0])
    disallowed = [[0 for _ in range(10)] for _ in range(length)]
    forced = [-1 for _ in range(length)]

    def rec(depth: int):
        if depth == len(data):
            print(forced)
            raise ValueError()
        sequence, target_score = data[depth]
        nb_forced = sum(c == forced_digit for c, forced_digit in zip(sequence, forced))
        if nb_forced > target_score:
            return
        target_score -= nb_forced
        allowed = [
            i
            for i in range(length)
            if not disallowed[i][sequence[i]] and forced[i] == -1
        ]
        if len(allowed) < target_score:
            return
        for subset in gen_subsets(allowed, target_score):
            if depth <= 2:
                print(forced)
            for i in allowed:
                if i in subset:
                    forced[i] = sequence[i]
                else:
                    disallowed[i][sequence[i]] += 1
            rec(depth + 1)
            for i in allowed:
                if i in subset:
                    forced[i] = -1
                else:
                    disallowed[i][sequence[i]] -= 1

    rec(0)


def check(sequence: list[int]):
    data = process(hard)
    for ref, score in data:
        actual = sum(i == j for i, j in zip(sequence, ref))
        if actual != score:
            print(ref, sequence, score, actual)
            return False
    return True


if __name__ == "__main__":
    # for i in range(10):
    #     pouet = [4, 6, 4, 0, 2, 6, 1, 5, 7, 1, 8, 4, i, 5, 3, 3]
    #     if check(pouet):
    #         print("".join(str(i) for i in pouet))
    main()
