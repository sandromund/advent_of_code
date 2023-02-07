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

    head_x, head_y = 0,0
    tail_x, tail_y = 0,0

    directions, amounts = get_data("data/day9.txt")
    for d, a in zip(directions, amounts):
        #print("===", d, "-", a,"===")
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
            for xi in range(tail_x-1, tail_x+2):
                for yi in range(tail_y-1, tail_y+2):
                    if xi == head_x and yi == head_y:
                        tail_close_to_head = True

            # move tail it necessary
            if not tail_close_to_head:
                if head_x > tail_x :
                    tail_x += 1
                elif head_x < tail_x:
                    tail_x -= 1
                if head_y > tail_y :
                    tail_y += 1
                elif head_y < tail_y:
                    tail_y -=1
            #print((tail_x, tail_y),(head_x, head_y))
            covered.add((tail_x, tail_y))

    return len(covered)

if __name__ == '__main__':
    task_1_solution = day_9_task_1()
    assert task_1_solution == 6470
    print("Day 9 - Task 1 =", task_1_solution)
