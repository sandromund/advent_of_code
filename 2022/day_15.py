from tqdm import tqdm


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class Sensor:

    def __init__(self, x, y, closest_beacon_x, closest_beacon_y):
        self.x = x
        self.y = y
        self.bx = closest_beacon_x
        self.by = closest_beacon_y
        self.distance = manhattan_distance(x, y, closest_beacon_x, closest_beacon_y)

    def __str__(self):
        return f"Sensor at x={self.x}, y={self.y}: closest beacon is at x={self.bx}, y={self.by}"


def read_data(path):
    sensors = []
    for line in open(path):
        sensor_str, beacon_str = line.split(":")
        sensor_str = sensor_str.replace("Sensor at ", "")
        beacon_str = beacon_str.replace("closest beacon is at ", "").replace("\n", "")

        sensors.append(Sensor(x=int(sensor_str.split(",")[0].split("=")[-1]),
                              y=int(sensor_str.split(",")[1].split("=")[-1]),
                              closest_beacon_x=int(beacon_str.split(",")[0].split("=")[-1]),
                              closest_beacon_y=int(beacon_str.split(",")[1].split("=")[-1])))
    return sensors


def get_n_beacons_on_target_row(target_row, sensor_list):
    n = set()
    for sensor_i in sensor_list:
        if sensor_i.by == target_row:
            n.add((sensor_i.bx, sensor_i.by))
    return len(n)


def day_15_task_1():
    excludable_x_positions = set()
    target_row_y_value = 2_000_000
    data = read_data(path="data/day_15.txt")

    for sensor in data:
        y_distance = abs(sensor.y - target_row_y_value)
        x_distance = sensor.distance - y_distance

        for x in range(sensor.x - x_distance, sensor.x + x_distance + 1):
            excludable_x_positions.add(x)

    k = get_n_beacons_on_target_row(target_row=target_row_y_value, sensor_list=data)
    return len(excludable_x_positions) - k


def point_is_out_of_range_for_all_sensors(x, y, sensors):
    for sensor in sensors:
        if manhattan_distance(x, y, sensor.x, sensor.y) <= sensor.distance:
            return False
    return True


def day_15_task_2():
    data = read_data(path="data/day_15.txt")
    for sensor in tqdm(data, "Iterating over Sensor borders."):
        # we are only interested in points around the sensor borders
        for dx in range(sensor.distance + 2):
            dy = sensor.distance + 1 - dx
            for x, y in [
                (sensor.x + dx, sensor.y + dy),
                (sensor.x + dx, sensor.y - dy),
                (sensor.x - dx, sensor.y + dy),
                (sensor.x - dx, sensor.y - dy),
            ]:
                if not (0 <= x <= 4_000_000 and 0 <= y <= 4_000_000):
                    continue
                if point_is_out_of_range_for_all_sensors(x, y, data):
                    return 4_000_000 * x + y


if __name__ == '__main__':
    # first challenge I needed help
    # https://www.youtube.com/watch?app=desktop&v=pV5nNyjMdFA
    assert day_15_task_1() == 4873353
    assert day_15_task_2() == 11600823139120
