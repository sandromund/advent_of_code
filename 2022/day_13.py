import logging


class Packet:

    def __init__(self):
        self.left = None
        self.right = None
        self.in_the_right_order = None

    def compare(self, left, right, depth=0):
        """
        """
        if self.in_the_right_order is not None:
            return
        logging.debug(depth * "   " + f"- Compare {left} vs {right}")

        if type(left) == int == type(right):
            if left < right:
                logging.debug((1 + depth) * "   " + "- Left side is smaller, so inputs are in the right order")
                self.in_the_right_order = True
            if left > right:
                logging.debug((1 + depth) * "   " + "- Right side is smaller, so inputs are not in the right order")
                self.in_the_right_order = False

        elif type(left) == list == type(right):

            if len(left) == len(right):
                for l, r in zip(left, right):
                    self.compare(l, r, depth=depth + 1)
            else:
                for i in range(min([len(left), len(right)])):
                    self.compare(left[i], right[i], depth=depth + 1)
                if self.in_the_right_order is None:
                    if len(left) > len(right):
                        logging.debug(
                            depth * "   " + f"- Right side ran out of items, so inputs are in the right order")
                        self.in_the_right_order = False
                    else:
                        logging.debug(depth * "   " + f"- Left side ran out of items, so inputs are in the right order")
                        self.in_the_right_order = True
        elif type(left) == list and type(right) == int:
            logging.debug(depth * "   " + f"- Mixed types; convert right to [{right}] and retry comparison")
            self.compare(left, [right], depth=depth + 1)
        elif type(left) == int and type(right) == list:
            logging.debug(depth * "   " + f"- Mixed types; convert left to [{left}] and retry comparison")
            self.compare([left], right, depth=depth + 1)
        else:
            raise TypeError


def read_data(path: str) -> list[Packet]:
    packet_list = []
    left = None
    right = None
    state = "read_left"
    for line in open(path):
        if "\n" in line:
            line = line.replace("\n", "")
        if state == "create_packet":
            p = Packet()
            exec("p.right = " + str(right))
            exec("p.left = " + str(left))
            packet_list.append(p)
            state = "read_left"
        elif state == "read_left":
            left = line
            state = "read_right"
        elif state == "read_right":
            right = line
            state = "create_packet"
        else:
            raise ValueError
    return packet_list


def day_13_example():
    data: list[Packet] = read_data(path="data/day_13_example.txt")

    for p in data:
        p.compare(left=p.left, right=p.right)

    sum_indices = 0
    for i in range(len(data)):
        if data[i].in_the_right_order:
            sum_indices += i + 1
    return sum_indices


def day_13_task_1():
    data: list[Packet] = read_data(path="data/day_13.txt")

    for p in data:
        p.compare(left=p.left, right=p.right)

    sum_indices = 0
    for i in range(len(data)):
        if data[i].in_the_right_order:
            sum_indices += i + 1
    return sum_indices


def read_data_tasks_2(path):
    signal_list = []
    for line in open(path):
        if "\n" in line:
            line = line.replace("\n", "")
        if len(line) < 1:
            continue
        exec("signal_list.append(" + str(line) + ")")
    return signal_list


def sort_signals(signals):
    signals_sorted = [signals[0]]

    # insertion sort
    for i in range(len(signals)):
        inserted = False
        for j in range(len(signals_sorted)):
            p = Packet()
            p.compare(left=signals[i], right=signals_sorted[j])
            if p.in_the_right_order:
                signals_sorted = signals_sorted[:j] + [signals[i]] + signals_sorted[j:]
                inserted = True
                break
        if not inserted:
            signals_sorted += [signals[i]]
    return signals_sorted


def day_13_task_2_example():
    signals = read_data_tasks_2("data/day_13_example.txt")
    signals.append([[2]])
    signals.append([[6]])
    signals_sorted = sort_signals(signals)
    return signals_sorted.index([[6]]) * signals_sorted.index([[2]])


def day_13_task_2():
    signals = read_data_tasks_2("data/day_13.txt")
    signals.append([[2]])
    signals.append([[6]])
    signals_sorted = sort_signals(signals)
    return signals_sorted.index([[6]]) * signals_sorted.index([[2]])


if __name__ == '__main__':
    logging.basicConfig(filename='logs/day_15.log', encoding='utf-8', level=logging.DEBUG, filemode='w')
    assert day_13_example() == 13
    assert day_13_task_1() == 6235
    assert day_13_task_2_example() == 140
    assert day_13_task_2() == 22866
