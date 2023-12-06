from itertools import accumulate


def get_data(path):
    result = []
    for line in open(path):
        result.append(list(line.replace("\n", "")))
    return result


def find_numbers(data):
    """
    -> [{'number_start_index': 0, 'number_row_index': 0, 'number_value_string': '467'}, ... ]
    """
    result = []
    for row_i in range(len(data)):
        number_start_index = None
        number_row_index = None
        number_value_string = None
        for col_i in range(len(data[0])):
            element = data[row_i][col_i]
            if str(element).isdigit():
                if number_start_index is None:
                    number_start_index = col_i
                    number_row_index = row_i
                    number_value_string = element
                else:
                    number_value_string += element
            else:
                if number_start_index is not None:
                    result.append({
                        "number_start_index": number_start_index,
                        "number_row_index": number_row_index,
                        "number_value_string": number_value_string
                    })
                    number_start_index = None
                    number_row_index = None
                    number_value_string = None
        if number_start_index is not None:
            result.append({
                "number_start_index": number_start_index,
                "number_row_index": number_row_index,
                "number_value_string": number_value_string
            })
    return result


def get_neighbors(number, data):
    # number := {'number_start_index': 0, 'number_row_index': 0, 'number_value_string': '467'}
    n_rows, n_cols = len(data), len(data[0])
    s = number["number_start_index"]
    r = number["number_row_index"]
    n = len(number["number_value_string"])
    result = []
    if r > 0:
        result += data[r - 1][s:s + n]
    if r + 1 < n_rows:
        result += data[r + 1][s:s + n]
    if s - 1 >= 0:
        result.append(data[r][s - 1])
        if r - 1 >= 0:
            result.append(data[r - 1][s - 1])
        if r + 1 < n_rows:
            result.append(data[r + 1][s - 1])
    if s + n < n_cols:
        result += [data[r][s + n]]
        if r - 1 >= 0:
            result.append(data[r - 1][s + n])
        if r + 1 < n_rows:
            result.append(data[r + 1][s + n])
    return set(result)


def day_3_task_1(data, symbols_set):
    result = 0
    for number in find_numbers(data):
        number_neighbors = get_neighbors(number, data)
        is_part_number = len(symbols_set.intersection(number_neighbors)) > 0
        if is_part_number:
            result += int(number["number_value_string"])
    return result


def get_all_symbols(data, remove_numbers=True):
    s = set()
    for row in data:
        s = s.union(set(row))
    if remove_numbers:
        for number in list(map(str, list(range(0, 10)))):
            if number in s:
                s.remove(number)
    if "." in s:
        s.remove(".")
    return s


def task_1():
    data_demo = get_data("data/day_3_demo.txt")
    symbols_demo = get_all_symbols(data_demo)
    result_day_3_task_1_demo = day_3_task_1(data_demo, symbols_demo)
    assert result_day_3_task_1_demo == 4361

    data_day_3 = get_data("data/day_3.txt")
    symbols = get_all_symbols(data_day_3)
    result_day_3_task_1 = day_3_task_1(data_day_3, symbols)
    assert result_day_3_task_1 == 544664

    assert day_3_task_1([list("....877*..")], symbols) == 877
    assert day_3_task_1([list("....*877..")], symbols) == 877
    assert day_3_task_1([list("....*....."), list(".....877..")], symbols) == 877
    assert day_3_task_1([list(".....877.."), list("....*.....")], symbols) == 877
    assert day_3_task_1([list("........*."), list(".....877..")], symbols) == 877
    assert day_3_task_1([list(".....877.."), list("........*.")], symbols) == 877
    assert day_3_task_1([list("....877*3.")], symbols) == 880
    assert day_3_task_1([list("...3*877..")], symbols) == 880
    assert day_3_task_1([list("...3*....."), list(".....877..")], symbols) == 880
    assert day_3_task_1([list(".....877.."), list("...3*.....")], symbols) == 880
    assert day_3_task_1([list("........*3"), list(".....877..")], symbols) == 880
    assert day_3_task_1([list(".....877.."), list("........*3")], symbols) == 880
    assert day_3_task_1([list("3*3*3*3")], symbols) == 12
    assert day_3_task_1([list("*3*3*3*3"), list("*3*3*3*3")], symbols) == 24
    assert day_3_task_1([list("3*3*3*3"), list("3*3*3*3")], symbols) == 24

    return result_day_3_task_1


def find_gear(number, data):
    # number := {'number_start_index': 0, 'number_row_index': 0, 'number_value_string': '467'}
    n_rows, n_cols = len(data), len(data[0])
    s = number["number_start_index"]
    r = number["number_row_index"]
    n = len(number["number_value_string"])
    result = []
    if r > 0:
        for i in range(s, s + n):
            if data[r - 1][i] == "*":
                result.append((r - 1, i))
    if r + 1 < n_rows:
        for i in range(s, s + n):
            if data[r + 1][i] == "*":
                result.append((r + 1, i))
    if s - 1 >= 0:
        if data[r][s - 1] == "*":
            result.append((r, s - 1))
        if r - 1 >= 0:
            if data[r - 1][s - 1] == "*":
                result.append((r - 1, s - 1))
        if r + 1 < n_rows:
            if data[r + 1][s - 1] == "*":
                result.append((r + 1, s - 1))
    if s + n < n_cols:
        if data[r][s + n] == "*":
            result.append((r, s + n))
        if r - 1 >= 0:
            if data[r - 1][s + n] == "*":
                result.append((r - 1, s + n))
        if r + 1 < n_rows:
            if data[r + 1][s + n] == "*":
                result.append((r + 1, s + n))
    return set(result)


def day_3_task_2(data):
    gear_dict = {}
    for number in find_numbers(data):
        gear_set = find_gear(number, data)
        if len(gear_set) > 0:
            gears = list(gear_set)
            assert len(gears) == 1
            gear = gears[0]
            if gear_dict.get(gear) is None:
                gear_dict[gear] = []
            gear_dict[gear].append(int(number["number_value_string"]))

    result = 0
    # gear_dict = {(1, 3): [467, 35], (4, 3): [617], (8, 5): [755, 598]}
    for gear, numbers_list in gear_dict.items():
        if len(numbers_list) > 1:
            assert len(numbers_list) < 3
            result += list(accumulate(numbers_list, (lambda x, y: x * y)))[-1]
    return result


def task_2():
    assert day_3_task_2(get_data("data/day_3_demo.txt")) == 467835
    assert day_3_task_2(get_data("data/day_3.txt")) == 84495585
    return 84495585


if __name__ == '__main__':
    print(task_1())
    print(task_2())
