import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from functools import cache


def read_data(path):
    cubes_list = []
    for line in open(path):
        line = line.replace("\n", "")
        x, y, z = list(map(int, line.split(",")))
        cubes_list.append([x, y, z])
    return np.array(cubes_list)


def plot_3d(array):
    k = np.amax(array)
    axes = [k + 1] * 3
    data = np.zeros(axes, dtype=bool)
    for (x, y, z) in array:
        data[x][y][z] = True
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(data, edgecolors='grey')
    plt.show()


def count_not_immediately_connected_sides(cubes):
    cube_set = set(map(tuple, cubes))
    neighbours = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
    k = 0  # not immediately connected to another cube
    for (x, y, z) in cubes:
        for (a, b, c) in neighbours:
            if (x + a, y + b, z + c) not in cube_set:
                k += 1
    return k


def day_18_example(make_plot=False):
    cubes = read_data(path="data/day_18_example.txt")
    if make_plot:
        plot_3d(cubes)
    return count_not_immediately_connected_sides(cubes)


def day_18_task_1(make_plot=False):
    cubes = read_data(path="data/day_18.txt")
    if make_plot:
        plot_3d(cubes)
    return count_not_immediately_connected_sides(cubes)


cubes = read_data(path="data/day_18.txt")
cube_set = set(map(tuple, cubes))
k = np.amax(cubes)
neighbours = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]


@cache
def is_reachable_by_water(cube) -> bool:
    queue = deque([cube])
    already_checked = set()
    while queue:
        cube = x, y, z = queue.pop()
        if cube in already_checked:
            continue
        already_checked.add(cube)
        if cube in cube_set:
            continue
        if any(map(lambda e: e < 0 or e > k, cube)):
            return True
        for (a, b, c) in neighbours:
            queue.append((x + a, y + b, z + c))
    return False


def day_18_task_2():
    result = 0
    for (x, y, z) in cubes:
        for (a, b, c) in neighbours:
            cube = (x + a, y + b, z + c)
            if is_reachable_by_water(cube):
                result += 1
    return result


if __name__ == '__main__':
    assert day_18_example() == 64
    assert day_18_task_1() == 4474
    assert day_18_task_2() == 2518
