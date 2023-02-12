from functools import cache


class Pipe:

    def __init__(self, name, flow_rate, lead_to):
        self.open = False
        self.name = name
        self.flow_rate = flow_rate
        self.lead_to = lead_to

    def __str__(self):
        connections = ",".join([c.name for c in self.lead_to])
        return f"Valve {self.name} has flow rate={self.flow_rate}; tunnels lead to valves {connections}"


def read_data(path):
    pipes = {}

    for line in open(path):
        name = line[6:8]
        line = line.replace("\n", "")
        split = line.split(";")
        lead_to = split[1].replace(" tunnels lead to valves ", "")
        lead_to = lead_to.replace(" tunnel leads to valve ", "").split("value ")[-1]
        lead_to = lead_to.replace(" ", "").split(",")

        pipes[name] = Pipe(name=name, flow_rate=int(split[0].split("=")[-1]), lead_to=lead_to)

    for name, _ in pipes.items():
        pointers = []
        for connection in pipes.get(name).lead_to:
            pointers.append(pipes[connection])
        pipes.get(name).lead_to = pointers

    return pipes


pipes = read_data(path="data/day_16_example.txt")


@cache
def depth_search(current: str, minutes_left: int, pressure_sum: int, open_pipes: str):
    pressure_sum += sum([p.flow_rate for p in pipes.values() if p.name in open_pipes])

    if minutes_left < 2:
        return pressure_sum

    paths = []
    for neighbor in pipes.get(current).lead_to:
        paths.append(
            depth_search(current=neighbor.name, minutes_left=minutes_left - 1, pressure_sum=pressure_sum,
                         open_pipes=open_pipes))
    if current not in open_pipes and pipes.get(current).flow_rate > 0:
        paths.append(
            depth_search(current=current, minutes_left=minutes_left - 1, pressure_sum=pressure_sum,
                         open_pipes=open_pipes + " " + str(current)))

    return pressure_sum + max(paths)


if __name__ == '__main__':
    print(depth_search(current="AA", minutes_left=29, pressure_sum=6, open_pipes=""))

    # 19375 to high
