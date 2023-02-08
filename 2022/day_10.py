
class CPU:

    def __init__(self, signal_strength=1, crt=None):
        self.x = 1
        self.noop_cycle = 0
        self.add_x_cycle = 0
        self.add_x_value = 0
        self.n_cycle = 0
        self.signal_strength = signal_strength
        self.signal_cycle = 20
        self.signal_sum = 0
        self.debug = False
        self.crt = crt

    def noop(self):
        self.noop_cycle += 1
        self.cycle(1)

    def add_x(self, v):
        self.add_x_cycle += 2
        self.add_x_value = v
        self.cycle(2)

    def cycle(self, n):
        for _ in range(n):
            if self.crt is not None:
                n = self.n_cycle % self.crt.width
                if self.x in [n, n+1, n-1]:
                    v = "#"
                else:
                    v = "."
                self.crt.set_pixel(p=self.n_cycle, v=v)

            self.n_cycle += 1
            self.signal_cycle -= 1

            if self.signal_cycle == 0:
                if self.debug:
                    print(self.n_cycle, "*", self.x, "=", self.x * self.n_cycle)
                self.signal_sum += self.x * self.n_cycle
                self.signal_cycle = 40

            if self.noop_cycle > 0:
                self.noop_cycle -= 1
            if self.add_x_cycle > 0:
                self.add_x_cycle -= 1
                if self.add_x_cycle == 0:
                    self.x += self.add_x_value


def small_example():
    path = "data/day10_small.txt"
    cpu = CPU()
    for line in open(path):
        args = line.split()
        if args[0] == 'noop':
            cpu.noop()
        elif args[0] == "addx":
            v = int(args[1])
            cpu.add_x(v)
        else:
            raise ValueError
    return cpu.x

def larger_problem():
    path = "data/day10_test.txt"
    cpu = CPU(signal_strength=20)
    for line in open(path):
        args = line.split()
        if args[0] == 'noop':
            cpu.noop()
        elif args[0] == "addx":
            v = int(args[1])
            cpu.add_x(v)
        else:
            raise ValueError
    return cpu.signal_sum

def day_10_task_1():
    path = "data/day10.txt"
    cpu = CPU(signal_strength=20)
    for line in open(path):
        args = line.split()
        if args[0] == 'noop':
            cpu.noop()
        elif args[0] == "addx":
            v = int(args[1])
            cpu.add_x(v)
        else:
            raise ValueError
    return cpu.signal_sum

class CRT:

    def __init__(self):
        self.width = 40
        self.height = 6
        self.pixels = ["."*self.width]*self.height

    def draw_screen(self):
        for row in self.pixels:
            print(row)

    def set_pixel(self, p, v="#"):
        x = p % self.width
        y = p // self.width
        self.pixels[y] = self.pixels[y][:x] + v + self.pixels[y][x+1:]


def task_2_example():
    path = "data/day10_test.txt"
    cpu = CPU(signal_strength=20, crt=CRT())
    for line in open(path):
        args = line.split()
        if args[0] == 'noop':
            cpu.noop()
        elif args[0] == "addx":
            v = int(args[1])
            cpu.add_x(v)
        else:
            raise ValueError
    cpu.crt.draw_screen()

def task_2():
    path = "data/day10.txt"
    cpu = CPU(signal_strength=20, crt=CRT())
    for line in open(path):
        args = line.split()
        if args[0] == 'noop':
            cpu.noop()
        elif args[0] == "addx":
            v = int(args[1])
            cpu.add_x(v)
        else:
            raise ValueError

    cpu.crt.draw_screen()


if __name__ == '__main__':
    assert small_example() == -1
    assert larger_problem() == 13140
    assert day_10_task_1() == 16480
    """
    task_2_example()
    ##..##..##..##..##..##..##..##..##..##..
    ###...###...###...###...###...###...###.
    ####....####....####....####....####....
    #####.....#####.....#####.....#####.....
    ######......######......######......####
    #######.......#######.......#######.....
    """
    task_2()
    """
    ###..#....####.####.#..#.#....###..###..
    #..#.#....#....#....#..#.#....#..#.#..#.
    #..#.#....###..###..#..#.#....#..#.###..
    ###..#....#....#....#..#.#....###..#..#.
    #....#....#....#....#..#.#....#....#..#.
    #....####.####.#.....##..####.#....###..
    """
    print("PLEFULPB")
