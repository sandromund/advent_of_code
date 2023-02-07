def get_data(path):
    directions, amounts = [], []
    for line in open(path):
        direction, amount = line.split()
        assert direction in "LRUD"
        directions.append(direction)
        amounts.append(int(amount))
    assert len(directions) == len(amounts)
    return directions, amounts


def day_9_task_1():
    covered = {(0, 0)}  # positions the tail visited at least once

    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0

    directions, amounts = get_data("data/day9.txt")
    for d, a in zip(directions, amounts):
        # print("===", d, "-", a,"===")
        for i in range(a):

            # move head
            if d == "R":
                head_x += 1
            elif d == "D":
                head_y -= 1
            elif d == "L":
                head_x -= 1
            elif d == "U":
                head_y += 1
            else:
                raise ValueError

            # check if tail has to move
            tail_close_to_head = False
            for xi in range(tail_x - 1, tail_x + 2):
                for yi in range(tail_y - 1, tail_y + 2):
                    if xi == head_x and yi == head_y:
                        tail_close_to_head = True

            # move tail it necessary
            if not tail_close_to_head:
                if head_x > tail_x:
                    tail_x += 1
                elif head_x < tail_x:
                    tail_x -= 1
                if head_y > tail_y:
                    tail_y += 1
                elif head_y < tail_y:
                    tail_y -= 1
            # print((tail_x, tail_y),(head_x, head_y))
            covered.add((tail_x, tail_y))

    return len(covered)


class Knot:

    def __init__(self, x, y, name, head=None, tail=None):
        self.x = x
        self.y = y
        self.head = head
        self.tail = tail
        self.name = name

    def move(self):
        if self.head:
            tail_close_to_head = False
            for xi in range(self.x - 1, self.x + 2):
                for yi in range(self.y - 1, self.y + 2):
                    if xi == self.head.x and yi == self.head.y:
                        tail_close_to_head = True

            if not tail_close_to_head:
                if self.head.x > self.x:
                    self.x += 1
                elif self.head.x < self.x:
                    self.x -= 1
                if self.head.y > self.y:
                    self.y += 1
                elif self.head.y < self.y:
                    self.y -= 1
                if self.tail:
                    self.tail.move()
        else:
            self.tail.move()


def get_head():
    head = Knot(x=0, y=0, name="H")
    knots = []
    for i in range(1, 10):
        knots.append(Knot(x=0, y=0, name=str(i)))
    head.tail = knots[0]
    for i in range(len(knots)):
        k = knots[i]
        if i == 0:
            k.head = head
        else:
            k.head = knots[i - 1]
        if i == len(knots) - 1:
            k.tail = None
        else:
            k.tail = knots[i + 1]
    return head


def print_snake_head_to_tail(head):
    print("Snake head to tail:")
    pointer = head
    while pointer:
        print(pointer.name, pointer.x , pointer.y)
        pointer = pointer.tail
    print()


def get_tail(head):
    pointer = head
    while pointer:
        if not pointer.tail:
            return pointer
        else:
            pointer = pointer.tail


def print_tail_to_head(tail):
    print("Snake tail to head:")
    pointer = tail
    while pointer:
        print(pointer.name)
        pointer = pointer.head
    print()


def day_9_task_2():
    covered = {(0, 0)}
    head = get_head()
    directions, amounts = get_data("data/day9.txt")
    for d, a in zip(directions, amounts):
        #print("===", d, "-", a, "===")
        for i in range(a):
            # move head
            if d == "R":
                head.x += 1
            elif d == "D":
                head.y -= 1
            elif d == "L":
                head.x -= 1
            elif d == "U":
                head.y += 1
            else:
                raise ValueError
            head.move()
            #print_snake_head_to_tail(head)
            tail = get_tail(head)
            covered.add((tail.x, tail.y))
    return len(covered)

    # print_snake_head_to_tail(head)
    # print_tail_to_head(get_tail(head))


if __name__ == '__main__':
    task_1_solution = day_9_task_1()
    assert task_1_solution == 6470
    print("Day 9 - Task 1 =", task_1_solution)

    task_2_solution = day_9_task_2()
    assert task_2_solution == 2658
    print("Day 9 - Task 2 =", task_2_solution)
