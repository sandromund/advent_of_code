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


def create_graph(array):
    # directed graph
    g = nx.DiGraph()

    # first we create all nodes
    for y, row in enumerate(array):
        for x, col in enumerate(row):
            g.add_node((x, y))

    # then we add edges the help us to get to the top
    nx.set_node_attributes(g, array.flatten(), "height")
    for x, row in enumerate(array):
        for y, col in enumerate(row):
            for neighbor_x, neighbor_y in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= neighbor_x < len(array) and 0 <= neighbor_y < len(row):
                    current_height = array[x][y]
                    neighbor_height = array[neighbor_x][neighbor_y]
                    if current_height == neighbor_height or current_height == neighbor_height - 1:
                        g.add_edge((x, y), (neighbor_x, neighbor_y))
    g.remove_nodes_from(list(nx.isolates(g)))
    return g


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


def plot_graph(nx_graph):
    nx.draw(nx_graph, with_labels=True)
    plt.show()


if __name__ == '__main__':
    data = read_data("data/day12_example.txt")
    # plot_3d(data)
    # plot_2d(data)

    g = create_graph(data)
    plot_graph(g)
