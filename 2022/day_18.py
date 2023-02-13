def read_data(path):
    cubes_list = []
    for line in open(path):
        line = line.replace("\n", "")
        x, y, z = list(map(int, line.split(",")))
        cubes_list.append((x, y, z))
    return cubes_list


def day_18_example():
    cubes = read_data(path="data/day_18_example.txt")
    for (x, y, z) in cubes:
        print(x, y, z)


if __name__ == '__main__':
    day_18_example()
