class Monkey:

    def __init__(self):
        self.id = None
        self.starting_items = None
        self.operation = None
        self.divisible_by = None
        self.if_true_throw_to = None
        self.if_false_throw_to = None
        self.operation_function = None
        self.function_str = None

    def __str__(self):
        return f"id:{self.id} \nitems: {self.starting_items}\noperation: {self.operation} \ndivisible_by: {self.divisible_by} \n"

    def operation(self, x):
        args = self.operation
        print()



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
            s = m.operation.replace("=", ":").replace("new", "x").replace("old", "x")
            m.function_str = s
            exec("m.operation_function = lambda " + s)
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
    for m in monkeys:
        m.if_false_throw_to = monkeys[m.if_false_throw_to]
        m.if_true_throw_to = monkeys[m.if_true_throw_to]
    return monkeys

def turn(monkey_list):
    for m in monkey_list:
        print(f"Monkey: {m.id}")
        for i in m.starting_items:
            print(f"    Monkey inspects an item with a worry level of {i}.")
            x = m.starting_items[0]
            new_x = m.operation_function(x)
            print("        Worry level is x="+str(x)+ " -> " + m.function_str + " = " + str(new_x))
            new_x = new_x // 3
            print(f"        Monkey gets bored with item. Worry level is divided by 3 to {new_x}.")
            if new_x % m.divisible_by != 0:
                print(f"        Current worry level is NOT divisible by {m.divisible_by }.")
                print(f"        Item with worry level {new_x} is thrown to monkey {m.if_false_throw_to.id}.")
                m.if_false_throw_to.starting_items.append(new_x)
            else:
                print(f"        Current worry level is divisible by {m.divisible_by }.")
                print(f"        Item with worry level {new_x} is thrown to monkey {m.if_true_throw_to.id}.")
                m.if_false_throw_to.starting_items.append(new_x)
            m.starting_items = m.starting_items[1:]

if __name__ == '__main__':
    monkeys = read_data(path="data/day11_example.txt")

    turn(monkeys)
