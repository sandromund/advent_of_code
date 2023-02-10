class Packet:

    def __init__(self):
        self.left = None
        self.right = None
        self.in_the_right_order = None

    def compare(self, left, right):
        """
        """
        if type(left) == int == type(right):
            if left < right:
                self.in_the_right_order = True
            if right > left:
                self.in_the_right_order = False

        elif type(left) == list == type(right):

            if len(left) == len(right):
                for l, r in zip(left, right):
                    self.compare(l, r)
            else:
                for i in range(min([len(left), len(right)])):
                    self.compare(left[i], right[i])
                if self.in_the_right_order is None:
                    if len(left) > len(right):
                        self.in_the_right_order = False
                    else:
                        self.in_the_right_order = True
        elif type(left) == list and type(right) == int:
            self.compare(left, [right])
        elif type(left) == int and type(right) == list:
            self.compare([left], right)
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


if __name__ == '__main__':
    data: list[Packet] = read_data(path="data/day_13_example.txt")

    for p in data:
        #print(p.left, ",", p.right)
        p.compare(left=p.left, right=p.right)
        print("in_the_right_order -->" ,p.in_the_right_order)
