def day_4(task):
    """
    https://adventofcode.com/2022/day/4
    
    """
    counter = 0
    for line in open("data/day4.txt"):
        i1, i2 = [list(map(int, x.split("-"))) for x in line.split(",")]
        if task == 1:
            if i1[0] <= i2[0] and i1[1] >= i2[1] or (i1[0] >= i2[0] and i1[1] <= i2[1]):
                counter += 1
        if task == 2:
            i2[1] += 1
            i1[1] += 1
            if max(0, min(i1[1], i2[1]) - max(i1[0], i2[0])) > 0:
                counter += 1
    print(counter)


if __name__ == '__main__':
    day_4(task=1)  # --> 538
    day_4(task=2)  # --> 792
