

def main():
    with open('./Data/0089_roman.txt') as f:
        numerals = f.read().splitlines()

    numerals = [numeral.lstrip('M') for numeral in numerals]
    nb_numeral = len(numerals)
    saved_chars = 0
    print(numerals)
    for i in range(nb_numeral):
        if 'IIII' in numerals[i]:
            saved_chars += 2
        numerals[i] = numerals[i].replace('IIII', 'IV')
    print(numerals)
    for i in range(nb_numeral):
        if 'VIV' in numerals[i]:
            saved_chars += 1
        numerals[i] = numerals[i].replace('VIV', 'IX')
    print(numerals)
    for i in range(nb_numeral):
        if 'XXXX' in numerals[i]:
            saved_chars += 2
        numerals[i] = numerals[i].replace('XXXX', 'XL')
    print(numerals)
    for i in range(nb_numeral):
        if 'LXL' in numerals[i]:
            saved_chars += 1
        numerals[i] = numerals[i].replace('LXL', 'XC')
    print(numerals)
    for i in range(nb_numeral):
        if 'CCCC' in numerals[i]:
            saved_chars += 2
        numerals[i] = numerals[i].replace('CCCC', 'CD')
    print(numerals)
    for i in range(nb_numeral):
        if 'DCD' in numerals[i]:
            saved_chars += 1
        numerals[i] = numerals[i].replace('DCD', 'CM')
    print(numerals)

    return saved_chars
