import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
    axes = [k+1]*3
    data = np.zeros(axes, dtype=bool)
    for (x, y, z) in array:
        data[x][y][z] = True
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(data, edgecolors='grey')
    plt.show()


def day_18_example():
    cubes = read_data(path="data/day_18.txt")
    plot_3d(cubes)


if __name__ == '__main__':
    day_18_example()
