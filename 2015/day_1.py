def read_data(txt_file_path):
    with open(txt_file_path, "r") as f:
        return f.read()


def day_1_task_1(data_string):
    """
    ( := floor up
    ) := floor down
    """
    return data_string.count("(") + (data_string.count(")") * -1)


def day_1_task_2(data_string):
    current_floor = 0
    basement = -1
    mapping = {"(": 1, ")": -1}
    for index, bracket in enumerate(data_string):
        current_floor += mapping.get(bracket)
        if current_floor == basement:
            return index + 1


if __name__ == '__main__':
    data = read_data(txt_file_path="data/day_1.txt")
    assert 280 == day_1_task_1(data)
    assert 1 == day_1_task_2(")")
    assert 5 == day_1_task_2("()())")
    assert 1797 == day_1_task_2(data_string=data)
