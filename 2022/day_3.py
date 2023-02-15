def priorities(x):
    if x.islower():
        return ord(x) - 96  # a = 97
    return ord(x) - 65 + 27  # A = 65


def day_3_task_1():
    result = 0
    for line in open("data/day3.txt"):
        split = (len(line) - 1) // 2
        left, right = line[:split], line[split:]
        e = list(set(list(left)).intersection(list(right)))[0]
        result += priorities(e)
    return result


def day_3_task_2():
    result = 0
    group_items = []
    for line in open("data/day3.txt"):
        group_items.append(set(list(line[:-1])))
        if len(group_items) == 3:
            e = list(group_items[0] & group_items[1] & group_items[2])[0]
            result += priorities(e)
            group_items = []
    return result


if __name__ == '__main__':
    day_3_task_1()  # --> 7990
    day_3_task_2()  # --> 2602
