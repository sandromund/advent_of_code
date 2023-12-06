def read_data(path):
    """
    -> [{'card_nr': 1, 'winning_numbers': [41, 48, 83, 86, 17], 'drawn_numbers': [83, 86, 6, 31, 17, 9, 48, 53]}, ... ]
    """
    result = []
    for line in open(path):
        line = line.replace("\n", "")
        split_1 = line.split(":")
        assert len(split_1) == 2
        card_nr = int(split_1[0].split()[-1])
        split_2 = split_1[1].split("|")
        assert len(split_2) == 2
        result.append({
            "card_nr": card_nr,
            "winning_numbers": list(map(int, split_2[0].strip().split())),
            "drawn_numbers": list(map(int, split_2[1].strip().split()))})
    return result


def day_4_task_1(data):
    result = 0
    for card in data:
        n = len(set(card["winning_numbers"]).intersection(set(card["drawn_numbers"])))
        if n > 0:
            result += 2 ** (n - 1)
    return result


def task_1():
    data_demo = read_data("data/day_4_demo.txt")
    assert day_4_task_1(data_demo) == 13
    data_day_4 = read_data("data/day_4.txt")
    assert day_4_task_1(data_day_4) == 23441
    return 23441


def day_4_task_2(data):
    result = {}
    for card in data:
        card["matching_numbers"] = len(set(card["winning_numbers"]).intersection(set(card["drawn_numbers"])))
        card["instances"] = 1
    for card in data:
        while card["instances"] > 0:
            for k in range(card["matching_numbers"]):
                index = card["card_nr"]
                data[index + k]["instances"] += 1

            card["instances"] -= 1
            if result.get(card["card_nr"]) is None:
                result[card["card_nr"]] = 0
            result[card["card_nr"]] += 1
    return sum(result.values())


if __name__ == '__main__':
    result_day_4_task_2_demo = day_4_task_2(read_data("data/day_4_demo.txt"))
    assert result_day_4_task_2_demo == 30

    result_day_4_task_2 = day_4_task_2(read_data("data/day_4.txt"))
    assert result_day_4_task_2 == 5923918
