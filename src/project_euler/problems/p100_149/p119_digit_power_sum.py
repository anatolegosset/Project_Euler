from src.project_euler.lib import sum_of_digits


def main():
    interesting_numbers = []
    for n in range(2, 100):
        temp_n = 1
        for i in range(9):
            temp_n *= n
            if temp_n > 9 and sum_of_digits(temp_n) == n:
                interesting_numbers.append(temp_n)
    interesting_numbers.sort()
    print(interesting_numbers)
    return interesting_numbers[29]
