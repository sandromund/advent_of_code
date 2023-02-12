import numpy as np
import matplotlib.pyplot as plt


class Cave:

    def __init__(self, path):
        self.cave = np.zeros(shape=(600, 600), dtype=int)
        self.max_y = None
        self.spawn = 500, 0  # The sand is pouring into the cave from point
        self.stone_encoding = 10
        self.sand_encoding = 5
        self.__load_data(path)

    def __read_line(self, line):
        if "\n" in line:
            line = line.replace("\n", "")
        points = line.split(" -> ")
        line_points = []
        for point in points:
            x, y = list(map(int, point.split(",")))
            line_points.append((x, y))
            if self.max_y is None or y > self.max_y:
                self.max_y = y
        return line_points

    def __load_data(self, path):
        for line in open(path):
            points = self.__read_line(line)
            for i in range(len(points) - 1):
                start_point_x, start_point_y = points[i]
                end_point_x, end_point_y = points[i + 1]
                if start_point_x <= end_point_x:
                    for x in range(start_point_x, end_point_x + 1):
                        self.cave[start_point_y][x] = self.stone_encoding
                else:
                    for x in range(start_point_x, end_point_x - 1, -1):
                        self.cave[start_point_y][x] = self.stone_encoding
                if start_point_y <= end_point_y:
                    for y in range(start_point_y, end_point_y + 1):
                        self.cave[y][start_point_x] = self.stone_encoding
                else:
                    for y in range(start_point_y, end_point_y - 1, -1):
                        self.cave[y][start_point_x] = self.stone_encoding

    def plot(self):
        plt.imshow(self.cave)
        plt.show()

    def sand_fall_down(self) -> int:
        m, n = self.cave.shape
        n_sand = -1
        while True:
            n_sand += 1
            x, y = self.spawn
            while True:
                if not (0 <= x < m - 1 and 0 <= y < n - 1):
                    return n_sand

                if self.cave[y + 1][x] == 0:  # try fall down
                    y = y + 1
                else:
                    if self.cave[y + 1][x - 1] == 0:  # try fall to the left
                        x, y = x - 1, y + 1
                    elif self.cave[y + 1][x + 1] == 0:  # try fall to the right
                        x, y = x + 1, y + 1
                    else:
                        break
            self.cave[y][x] = self.sand_encoding

    def add_floor(self):
        _, n = self.cave.shape
        y = self.max_y + 2
        for x in range(n):
            self.cave[y][x] = self.stone_encoding

    def task_2(self):
        self.add_floor()
        m, n = self.cave.shape
        n_sand = -1
        while True:
            n_sand += 1
            x, y = self.spawn
            while True:

                if y + 1 >= m or not (0 <= x < n and 0 <= y < m):
                    break
                if self.cave[y + 1][x] == 0:  # try fall down
                    y = y + 1
                else:
                    if x - 1 >= 0 and self.cave[y + 1][x - 1] == 0:  # try fall to the left
                        x, y = x - 1, y + 1
                    elif x + 1 < n and self.cave[y + 1][x + 1] == 0:  # try fall to the right
                        x, y = x + 1, y + 1
                    else:
                        break
            self.cave[y][x] = self.sand_encoding
            if (x, y) == self.spawn:
                return np.count_nonzero(self.cave == self.sand_encoding)


if __name__ == '__main__':
    # assert Cave(path="data/day_14_example.txt").sand_fall_down() == 24
    # assert Cave(path="data/day_14.txt").sand_fall_down() == 817
    # assert Cave(path="data/day_14_example.txt").max_y == 9
    print(Cave(path="data/day_14_example.txt").task_2())
    assert Cave(path="data/day_14_example.txt").task_2() == 93

    cave = Cave(path="data/day_14.txt")
    print(cave.task_2())
    cave.plot()
