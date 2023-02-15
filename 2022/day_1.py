def day_1_task_1():
    data_sums = sorted(
        [sum(list(map(int, x.split(" ")))) for x in open('data/day_1.txt', 'r').read().replace('\n', " ").split("  ")])
    return data_sums[-1]


def day_1_task_2():
    data_sums = sorted(
        [sum(list(map(int, x.split(" ")))) for x in open('data/day_1.txt', 'r').read().replace('\n', " ").split("  ")])
    return sum(data_sums[-3:])


if __name__ == '__main__':
    print(day_1_task_1())
    print(day_1_task_2())