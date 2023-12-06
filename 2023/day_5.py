def get_data(path):
    result = {}
    mapping = None
    mappings = []
    for line in open(path):
        line = line.replace("\n", "")
        if "seeds:" in line:
            result["seeds"] = list(map(int, line.split(":")[1].strip().split()))
        elif "map:" in line:
            if mapping is not None:
                result[mapping] = mappings
            mapping = line.replace(" map:", "")
            mappings = []
        else:
            if len(line) > 0:
                drs, srs, rl = line.split()
                mappings.append(
                    {"destination_range_start": int(drs),
                     "source_range_start": int(srs),
                     "range_length": int(rl)}
                )
    if mapping is not None:
        result[mapping] = mappings
    return result


def apply_mapping(number, mappings):
    """

    number : = 79

    mapping := [{'destination_range_start': 50, 'source_range_start': 98, 'range_length': 2},
                {'destination_range_start': 52, 'source_range_start': 50, 'range_length': 48}]

    """
    result = number
    for m in mappings:
        s = m["source_range_start"]
        l = m["range_length"]
        d = m["destination_range_start"]
        if s <= number <= s + l:
            result = number + d - s
    return result


def day_5_task_1(data):
    results = []
    for number in data["seeds"]:
        for mapping_name in ['seed-to-soil',
                             'soil-to-fertilizer',
                             'fertilizer-to-water',
                             'water-to-light',
                             'light-to-temperature',
                             'temperature-to-humidity',
                             'humidity-to-location']:
            number = apply_mapping(number, mappings=data[mapping_name])
            print(mapping_name, "->", number)
        results.append(number)
        print()
    print(results)
    return min(results)


if __name__ == '__main__':
    data_demo = get_data("data/day_5_demo.txt")

    assert apply_mapping(number=79, mappings=data_demo["seed-to-soil"]) == 81
    assert apply_mapping(number=14, mappings=data_demo["seed-to-soil"]) == 14
    assert apply_mapping(number=55, mappings=data_demo["seed-to-soil"]) == 57
    assert apply_mapping(number=13, mappings=data_demo["seed-to-soil"]) == 13

    result_day_5_task_1_demo = day_5_task_1(data_demo)

    assert result_day_5_task_1_demo == 35

    data_day_5 = get_data("data/day_5.txt")
    result_day_5_task_1 = day_5_task_1(data_day_5)

    assert result_day_5_task_1 == 424490994
