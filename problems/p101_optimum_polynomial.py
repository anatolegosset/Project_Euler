def _lagrange(seq):
    degree = len(seq)

    def _polynomial(x):
        result = 0
        for i, yi in enumerate(seq):
            temp_num = 1
            temp_den = 1
            for j in range(degree):
                if i != j:
                    temp_num *= (x - 1 - j)
                    temp_den *= (i - j)
            result += yi * (temp_num // temp_den)
        return result
    return _polynomial


def main():
    sequence = []
    for i in range(1, 14):
        value = 0
        for j in range(5):
            value += (i ** (2 * j) - i ** ((2 * j) + 1))
        value += i ** 10
        sequence.append(value)
    print(sequence)

    total = 0
    for i in range(1, len(sequence)):
        polynomial = _lagrange(sequence[:i])
        interpolated_values = [polynomial(x) for x in range(1, 13)]
        print(interpolated_values)
        for a, b in zip(interpolated_values, sequence):
            if a != b:
                total += a
                print(a, b, total)
                break
    return total
