from collections import Counter

from functools import cmp_to_key


def read_data(path):
    result = []
    for line in open(path):
        line = line.replace("\n", "")
        cards, number = line.split(" ")
        result.append((cards, int(number)))
    return result


def hand_score(hand):
    """
    """
    c = Counter(hand)

    m = max(c.values())

    #     Five of a kind, where all five cards have the same label
    if m == 5:
        return 7

    #     Four of a kind, where four cards have the same label and one card has a different label
    if m == 4:
        return 6

    #    Full house, where three cards have the same label, and the remaining two cards share a different label
    if m == 3 and m - 1 in c.values():
        return 5

    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand
    if m == 3:
        return 4

    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label
    if m == 2 and list(c.values()).count(2) == 2:
        return 3

    if m == 2:
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other
        return 2

    # High card, where all cards' labels are distinct
    return 1


def get_mapper():
    symbols = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")[::-1]
    return {symbols[i]: i for i in range(len(symbols))}


def high_card_old(h1, h2):
    n = len(h1)
    sum_h1 = sum([MAPPER[h1[i]] for i in range(n)])
    sum_h2 = sum([MAPPER[h2[i]] for i in range(n)])
    if sum_h1 > sum_h2:
        return -1
    if sum_h1 < sum_h2:
        return 1


def high_card(h1, h2):
    for i in range(len(h1)):
        if MAPPER[h1[i]] > MAPPER[h2[i]]:
            return -1
        if MAPPER[h1[i]] < MAPPER[h2[i]]:
            return 1
    return 1


def compare(hand_1, hand_2):
    h1, h2 = hand_1[0], hand_2[0]
    s1 = hand_score(h1)
    s2 = hand_score(h2)
    if s1 > s2:
        return -1
    if s1 < s2:
        return 1
    return high_card(h1, h2)


def day_7_task_1(data):
    sorted_data = sorted(data, key=cmp_to_key(compare), reverse=True)
    print(sorted_data)
    result = 0
    for i in range(len(data)):
        result += sorted_data[i][1] * (i + 1)
    return result


MAPPER = get_mapper()

if __name__ == '__main__':
    assert hand_score("AAAAA") == 7
    assert hand_score("AA8AA") == 6
    assert hand_score("23332") == 5
    assert hand_score("TTT98") == 4
    assert hand_score("23432") == 3
    assert hand_score("A23A4") == 2
    assert hand_score("32T4K") == 1

    assert day_7_task_1(read_data("data/day_7_demo.txt")) == 6440
    assert day_7_task_1(read_data("data/day_7.txt")) == 253933213
