def is_nice_string(data_string) -> bool:
    for forbidden_string in ["ab", "cd", "pq", "xy"]:
        if forbidden_string in data_string:
            return False
    n_vowels = 0
    vowels = set(list("aeiou"))
    last_letter = None
    letter_appears_twice_in_row = False
    for char in data_string:
        if char in vowels:
            n_vowels += 1
        if char is not None and last_letter == char:
            letter_appears_twice_in_row = True
        last_letter = char
    if letter_appears_twice_in_row and n_vowels > 2:
        return True
    return False


def read_data(data_path):
    with open(data_path, "r") as f:
        return f.readlines()


def day_5_task_1(data):
    return sum([is_nice_string(data_string) for data_string in data])


def is_nice_new_rules(data_string) -> bool:
    has_pair = False
    n = len(data_string)
    seen_pairs = dict()
    has_repeated_letter = False
    for i in range(n):
        if (not has_pair) and (0 < i < n):
            pair = (data_string[i - 1], data_string[i])
            if (pair in seen_pairs) and (seen_pairs.get(pair) < i - 1):
                if has_repeated_letter:
                    return True
                has_pair = True
            seen_pairs[pair] = i
        if (not has_repeated_letter) and (i > 1) and data_string[i - 2] == data_string[i]:
            if has_pair:
                return True
            has_repeated_letter = True
    return has_pair and has_repeated_letter


def day_5_task_2(data):
    return sum([is_nice_new_rules(data_string) for data_string in data])


if __name__ == '__main__':
    assert is_nice_string("ugknbfddgicrmopn")
    assert is_nice_string("aaa")
    assert is_nice_string("jchzalrnumimnmhp") is False
    assert is_nice_string("haegwjzuvuyypxyu") is False
    assert is_nice_string("dvszwmarrgswjxmb") is False

    data_day_5 = read_data(data_path="data/day_5.txt")

    assert 258 == day_5_task_1(data_day_5)

    assert is_nice_new_rules(data_string="qjhvhtzxzqqjkmpb")
    assert is_nice_new_rules(data_string="xxyxx")
    assert is_nice_new_rules(data_string="uurcxstgmygtbstg") is False
    assert is_nice_new_rules(data_string="ieodomkazucvgmuy") is False

    assert 53 == day_5_task_2(data=data_day_5)
