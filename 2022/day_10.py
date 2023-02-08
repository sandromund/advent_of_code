
class CPU:

    def __init__(self, signal_strength=1):
        self.x = 1
        self.noop_cycle = 0
        self.add_x_cycle = 0
        self.add_x_value = 0
        self.n_cycle = 0
        self.signal_strength = signal_strength
        self.signal_cycle = 20
        self.signal_sum = 0

    def noop(self):
        self.noop_cycle += 1
        self.cycle(1)

    def add_x(self, v):
        self.add_x_cycle += 2
        self.add_x_value = v
        self.cycle(2)

    def cycle(self, n):
        for _ in range(n):
            self.n_cycle += 1
            self.signal_cycle -= 1

            if self.signal_cycle == 0:
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

if __name__ == '__main__':
    assert small_example() == -1
    assert larger_problem() == 13140
    assert day_10_task_1() == 16480
