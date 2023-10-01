def set_house_received_present(data_string):
    x, y = 0, 0  # current_position
    visited_positions = {(x, y)}
    for direction in data_string:
        if direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        elif direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        else:
            raise ValueError
        visited_positions.add((x, y))
    return visited_positions


def n_house_received_present(data_string):
    return len(set_house_received_present(data_string))


def read_data(data_path):
    with open(data_path, "r") as f:
        return f.read()


def day_3_task_2(data_string):
    santa = set_house_received_present(data_string=data_string[1:][::2])
    robot = set_house_received_present(data_string=data_string[::2])
    return len(santa.union(robot))


if __name__ == '__main__':
    assert 2 == n_house_received_present(data_string=">")
    assert 4 == n_house_received_present(data_string="^>v<")
    assert 2 == n_house_received_present(data_string="^v^v^v^v^v")

    data_day_3 = read_data(data_path="data/day_3.txt")

    assert 2592 == n_house_received_present(data_string=data_day_3)

    assert 3 == day_3_task_2(data_string="^v")
    assert 3 == day_3_task_2(data_string="^>v<")
    assert 11 == day_3_task_2(data_string="^v^v^v^v^v")

    assert 2360 == day_3_task_2(data_string=data_day_3)
