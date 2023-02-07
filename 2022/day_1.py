data_sums = sorted(
    [sum(list(map(int, x.split(" ")))) for x in open('data/day1.txt', 'r').read().replace('\n', " ").split("  ")])
print(data_sums[-1])
print(sum(data_sums[-3:]))
