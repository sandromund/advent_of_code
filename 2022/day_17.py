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
                if (number, i) in self.current_rock_points:
                    line_str += " @ "
                elif number > 0:
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
                line.append(r.array[i][j])
                rock_positions.add((j + 2, len(self.data) + m - 1))
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
        invalid_move = False

        if any(map(lambda e: e[1] - 1 < 0, self.current_rock_points)):
            invalid_move = True

        if not invalid_move:
            new_rock_points = set()
            new_data = self.data
            for x, y in self.current_rock_points:
                if (x, y - 1) not in self.current_rock_points and new_data[y - 1][x] != 0:
                    invalid_move = True
                    break
                new_rock_points.add((x, y - 1))
                new_data[y][x] = 0
                new_data[y - 1][x] = 1

            if not invalid_move:
                self.current_rock_points = new_rock_points
                self.data = new_data
            else:
                self.spawn_rock()
        else:
            self.spawn_rock()

    def move_rock_left(self):
        if any(map(lambda e: e[0] - 1 < 0, self.current_rock_points)):
            return
        new_rock_points = set()
        new_data = self.data
        for x, y in sorted(list(self.current_rock_points)):
            new_position = (x - 1, y)
            if new_position not in self.current_rock_points and new_data[y][x - 1] != 0:
                return
            new_rock_points.add(new_position)
            new_data[y][x] = 0
            new_data[y][x - 1] = 1
        self.current_rock_points = new_rock_points
        self.data = new_data

    def move_rock_right(self):
        for x, _ in self.current_rock_points:
            if x + 1 >= self.wide:
                return
        new_rock_points = set()
        new_data = self.data
        for x, y in sorted(list(self.current_rock_points), reverse=True):
            new_position = (x + 1, y)
            if new_position not in self.current_rock_points and new_data[y][x + 1] != 0:
                return
            new_rock_points.add(new_position)
            new_data[y][x] = 0
            new_data[y][x + 1] = 1
        self.current_rock_points = new_rock_points
        self.data = new_data

    def run(self):
        pass


def day_17_task_1_example():
    chamber = Chamber(input_data_path="data/day_17_example.txt", vertical_chamber_wide=7)
    chamber.spawn_rock()
    chamber.print_chamber()

    for _ in range(20):
        chamber.move_rock_down()
        chamber.print_chamber()

    print(chamber.data)


if __name__ == '__main__':
    day_17_task_1_example()
