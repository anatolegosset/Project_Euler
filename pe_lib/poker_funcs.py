card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,
              "A": 14}
from collections import Counter


def hand_number_list(hand_list):
    return sorted([card_value[card[0]] for card in hand_list])


def straight(hand_list):
    number_list = hand_number_list(hand_list)
    initial_number = number_list[0]
    for i in range(1, 5):
        if initial_number + i != number_list[i]:
            return False, 0
    return True, number_list[0]


def is_flush(hand_list):
    return len(set([card[1] for card in hand_list])) == 1


def pairs(hand_list):
    number_counter = Counter(hand_number_list(hand_list))
    result = []
    for value in number_counter:
        if number_counter[value] == 2:
            result.append(value)
    return sorted(result)


def three_or_four(hand_list):
    number_counter = Counter(hand_number_list(hand_list))
    for value in number_counter:
        if number_counter[value] == 3 or number_counter[value] == 4:
            return number_counter[value], value
    return 0, 0


def rank(hand_list):
    if straight(hand_list)[0] and is_flush(hand_list):
        return 0, straight(hand_list)[1]
    if three_or_four(hand_list)[0] == 4:
        return 1, three_or_four(hand_list)[1]
    if three_or_four(hand_list)[0] == 3 and pairs(hand_list):
        return 2, three_or_four(hand_list)[1]
    if is_flush(hand_list):
        return 3, 0
    if straight(hand_list)[0]:
        return 4, straight(hand_list)[1]
    if three_or_four(hand_list)[0] == 3:
        return 5, three_or_four(hand_list)[1]
    if len(pairs(hand_list)) == 2:
        return 6, pairs(hand_list)[0], pairs(hand_list)[1]
    if pairs(hand_list):
        return 7, pairs(hand_list)[0]
    return 8, hand_number_list(hand_list)[4]


class PokerHand:
    def __init__(self, hand_str="5H 5C 6S 7S KD"):
        self.cards = hand_str.split(" ")
        self.hand_number_list = hand_number_list(self.cards)
        self.rank = rank(self.cards)

    def beats(self, other_hand):
        if self.rank[0] != other_hand.rank[0]:
            return self.rank[0] < other_hand.rank[0]
        elif self.rank[1] != other_hand.rank[1]:
            return self.rank[1] > other_hand.rank[1]
        else:
            for i in range(4, -1, -1):
                if self.hand_number_list[i] != other_hand.hand_number_list[i]:
                    return self.hand_number_list[i] > other_hand.hand_number_list[i]
        raise ValueError
