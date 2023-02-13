import numpy as np


def read_data(path) -> np.array:
    with open(path, 'r') as file:
        single_line_str = file.read().rstrip()
    single_line_str.replace(" ", "")
    array = []
    for symbol in list(single_line_str):
        if symbol == ">":
            array.append(1)
        elif symbol == "<":
            array.append(-1)
        else:
            print(symbol)
            raise ValueError
    return np.array(array)


class Rock:

    def __init__(self, form):
        self.form = form
        self.array = self.__get_array()

    def __str__(self):
        return self.form

    def __get_array(self):
        array = self.form.split("\n")[:-1]
        array = list(map(list, array))
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] == "#":
                    v = 1
                elif array[i][j] == ".":
                    v = 0
                else:
                    raise ValueError
                array[i][j] = v
        return np.array(array)


class Chamber:

    def __init__(self, input_data_path, vertical_chamber_wide):
        self.wide = vertical_chamber_wide
        self.rocks = [
            Rock(form="####\n"),
            Rock(form=".#.\n###\n.#.\n"),
            Rock(form="..#\n..#\n###\n"),
            Rock(form="##\n##\n")]
        self.jets_of_hot_gas = read_data(path=input_data_path)
        self.data = []
        self.current_rock_index = 0
        self.current_rock_points = None

    def print_chamber(self):
        for i in range(len(self.data) - 1, -1, -1):
            line_str = ""
            for number in self.data[i]:
                # if (number, i) in self.current_rock_points:
                #    line_str += " @ "
                if number > 0:
                    line_str += " # "
                else:
                    line_str += " . "
            line_str = "|" + line_str + "|"
            print(line_str)
        print("+---------------------+")

    def spawn_rock(self):
        """
         Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three
         units above the highest rock in the room (or the floor, if there isn't one).
        :return:
        """
        self.current_rock_points = None
        data = []
        # re remove all rows with only zeros:
        for i in range(len(self.data)):
            if len([x for x in self.data[i] if x > 0]) == 0:
                break
            data.append(self.data[i])
        self.data = data

        for _ in range(3):
            self.data.append([0] * self.wide)
        r = self.rocks[self.current_rock_index]
        m, n = r.array.shape
        rock_positions = set()
        for i in range(m):
            line = [0, 0]
            for j in range(n):
                if r.array[i][j] != 0:
                    rx = j + 2
                    ry = len(self.data)
                    line.append(1)
                    rock_positions.add((rx, ry))
                else:
                    line.append(0)
            while len(line) < self.wide:
                line.append(0)
            self.data.append(line)
        self.current_rock_index += 1
        if self.current_rock_index == len(self.rocks):
            self.current_rock_index = 0
        self.current_rock_points = rock_positions

    def move_rock_down(self):
        """
        If a downward movement would cause a falling rock to move into the floor or an already-fallen rock,
        the falling rock stops where it is (having landed on something) and a new rock immediately begins falling.
        """

        # we check if it can move down here
        for x, y in self.current_rock_points:
            if y - 1 < 0 or (self.data[y - 1][x] != 0 and (x, y - 1) not in self.current_rock_points):
                return

        # just move all points down
        for x, y in [(x, y) for x, y in self.current_rock_points]:
            self.data[y][x] = 0
        for x, y in [(x, y - 1) for x, y in self.current_rock_points]:
            self.data[y][x] = 1
        self.current_rock_points = set([(x, y - 1) for x, y in self.current_rock_points])

    def move_rock_left(self):

        # we check if it can move down here
        for x, y in self.current_rock_points:
            if x - 1 < 0 or (self.data[y][x - 1] != 0 and (x - 1, y) not in self.current_rock_points):
                return

        # just move all points left
        for x, y in [(x, y) for x, y in self.current_rock_points]:
            self.data[y][x] = 0
        for x, y in [(x - 1, y) for x, y in self.current_rock_points]:
            self.data[y][x] = 1
        self.current_rock_points = set([(x - 1, y) for x, y in self.current_rock_points])

    def move_rock_right(self):
        # we check if it can move down here
        for x, y in self.current_rock_points:
            if x + 1 >= self.wide or (self.data[y][x + 1] != 0 and (x + 1, y) not in self.current_rock_points):
                return

        # just move all points left
        for x, y in [(x, y) for x, y in self.current_rock_points]:
            self.data[y][x] = 0
        for x, y in [(x + 1, y) for x, y in self.current_rock_points]:
            self.data[y][x] = 1
        self.current_rock_points = set([(x + 1, y) for x, y in self.current_rock_points])

    def run(self):
        pass


def day_17_task_1_example():
    chamber = Chamber(input_data_path="data/day_17_example.txt", vertical_chamber_wide=7)

    chamber.spawn_rock()
    chamber.print_chamber()
    while True:
        arg = input(":")
        if arg == "s":
            chamber.move_rock_down()
        elif arg == "d":
            chamber.move_rock_right()
        elif arg == "a":
            chamber.move_rock_left()
        elif arg == "w":
            chamber.spawn_rock()
        else:
            break
        print(chamber.current_rock_points)
        chamber.print_chamber()


if __name__ == '__main__':
    day_17_task_1_example()
