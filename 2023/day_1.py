def read_data(path):
    result = []
    for line in open(path):
        result.append(line.replace("\n", ""))
    return result


def task_1(data):
    result = 0
    for line in data:
        result_i = ""
        n = len(line)
        for i in range(n):
            if line[i].isdigit():
                result_i = line[i]
                break
        for i in range(n - 1, -1, -1):
            if line[i].isdigit():
                result_i += line[i]
                break
        assert len(result_i) == 2
        result += int(result_i)
    return result


def task_2(data):
    num_names = "one,two,three,four,five,six,seven,eight,nine".split(",")
    num_values = list(range(1, 10))
    result = 0
    for line in data:
        # check string numbers
        smallest_index_found = None
        first_number = None
        for i in range(len(num_values)):
            num_index = line.find(num_names[i])
            if num_index < 0:
                continue
            if smallest_index_found is None or num_index < smallest_index_found:
                smallest_index_found = num_index
                first_number = num_values[i]
        # check int number
        for i in range(len(line)):
            if line[i].isdigit():
                if smallest_index_found is None or i < smallest_index_found:
                    first_number = line[i]
                    break

        biggest_index_found = None
        second_number = None
        for i in range(len(num_values)):
            num_index = line.rfind(num_names[i])
            if num_index < 0:
                continue
            if biggest_index_found is None or num_index > biggest_index_found:
                biggest_index_found = num_index
                second_number = num_values[i]


        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                if biggest_index_found is None or i > biggest_index_found:
                    second_number = line[i]
                    break
        number = int(str(first_number) + str(second_number))
        result += number
        print(line, "->", number)
    return result


if __name__ == '__main__':
    assert task_1(["1abc2"]) == 12
    assert task_1(["pqr3stu8vwx"]) == 38
    assert task_1(["a1b2c3d4e5f"]) == 15
    assert task_1(["treb7uchet"]) == 77
    assert task_1(read_data("data/day_1_demo.txt")) == 142

    print(task_1(read_data("data/day_1.txt")))  # 52974#

    assert task_2(["two1nine"]) == 29
    assert task_2(["eightwothree"]) == 83
    assert task_2(["abcone2threexyz"]) == 13
    assert task_2(["xtwone3four"]) == 24
    assert task_2(["4nineeightseven2"]) == 42
    assert task_2(["zoneight234"]) == 14
    assert task_2(["7pqrstsixteen"]) == 76

    print(task_2(read_data("data/day_1.txt")))  # 52974#
