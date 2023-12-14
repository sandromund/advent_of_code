import numpy as np
from tqdm import tqdm


def read_data(path):
    result = []
    for line in open(path):
        line = line.replace("\n", "")
        result.append(list(line))
    return result


def iterate(data):
    something_changed = True
    while something_changed:
        something_changed = False
        for row in range(1, len(data)):
            for col in range(len(data[0])):
                if data[row][col] == "O" and data[row - 1][col] == ".":
                    data[row][col], data[row - 1][col] = data[row - 1][col], data[row][col]
                    something_changed = True
    return data


def score(data):
    result = 0
    n = len(data)
    for i in range(n):
        result += data[i].count("O") * (n - i)
    return result


def day_14_task_1(data):
    return score(iterate(data))


def cycle_north(data):
    return iterate(data)


def cycle_south(data):
    something_changed = True
    while something_changed:
        something_changed = False
        for row in range(len(data) - 2, -1, -1):
            for col in range(len(data[0])):
                if data[row][col] == "O" and data[row + 1][col] == ".":
                    data[row][col], data[row + 1][col] = data[row + 1][col], data[row][col]
                    something_changed = True
    return data


def cycle_west(data):
    something_changed = True
    while something_changed:
        something_changed = False
        for row in range(len(data)):
            for col in range(1, len(data[0])):
                if data[row][col] == "O" and data[row][col - 1] == ".":
                    data[row][col], data[row][col - 1] = data[row][col - 1], data[row][col]
                    something_changed = True

    return data


def cycle_east(data):
    something_changed = True
    while something_changed:
        something_changed = False
        for row in range(len(data)):
            for col in range(len(data[0]) - 2, -1, -1):
                if data[row][col] == "O" and data[row][col + 1] == ".":
                    data[row][col], data[row][col + 1] = data[row][col + 1], data[row][col]
                    something_changed = True

    return data


def iterate_cycle(data):
    data = cycle_north(data)
    data = cycle_west(data)
    data = cycle_south(data)
    data = cycle_east(data)
    return data


def p(data):
    print(np.array(data))


def day_14_task_2(data):
    p(data)
    n_cycles = 1_000_000_000
    for i in tqdm(range(n_cycles)):
        data = iterate_cycle(data)
    return score(data)


if __name__ == '__main__':
    data_data_14_demo = read_data(path="data/day_14_demo.txt")
    # assert day_14_task_1(data_data_14_demo) == 136
    # data_data_14 = read_data(path="data/day_14.txt")
    # assert day_14_task_1(data_data_14) == 109385


    day_14_task_2(data_data_14_demo)
