import matplotlib.pyplot as plt
import numpy as np


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


if __name__ == '__main__':
    assert day_18_example(make_plot=True) == 64
    assert day_18_task_1() == 4474
