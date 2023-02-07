def day_6(signal, len_marker):
    for i in range(len_marker - 1, len(signal)):
        interval = [signal[j] for j in range(i, i - len_marker, -1)]
        if len(set(interval)) == len_marker:
            return i + 1


def day_6_task_1(signal):
    return day_6(signal, len_marker=4)


def day_6_task_2(signal):
    return day_6(signal, len_marker=14)


if __name__ == '__main__':
    assert day_6_task_1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert day_6_task_1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert day_6_task_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert day_6_task_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

    assert day_6_task_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert day_6_task_2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert day_6_task_2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert day_6_task_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert day_6_task_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26

    for line in open("data/day6.txt"):
        print(day_6_task_1(line))
        print(day_6_task_2(line))
