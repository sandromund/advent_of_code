
def read_data(path):
    result = []
    for line in open(path):
        result.append(line.replace("\n", ""))
    return result


def task_1(data):
    result = 0
    for line in data:
        result_i = ""
        n = len(line)
        for i in range(n):
            if line[i].isdigit():
                result_i = line[i]
                break
        for i in range(n-1, -1, -1):
            if line[i].isdigit():
                result_i += line[i]
                break
        assert len(result_i) == 2
        result += int(result_i)
    return result


if __name__ == '__main__':

    assert task_1(["1abc2"]) == 12
    assert task_1(["pqr3stu8vwx"]) == 38
    assert task_1(["a1b2c3d4e5f"]) == 15
    assert task_1(["treb7uchet"]) == 77
    assert task_1(read_data("data/day_1_demo.txt")) == 142

    print(task_1(read_data("data/day_1.txt")))