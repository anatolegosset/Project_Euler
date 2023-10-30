from pe_lib import is_palindrome


def main(max_n=100_000_000):
    squares = []
    i = 1
    while i * i < max_n:
        squares.append(i * i)
        i += 1
    palindromic_sums = set()
    for i, square in enumerate(squares):
        current_sum = square
        for j, other_square in enumerate(squares[i + 1:]):
            current_sum += other_square
            if current_sum >= max_n:
                break
            if is_palindrome(current_sum):
                print(current_sum, i + 1, i + 1 + j + 1)
                palindromic_sums.add(current_sum)
    return sum(palindromic_sums)
