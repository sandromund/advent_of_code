from collections import Counter

from functools import cmp_to_key


def read_data(path, transform=False):
    result = []
    for line in open(path):
        line = line.replace("\n", "")
        cards, number = line.split(" ")
        if transform:
            cards = transform_hand(cards)
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
        if TASK == 2:
            if c.get("J") is not None and c.get("J") == 1 or c.get("J") == 4:
                return 7
        return 6

    #    Full house, where three cards have the same label, and the remaining two cards share a different label
    if m == 3 and m - 1 in c.values():
        if TASK == 2:
            if c.get("J") is not None:
                if c.get("J") >= 2:
                    return 7
                if c.get("J") == 1:
                    return 6
        return 5

    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand
    if m == 3:
        if TASK == 2:
            if c.get("J") is not None and c.get("J") == 2:
                return 7
            if c.get("J") is not None and c.get("J") == 3:
                return 6
            if c.get("J") is not None and c.get("J") == 1:
                return 6
        return 4

    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label
    if m == 2 and list(c.values()).count(2) == 2:
        if TASK == 2:
            if c.get("J") is not None and c.get("J") == 1:
                return 4
            if c.get("J") is not None and c.get("J") == 2:
                return 6
        return 3

    if m == 2:
        if TASK == 2:
            if c.get("J") is not None and c.get("J") == 2:
                return 4
            if c.get("J") is not None and c.get("J") == 1:
                return 4
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other
        return 2

    if TASK == 2:
        if c.get("J") is not None and c.get("J") == 1:
            return 2
            # High card, where all cards' labels are distinct
    return 1


def get_mapper():
    symbols = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")[::-1]
    return {symbols[i]: i for i in range(len(symbols))}


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
    result = 0
    for i in range(len(data)):
        result += sorted_data[i][1] * (i + 1)
    return result


def transform_hand(hand):
    while "J" in hand:
        c = Counter(hand.replace("J", ""))
        m = c.most_common()
        if len(m) == 0:
            return hand.replace("J", "A")
        m_max_sym = m[0][0]
        m_max_val = m[0][1]
        candidates = [t[0] for t in m if t[1] == m_max_val]
        hand = hand.replace("J", m_max_sym)
    return hand


MAPPER = get_mapper()

TASK = 1

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

    MAPPER["J"] = -1
    TASK = 2

    assert day_7_task_1(read_data("data/day_7_demo.txt")) == 5905

    print(day_7_task_1(read_data("data/day_7.txt")))

    # answer is too high 253581728, 253589016
    # to low: 253406178,
    # 253295076

    # assert transform_hand("JJJJJ") == "AAAAA"
    # assert transform_hand("JJJJB") == "BBBBB"
    # ssert transform_hand("JJJAB") == "AAAAB"
