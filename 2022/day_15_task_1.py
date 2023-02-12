from tqdm import tqdm

x_min = None
x_max = None


def manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y):
    return abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)


TEST = False

if TEST:
    y = 11
    file_path = "data/day_15_test.txt"
else:
    y = 2000000
    file_path = "data/day_15.txt"

input_list = []
distance_list = []

for line in open(file_path):
    split = line.split()
    sensor_x = int(split[2].split("=")[-1].split(",")[0])
    sensor_y = int(split[3].split("=")[-1].split(":")[0])
    beacon_x = int(split[8].split("=")[-1].split(",")[0])
    beacon_y = int(split[9].split("=")[-1].split(",")[0])

    input_list.append((sensor_x, sensor_y, beacon_x, beacon_y))
    distance_list.append(manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y))

    x_min_i = min([sensor_x, beacon_x])
    if x_min is None or x_min_i < x_min:
        x_min = x_min_i

    x_max_i = max([sensor_x, beacon_x])
    if x_max is None or x_max_i > x_max:  #
        x_max = x_max_i

print(x_min, x_max)

counter = 0  # cant not use # result
threshold = abs(max(distance_list))
line = ""
for x in tqdm(range(x_min - threshold, x_max + 1 + threshold)):
    s = "."
    for i in range(len(input_list)):
        sensor_x, sensor_y, beacon_x, beacon_y = input_list[i]

        # print("x", x, "y", y, "input_list[i]", distance_list[i], manhattan_distance(sensor_x, sensor_y, x, y), "counter", counter )
        if manhattan_distance(sensor_x, sensor_y, x, y) <= distance_list[i]:
            if beacon_x == x and beacon_y == y:
                s = "B"
                break
            if sensor_y == y and sensor_x == x:
                s = "S"
                break
            counter += 1
            s = "#"
            break
    line += s

print("counter:", counter)  # 4361861 # 4462075 (to small)
print(distance_list)
# print(line)
print(len(line))
