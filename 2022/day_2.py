mapper = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

points = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}


def get_game_points(enemy_hand, my_hand):
    if enemy_hand == my_hand:
        return 3  # "Draw"
    if (enemy_hand == "Rock" and my_hand == "Scissors") \
            or (enemy_hand == "Paper" and my_hand == "Rock") \
            or (enemy_hand == "Scissors" and my_hand == "Paper"):
        return 0  # "Lose"
    return 6  # "Win"


def day_2_task_1():
    with open('data/day2.txt', 'r') as fin:
        lines = fin.readlines()
    points_sum = 0
    for line in lines:
        h1 = mapper[line[0]]
        h2 = mapper[line[2]]
        points_selection = points[h2]
        won_point = get_game_points(h1, h2)
        points_sum += points_selection + won_point
    return points_sum


def get_winning_hand(hand):
    order = ["Rock", "Paper", "Scissors"]
    winner_index = (order.index(hand) + 1) % len(order)
    return order[winner_index]


def get_losing_hand(hand):
    order = ["Rock", "Paper", "Scissors"]
    loser_index = (order.index(hand) - 1)
    if loser_index < 0:
        loser_index = len(order) - 1
    return order[loser_index]


def day_2_task_2():
    with open('data/day2.txt', 'r') as fin:
        lines = fin.readlines()
    points_sum = 0
    for line in lines:
        h1 = mapper[line[0]]
        h2 = line[2]
        if h2 == "X":  # Lose
            h2 = get_losing_hand(h1)
        if h2 == "Y":  # Draw
            h2 = h1
        if h2 == "Z":  # Win
            h2 = get_winning_hand(h1)
        points_selection = points[h2]
        won_point = get_game_points(h1, h2)
        points_sum += points_selection + won_point
    return points_sum


if __name__ == '__main__':
    print(day_2_task_1())
    print(day_2_task_2())
