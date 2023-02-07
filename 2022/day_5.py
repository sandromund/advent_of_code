def day_5(task):
    """
    https://adventofcode.com/2022/day/5

    """
    s = ["BWN", "LZSPTDMB", "QHZWR", "WDVJZR", "SHMB", "LGNJHVPB", "JQZFHDLS", "WSFJGQB", "ZWMSCDJ"]
    s = [list(x) for x in s]
    start_index = 11
    index = 0
    for line in open("data/day5.txt"):
        index += 1
        if index < start_index:
            continue
        cmd = line.split()
        move, fro, to = int(cmd[1]), int(cmd[3]) - 1, int(cmd[5]) - 1
        if task == 2:
            s[to] += s[fro][-move:]
        else:  # task == 1
            s[to] += s[fro][-move:][::-1]
        s[fro] = s[fro][:-move]
    print("".join([x[-1] for x in s]))


if __name__ == '__main__':
    day_5(task=1)  # --> MQSHJMWNH
    day_5(task=2)  # --> LLWJRBHVZ
