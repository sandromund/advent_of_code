import numpy as np


def read_data(path):
    array = []
    for line in open(path):
        array.append(int(line.replace("\n", "")))
    return array


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

    new_indices_list = []
    for i in range(n):
        if (i < index and i < new_index) or (i > index and i > new_index):
            new_indices_list.append(i)
        elif index > i > new_index:
            new_indices_list.append(i + 1)
        elif index < i < new_index:
            new_indices_list.append(i - 1)
        elif index == i:
            new_indices_list.append(new_index)
        elif i == new_index:
            new_indices_list.append(index)
        else:
            print(array, i, index, new_index)
            assert 1 / 0 == 0 / 1

    return array, new_indices_list


def check_new_indices(old_array, new_array, new_indices):
    for old_index, new_index in zip(new_indices, range(len(old_array))):
        assert old_array[old_index] == new_array[new_indices[old_index]]


def day_20_task_example():
    data = read_data(path="data/day_20_example.txt")

    array, indices = data, list(range(len(data)))
    for i in range(len(data)):
        print(i, " Iteration",array,  data[i], "is", array[indices[i]])
        array, indices = move(indices[i], array)


if __name__ == '__main__':
    # https://adventofcode.com/2022/day/20
    assert move(index=3, array=[4, 5, 6, 1, 7, 8, 9])[0] == [4, 5, 6, 7, 1, 8, 9]
    assert move(index=1, array=[4, -2, 5, 6, 7, 8, 9])[0] == [4, 5, 6, 7, 8, -2, 9]

    day_20_task_example()

    exit()
    old_array = [4, 5, 6, 1, 7, 8, 9]
    new_array, new_indices = move(3, old_array)
    print(old_array, new_array, new_indices)
    check_new_indices(old_array, new_array, new_indices)
