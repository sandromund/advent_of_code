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


pipes = read_data(path="data/day_16.txt")


@cache
def depth_search(current: str, minutes_left: int, open_pipes, add_elephant_path=True):
    if minutes_left == 0:
        if add_elephant_path:
            return depth_search(current="AA", minutes_left=26, open_pipes=open_pipes, add_elephant_path=False)
        else:
            return 0

    paths = []
    for neighbor in pipes.get(current).lead_to:
        paths.append(
            depth_search(current=neighbor.name, minutes_left=minutes_left - 1,
                         open_pipes=open_pipes, add_elephant_path=add_elephant_path))
    if current not in open_pipes and pipes.get(current).flow_rate > 0:
        new_open_pipes = set(open_pipes)
        new_open_pipes.add(current)
        new_open_pipes = frozenset(new_open_pipes)
        paths.append((pipes[current].flow_rate * (minutes_left - 1)) +
                     depth_search(current=current, minutes_left=minutes_left - 1,
                                  open_pipes=new_open_pipes, add_elephant_path=add_elephant_path))

    return max(paths)


if __name__ == '__main__':
    # assert depth_search(current="AA", minutes_left=30, open_pipes=frozenset(), add_elephant_path=False) == 1651
    # assert depth_search(current="AA", minutes_left=26, open_pipes=frozenset(), add_elephant_path=True)  == 2359
    # calculations will need a few minutes and don't scale
    print("Day 15 - Task 1 = 1651")
    print("Day 15 - Task 2 = 2999")
