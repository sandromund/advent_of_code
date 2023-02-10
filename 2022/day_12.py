import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mpl
import networkx as nx
from networkx import NetworkXNoPath


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
    for x, row in enumerate(array):
        for y, col in enumerate(row):
            g.add_node((x, y), size=array[x][y])

    # then we add edges the help us to get to the top
    # nx.set_node_attributes(g, array.flatten(), "height")
    for x, row in enumerate(array):
        for y, col in enumerate(row):
            for neighbor_x, neighbor_y in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= neighbor_x < len(array) and 0 <= neighbor_y < len(row):
                    current_height = array[x][y]
                    neighbor_height = array[neighbor_x][neighbor_y]
                    if current_height == neighbor_height or current_height == neighbor_height - 1 \
                            or current_height > neighbor_height:
                        g.add_edge((x, y), (neighbor_x, neighbor_y))
    g.remove_nodes_from(list(nx.isolates(g)))
    return g


def plot_3d(array):
    n, m = array.shape
    x = np.array([[i for i in range(m)] for _ in range(n)]).flatten()
    y = np.array([[i] * m for i in range(n)]).flatten()
    z = array.flatten()
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot_trisurf(x, y, z, cmap=plt.cm.jet)
    plt.show()


def plot_2d(array):
    mpl.imshow(array)
    mpl.show()


def plot_graph(nx_graph, array):
    color_map = [array[x][y] for x, y in nx_graph]
    nx.draw(nx_graph, with_labels=True, node_color=color_map, cmap=plt.cm.Greens)
    plt.show()


def day_12_example(plots=False):
    data = read_data("data/day12_example.txt")
    g = create_graph(data)
    if plots:
        plot_3d(data)
        plot_2d(data)
        plot_graph(g, data)
    return nx.shortest_path_length(g, source=(0, 0), target=(2, 5))


def day_12_task_1(plots=False):
    data = read_data("data/day12.txt")
    if plots:
        plot_3d(data)
        plot_2d(data)
    g = create_graph(data)
    return nx.shortest_path_length(g, source=(20, 0), target=(20, 40))


def get_goal_pos(data):
    x, y = np.where(data == data.max())
    x, y = x[0], y[0]
    return x, y


def day_12_task_2():
    min_dist = None
    data = read_data("data/day12.txt")
    starting_points = np.where(data < 1)
    g = create_graph(data)
    for x, y in zip(starting_points[0], starting_points[1]):
        try:
            d = nx.shortest_path_length(g, source=(x, y), target=(20, 40))
        except NetworkXNoPath:
            d = None
        if d is not None and (min_dist is None or d < min_dist):
            min_dist = d
    return min_dist


if __name__ == '__main__':
    # We are using the dijkstra algo. here
    assert day_12_example() == 31
    assert day_12_task_1() == 370
    assert day_12_task_2() == 363
    print("day_12_task_1() == 370")
    print("day_12_task_2() == 363")
