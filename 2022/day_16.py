class Pipe:

    def __init__(self, name, flow_rate, lead_to):
        self.open = False
        self.name = name
        self.flow_rate = flow_rate
        self.lead_to = lead_to

    def __str__(self):
        connections = ",".join([c.name for c in self.lead_to])
        return f"Valve {self.name} has flow rate={self.flow_rate}; tunnels lead to valves {connections}"


def read_data(path) -> dict[Pipe]:

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


if __name__ == '__main__':
    data = read_data(path="data/day_16_example.txt")

    for pipe in data.values():
        print(pipe)
