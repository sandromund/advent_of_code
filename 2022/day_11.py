class Monkey:

    def __init__(self):
        self.id = None
        self.starting_items = None
        self.operation = None
        self.divisible_by = None
        self.if_true_throw_to = None
        self.if_false_throw_to = None

    def __str__(self):
        s = f"id:{self.id} \nitems: {self.starting_items}\noperation: {self.operation} \ndivisible_by: {self.divisible_by}"
        return  s + f"\nif_false_throw_to: {self.if_false_throw_to} \nif_false_throw_to: {self.if_false_throw_to}\n"


def read_data(path):
    monkeys = []
    m = Monkey()
    for line in open(path):
        args = line.split()
        if len(args) == 0:
            monkeys.append(m)
            m = Monkey()
        elif args[0] == "Monkey":
            m.id = int(args[1].split(":")[0])
        elif args[0] == "Starting":
            numbers = [n.replace(",", "") for n in args[2:]]
            m.starting_items = list(map(int, numbers))
        elif args[0] == "Operation:":
            m.operation = " ".join(args[1:])
        elif args[0] == "Test:":
            m.divisible_by = int(args[3])
        elif args[0] == "If":
            if args[1] == "true:":
                m.if_true_throw_to = int(args[-1])
            elif args[1] == "false:":
                m.if_false_throw_to = int(args[-1])
            else:
                print(args[1])
                raise ValueError
        else:
            print(args)
            raise ValueError
    return monkeys


if __name__ == '__main__':
    monkeys = read_data(path="data/day11_example.txt")

    for m in monkeys:
        print(m)
