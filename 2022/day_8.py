import numpy as np
import matplotlib.pyplot as plt


def read_data(path):
    d = []
    for line in open(path):
        d.append(list(map(int, list(line[:-1]))))
    return np.array(d)


def plot_2d(array):
    plt.imshow(array)
    plt.show()


def plot_3d(array):
    n, m = array.shape
    x = np.array([[i for i in range(m)] for _ in range(n)]).flatten()
    y = np.array([[i] * m for i in range(n)]).flatten()
    z = array.flatten()
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot_trisurf(x, y, z, cmap=plt.cm.jet)
    plt.show()


def is_visible(x, y, array):
    n, m = array.shape
    v = array[x][y]

    is_visible_top = True
    for i in range(x - 1, -1, -1):
        w = array[i][y]
        if w >= v:
            is_visible_top = False
            break
    if is_visible_top:
        return True
    is_visible_down = True
    for i in range(x + 1, n):
        w = array[i][y]
        if w >= v:
            is_visible_down = False
            break
    if is_visible_down:
        return True
    is_visible_left = True
    for j in range(y - 1, -1, -1):
        w = array[x][j]
        if w >= v:
            is_visible_left = False
            break
    if is_visible_left:
        return True
    is_visible_right = True
    for j in range(y + 1, m):
        w = array[x][j]
        if w >= v:
            is_visible_right = False
            break
    if is_visible_right:
        return True
    return False


def day_8_task_1(array):
    n_visible = 0
    n, m = array.shape
    for x in range(n):
        for y in range(m):
            if is_visible(x, y, array):
                n_visible += 1
    return n_visible


def scenic_score(x, y, array):
    n, m = array.shape
    v = array[x][y]

    n_visible_top = 0
    for i in range(x - 1, -1, -1):
        w = array[i][y]
        n_visible_top += 1
        if w >= v:
            break

    n_visible_down = 0
    for i in range(x + 1, n):
        n_visible_down += 1
        w = array[i][y]
        if w >= v:
            break

    n_visible_left = 0
    for j in range(y - 1, -1, -1):
        n_visible_left += 1
        w = array[x][j]
        if w >= v:
            break

    n_visible_right = 0
    for j in range(y + 1, m):
        n_visible_right += 1
        w = array[x][j]
        if w >= v:
            break

    return n_visible_top * n_visible_down * n_visible_left * n_visible_right


def day_8_task_2(array):
    max_scenic_score = None
    n, m = array.shape
    for x in range(n):
        for y in range(m):
            s = scenic_score(x, y, array)
            if max_scenic_score is None or s > max_scenic_score:
                max_scenic_score = s
    return max_scenic_score


if __name__ == '__main__':
    assert day_8_task_1(read_data(path="data/day8_test.txt")) == 21
    assert day_8_task_1(read_data(path="data/day8.txt")) == 1827
    assert day_8_task_2(read_data(path="data/day8_test.txt")) == 8
    assert day_8_task_2(read_data(path="data/day8.txt")) == 335580
