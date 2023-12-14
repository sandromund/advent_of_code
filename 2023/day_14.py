import numpy as np


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


if __name__ == '__main__':
    data_data_14_demo = read_data(path="data/day_14_demo.txt")

    print(np.matrix(data_data_14_demo))
    print()
    print(np.matrix(iterate(data_data_14_demo)))

    assert day_14_task_1(data_data_14_demo) == 136

    data_data_14 = read_data(path="data/day_14.txt")
    print(day_14_task_1(data_data_14))