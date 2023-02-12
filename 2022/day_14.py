import numpy as np
import matplotlib.pyplot as plt


class Cave:

    def __init__(self, path):
        self.cave = np.zeros(shape=(600, 600), dtype=int)
        self.spawn = 500, 0  # The sand is pouring into the cave from point
        self.stone_encoding = 10
        self.sand_encoding = 5
        self.__load_data(path)

    @staticmethod
    def __read_line(line):
        if "\n" in line:
            line = line.replace("\n", "")
        points = line.split(" -> ")
        line_points = []
        for point in points:
            x, y = list(map(int, point.split(",")))
            line_points.append((x, y))
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
        """
        Sand is produced one unit at a time, and the next unit of sand is not produced until the previous
        unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

        A unit of sand always falls down one step if possible. If the tile immediately below is blocked
        (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left.
        If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right.
        Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left,
        then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and
        no longer moves, at which point the next unit of sand is created back at the source.

        """
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


def day_14_example():
    return


if __name__ == '__main__':
    assert Cave(path="data/day_14_example.txt").sand_fall_down() == 24
    assert Cave(path="data/day_14.txt").sand_fall_down() == 817
