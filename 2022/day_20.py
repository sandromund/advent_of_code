import numpy as np


def read_data(path):
    array = []
    for line in open(path):
        array.append(int(line.replace("\n", "")))
    return np.array(array)


def move(index, array):
    array = list(array)
    n = len(array)
    new_index = index + array[index]
    if new_index < 0:
        new_index += n - 1
    elif index >= n:
        new_index -= n
    v = array[index]
    array = array[:index] + array[index + 1:]
    array.insert(new_index, v)
    return array


if __name__ == '__main__':
    # https://adventofcode.com/2022/day/20
    assert move(index=3, array=[4, 5, 6, 1, 7, 8, 9]) == [4, 5, 6, 7, 1, 8, 9]
    assert move(index=1, array=[4, -2, 5, 6, 7, 8, 9]) == [4, 5, 6, 7, 8, -2, 9]
