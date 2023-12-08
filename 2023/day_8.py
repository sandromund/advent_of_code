"""
--- Day 8: Haunted Wasteland ---

"""


def read_data(path):
    mapping = {}
    instructions = None
    for line in open(path):
        line = line.replace("\n", "")
        if len(line) < 1:
            continue
        elif "=" in line:
            key = line.split("=")[0].strip()
            left = line.split("=")[-1].split(",")[0].replace("(", "").strip()
            right = line.split("=")[-1].split(",")[-1].replace(")", "").strip()
            mapping[key] = (left, right)
        else:
            if instructions is not None:
                raise ValueError
            instructions = list(line)
    return instructions, mapping


def day_8_task_1(data):
    instructions, mapping = data
    current_position = "AAA"
    n_steps = 0
    tuple_mapping = {"L": 0, "R": 1}
    while current_position != "ZZZ":
        for direction in instructions:
            current_position = mapping[current_position][tuple_mapping[direction]]
            n_steps += 1
    return n_steps


if __name__ == '__main__':
    assert day_8_task_1(read_data(path="data/day_8_demo_1.txt")) == 2
    assert day_8_task_1(read_data(path="data/day_8_demo_2.txt")) == 6
    assert day_8_task_1(read_data(path="data/day_8.txt")) == 15989
