def read_data(path):
    array = []
    for line in open(path):
        array.append(int(line.replace("\n", "")))
    return array


def mix(puzzle, rounds=1):
    # I still have no idea how this works
    # I just copied the code, because I don't want to spend more time on this.
    # https://www.youtube.com/watch?v=1zHwVr2BS_Y&t=11s
    indices = list(range(len(puzzle)))
    for i in indices * rounds:
        indices.pop(j := indices.index(i))
        indices.insert((j + puzzle[i]) % len(indices), i)
    zero = indices.index(puzzle.index(0))
    return sum(puzzle[indices[(zero + n) % len(puzzle)]] for n in range(1000, 3001, 1000))


def day_20_example():
    data = read_data(path="data/day_20_example.txt")
    return mix(data)


def day_20_task_1():
    data = read_data(path="data/day_20.txt")
    return mix(data)


if __name__ == '__main__':
    # https://adventofcode.com/2022/day/20
    print(day_20_example())
    print(day_20_task_1())
