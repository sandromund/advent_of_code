def get_data(path):
    """
    -> {1: [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}], ...
    """
    result = {}
    for line in open(path):
        line = line.replace("\n", "")
        game_sets = line.split(":")[1].split(";")
        game_id = int(line.split(":")[0].split(" ")[-1])

        games = []
        for game_set in game_sets:
            game = {}
            for draw_str in game_set.split(","):
                number, color = draw_str.strip().split()
                game[color] = int(number)
            games.append(game)
        result[game_id] = games
    return result


def is_possible(draws: list, limits: dict) -> bool:
    for game_round in draws:
        for color, limit in limits.items():
            if game_round.get(color) is not None and game_round.get(color) > limit:
                return False
    return True


def day2_task_1(data, limits):
    result = 0
    for game_id, draws in data.items():
        if is_possible(draws, limits):
            result += game_id
    return result


def power_of_set(draws, colors):
    result = 1
    for color in colors:
        color_max = None
        # game_round = {'blue': 3, 'red': 4}
        for game_round in draws:
            if game_round.get(color) is not None:
                if color_max is None or color_max < game_round.get(color):
                    color_max = game_round.get(color)
        result *= color_max
    return result


def day_2_task_2(data, colors):
    result = 0
    for game_id, draws in data.items():
        if power_of_set(draws, colors):
            result += power_of_set(draws, colors)
    return result


if __name__ == '__main__':
    result_day_2_example = day2_task_1(data=get_data(path="data/day_2_demo.txt"),
                                       limits={"red": 12, "green": 13, "blue": 14})
    assert result_day_2_example == 8

    result_day_2_task_1 = day2_task_1(data=get_data(path="data/day_2.txt"),
                                      limits={"red": 12, "green": 13, "blue": 14})
    assert result_day_2_task_1 == 2810

    result_day_2_task_2_example = day_2_task_2(data=get_data(path="data/day_2_demo.txt"),
                                               colors=["blue", "red", "green"])
    assert result_day_2_task_2_example == 2286

    result_day_2_task_2 = day_2_task_2(data=get_data(path="data/day_2.txt"),
                                       colors=["blue", "red", "green"])
    assert result_day_2_task_2 == 69110
