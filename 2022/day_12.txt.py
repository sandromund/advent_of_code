import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mpl
import networkx as nx


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

if __name__ == '__main__':
    data = read_data("data/day12_example.txt")

    # mpl.imshow(data)
    # mpl.show()
    create_graph(data)

    G = nx.complete_graph(5)
    nx.draw(G)
    plt.show()