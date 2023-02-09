import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mpl
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def read_data(path):
    hill = []
    for line in open(path):
        row = list(line)
        if "\n" in row:
            row.remove("\n")
        row = list(map(map_chars_to_int, row))
        hill.append(row)
    return np.array(hill)


def map_chars_to_int(x):
    if x == "S":
        return -1
    if x == "E":
        return 26
    return "abcdefghijklmnopqrstuvwxyz".index(x)


def create_graph(data):
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            print(data[y][x])


def plot_3d(array):
    n, m = array.shape
    x = np.array([[i for i in range(m)] for _ in range(n)]).flatten()
    y = np.array([[i] * m for i in range(n)]).flatten()
    z = array.flatten()

    print(x, y, z, sep="\n")
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot_trisurf(x, y, z, cmap=plt.cm.jet)
    plt.show()


def plot_2d(array):
    mpl.imshow(array)
    mpl.show()

if __name__ == '__main__':
    data = read_data("data/day12.txt")

    # create_graph(data)

    # G = nx.complete_graph(5)
    # nx.draw(G)
    # plt.show()
    plot_2d(data)
