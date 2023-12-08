import math


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


def day_8_task_2_brute_force(data):
    instructions, mapping = data
    current_positions = [start for start in mapping.keys() if start.endswith("A")]
    n = len(current_positions)
    n_steps = 0
    tuple_mapping = {"L": 0, "R": 1}
    while n != len([p for p in current_positions if p.endswith("Z")]):
        for direction in instructions:
            for i in range(n):
                c = current_positions[i]
                current_positions[i] = mapping[current_positions[i]][tuple_mapping[direction]]
                print(c, "->", current_positions[i])
            n_steps += 1
    return n_steps


def day_8_task_2(data):
    instructions, mapping = data
    current_positions = [start for start in mapping.keys() if start.endswith("A")]
    tuple_mapping = {"L": 0, "R": 1}
    solutions = []
    for current_position in current_positions:
        n_steps = 0
        while not current_position.endswith("Z"):
            for direction in instructions:
                current_position = mapping[current_position][tuple_mapping[direction]]
                n_steps += 1
        solutions.append(n_steps)
    return math.lcm(*solutions)


if __name__ == '__main__':
    assert day_8_task_1(read_data(path="data/day_8_demo_1.txt")) == 2
    assert day_8_task_1(read_data(path="data/day_8_demo_2.txt")) == 6
    assert day_8_task_1(read_data(path="data/day_8.txt")) == 15989
    assert day_8_task_2(read_data(path="data/day_8_demo_3.txt")) == 6
    assert day_8_task_2(read_data(path="data/day_8.txt")) == 13830919117339
