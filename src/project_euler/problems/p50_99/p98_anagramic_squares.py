import math
from collections import Counter
from src.project_euler.lib import check_gonal


def main():
    with open("./Data/0098_words.txt") as f:
        words = [word.strip('"') for word in f.read().split(",")]

    words_dict = {i: [] for i in range(1, 15)}
    for word in words:
        words_dict[len(word)].append(word)
    print(words_dict)
    anagrams = {i: [] for i in range(1, 10)}
    anagram_perms = {i: [] for i in range(1, 10)}

    for i in range(1, 10):
        for j, word1 in enumerate(words_dict[i]):
            for word2 in words_dict[i][j + 1 :]:
                if Counter(word1) == Counter(word2) and word1 not in [
                    "SHEET",
                    "THESE",
                    "CENTRE",
                    "RECENT",
                    "EXCEPT",
                    "EXPECT",
                    "FORMER",
                    "REFORM",
                ]:
                    anagrams[i].append((word1, word2))
                    if [word2.index(char) for char in word1] not in anagram_perms[i]:
                        anagram_perms[i].append([word2.index(char) for char in word1])

    print(anagrams)
    print(anagram_perms)
    for i in range(1, 10):
        for word1, word2 in anagrams[i]:
            if len(set(word1)) != len(word1):
                print(i, word1, word2)

    largest_square = 0

    for i in range(int(math.sqrt(10**9))):
        square = i * i
        square_str = str(square)
        nb_char = len(square_str)

        if len(set(square_str)) < nb_char:
            continue
        for permutation in anagram_perms[nb_char]:
            permuted = int(
                "".join([square_str[permutation[j]] for j in range(nb_char)])
            )
            if check_gonal(permuted, 4):
                if max(permuted, square) > largest_square and len(str(permuted)) == len(
                    square_str
                ):
                    print(permuted, square)
                    largest_square = max(permuted, square)
    return largest_square
