data = []
for line in open("data/day8_test.txt"):
    data.append(list(line[:-1]))

n_cols = len(data)
n_rows = len(data[0])

# add borders with zeros
for i in range(len(data)):
    data[i] = [-1] + list(map(int, data[i])) + [-1]
data.insert(0, [-1] * (n_cols + 2))
data.append([-1] * (n_cols + 2))

index_left, index_right = 1, n_rows

index_top_border = 1
index_left_border = 1
index_right_border = n_rows
index_bottom_border = n_cols



visible = 0
stop = False

while not stop:


    visible_top = 0
    visible_bot = 0
    visible_left = 0
    visible_right = 0
    # check top border
    for i in range(index_left, index_right + 1):
        if int(data[index_top_border][i]) > int(data[index_top_border - 1][i]):
            visible_top += 1
        data[index_top_border][i] = max(data[index_top_border][i], data[index_top_border - 1][i])


        # check bottom border
        if int(data[index_bottom_border][i]) > int(data[index_bottom_border + 1][i]):
            visible_bot += 1
        data[index_bottom_border][i] = max(data[index_bottom_border][i], data[index_bottom_border + 1][i])

    # check left side
    for i in range(index_top_border, index_bottom_border + 1):
        if data[i][index_left_border] > data[i][index_left_border - 1]:
            visible_left += 1
        data[i][index_left_border] = max(data[i][index_left_border], data[i][index_left_border - 1])

        # check right side
        if data[i][index_right_border] > data[i][index_right_border + 1]:
            visible_right += 1
        data[i][index_right_border] = max(data[i][index_right_border], data[i][index_right_border + 1])

        # check edges
    # left top
    if data[index_top_border][index_left_border] > data[index_top_border - 1][index_left_border] or \
            data[index_top_border][index_left_border - 1]:
        visible += 1

    # right top
    if data[index_top_border][index_right_border] > data[index_top_border - 1][index_right_border] or \
            data[index_top_border][index_right_border - 1]:
        visible += 1

    # left bot
    if data[index_bottom_border][index_left_border] > data[index_bottom_border - 1][index_left_border] or \
            data[index_bottom_border][index_left_border - 1]:
        visible += 1

    # right bot
    if data[index_bottom_border][index_right_border] > data[index_bottom_border - 1][index_right_border] or \
            data[index_bottom_border][index_right_border - 1]:
        visible += 1

    for l in data:
        print(l)

    print("visible_top", visible_top)
    print("visible_bot", visible_bot)
    print("visible_right", visible_right)
    print("visible_left", visible_left)

    print("!", index_right_border +1 - index_left_border )

    index_right_border -= 1
    index_left_border += 1
    index_top_border += 1
    index_bottom_border -= 1
    index_left += 1
    index_right -= 1

    if index_top_border == index_bottom_border -1:
        stop = True





    visible += visible_top +visible_bot + visible_right + visible_left

    print()

print(visible -4)
